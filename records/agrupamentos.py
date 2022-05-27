from samples import *
import json

class agrupamentos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, agrupamentos, cadastro, desativado, id_cloud, descricao):
        try:
            sql = """
                INSERT INTO agrupamentos (
                    id_organograma,
                    id_identificador_desktop_transparencia,
                    id_responsavel,
                    id_cloud,
                    descricao
                ) VALUES (
                    %(id_organograma)s,
                    %(id_identificador_desktop_transparencia)s,
                    %(id_responsavel)s,
                    %(id_cloud)s,
                    %(descricao)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                agrupamentos = agrupamentos,
                cadastro = cadastro,
                desativado = desativado,
                id_cloud = id_cloud,
                descricao = descricao
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {descricao} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o agrupamento {descricao}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM agrupamentos"
            if not self.query(sql_s):
                send_log_warning(f"Agrupamentos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM agrupamentos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"Agrupamentos excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do agrupamentos. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM agrupamentos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"Agrupamentos {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    agrupamentos 
                SET 
                    id_cloud = %(id_cloud)s,
                    json_post = %(json)s,
                    resposta_post = %(mensagem)s
                WHERE
                    id = %(id)s
                """
            data = dict (
                id = id,
                id_cloud = id_cloud,
                json = json,
                mensagem = mensagem
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {id} atualizado com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de atualização do agrupamentos. {error}")

    def db_search(self, id):
        try:
            sql = f"SELECT * FROM agrupamentos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"Agrupamentos {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM agrupamentos WHERE id_cloud is null"
            data = self.query(sql)
            if data:
                send_log_info("Consulta de todos os agrupamentos realizada com sucesso.")
                return data
            return None
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def get_id_cloud(self, id):
        if (id == None):
            return None
        try:
            sql = f"SELECT id_cloud FROM agrupamentos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"agrupamentos {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, cadastro, desativado, descricao ):
        objeto = {
            "idIntegracao": f"agrupamentos{id}",
            "content": {}                                 
        }

        if descricao:
            objeto["content"]["descricao"] = f"{descricao}"
        
        if cadastro:
            objeto["content"]["cadastro"] = f"{cadastro}"
        
        if desativado:
            objeto["content"]["desativado"] = f"{desativado}"        
     
        envio = api_post("agrupamentos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

agrupamentos = agrupamentos()