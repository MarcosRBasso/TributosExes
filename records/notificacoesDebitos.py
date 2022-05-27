from samples import *
import json

class notificacoesDebitos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idContribuinte, idGuia, idCreditoTributario, idConfigGeracaoParcelas, idReferente, modelo, protocoloExecucao, nroDocumento, 
                dataEmissao, cancelada, ano, dataInscricao, parcela, dataVencimento, situacaoParcela, lancamentoComplementar, valorDebito, tipoReferente):
        try:
            sql = """
                INSERT INTO notificacoesDebitos (                    
                    idIntegracao,                   
                    id_cloud, 
                    idContribuinte,
                    idGuia,                                               
                    idCreditoTributario, 
                    idConfigGeracaoParcelas,
                    idReferente,
                    protocoloExecucao,
                    nroDocumento,
                    modelo,
                    dataEmissao,                    
                    cancelada,
                    dataInscricao,
                    ano,
                    parcela,
                    dataVencimento,
                    situacaoParcela,
                    lancamentoComplementar, 
                    valorDebito, 
                    tipoReferente                
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idContribuinte)s,
                    %(idGuia)s,
                    %(idCreditoTributario)s,
                    %(idConfigGeracaoParcelas)s,
                    %(idReferente)s,
                    %(protocoloExecucao)s,
                    %(nroDocumento)s,
                    %(modelo)s,
                    %(dataEmissao)s,                    
                    %(cancelada)s,
                    %(dataInscricao)s,
                    %(ano)s,
                    %(parcela)s,
                    %(dataVencimento)s,
                    %(situacaoParcela)s,
                    %(lancamentoComplementar)s, 
                    %(valorDebito)s, 
                    %(tipoReferente)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idContribuinte = idContribuinte,
                idGuia = idGuia,
                idCreditoTributario = idCreditoTributario,                               
                idConfigGeracaoParcelas = idConfigGeracaoParcelas,
                idReferente = idReferente,
                protocoloExecucao = protocoloExecucao,                               
                nroDocumento = nroDocumento,
                modelo = modelo,
                dataEmissao = dataEmissao,                                               
                cancelada = cancelada,
                dataInscricao = dataInscricao,                               
                ano = ano,
                parcela = parcela,
                dataVencimento = dataVencimento,                               
                situacaoParcela = situacaoParcela,
                lancamentoComplementar = lancamentoComplementar, 
                valorDebito = valorDebito, 
                tipoReferente = tipoReferente
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {notificacoesDebitos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {notificacoesDebitos}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM notificacoesDebitos"
            if not self.query(sql_s):
                send_log_warning(f"notificacoesDebitos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM notificacoesDebitos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM notificacoesDebitos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    notificacoesDebitos 
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
            sql = f"SELECT * FROM notificacoesDebitos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM notificacoesDebitos WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM notificacoesDebitos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idContribuinte, idGuia, idCreditoTributario, idConfigGeracaoParcelas, idReferente, modelo, protocoloExecucao, nroDocumento, 
                dataEmissao, cancelada, ano, dataInscricao, parcela, dataVencimento, situacaoParcela, lancamentoComplementar, valorDebito, tipoReferente):
        objeto = {
            "idIntegracao": f"notificacoesDebitos{id}",
            "content": {}                                 
        }
        if valorDebito:
            objeto["content"]["valorDebito"] = f"{valorDebito}"

        if tipoReferente:
            objeto["content"]["tipoReferente"] = f"{tipoReferente}"

        if idContribuinte:
            objeto["content"]["idContribuinte"] = { "id": int(idContribuinte)}
        
        if nroDocumento:
            objeto["content"]["nroDocumento"] = { "id": int(nroDocumento)}

        if idGuia:
            objeto["content"]["idGuia"] = { "id": int(idGuia)}
        
        if idConfigGeracaoParcelas:
            objeto["content"]["idConfigGeracaoParcelas"] = { "id": int(idConfigGeracaoParcelas)} 

        if dataInscricao:
            objeto["content"]["dataInscricao"] = f"{dataInscricao}"  

        if situacaoParcela:
            objeto["content"]["situacaoParcela"] = f"{situacaoParcela}"       
       
        if idReferente:
            objeto["content"]["idReferente"] = { "id": int(idReferente)}

        if protocoloExecucao:
            objeto["content"]["protocoloExecucao"] = f"{protocoloExecucao}"   

        if cancelada:
            objeto["content"]["cancelada"] = f"{cancelada}"
        
        if dataEmissao:
            objeto["content"]["dataEmissao"] = f"{dataEmissao}"
           
        if ano:
            objeto["content"]["ano"] = f"{ano}"
        
        if dataVencimento:
            objeto["content"]["dataVencimento"] = f"{dataVencimento}"

        if modelo:
            objeto["content"]["modelo"] = f"{modelo}"

        if idCreditoTributario != None:
            objeto[0]["content"]["idCreditoTributario"] = { "id": int(idCreditoTributario) }               

        if parcela != None:
            objeto[0]["content"]["parcela"] = f"{parcela}"

        if lancamentoComplementar != None:
            objeto[0]["content"]["lancamentoComplementar"] = f"{lancamentoComplementar}"
            
        envio = api_post("notificacoesDebitos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

notificacoesDebitos = notificacoesDebitos()