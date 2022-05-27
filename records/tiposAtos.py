from samples import *
import json

class tiposAtos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, descricao, classificacao):
        try:
            sql = """
                INSERT INTO tiposAtos (                    
                    idIntegracao,                   
                    id_cloud, 
                    descricao,                                               
                    classificacao              
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,                    
                    %(descricao)s,
                    %(classificacao)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud, 
                descricao = descricao,
                classificacao = classificacao
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {tiposAtos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {tiposAtos}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM tiposAtos"
            if not self.query(sql_s):
                send_log_warning(f"tiposAtos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM tiposAtos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM tiposAtos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    tiposAtos 
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
            send_log_info(f"atividades Economicas {id} atualizado com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de atualização da atividades Economicas. {error}")

    def db_search(self, id):
        try:
            sql = f"SELECT * FROM tiposAtos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM tiposAtos WHERE id_cloud is null"
            data = self.query(sql)
            if data:
                send_log_info("Consulta de todos os atividades Economicas realizada com sucesso.")
                return data
            return None
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def get_id_cloud(self, id):
        if (id == None):
            return None
        try:
            sql = f"SELECT id_cloud FROM tiposAtos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id,descricao, classificacao):
        objeto = {
            "idIntegracao": f"tiposAtos{id}",
            "content": {}                                 
        }

        if descricao:
            objeto["content"]["descricao"] = f"{descricao}"               

        if classificacao != None:
            objeto[0]["content"]["classificacao"] = f"{classificacao}"    
            
        envio = api_post("tiposAtos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

tiposAtos = tiposAtos()