from samples import *
import json

class obrasConstrutoras(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idConstrutoras, idObras, dtValidade):
        try:
            sql = """
                INSERT INTO obrasConstrutoras (                    
                    idIntegracao,                   
                    id_cloud, 
                    idConstrutoras,
                    idObras,                                               
                    dtValidade               
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idConstrutoras)s,
                    %(idObras)s,
                    %(dtValidade)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idConstrutoras = idConstrutoras,
                idObras = idObras,
                dtValidade = dtValidade
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {obrasConstrutoras} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {obrasConstrutoras}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM obrasConstrutoras"
            if not self.query(sql_s):
                send_log_warning(f"obrasConstrutoras não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM obrasConstrutoras WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM obrasConstrutoras WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    obrasConstrutoras 
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
            sql = f"SELECT * FROM obrasConstrutoras WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM obrasConstrutoras WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM obrasConstrutoras WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idConstrutoras, idObras, dtValidade):
        objeto = {
            "idIntegracao": f"obrasConstrutoras{id}",
            "content": {}                                 
        }
        if idConstrutoras:
            objeto["content"]["idConstrutoras"] = { "id": int(idConstrutoras)}

        if idObras:
            objeto["content"]["idObras"] = f"{idObras}"                   

        if dtValidade != None:
            objeto[0]["content"]["dtValidade"] = f"{dtValidade}"    
            
        envio = api_post("obrasConstrutoras", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

obrasConstrutoras = obrasConstrutoras()