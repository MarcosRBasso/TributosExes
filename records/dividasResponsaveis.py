from samples import *
import json

class dividasResponsaveis(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idDivida, idResponsavel):
        try:
            sql = """
                INSERT INTO dividasResponsaveis (                    
                    idIntegracao,                   
                    id_cloud,                                                           
                    idDivida, 
                    idResponsavel                                             
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,                                                            
                    %(idDivida)s,
                    %(idResponsavel)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                                                               
                idDivida = idDivida,
                idResponsavel = idResponsavel
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {dividasResponsaveis} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {dividasResponsaveis}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM dividasResponsaveis"
            if not self.query(sql_s):
                send_log_warning(f"dividasResponsaveis não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM dividasResponsaveis WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, descricao):
        try:
            sql_s = f"SELECT * FROM dividasResponsaveis WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    dividasResponsaveis 
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
            sql = f"SELECT * FROM dividasResponsaveis WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM dividasResponsaveis WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM dividasResponsaveis WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idDivida, idResponsavel):
        objeto = {
            "idIntegracao": f"dividasResponsaveis{id}",
            "content": {}                                 
        }
        if idResponsavel != None:
            objeto[0]["content"]["idResponsavel"] = { "id": int(idResponsavel)}   
               
        if idDivida != None:
            objeto[0]["camposadicionais"]["idDivida"] = { "id": int(idDivida)}

        envio = api_post("dividasResponsaveis", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["descricao"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["descricao"], ensure_ascii=False))

dividasResponsaveis = dividasResponsaveis()