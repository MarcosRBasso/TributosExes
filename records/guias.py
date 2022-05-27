from samples import *
import json

class guias(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idLancamentos, idConfiguracoesGeracaoParcelas, codigoBarrases, dataVcto, nroParcela, situacao, valorLancado, valorDesconto, 
                  unica, lancamentoEnglobado, complementar, idCompetencias, idPessoaAtual, valorPago, idPessoas, numeroBaixa, das, daf,
                  idPagamentos, valorCorrecaoPrefixada, valorJuroFinanciamento, parcelamentoDaf, nroOperacao, dataOperacao, dhLancamento, dhCancelamento, usuarioCancelamento, vlTotalTaxa,
                  dataCredito, dataMovimentacao, 
                  geradaPorDiferencaPagamento, origem, situacaoAnterior, nroProcesso, codigoBarras, representacaoNumerica, iGuias, idImovel, idEconomico, idReceitaDiversa, idReceitaDiversaLanctos,
                  idTransfImoveis, idNotaAvulsa, idContribuicaoMelhorias, idContribuicaoMelhoriasImoveis, idCreditoTributario, idObras, ano ):
        try: 
            sql = """
                INSERT INTO guias (                    
                    idIntegracao,                   
                    id_cloud, 
                    idLancamentos,
                    idConfiguracoesGeracaoParcelas,                                               
                    codigoBarrases, 
                    dataVcto,
                    nroParcela,
                    valorLancado,
                    valorDesconto,
                    situacao,
                    unica,                    
                    lancamentoEnglobado,
                    complementar,
                    idCompetencias,
                    idPessoaAtual,
                    valorPago,
                    idPessoas,
                    numeroBaixa,
                    das,
                    daf,
                    idPagamentos,
                    valorCorrecaoPrefixada,
                    valorJuroFinanciamento, 
                    parcelamentoDaf,
                    nroOperacao, 
                    dataOperacao,
                    dhLancamento,
                    dhCancelamento, 
                    usuarioCancelamento, 
                    vlTotalTaxa,
                    dataCredito,
                    dataMovimentacao,
                    das,
                    daf,
                    geradaPorDiferencaPagamento,
                    origem,
                    situacaoAnterior,
                    nroProcesso, 
                    codigoBarras, 
                    representacaoNumerica, 
                    iGuias, 
                    idImovel, 
                    idEconomico, 
                    idReceitaDiversa, 
                    idReceitaDiversaLanctos, 
                    idTransfImoveis,
                    idNotaAvulsa,
                    idContribuicaoMelhorias, 
                    idContribuicaoMelhoriasImoveis, 
                    idCreditoTributario, 
                    idObras, 
                    ano 
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idLancamentos)s,
                    %(idConfiguracoesGeracaoParcelas)s,
                    %(codigoBarrases)s,
                    %(dataVcto)s,
                    %(nroParcela)s,
                    %(valorLancado)s,
                    %(valorDesconto)s,
                    %(situacao)s,
                    %(unica)s,                    
                    %(lancamentoEnglobado)s,
                    %(complementar)s,
                    %(idCompetencias)s,
                    %(idPessoaAtual)s,
                    %(valorPago)s,
                    %(idPessoas)s,
                    %(numeroBaixa)s,
                    %(idPagamentos)s,
                    %(daf)s,                    
                    %(das)s,
                    %(idPagamentos)s,                    
                    %(valorCorrecaoPrefixada)s,
                    %(valorJuroFinanciamento)s,
                    %(parcelamentoDaf)s,
                    %(nroOperacao)s,
                    %(dataOperacao)s,
                    %(dhLancamento)s,
                    %(dhCancelamento)s,
                    %(usuarioCancelamento)s,
                    %(vlTotalTaxa)s,
                    %(dataCredito)s,                    
                    %(dataMovimentacao)s,
                    %(das)s,
                    %(daf)s,
                    %(geradaPorDiferencaPagamento)s,
                    %(origem)s,
                    %(situacaoAnterior)s,
                    %(nroProcesso)s,
                    %(codigoBarras)s,
                    %(representacaoNumerica)s,
                    %(iGuias)s,                    
                    %(idImovel)s,
                    %(idEconomico)s,
                    %(idReceitaDiversa)s,
                    %(idReceitaDiversaLanctos)s,
                    %(idTransfImoveis)s,
                    %(idNotaAvulsa)s,
                    %(idContribuicaoMelhorias)s, 
                    %(idContribuicaoMelhoriasImoveis)s, 
                    %(idCreditoTributario)s, 
                    %(idObras)s, 
                    %(ano)s 
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idLancamentos = idLancamentos,
                idConfiguracoesGeracaoParcelas = idConfiguracoesGeracaoParcelas,
                codigoBarrases = codigoBarrases,                               
                dataVcto = dataVcto,
                nroParcela = nroParcela,
                valorLancado = valorLancado,                               
                valorDesconto = valorDesconto,
                situacao = situacao,
                unica = unica,                                               
                lancamentoEnglobado = lancamentoEnglobado,
                complementar = complementar,                               
                idCompetencias = idCompetencias,
                idPessoaAtual = idPessoaAtual,
                valorPago = valorPago,                               
                idPessoas = idPessoas,
                numeroBaixa = numeroBaixa,
                idPagamentos = idPagamentos,
                daf = daf,
                das = das,
                valorCorrecaoPrefixada = valorCorrecaoPrefixada,
                valorJuroFinanciamento = valorJuroFinanciamento, 
                parcelamentoDaf = parcelamentoDaf, 
                nroOperacao = nroOperacao, 
                dataOperacao = dataOperacao, 
                dhLancamento = dhLancamento, 
                dhCancelamento = dhCancelamento, 
                usuarioCancelamento = usuarioCancelamento, 
                vlTotalTaxa = vlTotalTaxa, 
                dataCredito = dataCredito, 
                dataMovimentacao = dataMovimentacao, 
                geradaPorDiferencaPagamento = geradaPorDiferencaPagamento,   
                origem = origem, 
                situacaoAnterior = situacaoAnterior, 
                nroProcesso = nroProcesso, 
                codigoBarras = codigoBarras, 
                representacaoNumerica = representacaoNumerica, 
                iGuias = iGuias, 
                idImovel = idImovel, 
                idEconomico = idEconomico, 
                idReceitaDiversa = idReceitaDiversa, 
                idReceitaDiversaLanctos = idReceitaDiversaLanctos, 
                idTransfImoveis = idTransfImoveis, 
                idNotaAvulsa = idNotaAvulsa,
                idContribuicaoMelhorias = idContribuicaoMelhorias, 
                idContribuicaoMelhoriasImoveis = idContribuicaoMelhoriasImoveis, 
                idCreditoTributario = idCreditoTributario, 
                idObras = idObras, 
                ano = ano 
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {guias} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao inserir o anistias {guias}. {contribuintesr}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM guias"
            if not self.query(sql_s):
                send_log_warning(f"guias não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM guias WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de exclusão do atividades econômicas. {contribuintesr}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM guias WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    guias 
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
            sql = f"SELECT * FROM guias WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def db_list(self):
        try:
            sql = "SELECT * FROM guias WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM guias WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def send_post(self, id, idLancamentos, idConfiguracoesGeracaoParcelas, codigoBarrases, dataVcto, nroParcela, situacao, valorLancado, valorDesconto, 
                  unica, lancamentoEnglobado, complementar, idCompetencias, idPessoaAtual, valorPago, idPessoas, numeroBaixa, das, daf,
                  idPagamentos, valorCorrecaoPrefixada, valorJuroFinanciamento, parcelamentoDaf, nroOperacao, dataOperacao, dhLancamento, dhCancelamento, usuarioCancelamento, vlTotalTaxa, dataCredito, dataMovimentacao, 
                  geradaPorDiferencaPagamento, origem, situacaoAnterior, nroProcesso, codigoBarras, representacaoNumerica, iGuias, idImovel, idEconomico, idReceitaDiversa,
                  idReceitaDiversaLanctos, idTransfImoveis, idNotaAvulsa, idContribuicaoMelhorias, idContribuicaoMelhoriasImoveis, idCreditoTributario, idObras, ano ):
        objeto = {
            "idIntegracao": f"Atos{id}",
            "content": {}
        }
        if idObras:
            objeto["content"]["idObras"] = { "id": int(idObras)}
        
        if ano:
            objeto["content"]["ano"] = f"{ano}"

        if idContribuicaoMelhorias:
            objeto["content"]["idContribuicaoMelhorias"] = { "id": int(idContribuicaoMelhorias)}
        
        if idContribuicaoMelhoriasImoveis:
            objeto["content"]["idContribuicaoMelhoriasImoveis"] = { "id": int(idContribuicaoMelhoriasImoveis)}
        
        if idCreditoTributario:
            objeto["content"]["idCreditoTributario"] = { "id": int(idCreditoTributario)}

        if idLancamentos:
            objeto["content"]["VctoFeriado"] = { "id": int(idLancamentos)}
        
        if codigoBarrases:
            objeto["content"]["codigoBarrases"] = { "id": int(codigoBarrases)}
        
        if idConfiguracoesGeracaoParcelas:
            objeto["content"]["idConfiguracoesGeracaoParcelas"] = { "id": int(idConfiguracoesGeracaoParcelas)}
        
        if dataVcto:
            objeto["content"]["dataVcto"] = f"{dataVcto}"
        
        if idPessoas:
            objeto["content"]["idPessoas"] = { "id": int(idPessoas)}
        
        if numeroBaixa:
            objeto["content"]["numeroBaixa"] = f"{numeroBaixa}"
        
        if nroParcela:
            objeto["content"]["nroParcela"] = { "id": int(nroParcela)}
        
        if valorLancado:
            objeto["content"]["valorLancado"] = { "id": int(valorLancado)}    

        if valorCorrecaoPrefixada:
            objeto["content"]["valorCorrecaoPrefixada"] = f"{valorCorrecaoPrefixada}"
        
        if valorPago:
            objeto["content"]["valorPago"] = f"{valorPago}" 

        if idPagamentos:
            objeto["content"]["idPagamentos"] = { "id": int(idPagamentos)}

        if situacao:
            objeto["content"]["situacao"] = f"{situacao}"     

        if valorDesconto:
            objeto["content"]["valorDesconto"] = f"{valorDesconto}"    

        if unica:
            objeto["content"]["unica"] = f"{unica}"

        if lancamentoEnglobado:
            objeto["content"]["lancamentoEnglobado"] = f"{lancamentoEnglobado}"

        if complementar:
            objeto["content"]["complementar"] = f"{complementar}"

        if valorJuroFinanciamento:
            objeto["content"]["valorJuroFinanciamento"] = f"{valorJuroFinanciamento}"     

        if parcelamentoDaf:
            objeto["content"]["parcelamentoDaf"] = f"{parcelamentoDaf}"    

        if nroOperacao:
            objeto["content"]["nroOperacao"] = f"{nroOperacao}"

        if dataOperacao:
            objeto["content"]["dataOperacao"] = f"{dataOperacao}"

        if dhLancamento:
            objeto["content"]["dhLancamento"] = f"{dhLancamento}"  

        if dhCancelamento:
            objeto["content"]["dhCancelamento"] = f"{dhCancelamento}"

        if usuarioCancelamento:
            objeto["content"]["usuarioCancelamento"] = f"{usuarioCancelamento}"

        if vlTotalTaxa:
            objeto["content"]["vlTotalTaxa"] = f"{vlTotalTaxa}"

        if dataCredito:
            objeto["content"]["dataCredito"] = f"{dataCredito}"             
        
        if dataMovimentacao:
            objeto["content"]["dataMovimentacao"] = f"{dataMovimentacao}"
        
        if das:
            objeto["content"]["das"] = f"{das}"

        if daf:
            objeto["content"]["daf"] = f"{daf}"    

        if geradaPorDiferencaPagamento:
            objeto["content"]["geradaPorDiferencaPagamento"] = f"{geradaPorDiferencaPagamento}"

        if origem:
            objeto["content"]["origem"] = f"{origem}"

        if situacaoAnterior:
            objeto["content"]["situacaoAnterior"] = f"{situacaoAnterior}"  

        if nroProcesso:
            objeto["content"]["nroProcesso"] = { "id": int(nroProcesso)}

        if codigoBarras:
            objeto["content"]["codigoBarras"] = { "id": int(codigoBarras)}

        if representacaoNumerica:
            objeto["content"]["representacaoNumerica"] = { "id": int(representacaoNumerica)}

        if iGuias:
            objeto["content"]["iGuias"] = { "id": int(iGuias)}             
        
        if idImovel:
            objeto["content"]["idImovel"] = { "id": int(idImovel)}
        
        if idEconomico:
            objeto["content"]["parcelamentoDaf0"] = { "id": int(idEconomico)}            
        
        if idReceitaDiversa:
            objeto["content"]["idReceitaDiversa"] = { "id": int(idReceitaDiversa)}
        
        if idReceitaDiversaLanctos:
            objeto["content"]["idReceitaDiversaLanctos"] = { "id": int(idReceitaDiversaLanctos)}      
        
        if idTransfImoveis:
            objeto["content"]["idTransfImoveis"] = { "id": int(idTransfImoveis)}
        
        if idNotaAvulsa:
            objeto["content"]["idNotaAvulsa"] = { "id": int(idNotaAvulsa)}
        
        if idPessoaAtual != None:
            objeto[0]["calculotributario"]["creditotributario"] = { "id": int(idPessoaAtual)}  
        
        if idCompetencias:
            objeto["content"]["idCompetencias"] = { "id": int(idCompetencias)}   

        envio = api_post("guias", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

guias = guias()