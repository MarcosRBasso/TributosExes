from samples import *
import json

class termosParcelamento(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idContribuinte, idParcelamento, idParcelamentoParcela, nroParcelamento, idConfigParcelamento, leiParcelamento, idCreditoTributario,
                 idGuia, 
                  idParcelamentoAnterior, idReceita, idEnderecoContribuinte, idTelefoneContribuinte, nroDocumento, intervalo, qtdParcelas, qtdParcelasOriginal, nroParcela, 
                  anoCredito,
                  nroProcesso, referente, vlRendaFamiliar, vlEntrada, percEntrada, vlCorrecaoPrefixada, ano, vlDesconto, vlJuroFinanciamento, vlParcela, vlReforco, vlTotalTaxa, 
                  valorReceita, valorDescontoReceita, valorCorrecao, valorDescontoCorrecao, valorJuro, valorDescontoJuro, valorMultaReceita, valorDescontoMulta, saldoParcela,
                  correcaoParcela, idDivida, juroParcela, valorMultaParcela,
                  totalAcrescimos, situacaoParcelamento, tipoEntrada, intervaloVencimento, possuiReforco, situacaoParcela, tipoCredito, dhParcelamento, dtVencimentoParcelamento):
        try: 
            sql = """
                INSERT INTO termosParcelamento (                    
                    idIntegracao,                   
                    id_cloud, 
                    idContribuinte,
                    idParcelamento,                                               
                    idParcelamentoParcela, 
                    nroParcelamento,
                    idConfigParcelamento,
                    idCreditoTributario,
                    idGuia,
                    leiParcelamento,
                    idParcelamentoAnterior,                    
                    idReceita,
                    idEnderecoContribuinte,
                    idTelefoneContribuinte,
                    nroDocumento,
                    intervalo,
                    qtdParcelas,
                    qtdParcelasOriginal,
                    nroParcela,
                    anoCredito,
                    nroProcesso,
                    referente,
                    vlRendaFamiliar, 
                    vlEntrada,
                    percEntrada, 
                    vlCorrecaoPrefixada,
                    ano,
                    vlDesconto, 
                    vlJuroFinanciamento, 
                    vlParcela,
                    vlReforco,
                    vlTotalTaxa,
                    valorReceita,
                    valorDescontoReceita,
                    valorCorrecao,
                    valorDescontoCorrecao,
                    valorJuro,
                    valorDescontoJuro, 
                    valorMultaReceita, 
                    valorDescontoMulta, 
                    saldoParcela, 
                    correcaoParcela, 
                    idDivida, 
                    juroParcela, 
                    valorMultaParcela, 
                    totalAcrescimos,
                    situacaoParcelamento,
                    tipoEntrada, 
                    intervaloVencimento, 
                    possuiReforco, 
                    situacaoParcela, 
                    tipoCredito, 
                    dhParcelamento, 
                    dtVencimentoParcelamento
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idContribuinte)s,
                    %(idParcelamento)s,
                    %(idParcelamentoParcela)s,
                    %(nroParcelamento)s,
                    %(idConfigParcelamento)s,
                    %(idCreditoTributario)s,
                    %(idGuia)s,
                    %(leiParcelamento)s,
                    %(idParcelamentoAnterior)s,                    
                    %(idReceita)s,
                    %(idEnderecoContribuinte)s,
                    %(idTelefoneContribuinte)s,
                    %(nroDocumento)s,
                    %(intervalo)s,
                    %(qtdParcelas)s,
                    %(qtdParcelasOriginal)s,
                    %(nroProcesso)s,
                    %(anoCredito)s,                    
                    %(nroParcela)s,
                    %(nroProcesso)s,                    
                    %(referente)s,
                    %(vlRendaFamiliar)s,
                    %(vlEntrada)s,
                    %(percEntrada)s,
                    %(vlCorrecaoPrefixada)s,
                    %(ano)s,
                    %(vlDesconto)s,
                    %(vlJuroFinanciamento)s,
                    %(vlParcela)s,
                    %(vlReforco)s,                    
                    %(vlTotalTaxa)s,
                    %(valorReceita)s,
                    %(valorDescontoReceita)s,
                    %(valorCorrecao)s,
                    %(valorDescontoCorrecao)s,
                    %(valorJuro)s,
                    %(valorDescontoJuro)s,
                    %(valorMultaReceita)s,
                    %(valorDescontoMulta)s,
                    %(saldoParcela)s,                    
                    %(correcaoParcela)s,
                    %(idDivida)s,
                    %(juroParcela)s,
                    %(valorMultaParcela)s,
                    %(totalAcrescimos)s,
                    %(situacaoParcelamento)s,
                    %(tipoEntrada)s, 
                    %(intervaloVencimento)s, 
                    %(possuiReforco)s, 
                    %(situacaoParcela)s, 
                    %(tipoCredito)s, 
                    %(dhParcelamento)s, 
                    %(dtVencimentoParcelamento)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idContribuinte = idContribuinte,
                idParcelamento = idParcelamento,
                idParcelamentoParcela = idParcelamentoParcela,                               
                nroParcelamento = nroParcelamento,
                idConfigParcelamento = idConfigParcelamento,
                idCreditoTributario = idCreditoTributario,                               
                idGuia = idGuia,
                leiParcelamento = leiParcelamento,
                idParcelamentoAnterior = idParcelamentoAnterior,                                               
                idReceita = idReceita,
                idEnderecoContribuinte = idEnderecoContribuinte,                               
                idTelefoneContribuinte = idTelefoneContribuinte,
                nroDocumento = nroDocumento,
                intervalo = intervalo,                               
                qtdParcelas = qtdParcelas,
                qtdParcelasOriginal = qtdParcelasOriginal,
                nroProcesso = nroProcesso,
                anoCredito = anoCredito,
                nroParcela = nroParcela,
                referente = referente,
                vlRendaFamiliar = vlRendaFamiliar, 
                vlEntrada = vlEntrada, 
                percEntrada = percEntrada, 
                vlCorrecaoPrefixada = vlCorrecaoPrefixada, 
                ano = ano, 
                vlDesconto = vlDesconto, 
                vlJuroFinanciamento = vlJuroFinanciamento, 
                vlParcela = vlParcela, 
                vlReforco = vlReforco, 
                vlTotalTaxa = vlTotalTaxa, 
                valorReceita = valorReceita, 
                valorDescontoReceita = valorDescontoReceita, 
                valorCorrecao = valorCorrecao,   
                valorDescontoCorrecao = valorDescontoCorrecao, 
                valorJuro = valorJuro, 
                valorDescontoJuro = valorDescontoJuro, 
                valorMultaReceita = valorMultaReceita, 
                valorDescontoMulta = valorDescontoMulta, 
                saldoParcela = saldoParcela, 
                correcaoParcela = correcaoParcela, 
                idDivida = idDivida, 
                juroParcela = juroParcela, 
                valorMultaParcela = valorMultaParcela, 
                totalAcrescimos = totalAcrescimos, 
                situacaoParcelamento = situacaoParcelamento,
                tipoEntrada = tipoEntrada, 
                intervaloVencimento = intervaloVencimento, 
                possuiReforco = possuiReforco, 
                situacaoParcela = situacaoParcela, 
                tipoCredito = tipoCredito, 
                dhParcelamento = dhParcelamento, 
                dtVencimentoParcelamento = dtVencimentoParcelamento
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {termosParcelamento} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao inserir o anistias {termosParcelamento}. {contribuintesr}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM termosParcelamento"
            if not self.query(sql_s):
                send_log_warning(f"termosParcelamento não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM termosParcelamento WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de exclusão do atividades econômicas. {contribuintesr}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM termosParcelamento WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    termosParcelamento 
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
            sql = f"SELECT * FROM termosParcelamento WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def db_list(self):
        try:
            sql = "SELECT * FROM termosParcelamento WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM termosParcelamento WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def send_post(self, id, idContribuinte, idParcelamento, idParcelamentoParcela, nroParcelamento, idConfigParcelamento, leiParcelamento, idCreditoTributario, idGuia, 
                  idParcelamentoAnterior, idReceita, idEnderecoContribuinte, idTelefoneContribuinte, nroDocumento, intervalo, qtdParcelas, qtdParcelasOriginal, nroParcela, anoCredito,
                  nroProcesso, referente, vlRendaFamiliar, vlEntrada, percEntrada, vlCorrecaoPrefixada, ano, vlDesconto, vlJuroFinanciamento, vlParcela, vlReforco, vlTotalTaxa, 
                  valorReceita, valorDescontoReceita, valorCorrecao, valorDescontoCorrecao, valorJuro, valorDescontoJuro, valorMultaReceita, valorDescontoMulta, saldoParcela, correcaoParcela, idDivida, juroParcela,
                  valorMultaParcela, totalAcrescimos, situacaoParcelamento, tipoEntrada, intervaloVencimento, possuiReforco, situacaoParcela, tipoCredito, dhParcelamento, 
                  dtVencimentoParcelamento):
        objeto = {
            "idIntegracao": f"Atos{id}",
            "content": {}
        }
        if tipoEntrada:
            objeto["content"]["tipoEntrada"] = f"{tipoEntrada}"

        if intervaloVencimento:
            objeto["content"]["intervaloVencimento"] = f"{intervaloVencimento}"

        if possuiReforco:
            objeto["content"]["possuiReforco"] = f"{possuiReforco}"     

        if situacaoParcela:
            objeto["content"]["situacaoParcela"] = f"{situacaoParcela}"    

        if tipoCredito:
            objeto["content"]["tipoCredito"] = f"{tipoCredito}"

        if dhParcelamento:
            objeto["content"]["dhParcelamento"] = f"{dhParcelamento}"

        if dtVencimentoParcelamento:
            objeto["content"]["dtVencimentoParcelamento"] = f"{dtVencimentoParcelamento}"  

        if idContribuinte:
            objeto["content"]["VctoFeriado"] = { "id": int(idContribuinte)}
        
        if idParcelamentoParcela:
            objeto["content"]["idParcelamentoParcela"] = { "id": int(idParcelamentoParcela)}
        
        if idParcelamento:
            objeto["content"]["idParcelamento"] = { "id": int(idParcelamento)}
        
        if nroParcelamento:
            objeto["content"]["nroParcelamento"] = { "id": int(nroParcelamento)}
        
        if qtdParcelas:
            objeto["content"]["qtdParcelas"] = f"{qtdParcelas}"
        
        if qtdParcelasOriginal:
            objeto["content"]["qtdParcelasOriginal"] = f"{qtdParcelasOriginal}"
        
        if idConfigParcelamento:
            objeto["content"]["idConfigParcelamento"] = { "id": int(idConfigParcelamento)}
        
        if idCreditoTributario:
            objeto["content"]["idCreditoTributario"] = { "id": int(idCreditoTributario)}
        
        if nroParcela:
            objeto["content"]["nroParcela"] = f"{nroParcela}"       

        if referente:
            objeto["content"]["referente"] = { "id": int(referente) }
        
        if intervalo:
            objeto["content"]["intervalo"] = f"{intervalo}" 

        if anoCredito:
            objeto["content"]["anoCredito"] = f"{anoCredito}"

        if nroProcesso:
            objeto["content"]["nroProcesso"] = f"{nroProcesso}"

        if leiParcelamento:
            objeto["content"]["leiParcelamento"] = f"{leiParcelamento}"     

        if idGuia:
            objeto["content"]["idGuia"] = { "id": int(idGuia)}    

        if idParcelamentoAnterior:
            objeto["content"]["idParcelamentoAnterior"] = { "id": int(idParcelamentoAnterior)}

        if idReceita:
            objeto["content"]["idReceita"] = { "id": int(idReceita)}

        if idEnderecoContribuinte:
            objeto["content"]["idEnderecoContribuinte"] = { "id": int(idEnderecoContribuinte)}

        if vlRendaFamiliar:
            objeto["content"]["vlRendaFamiliar"] = f"{vlRendaFamiliar}"     

        if vlEntrada:
            objeto["content"]["vlEntrada"] = f"{vlEntrada}"    

        if percEntrada:
            objeto["content"]["percEntrada"] = f"{percEntrada}"

        if vlCorrecaoPrefixada:
            objeto["content"]["vlCorrecaoPrefixada"] = f"{vlCorrecaoPrefixada}"

        if ano:
            objeto["content"]["ano"] = f"{ano}"  

        if vlDesconto:
            objeto["content"]["vlDesconto"] = { "id": int(vlDesconto)}

        if vlJuroFinanciamento:
            objeto["content"]["vlJuroFinanciamento"] = f"{vlJuroFinanciamento}"

        if vlParcela:
            objeto["content"]["vlParcela"] = f"{vlParcela}"

        if vlReforco:
            objeto["content"]["vlReforco"] = f"{vlReforco}"             
        
        if vlTotalTaxa:
            objeto["content"]["vlTotalTaxa"] = f"{vlTotalTaxa}"
        
        if valorReceita:
            objeto["content"]["valorReceita"] = f"{valorReceita}"

        if valorDescontoReceita:
            objeto["content"]["valorDescontoReceita"] = f"{valorDescontoReceita}"    

        if valorCorrecao:
            objeto["content"]["valorCorrecao"] = f"{valorCorrecao}"

        if valorDescontoCorrecao:
            objeto["content"]["valorDescontoCorrecao"] = f"{valorDescontoCorrecao}"

        if valorJuro:
            objeto["content"]["valorJuro"] = f"{valorJuro}"  

        if valorDescontoJuro:
            objeto["content"]["valorDescontoJuro"] = f"{valorDescontoJuro}"

        if valorMultaReceita:
            objeto["content"]["valorMultaReceita"] = f"{valorMultaReceita}"

        if valorDescontoMulta:
            objeto["content"]["valorDescontoMulta"] = f"{valorDescontoMulta}"

        if saldoParcela:
            objeto["content"]["saldoParcela"] = f"{saldoParcela}"             
        
        if correcaoParcela:
            objeto["content"]["correcaoParcela"] = f"{correcaoParcela}"
        
        if idDivida:
            objeto["content"]["vlEntrada0"] = { "id": int(idDivida)}            
        
        if juroParcela:
            objeto["content"]["juroParcela"] = f"{juroParcela}"
        
        if valorMultaParcela:
            objeto["content"]["valorMultaParcela"] = f"{valorMultaParcela}"      
        
        if totalAcrescimos:
            objeto["content"]["totalAcrescimos"] = f"{totalAcrescimos}",
        
        if situacaoParcelamento:
            objeto["content"]["situacaoParcelamento"] = f"{situacaoParcelamento}"
        
        if nroDocumento != None:
            objeto[0]["calculotributario"]["creditotributario"] = f"{nroDocumento}"  
        
        if idTelefoneContribuinte:
            objeto["content"]["idTelefoneContribuinte"] = { "id": int(idTelefoneContribuinte)}   

        envio = api_post("termosParcelamento", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

termosParcelamento = termosParcelamento()