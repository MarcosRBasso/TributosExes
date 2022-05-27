from samples import *
import json

class dividas(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idPessoa, idReceitaDiversaLancto, idEconomico, idContribMelhoriaImovel, idCreditoTributario, idSimulacao, idGuia, idImovel, 
                  dataVencimento, dataInscricao, dataLancamento, livro, folha, inscricao, posicao, processoInscricao, situacaoDivida, valorInscrito,
                  valorCorrecao, valorJuro, valorMulta, guiaComplementar, parcela, anoLivro, ano, idMotivoEstorno, dataEstorno, processoEstorno, usuarioEstorno, idContribuicaoMelhoria, 
                  das, daf, codDeclaracaoSimples, valorSaldo, simplesNacional, idNotaAvulsa, idIndexador, idReceitasDiversas, idTransferenciaImoveis, idObras, idDivida, penhora, possuiCdaEmitida,
                  anoCda, nroCda):
        try: 
            sql = """
                INSERT INTO dividas (                    
                    idIntegracao,                   
                    id_cloud, 
                    idPessoa,
                    idReceitaDiversaLancto,                                               
                    idEconomico, 
                    idContribMelhoriaImovel,
                    idCreditoTributario,
                    idGuia,
                    idImovel,
                    idSimulacao,
                    dataVencimento,                    
                    dataInscricao,
                    dataLancamento,
                    livro,
                    folha,
                    inscricao,
                    posicao,
                    processoInscricao,
                    situacaoDivida,
                    valorInscrito,
                    valorCorrecao,
                    valorJuro,
                    valorMulta, 
                    guiaComplementar,
                    parcela, 
                    anoLivro,
                    ano,
                    idMotivoEstorno, 
                    dataEstorno, 
                    processoEstorno,
                    usuarioEstorno,
                    idContribuicaoMelhoria,
                    das,
                    daf,
                    codDeclaracaoSimples,
                    valorSaldo,
                    simplesNacional,
                    idNotaAvulsa, 
                    idIndexador, 
                    idReceitasDiversas, 
                    idTransferenciaImoveis, 
                    idObras, 
                    idDivida, 
                    penhora, 
                    possuiCdaEmitida, 
                    anoCda,
                    nroCda
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idPessoa)s,
                    %(idReceitaDiversaLancto)s,
                    %(idEconomico)s,
                    %(idContribMelhoriaImovel)s,
                    %(idCreditoTributario)s,
                    %(idGuia)s,
                    %(idImovel)s,
                    %(idSimulacao)s,
                    %(dataVencimento)s,                    
                    %(dataInscricao)s,
                    %(dataLancamento)s,
                    %(livro)s,
                    %(folha)s,
                    %(inscricao)s,
                    %(posicao)s,
                    %(processoInscricao)s,
                    %(valorCorrecao)s,
                    %(valorInscrito)s,                    
                    %(situacaoDivida)s,
                    %(valorCorrecao)s,                    
                    %(valorJuro)s,
                    %(valorMulta)s,
                    %(guiaComplementar)s,
                    %(parcela)s,
                    %(anoLivro)s,
                    %(ano)s,
                    %(idMotivoEstorno)s,
                    %(dataEstorno)s,
                    %(processoEstorno)s,
                    %(usuarioEstorno)s,                    
                    %(idContribuicaoMelhoria)s,
                    %(das)s,
                    %(daf)s,
                    %(codDeclaracaoSimples)s,
                    %(valorSaldo)s,
                    %(simplesNacional)s,
                    %(idNotaAvulsa)s,
                    %(idIndexador)s,
                    %(idReceitasDiversas)s,
                    %(idTransferenciaImoveis)s,                    
                    %(idObras)s,
                    %(idDivida)s,
                    %(penhora)s,
                    %(possuiCdaEmitida)s,
                    %(anoCda)s,
                    %(nroCda)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idPessoa = idPessoa,
                idReceitaDiversaLancto = idReceitaDiversaLancto,
                idEconomico = idEconomico,                               
                idContribMelhoriaImovel = idContribMelhoriaImovel,
                idCreditoTributario = idCreditoTributario,
                idGuia = idGuia,                               
                idImovel = idImovel,
                idSimulacao = idSimulacao,
                dataVencimento = dataVencimento,                                               
                dataInscricao = dataInscricao,
                dataLancamento = dataLancamento,                               
                livro = livro,
                folha = folha,
                inscricao = inscricao,                               
                posicao = posicao,
                processoInscricao = processoInscricao,
                valorCorrecao = valorCorrecao,
                valorInscrito = valorInscrito,
                situacaoDivida = situacaoDivida,
                valorJuro = valorJuro,
                valorMulta = valorMulta, 
                guiaComplementar = guiaComplementar, 
                parcela = parcela, 
                anoLivro = anoLivro, 
                ano = ano, 
                idMotivoEstorno = idMotivoEstorno, 
                dataEstorno = dataEstorno, 
                processoEstorno = processoEstorno, 
                usuarioEstorno = usuarioEstorno, 
                idContribuicaoMelhoria = idContribuicaoMelhoria, 
                das = das, 
                daf = daf, 
                codDeclaracaoSimples = codDeclaracaoSimples,   
                valorSaldo = valorSaldo, 
                simplesNacional = simplesNacional, 
                idNotaAvulsa = idNotaAvulsa, 
                idIndexador = idIndexador, 
                idReceitasDiversas = idReceitasDiversas, 
                idTransferenciaImoveis = idTransferenciaImoveis, 
                idObras = idObras, 
                idDivida = idDivida, 
                penhora = penhora, 
                possuiCdaEmitida = possuiCdaEmitida, 
                anoCda = anoCda, 
                nroCda = nroCda
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {dividas} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao inserir o anistias {dividas}. {contribuintesr}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM dividas"
            if not self.query(sql_s):
                send_log_warning(f"dividas não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM dividas WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de exclusão do atividades econômicas. {contribuintesr}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM dividas WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    dividas 
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
            sql = f"SELECT * FROM dividas WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def db_list(self):
        try:
            sql = "SELECT * FROM dividas WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM dividas WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def send_post(self, id, idPessoa, idReceitaDiversaLancto, idEconomico, idContribMelhoriaImovel, idCreditoTributario, idSimulacao, idGuia, idImovel, 
                  dataVencimento, dataInscricao, dataLancamento, livro, folha, inscricao, posicao, processoInscricao, situacaoDivida, valorInscrito,
                  valorCorrecao, valorJuro, valorMulta, guiaComplementar, parcela, anoLivro, ano, idMotivoEstorno, dataEstorno, processoEstorno, usuarioEstorno, idContribuicaoMelhoria, 
                  das, daf, codDeclaracaoSimples, valorSaldo, simplesNacional, idNotaAvulsa, idIndexador, idReceitasDiversas, idTransferenciaImoveis, idObras, idDivida, penhora,
                  possuiCdaEmitida, anoCda, nroCda):
        objeto = {
            "idIntegracao": f"Atos{id}",
            "content": {}
        }
        if idPessoa:
            objeto["content"]["VctoFeriado"] = { "id": int(idPessoa)}
        
        if idEconomico:
            objeto["content"]["idEconomico"] = { "id": int(idEconomico)}
        
        if idReceitaDiversaLancto:
            objeto["content"]["idReceitaDiversaLancto"] = { "id": int(idReceitaDiversaLancto)}
        
        if idContribMelhoriaImovel:
            objeto["content"]["idContribMelhoriaImovel"] = { "id": int(idContribMelhoriaImovel)}
        
        if posicao:
            objeto["content"]["posicao"] = f"{posicao}"
        
        if processoInscricao:
            objeto["content"]["processoInscricao"] = f"{processoInscricao}"
        
        if idCreditoTributario:
            objeto["content"]["idCreditoTributario"] = { "id": int(idCreditoTributario)}
        
        if idGuia:
            objeto["content"]["idGuia"] = { "id": int(idGuia)}
        
        if situacaoDivida:
            objeto["content"]["situacaoDivida"] = f"{situacaoDivida}"       

        if valorJuro:
            objeto["content"]["valorJuro"] = { "id": int(valorJuro) }
        
        if inscricao:
            objeto["content"]["inscricao"] = f"{inscricao}" 

        if valorInscrito:
            objeto["content"]["valorInscrito"] = f"{valorInscrito}"

        if valorCorrecao:
            objeto["content"]["valorCorrecao"] = f"{valorCorrecao}"

        if idSimulacao:
            objeto["content"]["idSimulacao"] = { "id": int(idSimulacao)}     

        if idImovel:
            objeto["content"]["idImovel"] = { "id": int(idImovel)}    

        if dataVencimento:
            objeto["content"]["dataVencimento"] = f"{dataVencimento}"

        if dataInscricao:
            objeto["content"]["dataInscricao"] = f"{dataInscricao}"

        if dataLancamento:
            objeto["content"]["dataLancamento"] = f"{dataLancamento}"

        if valorMulta:
            objeto["content"]["valorMulta"] = f"{valorMulta}"     

        if guiaComplementar:
            objeto["content"]["guiaComplementar"] = f"{guiaComplementar}"    

        if parcela:
            objeto["content"]["parcela"] = f"{parcela}"

        if anoLivro:
            objeto["content"]["anoLivro"] = f"{anoLivro}"

        if ano:
            objeto["content"]["ano"] = f"{ano}"  

        if idMotivoEstorno:
            objeto["content"]["idMotivoEstorno"] = { "id": int(idMotivoEstorno)}

        if dataEstorno:
            objeto["content"]["dataEstorno"] = f"{dataEstorno}"

        if processoEstorno:
            objeto["content"]["processoEstorno"] = f"{processoEstorno}"

        if usuarioEstorno:
            objeto["content"]["usuarioEstorno"] = f"{usuarioEstorno}"             
        
        if idContribuicaoMelhoria:
            objeto["content"]["idContribuicaoMelhoria"] = { "id": int(idContribuicaoMelhoria)}
        
        if das:
            objeto["content"]["das"] = f"{das}"

        if daf:
            objeto["content"]["daf"] = f"{daf}"    

        if codDeclaracaoSimples:
            objeto["content"]["codDeclaracaoSimples"] = f"{codDeclaracaoSimples}"

        if valorSaldo:
            objeto["content"]["valorSaldo"] = f"{valorSaldo}"

        if simplesNacional:
            objeto["content"]["simplesNacional"] = f"{simplesNacional}"  

        if idNotaAvulsa:
            objeto["content"]["idNotaAvulsa"] = { "id": int(idNotaAvulsa)}

        if idIndexador:
            objeto["content"]["idIndexador"] = { "id": int(idIndexador)}

        if idReceitasDiversas:
            objeto["content"]["idReceitasDiversas"] = { "id": int(idReceitasDiversas)}

        if idTransferenciaImoveis:
            objeto["content"]["idTransferenciaImoveis"] = { "id": int(idTransferenciaImoveis)}             
        
        if idObras:
            objeto["content"]["idObras"] = { "id": int(idObras)}
        
        if idDivida:
            objeto["content"]["guiaComplementar0"] = { "id": int(idDivida)}            
        
        if penhora:
            objeto["content"]["penhora"] = f"{penhora}"
        
        if possuiCdaEmitida:
            objeto["content"]["possuiCdaEmitida"] = f"{possuiCdaEmitida}"      
        
        if anoCda:
            objeto["content"]["anoCda"] = f"{anoCda}",
        
        if nroCda:
            objeto["content"]["nroCda"] = f"{nroCda}"
        
        if folha != None:
            objeto[0]["calculotributario"]["creditotributario"] = f"{folha}"  
        
        if livro:
            objeto["content"]["livro"] = f"{livro}"   

        envio = api_post("dividas", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

dividas = dividas()