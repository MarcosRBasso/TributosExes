from samples import *
import json

class notificacoesDividas(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, modelo, idDivida, idCreditoTributario, idContribuinte, idReferente, protocoloExecucao, nroDocumento, dataEmissao, 
                cancelada, ano, parcela, numeroInscricao, dataInscricao, dataVencimento, situacaoDivida, valorDivida, tipoReferente):
        try:
            sql = """
                INSERT INTO notificacoesDividas (                    
                    idIntegracao,                   
                    id_cloud, 
                    modelo,
                    idDivida,                                               
                    idCreditoTributario, 
                    idContribuinte,
                    idReferente,
                    nroDocumento,
                    dataEmissao,
                    protocoloExecucao,
                    cancelada,                    
                    ano,
                    parcela,
                    numeroInscricao,
                    dataInscricao,
                    dataVencimento,
                    situacaoDivida, 
                    valorDivida, 
                    tipoReferente               
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(modelo)s,
                    %(idDivida)s,
                    %(idCreditoTributario)s,
                    %(idContribuinte)s,
                    %(idReferente)s,
                    %(nroDocumento)s,
                    %(dataEmissao)s,
                    %(protocoloExecucao)s,
                    %(cancelada)s,                    
                    %(ano)s,
                    %(parcela)s,
                    %(numeroInscricao)s,
                    %(dataInscricao)s,
                    %(dataVencimento)s,
                    %(situacaoDivida)s, 
                    %(valorDivida)s, 
                    %(tipoReferente)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                modelo = modelo,
                idDivida = idDivida,
                idCreditoTributario = idCreditoTributario,                               
                idContribuinte = idContribuinte,
                idReferente = idReferente,
                nroDocumento = nroDocumento,                               
                dataEmissao = dataEmissao,
                protocoloExecucao = protocoloExecucao,
                cancelada = cancelada,                                               
                ano = ano,
                parcela = parcela,                               
                numeroInscricao = numeroInscricao,
                dataInscricao = dataInscricao,
                dataVencimento = dataVencimento,
                situacaoDivida = situacaoDivida, 
                valorDivida = valorDivida, 
                tipoReferente = tipoReferente
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {notificacoesDividas} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {notificacoesDividas}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM notificacoesDividas"
            if not self.query(sql_s):
                send_log_warning(f"notificacoesDividas não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM notificacoesDividas WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM notificacoesDividas WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    notificacoesDividas 
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
            sql = f"SELECT * FROM notificacoesDividas WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM notificacoesDividas WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM notificacoesDividas WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, modelo, idDivida, idCreditoTributario, idContribuinte, idReferente, protocoloExecucao, nroDocumento, dataEmissao, 
                cancelada, ano, parcela, numeroInscricao, dataInscricao, dataVencimento, situacaoDivida, valorDivida, tipoReferente):
        objeto = {
            "idIntegracao": f"notificacoesDividas{id}",
            "content": {}                                 
        }
        if modelo:
            objeto["content"]["modelo"] = f"{modelo}"

        if situacaoDivida:
            objeto["content"]["situacaoDivida"] = f"{situacaoDivida}"   

        if valorDivida:
            objeto["content"]["valorDivida"] = f"{valorDivida}"
        
        if tipoReferente:
            objeto["content"]["tipoReferente"] = f"{tipoReferente}"         
        
        if dataEmissao:
            objeto["content"]["dataEmissao"] = f"{dataEmissao}"

        if idDivida:
            objeto["content"]["idDivida"] =  { "id": int(idDivida)}           
        
        if idContribuinte:
            objeto["content"]["idContribuinte"] =  { "id": int(idContribuinte)} 

        if parcela:
            objeto["content"]["parcela"] = f"{parcela}"  

        if idReferente:
            objeto["content"]["idReferente"] =  { "id": int(idReferente)}

        if nroDocumento:
            objeto["content"]["nroDocumento"] = f"{nroDocumento}"   

        if ano:
            objeto["content"]["ano"] = f"{ano}"
        
        if cancelada:
            objeto["content"]["cancelada"] = f"{cancelada}"
           
        if numeroInscricao:
            objeto["content"]["numeroInscricao"] = f"{numeroInscricao}"
        
        if dataVencimento:
            objeto["content"]["dataVencimento"] = f"{dataVencimento}"
        
        if protocoloExecucao:
            objeto["content"]["protocoloExecucao"] = f"{protocoloExecucao}"

        if idCreditoTributario != None:
            objeto[0]["content"]["idCreditoTributario"] = { "id": int(idCreditoTributario) }               

        if dataInscricao != None:
            objeto[0]["content"]["dataInscricao"] = f"{dataInscricao}"        
            
        envio = api_post("notificacoesDividas", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

notificacoesDividas = notificacoesDividas()