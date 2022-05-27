from samples import *
import json

class transferenciaImoveis(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, codigo, idPagador, anoTransferencia, dtCadastro, dtTransferencia, dtVencimento, formaTransf, lancamentoGerado, 
                statusCertidaoITBI, situacao, tipoCobranca, tipoImovel):
        try:
            sql = """
                INSERT INTO transferenciaImoveis (                    
                    idIntegracao,                   
                    id_cloud, 
                    codigo,
                    idPagador,                                               
                    anoTransferencia, 
                    dtCadastro,
                    dtTransferencia,
                    formaTransf,
                    lancamentoGerado,
                    situacao,
                    statusCertidaoITBI,                    
                    dtVencimento,
                    tipoCobranca,
                    tipoImovel        
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(codigo)s,
                    %(idPagador)s,
                    %(anoTransferencia)s,
                    %(dtCadastro)s,
                    %(dtTransferencia)s,
                    %(formaTransf)s,
                    %(lancamentoGerado)s,
                    %(situacao)s,
                    %(statusCertidaoITBI)s,                    
                    %(dtVencimento)s,
                    %(tipoCobranca)s,
                    %(tipoImovel)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                codigo = codigo,
                idPagador = idPagador,
                anoTransferencia = anoTransferencia,                               
                dtCadastro = dtCadastro,
                dtTransferencia = dtTransferencia,
                formaTransf = formaTransf,                               
                lancamentoGerado = lancamentoGerado,
                situacao = situacao,
                statusCertidaoITBI = statusCertidaoITBI,                                               
                dtVencimento = dtVencimento,
                tipoCobranca = tipoCobranca,                               
                tipoImovel = tipoImovel
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {transferenciaImoveis} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {transferenciaImoveis}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM transferenciaImoveis"
            if not self.query(sql_s):
                send_log_warning(f"transferenciaImoveis não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM transferenciaImoveis WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM transferenciaImoveis WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    transferenciaImoveis 
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
            sql = f"SELECT * FROM transferenciaImoveis WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM transferenciaImoveis WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM transferenciaImoveis WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, codigo, idPagador, anoTransferencia, dtCadastro, dtTransferencia, dtVencimento, formaTransf, lancamentoGerado, 
                statusCertidaoITBI, situacao, tipoCobranca, tipoImovel):
        objeto = {
            "idIntegracao": f"transferenciaImoveis{id}",
            "content": {}                                 
        }
        if codigo:
            objeto["content"]["codigo"] = { "id": int(codigo)}          
        
        if lancamentoGerado:
            objeto["content"]["lancamentoGerado"] = f"{lancamentoGerado}"

        if idPagador:
            objeto["content"]["idPagador"] = { "id": int(idPagador)}           
        
        if dtCadastro:
            objeto["content"]["dtCadastro"] = f"{dtCadastro}" 

        if tipoCobranca:
            objeto["content"]["tipoCobranca"] = f"{tipoCobranca}"  

        if dtTransferencia:
            objeto["content"]["dtTransferencia"] = f"{dtTransferencia}"

        if formaTransf:
            objeto["content"]["formaTransf"] = f"{formaTransf}"   

        if situacao:
            objeto["content"]["situacao"] = f"{situacao}"
        
        if statusCertidaoITBI:
            objeto["content"]["statusCertidaoITBI"] = f"{statusCertidaoITBI}"
           
        if tipoImovel:
            objeto["content"]["tipoImovel"] = f"{tipoImovel}"
        
        if dtVencimento:
            objeto["content"]["dtVencimento"] = f"{dtVencimento}"

        if anoTransferencia != None:
            objeto[0]["content"]["anoTransferencia"] = { "id": int(anoTransferencia) }       
            
        envio = api_post("transferenciaImoveis", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

transferenciaImoveis = transferenciaImoveis()