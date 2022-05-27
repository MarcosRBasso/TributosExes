from samples import *
import json

class contribMelhoriasSaldos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idContribMelhoriaImovel, idContribuicaoMelhoria, idCreditoTributario, idCreditoTributarioRec, idImoveis, valorDeclarado, 
                  valorLancado, valorPago):
        try:
            sql = """
                INSERT INTO contribMelhoriasSaldos (                    
                    idIntegracao,                   
                    id_cloud,                     
                    idContribMelhoriaImovel,                                               
                    idContribuicaoMelhoria, 
                    idCreditoTributario,
                    idCreditoTributarioRec,
                    idImoveis,
                    valorDeclarado,
                    valorLancado, 
                    valorPago                                 
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,                                        
                    %(idContribMelhoriaImovel)s,
                    %(idContribuicaoMelhoria)s,
                    %(idCreditoTributario)s,
                    %(idCreditoTributarioRec)s,
                    %(idImoveis)s,
                    %(valorDeclarado)s,
                    %(valorLancado)s, 
                    %(valorPago)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                                               
                idContribMelhoriaImovel = idContribMelhoriaImovel,
                idContribuicaoMelhoria = idContribuicaoMelhoria,                               
                idCreditoTributario = idCreditoTributario,
                idCreditoTributarioRec = idCreditoTributarioRec,
                idImoveis = idImoveis,                               
                valorDeclarado = valorDeclarado,
                valorLancado = valorLancado, 
                valorPago = valorPago
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {contribMelhoriasSaldos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {contribMelhoriasSaldos}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM contribMelhoriasSaldos"
            if not self.query(sql_s):
                send_log_warning(f"contribMelhoriasSaldos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM contribMelhoriasSaldos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM contribMelhoriasSaldos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    contribMelhoriasSaldos 
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
            sql = f"SELECT * FROM contribMelhoriasSaldos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM contribMelhoriasSaldos WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM contribMelhoriasSaldos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idContribMelhoriaImovel, idContribuicaoMelhoria, idCreditoTributario, idCreditoTributarioRec, idImoveis, valorDeclarado,valorLancado, valorPago):
        objeto = {
            "idIntegracao": f"contribMelhoriasSaldos{id}",
            "content": {}                                 
        }
        if valorLancado:
            objeto["content"]["valorLancado"] = f"{valorLancado}"
           
        if valorPago:
            objeto["content"]["valorPago"] = f"{valorPago}"
        if idCreditoTributario:
            objeto["content"]["idCreditoTributario"] =  { "id": int(idCreditoTributario)}
        
        if idCreditoTributarioRec:
            objeto["content"]["idCreditoTributarioRec"] =  { "id": int(idCreditoTributarioRec)}

        if idContribMelhoriaImovel:
            objeto["content"]["idContribMelhoriaImovel"] =  { "id": int(idContribMelhoriaImovel)}
           
        if idContribuicaoMelhoria:
            objeto["content"]["idContribuicaoMelhoria"] =  { "id": int(idContribuicaoMelhoria)}
        
        if valorDeclarado:
            objeto["content"]["valorDeclarado"] =  f"{valorDeclarado}"
        
        if idImoveis:
            objeto["content"]["idImoveis"] =  { "id": int(idImoveis)}
        envio = api_post("contribMelhoriasSaldos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

contribMelhoriasSaldos = contribMelhoriasSaldos()