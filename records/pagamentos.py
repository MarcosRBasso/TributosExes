from samples import *
import json

class pagamentos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idGuiasUnificadas, idPessoas, idBaixaManual, idBaixaAutomatica, idConvenio, idParcelamentoParcela, idGuia, numeroBaixa, 
                  dtPagamento, dhEstorno, dtCredito, dtPagamentoRetroativo, tipoBaixa, tipoPagamento, vlPago, vlCorrecao, vlJuro, vlMulta,
                  vlJuroFinanciamento, vlCorrecaoPreFixada, vlDiferenca, vlDescontoTributo, vlDescontoCorrecao, vlDescontoJuro, vlDescontoMulta, vlTributoDevido, vlCorrecaoDevido, 
                  vlJuroDevido, vlMultaDevido, vlJuroFinanciamentoDevido, idDivida,
                  vlCorrecaoPreFixadaDevido, vlTributoPago, usuarioEstorno, quitadoPorLimiteArrecadacao, saldoGerado, saldoUtilizado, situacaoSaldoAnterior, situacaoSaldoAtual):
        try: 
            sql = """
                INSERT INTO pagamentos (                    
                    idIntegracao,                   
                    id_cloud, 
                    idGuiasUnificadas,
                    idPessoas,                                               
                    idBaixaManual, 
                    idBaixaAutomatica,
                    idConvenio,
                    idGuia,
                    numeroBaixa,
                    idParcelamentoParcela,
                    dtPagamento,                    
                    dhEstorno,
                    dtCredito,
                    dtPagamentoRetroativo,
                    tipoBaixa,
                    tipoPagamento,
                    vlPago,
                    vlCorrecao,
                    vlJuro,
                    vlMulta,
                    vlJuroFinanciamento,
                    vlCorrecaoPreFixada,
                    vlDiferenca, 
                    vlDescontoTributo,
                    vlDescontoCorrecao, 
                    vlDescontoJuro,
                    vlDescontoMulta,
                    vlTributoDevido, 
                    vlCorrecaoDevido, 
                    vlJuroDevido,
                    vlMultaDevido,
                    vlJuroFinanciamentoDevido,
                    vlCorrecaoPreFixadaDevido,
                    vlTributoPago,
                    usuarioEstorno,
                    quitadoPorLimiteArrecadacao,
                    saldoGerado, 
                    saldoUtilizado, 
                    situacaoSaldoAnterior, 
                    situacaoSaldoAtual,
                    idDivida
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idGuiasUnificadas)s,
                    %(idPessoas)s,
                    %(idBaixaManual)s,
                    %(idBaixaAutomatica)s,
                    %(idConvenio)s,
                    %(idGuia)s,
                    %(numeroBaixa)s,
                    %(idParcelamentoParcela)s,
                    %(dtPagamento)s,                    
                    %(dhEstorno)s,
                    %(dtCredito)s,
                    %(dtPagamentoRetroativo)s,
                    %(tipoBaixa)s,
                    %(tipoPagamento)s,
                    %(vlPago)s,
                    %(vlCorrecao)s,
                    %(vlJuroFinanciamento)s,
                    %(vlMulta)s,                    
                    %(vlJuro)s,
                    %(vlJuroFinanciamento)s,                    
                    %(vlCorrecaoPreFixada)s,
                    %(vlDiferenca)s,
                    %(vlDescontoTributo)s,
                    %(vlDescontoCorrecao)s,
                    %(vlDescontoJuro)s,
                    %(vlDescontoMulta)s,
                    %(vlTributoDevido)s,
                    %(vlCorrecaoDevido)s,
                    %(vlJuroDevido)s,
                    %(vlMultaDevido)s,                    
                    %(vlJuroFinanciamentoDevido)s,
                    %(vlCorrecaoPreFixadaDevido)s,
                    %(vlTributoPago)s,
                    %(usuarioEstorno)s,
                    %(quitadoPorLimiteArrecadacao)s,
                    %(saldoGerado)s,
                    %(saldoUtilizado)s,
                    %(situacaoSaldoAnterior)s,
                    %(situacaoSaldoAtual)s,
                    %(idDivida)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idGuiasUnificadas = idGuiasUnificadas,
                idPessoas = idPessoas,
                idBaixaManual = idBaixaManual,                               
                idBaixaAutomatica = idBaixaAutomatica,
                idConvenio = idConvenio,
                idGuia = idGuia,                               
                numeroBaixa = numeroBaixa,
                idParcelamentoParcela = idParcelamentoParcela,
                dtPagamento = dtPagamento,                                               
                dhEstorno = dhEstorno,
                dtCredito = dtCredito,                               
                dtPagamentoRetroativo = dtPagamentoRetroativo,
                tipoBaixa = tipoBaixa,
                tipoPagamento = tipoPagamento,                               
                vlPago = vlPago,
                vlCorrecao = vlCorrecao,
                vlJuroFinanciamento = vlJuroFinanciamento,
                vlMulta = vlMulta,
                vlJuro = vlJuro,
                vlCorrecaoPreFixada = vlCorrecaoPreFixada,
                vlDiferenca = vlDiferenca, 
                vlDescontoTributo = vlDescontoTributo, 
                vlDescontoCorrecao = vlDescontoCorrecao, 
                vlDescontoJuro = vlDescontoJuro, 
                vlDescontoMulta = vlDescontoMulta, 
                vlTributoDevido = vlTributoDevido, 
                vlCorrecaoDevido = vlCorrecaoDevido, 
                vlJuroDevido = vlJuroDevido, 
                vlMultaDevido = vlMultaDevido, 
                vlJuroFinanciamentoDevido = vlJuroFinanciamentoDevido,
                vlCorrecaoPreFixadaDevido = vlCorrecaoPreFixadaDevido, 
                vlTributoPago = vlTributoPago,   
                usuarioEstorno = usuarioEstorno, 
                quitadoPorLimiteArrecadacao = quitadoPorLimiteArrecadacao, 
                saldoGerado = saldoGerado, 
                saldoUtilizado = saldoUtilizado, 
                situacaoSaldoAnterior = situacaoSaldoAnterior, 
                situacaoSaldoAtual = situacaoSaldoAtual,
                idDivida = idDivida
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {pagamentos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao inserir o anistias {pagamentos}. {contribuintesr}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM pagamentos"
            if not self.query(sql_s):
                send_log_warning(f"pagamentos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM pagamentos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de exclusão do atividades econômicas. {contribuintesr}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM pagamentos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    pagamentos 
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
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de atualização da atividades Economicas. {contribuintesr}")

    def db_search(self, id):
        try:
            sql = f"SELECT * FROM pagamentos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def db_list(self):
        try:
            sql = "SELECT * FROM pagamentos WHERE id_cloud is null"
            data = self.query(sql)
            if data:
                send_log_info("Consulta de todos os atividades Economicas realizada com sucesso.")
                return data
            return None
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def get_id_cloud(self, id):
        if (id == None):
            return None
        try:
            sql = f"SELECT id_cloud FROM pagamentos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def send_post(self, id, idGuiasUnificadas, idPessoas, idBaixaManual, idBaixaAutomatica, idConvenio, idParcelamentoParcela, idGuia, numeroBaixa, 
                  dtPagamento, dhEstorno, dtCredito, dtPagamentoRetroativo, tipoBaixa, tipoPagamento, vlPago, vlCorrecao, vlJuro, vlMulta,
                  vlJuroFinanciamento, vlCorrecaoPreFixada, vlDiferenca, vlDescontoTributo, vlDescontoCorrecao, vlDescontoJuro, vlDescontoMulta, vlTributoDevido, vlCorrecaoDevido, vlJuroDevido, vlMultaDevido, vlJuroFinanciamentoDevido, 
                  vlCorrecaoPreFixadaDevido, vlTributoPago, usuarioEstorno, quitadoPorLimiteArrecadacao, saldoGerado, saldoUtilizado, situacaoSaldoAnterior, situacaoSaldoAtual, idDivida):
        objeto = {
            "idIntegracao": f"Atos{id}",
            "content": {}
        }
        if idDivida:
            objeto["content"]["idDivida"] = { "id": int(idDivida)}

        if idGuiasUnificadas:
            objeto["content"]["idGuiasUnificadas"] = { "id": int(idGuiasUnificadas)}
        
        if idBaixaManual:
            objeto["content"]["idBaixaManual"] = { "id": int(idBaixaManual)}
        
        if idPessoas:
            objeto["content"]["idPessoas"] = { "id": int(idPessoas)}
        
        if idBaixaAutomatica:
            objeto["content"]["idBaixaAutomatica"] = { "id": int(idBaixaAutomatica)}
        
        if vlPago:
            objeto["content"]["vlPago"] = f"{vlPago}"
        
        if vlCorrecao:
            objeto["content"]["vlCorrecao"] = f"{vlCorrecao}"
        
        if idConvenio:
            objeto["content"]["idConvenio"] = { "id": int(idConvenio)}
        
        if idGuia:
            objeto["content"]["idGuia"] = { "id": int(idGuia)}
        
        if vlJuro:
            objeto["content"]["vlJuro"] = f"{vlJuro}"       

        if vlCorrecaoPreFixada:
            objeto["content"]["vlCorrecaoPreFixada"] = f"{vlCorrecaoPreFixada}"
        
        if tipoPagamento:
            objeto["content"]["tipoPagamento"] = f"{tipoPagamento}" 

        if vlMulta:
            objeto["content"]["vlMulta"] = f"{vlMulta}"

        if vlJuroFinanciamento:
            objeto["content"]["vlJuroFinanciamento"] = f"{vlJuroFinanciamento}"

        if idParcelamentoParcela:
            objeto["content"]["idParcelamentoParcela"] = { "id": int(idParcelamentoParcela)}     

        if numeroBaixa:
            objeto["content"]["numeroBaixa"] = { "id": int(numeroBaixa)}    

        if dtPagamento:
            objeto["content"]["dtPagamento"] = f"{dtPagamento}"

        if dhEstorno:
            objeto["content"]["dhEstorno"] = f"{dhEstorno}"

        if dtCredito:
            objeto["content"]["dtCredito"] = f"{dtCredito}"

        if vlDiferenca:
            objeto["content"]["vlDiferenca"] = f"{vlDiferenca}"     

        if vlDescontoTributo:
            objeto["content"]["vlDescontoTributo"] = f"{vlDescontoTributo}"    

        if vlDescontoCorrecao:
            objeto["content"]["vlDescontoCorrecao"] = f"{vlDescontoCorrecao}"

        if vlDescontoJuro:
            objeto["content"]["vlDescontoJuro"] = f"{vlDescontoJuro}"

        if vlDescontoMulta:
            objeto["content"]["vlDescontoMulta"] = f"{vlDescontoMulta}"  

        if vlTributoDevido:
            objeto["content"]["vlTributoDevido"] = f"{vlTributoDevido}"

        if vlCorrecaoDevido:
            objeto["content"]["vlCorrecaoDevido"] = f"{vlCorrecaoDevido}"

        if vlJuroDevido:
            objeto["content"]["vlJuroDevido"] = f"{vlJuroDevido}"

        if vlMultaDevido:
            objeto["content"]["vlMultaDevido"] = f"{vlMultaDevido}"             
        
        if vlJuroFinanciamentoDevido:
            objeto["content"]["vlJuroFinanciamentoDevido"] = f"{vlJuroFinanciamentoDevido}"
        
        if vlCorrecaoPreFixadaDevido:
            objeto["content"]["vlCorrecaoPreFixadaDevido"] = f"{vlCorrecaoPreFixadaDevido}"    

        if vlTributoPago:
            objeto["content"]["vlTributoPago"] = f"{vlTributoPago}"

        if usuarioEstorno:
            objeto["content"]["usuarioEstorno"] = f"{usuarioEstorno}"

        if quitadoPorLimiteArrecadacao:
            objeto["content"]["quitadoPorLimiteArrecadacao"] = f"{quitadoPorLimiteArrecadacao}"  

        if saldoGerado:
            objeto["content"]["saldoGerado"] = f"{saldoGerado}"

        if saldoUtilizado:
            objeto["content"]["saldoUtilizado"] = f"{saldoUtilizado}"

        if situacaoSaldoAnterior:
            objeto["content"]["situacaoSaldoAnterior"] = f"{situacaoSaldoAnterior}"

        if situacaoSaldoAtual:
            objeto["content"]["situacaoSaldoAtual"] = f"{situacaoSaldoAtual}"             
                
        if tipoBaixa != None:
            objeto[0]["calculotributario"]["creditotributario"] = f"{tipoBaixa}"  
        
        if dtPagamentoRetroativo:
            objeto["content"]["dtPagamentoRetroativo"] = f"{dtPagamentoRetroativo}"   

        envio = api_post("pagamentos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, nsure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

pagamentos = pagamentos()