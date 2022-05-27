from samples import *
import json

class estados(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idPaises, idTemplate, nome, uf, codigoIBGE, versionTemplate):
        try:
            sql = """
                INSERT INTO estados (                    
                    idIntegracao,                   
                    id_cloud, 
                    idPaises,
                    idTemplate,                                               
                    nome, 
                    uf,
                    codigoIBGE,
                    versionTemplate                
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idPaises)s,
                    %(idTemplate)s,
                    %(nome)s,
                    %(uf)s,
                    %(codigoIBGE)s,
                    %(versionTemplate)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idPaises = idPaises,
                idTemplate = idTemplate,
                nome = nome,                               
                uf = uf,
                codigoIBGE = codigoIBGE,
                versionTemplate = versionTemplate
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {estados} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {estados}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM estados"
            if not self.query(sql_s):
                send_log_warning(f"estados não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM estados WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM estados WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    estados 
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
            sql = f"SELECT * FROM estados WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM estados WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM estados WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idPaises, idTemplate, nome, uf, codigoIBGE, versionTemplate):
        objeto = {
            "idIntegracao": f"estados{id}",
            "content": {}                                 
        }
        if idPaises:
            objeto["content"]["idPaises"] = { "id": int(idPaises)}

        if idTemplate:
            objeto["content"]["idTemplate"] = { "id": int(idTemplate)}        
       
        if uf:
            objeto["content"]["uf"] = f"{uf}"       
       
        if codigoIBGE:
            objeto["content"]["codigoIBGE"] = { "id": int(codigoIBGE)}
        
        if versionTemplate:
            objeto["content"]["versionTemplate"] = f"{versionTemplate}"              

        if nome != None:
            objeto[0]["content"]["nome"] = f"{nome}"    
            
        envio = api_post("estados", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

estados = estados()