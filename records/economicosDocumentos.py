from samples import *
import json

class economicosDocumentos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idEconomico, idTipoDocumento, responsavel, dtDocumento, situacaoDocumento):
        try:
            sql = """
                INSERT INTO economicosDocumentos (                    
                    idIntegracao,                   
                    id_cloud, 
                    idEconomico,
                    idTipoDocumento,                                               
                    responsavel, 
                    dtDocumento,
                    situacaoDocumento         
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idEconomico)s,
                    %(idTipoDocumento)s,
                    %(responsavel)s,
                    %(dtDocumento)s,
                    %(situacaoDocumento)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idEconomico = idEconomico,
                idTipoDocumento = idTipoDocumento,
                responsavel = responsavel,                               
                dtDocumento = dtDocumento,
                situacaoDocumento = situacaoDocumento
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {economicosDocumentos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {economicosDocumentos}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM economicosDocumentos"
            if not self.query(sql_s):
                send_log_warning(f"economicosDocumentos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM economicosDocumentos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM economicosDocumentos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    economicosDocumentos 
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
            sql = f"SELECT * FROM economicosDocumentos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM economicosDocumentos WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM economicosDocumentos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idEconomico, idTipoDocumento, responsavel, dtDocumento, situacaoDocumento):
        objeto = {
            "idIntegracao": f"economicosDocumentos{id}",
            "content": {}                                 
        }
        if idEconomico:
            objeto["content"]["idEconomico"] = { "id": int(idEconomico)}

        if idTipoDocumento:
            objeto["content"]["idTipoDocumento"] = { "id": int(idTipoDocumento)}        
       
        if dtDocumento:
            objeto["content"]["dtDocumento"] = f"{dtDocumento}"       
       
        if situacaoDocumento:
            objeto["content"]["situacaoDocumento"] = f"{situacaoDocumento}"              

        if responsavel != None:
            objeto[0]["content"]["responsavel"] = f"{responsavel}"    
            
        envio = api_post("economicosDocumentos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

economicosDocumentos = economicosDocumentos()