from samples import *
import json

class configTransfImoMotivos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idConfigTransfImoveis, idMotivos, percAliqAvista, percAliqBenfeitoria, percAliqFinanciada, percAliqOutros, nomenclaturaCompra, nomenclaturaVenda):
        try:
            sql = """
                INSERT INTO configTransfImoMotivos (                    
                    idIntegracao,                   
                    id_cloud,                     
                    idConfigTransfImoveis,                                               
                    idMotivos, 
                    percAliqAvista,
                    percAliqBenfeitoria,
                    percAliqFinanciada,
                    percAliqOutros,
                    nomenclaturaCompra, 
                    nomenclaturaVenda                               
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,                                        
                    %(idConfigTransfImoveis)s,
                    %(idMotivos)s,
                    %(percAliqAvista)s,
                    %(percAliqBenfeitoria)s,
                    %(percAliqFinanciada)s,
                    %(percAliqOutros)s,
                    %(nomenclaturaCompra)s, 
                    %(nomenclaturaVenda)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                                               
                idConfigTransfImoveis = idConfigTransfImoveis,
                idMotivos = idMotivos,                               
                percAliqAvista = percAliqAvista,
                percAliqBenfeitoria = percAliqBenfeitoria,
                percAliqFinanciada = percAliqFinanciada,                               
                percAliqOutros = percAliqOutros,
                nomenclaturaCompra = nomenclaturaCompra, 
                nomenclaturaVenda = nomenclaturaVenda               
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {configTransfImoMotivos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {configTransfImoMotivos}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM configTransfImoMotivos"
            if not self.query(sql_s):
                send_log_warning(f"configTransfImoMotivos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM configTransfImoMotivos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM configTransfImoMotivos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    configTransfImoMotivos 
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
            sql = f"SELECT * FROM configTransfImoMotivos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM configTransfImoMotivos WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM configTransfImoMotivos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idConfigTransfImoveis, idMotivos, percAliqAvista, percAliqBenfeitoria, percAliqFinanciada, percAliqOutros,nomenclaturaCompra, nomenclaturaVenda):
        objeto = {
            "idIntegracao": f"configTransfImoMotivos{id}",
            "content": {}                                 
        }
        if nomenclaturaCompra:
            objeto["content"]["nomenclaturaCompra"] = f"{nomenclaturaCompra}"
           
        if nomenclaturaVenda:
            objeto["content"]["nomenclaturaVenda"] = f"{nomenclaturaVenda}"

        if percAliqAvista:
            objeto["content"]["percAliqAvista"] =  { "id": int(percAliqAvista)}
        
        if percAliqBenfeitoria:
            objeto["content"]["percAliqBenfeitoria"] =  { "id": int(percAliqBenfeitoria)}

        if idConfigTransfImoveis:
            objeto["content"]["idConfigTransfImoveis"] =  { "id": int(idConfigTransfImoveis)}
           
        if idMotivos:
            objeto["content"]["idMotivos"] =  { "id": int(idMotivos)}
        
        if percAliqOutros:
            objeto["content"]["percAliqOutros"] =  { "id": int(percAliqOutros)}
        
        if percAliqFinanciada:
            objeto["content"]["percAliqFinanciada"] =  { "id": int(percAliqFinanciada)}
        envio = api_post("configTransfImoMotivos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

configTransfImoMotivos = configTransfImoMotivos()