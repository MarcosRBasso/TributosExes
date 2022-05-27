from samples import *
import json

class engenheirosArquitetos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idPessoa, nroRegistro, dtRegistro):
        try:
            sql = """
                INSERT INTO engenheirosArquitetos (                    
                    idIntegracao,                   
                    id_cloud,                                                           
                    idPessoa, 
                    nroRegistro,
                    dtRegistro                                             
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,                                                            
                    %(idPessoa)s,
                    %(nroRegistro)s,
                    %(dtRegistro)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                                                               
                idPessoa = idPessoa,                               
                nroRegistro = nroRegistro,
                dtRegistro = dtRegistro
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {engenheirosArquitetos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {engenheirosArquitetos}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM engenheirosArquitetos"
            if not self.query(sql_s):
                send_log_warning(f"engenheirosArquitetos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM engenheirosArquitetos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, descricao):
        try:
            sql_s = f"SELECT * FROM engenheirosArquitetos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    engenheirosArquitetos 
                SET 
                    id_cloud = %(id_cloud)s,
                    json_post = %(json)s,
                    resposta_post = %(descricao)s
                WHERE
                    id = %(id)s
                """
            data = dict (
                id = id,
                id_cloud = id_cloud,
                json = json,
                descricao = descricao
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"atividades Economicas {id} atualizado com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de atualização da atividades Economicas. {error}")

    def db_search(self, id):
        try:
            sql = f"SELECT * FROM engenheirosArquitetos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM engenheirosArquitetos WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM engenheirosArquitetos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idPessoa, nroRegistro, dtRegistro):
        objeto = {
            "idIntegracao": f"engenheirosArquitetos{id}",
            "content": {}                                 
        }
        if dtRegistro != None:
            objeto[0]["content"]["dtRegistro"] = f"{dtRegistro}"  

        if nroRegistro != None:
            objeto[0]["content"]["nroRegistro"] = { "id": int(nroRegistro)}    
               
        if idPessoa != None:
            objeto[0]["camposadicionais"]["idPessoa"] = { "id": int(idPessoa)}

        envio = api_post("engenheirosArquitetos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["descricao"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["descricao"], ensure_ascii=False))

engenheirosArquitetos = engenheirosArquitetos()