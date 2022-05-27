from samples import *
import json

class dividasMovtos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idAtoManutencao, comentario, dhEstorno, dhManutencao, dhMovimentacao, idDividas, dtEstornoInscricao, dataInscricao, 
                  dtValidadeAnistia, especificacoesManutencao, formasPagamentoPrestacaoDiversa, idHomologManutencao, idMotivoEstornoInscricao, idMotivoManutencao, nroParcelamento,
                  nroParcelas, nroProcesso,
                  nroProcessoManutencao, obsHomologManutencao, observacaoManutencao, percAnistiaCorrecao, percAnistiaJuro, percAnistiaMulta, percAnistiaSaldo, idScriptManutencao, 
                  situacaoAnterior, situacaoAtual, acoesDocumentos, tiposDocumentosDividas, 
                  tiposManutencoesDividas, tiposMovimentacoesDivida, nroDocumento, vlAnistiaCorrecao, vlAnistiaJuro, vlAnistiaMulta, vlAnistiaSaldo, vlCorrecao, vlInscrito, vlJuros,
                  valorMulta, vlPago, vlPrestacaoDiversa,
                  vlRemissaoSaldo, vlSaldo):
        try: 
            sql = """
                INSERT INTO dividasMovtos (                    
                    idIntegracao,                   
                    id_cloud, 
                    idAtoManutencao,
                    comentario,                                               
                    dhEstorno, 
                    dhManutencao,
                    dhMovimentacao,
                    dtEstornoInscricao,
                    especificacoesManutencao,
                    idDividas,
                    dtValidadeAnistia,                    
                    dataInscricao,
                    formasPagamentoPrestacaoDiversa,
                    idHomologManutencao,
                    idMotivoEstornoInscricao,
                    idMotivoManutencao,
                    nroParcelamento,
                    nroParcelas,
                    nroProcesso,
                    nroProcessoManutencao,
                    obsHomologManutencao,
                    observacaoManutencao, 
                    percAnistiaCorrecao,
                    percAnistiaJuro, 
                    percAnistiaSaldo,
                    percAnistiaMulta,
                    idScriptManutencao, 
                    situacaoAnterior, 
                    situacaoAtual,
                    acoesDocumentos,
                    tiposDocumentosDividas,
                    tiposManutencoesDividas,
                    tiposMovimentacoesDivida,
                    nroDocumento,
                    vlAnistiaCorrecao,
                    vlAnistiaJuro,
                    vlAnistiaMulta, 
                    vlAnistiaSaldo, 
                    vlCorrecao, 
                    vlInscrito, 
                    vlJuros, 
                    valorMulta, 
                    vlPago, 
                    vlPrestacaoDiversa, 
                    vlRemissaoSaldo,
                    vlSaldo
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idAtoManutencao)s,
                    %(comentario)s,
                    %(dhEstorno)s,
                    %(dhManutencao)s,
                    %(dhMovimentacao)s,
                    %(dtEstornoInscricao)s,
                    %(especificacoesManutencao)s,
                    %(idDividas)s,
                    %(dtValidadeAnistia)s,                    
                    %(dataInscricao)s,
                    %(formasPagamentoPrestacaoDiversa)s,
                    %(idHomologManutencao)s,
                    %(idMotivoEstornoInscricao)s,
                    %(idMotivoManutencao)s,
                    %(nroParcelamento)s,
                    %(nroProcessoManutencao)s,
                    %(nroProcesso)s,                    
                    %(nroParcelas)s,
                    %(nroProcessoManutencao)s,                    
                    %(obsHomologManutencao)s,
                    %(observacaoManutencao)s,
                    %(percAnistiaCorrecao)s,
                    %(percAnistiaJuro)s,
                    %(percAnistiaSaldo)s,
                    %(percAnistiaMulta)s,
                    %(idScriptManutencao)s,
                    %(situacaoAnterior)s,
                    %(situacaoAtual)s,
                    %(acoesDocumentos)s,                    
                    %(tiposDocumentosDividas)s,
                    %(tiposManutencoesDividas)s,
                    %(tiposMovimentacoesDivida)s,
                    %(nroDocumento)s,
                    %(vlAnistiaCorrecao)s,
                    %(vlAnistiaJuro)s,
                    %(vlAnistiaMulta)s,
                    %(vlAnistiaSaldo)s,
                    %(vlCorrecao)s,
                    %(vlInscrito)s,                    
                    %(vlJuros)s,
                    %(valorMulta)s,
                    %(vlPago)s,
                    %(vlPrestacaoDiversa)s,
                    %(vlRemissaoSaldo)s,
                    %(vlSaldo)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idAtoManutencao = idAtoManutencao,
                comentario = comentario,
                dhEstorno = dhEstorno,                               
                dhManutencao = dhManutencao,
                dhMovimentacao = dhMovimentacao,
                dtEstornoInscricao = dtEstornoInscricao,                               
                especificacoesManutencao = especificacoesManutencao,
                idDividas = idDividas,
                dtValidadeAnistia = dtValidadeAnistia,                                               
                dataInscricao = dataInscricao,
                formasPagamentoPrestacaoDiversa = formasPagamentoPrestacaoDiversa,                               
                idHomologManutencao = idHomologManutencao,
                idMotivoEstornoInscricao = idMotivoEstornoInscricao,               
                idMotivoManutencao = idMotivoManutencao,
                nroParcelamento = nroParcelamento,
                nroProcessoManutencao = nroProcessoManutencao,
                nroProcesso = nroProcesso,
                nroParcelas = nroParcelas,
                obsHomologManutencao = obsHomologManutencao,
                observacaoManutencao = observacaoManutencao, 
                percAnistiaCorrecao = percAnistiaCorrecao, 
                percAnistiaJuro = percAnistiaJuro, 
                percAnistiaSaldo = percAnistiaSaldo, 
                percAnistiaMulta = percAnistiaMulta, 
                idScriptManutencao = idScriptManutencao, 
                situacaoAnterior = situacaoAnterior, 
                situacaoAtual = situacaoAtual, 
                acoesDocumentos = acoesDocumentos, 
                tiposDocumentosDividas = tiposDocumentosDividas, 
                tiposManutencoesDividas = tiposManutencoesDividas, 
                tiposMovimentacoesDivida = tiposMovimentacoesDivida, 
                nroDocumento = nroDocumento,   
                vlAnistiaCorrecao = vlAnistiaCorrecao, 
                vlAnistiaJuro = vlAnistiaJuro, 
                vlAnistiaMulta = vlAnistiaMulta, 
                vlAnistiaSaldo = vlAnistiaSaldo, 
                vlCorrecao = vlCorrecao, 
                vlInscrito = vlInscrito, 
                vlJuros = vlJuros, 
                valorMulta = valorMulta, 
                vlPago = vlPago, 
                vlPrestacaoDiversa = vlPrestacaoDiversa, 
                vlRemissaoSaldo = vlRemissaoSaldo, 
                vlSaldo = vlSaldo
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {dividasMovtos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao inserir o anistias {dividasMovtos}. {contribuintesr}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM dividasMovtos"
            if not self.query(sql_s):
                send_log_warning(f"dividas não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM dividasMovtos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de exclusão do atividades econômicas. {contribuintesr}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM dividasMovtos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    dividasMovtos 
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
            sql = f"SELECT * FROM dividasMovtos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def db_list(self):
        try:
            sql = "SELECT * FROM dividasMovtos WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM dividasMovtos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def send_post(self, id, idAtoManutencao, comentario, dhEstorno, dhManutencao, dhMovimentacao, idDividas, dtEstornoInscricao, dataInscricao, 
                  dtValidadeAnistia, especificacoesManutencao, formasPagamentoPrestacaoDiversa, idHomologManutencao, idMotivoEstornoInscricao, idMotivoManutencao, nroParcelamento, nroParcelas, nroProcesso,
                  nroProcessoManutencao, obsHomologManutencao, observacaoManutencao, percAnistiaCorrecao, percAnistiaJuro, percAnistiaSaldo, percAnistiaMulta, idScriptManutencao, situacaoAnterior, situacaoAtual, acoesDocumentos, tiposDocumentosDividas, 
                  tiposManutencoesDividas, tiposMovimentacoesDivida, nroDocumento, vlAnistiaCorrecao, vlAnistiaJuro, vlAnistiaMulta, vlAnistiaSaldo, vlCorrecao, vlInscrito, vlJuros, valorMulta, vlPago,
                  vlPrestacaoDiversa, vlRemissaoSaldo, vlSaldo):
        objeto = {
            "idIntegracao": f"Atos{id}",
            "content": {}
        }
        if idAtoManutencao:
            objeto["content"]["VctoFeriado"] = { "id": int(idAtoManutencao)}
        
        if dhEstorno:
            objeto["content"]["dhEstorno"] = f"{dhEstorno}"
        
        if comentario:
            objeto["content"]["comentario"] = f"{comentario}"
        
        if dhManutencao:
            objeto["content"]["dhManutencao"] = f"{dhManutencao}"
        
        if idMotivoManutencao:
            objeto["content"]["idMotivoManutencao"] = { "id": int(idMotivoManutencao)}
        
        if nroParcelamento:
            objeto["content"]["nroParcelamento"] = f"{nroParcelamento}"
        
        if dhMovimentacao:
            objeto["content"]["dhMovimentacao"] = f"{dhMovimentacao}"
        
        if dtEstornoInscricao:
            objeto["content"]["dtEstornoInscricao"] = f"{dtEstornoInscricao}"
        
        if nroParcelas:
            objeto["content"]["nroParcelas"] = f"{nroParcelas}"       

        if obsHomologManutencao:
            objeto["content"]["obsHomologManutencao"] = f"{obsHomologManutencao}"

        if nroProcesso:
            objeto["content"]["nroProcesso"] = f"{nroProcesso}"

        if nroProcessoManutencao:
            objeto["content"]["nroProcessoManutencao"] = f"{nroProcessoManutencao}"

        if idDividas:
            objeto["content"]["idDividas"] = { "id": int(idDividas)}     

        if especificacoesManutencao:
            objeto["content"]["especificacoesManutencao"] = f"{especificacoesManutencao}"    

        if dtValidadeAnistia:
            objeto["content"]["dtValidadeAnistia"] = f"{dtValidadeAnistia}"

        if dataInscricao:
            objeto["content"]["dataInscricao"] = f"{dataInscricao}"

        if formasPagamentoPrestacaoDiversa:
            objeto["content"]["formasPagamentoPrestacaoDiversa"] = f"{formasPagamentoPrestacaoDiversa}"

        if observacaoManutencao:
            objeto["content"]["observacaoManutencao"] = f"{observacaoManutencao}"     

        if percAnistiaCorrecao:
            objeto["content"]["percAnistiaCorrecao"] = f"{percAnistiaCorrecao}"    

        if percAnistiaJuro:
            objeto["content"]["percAnistiaJuro"] = f"{percAnistiaJuro}"

        if percAnistiaSaldo:
            objeto["content"]["percAnistiaSaldo"] = f"{percAnistiaSaldo}"

        if percAnistiaMulta:
            objeto["content"]["percAnistiaMulta"] = f"{percAnistiaMulta}"  

        if idScriptManutencao:
            objeto["content"]["idScriptManutencao"] = { "id": int(idScriptManutencao)}

        if situacaoAnterior:
            objeto["content"]["situacaoAnterior"] = f"{situacaoAnterior}"

        if situacaoAtual:
            objeto["content"]["situacaoAtual"] = f"{situacaoAtual}"

        if acoesDocumentos:
            objeto["content"]["acoesDocumentos"] = f"{acoesDocumentos}"             
        
        if tiposDocumentosDividas:
            objeto["content"]["tiposDocumentosDividas"] = f"{tiposDocumentosDividas}"
        
        if tiposManutencoesDividas:
            objeto["content"]["tiposManutencoesDividas"] = f"{tiposManutencoesDividas}"

        if tiposMovimentacoesDivida:
            objeto["content"]["tiposMovimentacoesDivida"] = f"{tiposMovimentacoesDivida}"    

        if nroDocumento:
            objeto["content"]["nroDocumento"] = f"{nroDocumento}"

        if vlAnistiaCorrecao:
            objeto["content"]["vlAnistiaCorrecao"] = f"{vlAnistiaCorrecao}"

        if vlAnistiaJuro:
            objeto["content"]["vlAnistiaJuro"] = f"{vlAnistiaJuro}"  

        if vlAnistiaMulta:
            objeto["content"]["vlAnistiaMulta"] = f"{vlAnistiaMulta}"

        if vlAnistiaSaldo:
            objeto["content"]["vlAnistiaSaldo"] = f"{vlAnistiaSaldo}"

        if vlCorrecao:
            objeto["content"]["vlCorrecao"] = f"{vlCorrecao}"

        if vlInscrito:
            objeto["content"]["vlInscrito"] = f"{vlInscrito}"             
        
        if vlJuros:
            objeto["content"]["vlJuros"] = f"{vlJuros}"
        
        if valorMulta:
            objeto["content"]["percAnistiaCorrecao0"] = f"{valorMulta}"            
        
        if vlPago:
            objeto["content"]["vlPago"] = f"{vlPago}"
        
        if vlPrestacaoDiversa:
            objeto["content"]["vlPrestacaoDiversa"] = f"{vlPrestacaoDiversa}"      
        
        if vlRemissaoSaldo:
            objeto["content"]["vlRemissaoSaldo"] = f"{vlRemissaoSaldo}",
        
        if vlSaldo:
            objeto["content"]["vlSaldo"] = f"{vlSaldo}"
        
        if idMotivoEstornoInscricao != None:
            objeto[0]["calculotributario"]["creditotributario"] = { "id": int(idMotivoEstornoInscricao)}  
        
        if idHomologManutencao:
            objeto["content"]["idHomologManutencao"] = { "id": int(idHomologManutencao)}   

        envio = api_post("dividasMovtos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

dividasMovtos = dividasMovtos()