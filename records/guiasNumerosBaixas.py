from samples import *
import json

class guiasNumerosBaixas(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, id, systemId, utilizado, vlGuia, nroConvenio, nroBanco, idGuia, dtValidade, 
                dtVencimento, cedente, integrado, dhGeracao, dhIntegracao, idGuiaEmitida, idGuiaUnificada):
        try:
            sql = """
                INSERT INTO guiasNumerosBaixas (                    
                    idIntegracao,                   
                    id_cloud, 
                    id,
                    systemId,                                               
                    utilizado, 
                    vlGuia,
                    nroConvenio,
                    idGuia,
                    dtValidade,
                    nroBanco,
                    dtVencimento,                    
                    cedente,
                    integrado,
                    dhGeracao,
                    dhIntegracao,
                    idGuiaEmitida,
                    idGuiaUnificada                
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(id)s,
                    %(systemId)s,
                    %(utilizado)s,
                    %(vlGuia)s,
                    %(nroConvenio)s,
                    %(idGuia)s,
                    %(dtValidade)s,
                    %(nroBanco)s,
                    %(dtVencimento)s,                    
                    %(cedente)s,
                    %(integrado)s,
                    %(dhGeracao)s,
                    %(dhIntegracao)s,
                    %(idGuiaEmitida)s,
                    %(idGuiaUnificada)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                id = id,
                systemId = systemId,
                utilizado = utilizado,                               
                vlGuia = vlGuia,
                nroConvenio = nroConvenio,
                idGuia = idGuia,                               
                dtValidade = dtValidade,
                nroBanco = nroBanco,
                dtVencimento = dtVencimento,                                               
                cedente = cedente,
                integrado = integrado,                               
                dhGeracao = dhGeracao,
                dhIntegracao = dhIntegracao,
                idGuiaEmitida = idGuiaEmitida,                               
                idGuiaUnificada = idGuiaUnificada
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {guiasNumerosBaixas} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {guiasNumerosBaixas}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM guiasNumerosBaixas"
            if not self.query(sql_s):
                send_log_warning(f"guiasNumerosBaixas não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM guiasNumerosBaixas WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM guiasNumerosBaixas WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    guiasNumerosBaixas 
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
            sql = f"SELECT * FROM guiasNumerosBaixas WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM guiasNumerosBaixas WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM guiasNumerosBaixas WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, systemId, utilizado, vlGuia, nroConvenio, nroBanco, idGuia, dtValidade, 
                dtVencimento, cedente, integrado, dhGeracao, dhIntegracao, idGuiaEmitida, idGuiaUnificada):
        objeto = {
            "idIntegracao": f"guiasNumerosBaixas{id}",
            "content": {}                                 
        }
        if id:
            objeto["content"]["id"] = { "id": int(id)}
        
        if dtValidade:
            objeto["content"]["dtValidade"] = f"{dtValidade}"

        if systemId:
            objeto["content"]["systemId"] = f"{systemId}"
        
        if vlGuia:
            objeto["content"]["vlGuia"] = f"{vlGuia}" 

        if integrado:
            objeto["content"]["integrado"] = f"{integrado}"  

        if idGuiaUnificada:
            objeto["content"]["idGuiaUnificada"] = { "id": int(idGuiaUnificada)}       
       
        if nroConvenio:
            objeto["content"]["nroConvenio"] = f"{nroConvenio}"

        if idGuia:
            objeto["content"]["idGuia"] = { "id": int(idGuia)}   

        if cedente:
            objeto["content"]["cedente"] = f"{cedente}"
        
        if dtVencimento:
            objeto["content"]["dtVencimento"] = f"{dtVencimento}"
           
        if dhGeracao:
            objeto["content"]["dhGeracao"] = f"{dhGeracao}"
        
        if idGuiaEmitida:
            objeto["content"]["idGuiaEmitida"] = { "id": int(idGuiaEmitida)}

        if nroBanco:
            objeto["content"]["nroBanco"] = f"{nroBanco}"

        if utilizado != None:
            objeto[0]["content"]["utilizado"] = f"{utilizado}"               

        if dhIntegracao != None:
            objeto[0]["content"]["dhIntegracao"] = f"{dhIntegracao}"  
            
        envio = api_post("guiasNumerosBaixas", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

guiasNumerosBaixas = guiasNumerosBaixas()