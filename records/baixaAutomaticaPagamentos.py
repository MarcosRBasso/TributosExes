from samples import *
import json

class baixaAutomaticaPagamentos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idBaixaAutomatica, idCredito, dataCredito, dataPagamento, dataVencto, idGuiaUnificada, idLancamento, inconsistencia, inscrita, 
                  nroBaixa, dhTermino, parcela, idReferente, tipoLancamento, tipoPagamento, valorDiferenca, valorPago):
        try:
            sql = """
                INSERT INTO baixaAutomaticaPagamentos (                    
                    idIntegracao,                   
                    id_cloud, 
                    idBaixaAutomatica,
                    idCredito,                                               
                    dataCredito, 
                    dataVencto,
                    idGuiaUnificada,
                    idLancamento,
                    inscrita,
                    dataPagamento,
                    nroBaixa,                    
                    dhTermino,
                    parcela,
                    idReferente,
                    inconsistencia,
                    tipoLancamento,
                    tipoPagamento,
                    valorDiferenca,
                    valorPago                   
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idBaixaAutomatica)s,
                    %(idCredito)s,
                    %(dataCredito)s,
                    %(dataVencto)s,
                    %(idGuiaUnificada)s,
                    %(idLancamento)s,
                    %(inscrita)s,
                    %(dataPagamento)s,
                    %(nroBaixa)s,                    
                    %(dhTermino)s,
                    %(parcela)s,
                    %(idReferente)s,
                    %(inconsistencia)s,
                    %(tipoLancamento)s,
                    %(tipoPagamento)s,
                    %(valorDiferenca)s,
                    %(valorPago)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idBaixaAutomatica = idBaixaAutomatica,
                idCredito = idCredito,
                dataCredito = dataCredito,                               
                dataVencto = dataVencto,
                idGuiaUnificada = idGuiaUnificada,
                idLancamento = idLancamento,                               
                inscrita = inscrita,
                dataPagamento = dataPagamento,
                nroBaixa = nroBaixa,                                               
                dhTermino = dhTermino,
                parcela = parcela,                               
                idReferente = idReferente,
                inconsistencia = inconsistencia,
                tipoLancamento = tipoLancamento,                               
                tipoPagamento = tipoPagamento,
                valorDiferenca = valorDiferenca,
                valorPago = valorPago
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {baixaAutomaticaPagamentos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {baixaAutomaticaPagamentos}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM baixaAutomaticaPagamentos"
            if not self.query(sql_s):
                send_log_warning(f"baixaAutomaticaPagamentos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM baixaAutomaticaPagamentos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM baixaAutomaticaPagamentos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    baixaAutomaticaPagamentos 
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
            sql = f"SELECT * FROM baixaAutomaticaPagamentos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM baixaAutomaticaPagamentos WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM baixaAutomaticaPagamentos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idBaixaAutomatica, dataCredito, dataPagamento, dataVencto, idGuiaUnificada, idLancamento, inconsistencia, inscrita, 
                  nroBaixa, dhTermino, parcela, idReferente, tipoLancamento, tipoPagamento, valorDiferenca, valorPago):
        objeto = {
            "idIntegracao": f"baixaAutomaticaPagamentos{id}",
            "content": {}                                 
        }
        if nroBaixa:
            objeto["content"]["nroBaixa"] = f"{nroBaixa}"
        
        if dataCredito:
            objeto["content"]["dataCredito"] = f"{dataCredito}"
        
        if inconsistencia:
            objeto["content"]["inconsistencia"] = f"{inconsistencia}"
        
        if parcela:
            objeto["content"]["parcela"] = f"{parcela}"
        
        if dataVencto:
            objeto["content"]["dataVencto"] = f"{dataVencto}" 

        if dataPagamento:
            objeto["content"]["dataPagamento"] = f"{dataPagamento}"  

        if inscrita:
            objeto["content"]["inscrita"] = f"{inscrita}"
        
        if tipoLancamento:
            objeto["content"]["tipoLancamento"] = f"{tipoLancamento}"
        
        if valorDiferenca:
            objeto["content"]["valorDiferenca"] = f"{valorDiferenca}"
        
        if tipoPagamento:
            objeto["content"]["tipoPagamento"] = f"{tipoPagamento}"
        
        if valorPago:
            objeto["content"]["valorPago"] = f"{valorPago}" 

        if arquivo:
            objeto["content"]["arquivo"] = f"{arquivo}"
        
        if dhTermino:
            objeto["content"]["dhTermino"] = f"{dhTermino}"        

        if idBaixaAutomatica != None:
            objeto[0]["content"]["BaixaAutomatica"] = { "id": int(idBaixaAutomatica) }               

        if idLancamento != None:
            objeto[0]["content"]["Lancamento"] = { "id": int(idLancamento) }

        if idReferente != None:
            objeto[0]["content"]["Referente"] = { "id": int(idReferente) }
                    
        if idGuiaUnificada != None:
            objeto[0]["content"]["GuiaUnificada"] = { "id": int(idGuiaUnificada) }
        
        envio = api_post("baixaAutomaticaPagamentos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

baixaAutomaticaPagamentos = baixaAutomaticaPagamentos()