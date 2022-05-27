from samples import *
import json

class pagamentosDetalhados(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idPagamento, tipoReceitaPagamento, idParcelamentoParcela, idEconomico, idCreditoTributario, idReceitaDiversaLanctos, idGuia, idImovel, 
                  idTransfImoveis, idContribuicaoMelhorias, idContribuicaoMelhoriasImoveis, idPessoas, dataVctoOriginal, complementar, valorAnistiadoCorrecao, valorPagoIndexador, 
                  valorAnistiadoJuros, valorAnistiadoLancado,
                  valorAnistiadoMulta, valorDescontoConcedidoCorrecao, valorDescontoConcedidoJuros, valorDescontoConcedidoLancado, valorDescontoConcedidoMulta, valorDescontoCorrecao, 
                  ano, valorDescontoJuros, valorDescontoLancado, valorDescontoMulta, valorDevidoCorrecao, idContribuicaoMelhoria, 
                  valorDevidoJuros, valorDevidoLancado, valorDevidoMulta, valorDiferencaCorrecao, valorDiferencaJuros, idNotaAvulsa, valorDiferencaMulta, idReceitasDiversa, 
                  valorDiferencaTributo, idObras, idDivida, valorPagoCorrecao, valorPagoCorrecaoParcelada,
                  valorPagoJuros, valorPagoJurosParcelado, valorPagoLancado, valorPagoMulta, valorPagoMultaParcelada, valorRemidoCorrecao, valorRemidoJuros, valorRemidoLancado, 
                  valorRemidoMulta, valorDevidoJuroParcelado, valorDevidoMultaParcelado, valorDevidoCorrecaoParcelado, outrosDescCorrecao, outrosDescJuros, outrosDescMulta, 
                  outrosDescLancado):
        try: 
            sql = """
                INSERT INTO pagamentosDetalhados (                    
                    idIntegracao,                   
                    id_cloud, 
                    idPagamento,
                    tipoReceitaPagamento,                                               
                    idParcelamentoParcela, 
                    idEconomico,
                    idCreditoTributario,
                    idGuia,
                    idImovel,
                    idReceitaDiversaLanctos,
                    idTransfImoveis,                    
                    idContribuicaoMelhorias,
                    idContribuicaoMelhoriasImoveis,
                    idPessoas,
                    dataVctoOriginal,
                    complementar,
                    valorAnistiadoCorrecao,
                    valorPagoIndexador,
                    valorAnistiadoJuros,
                    valorAnistiadoLancado,
                    valorAnistiadoMulta,
                    valorDescontoConcedidoCorrecao,
                    valorDescontoConcedidoJuros, 
                    valorDescontoConcedidoLancado,
                    valorDescontoConcedidoMulta, 
                    valorDescontoCorrecao,
                    ano,
                    valorDescontoJuros, 
                    valorDescontoLancado, 
                    valorDescontoMulta,
                    valorDevidoCorrecao,
                    idContribuicaoMelhoria,
                    valorDevidoJuros,
                    valorDevidoLancado,
                    valorDevidoMulta,
                    valorDiferencaCorrecao,
                    valorDiferencaJuros,
                    idNotaAvulsa, 
                    valorDiferencaMulta, 
                    idReceitasDiversa, 
                    valorDiferencaTributo, 
                    idObras, 
                    idDivida, 
                    valorPagoCorrecao, 
                    valorPagoCorrecaoParcelada, 
                    valorPagoJuros,
                    valorPagoJurosParcelado,
                    valorPagoLancado, 
                    valorPagoMulta, 
                    valorPagoMultaParcelada, 
                    valorRemidoCorrecao, 
                    valorRemidoJuros, 
                    valorRemidoLancado, 
                    valorRemidoMulta, 
                    valorDevidoJuroParcelado, 
                    valorDevidoMultaParcelado, 
                    valorDevidoCorrecaoParcelado, 
                    outrosDescCorrecao, 
                    outrosDescJuros, 
                    outrosDescMulta, 
                    outrosDescLancado
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idPagamento)s,
                    %(tipoReceitaPagamento)s,
                    %(idParcelamentoParcela)s,
                    %(idEconomico)s,
                    %(idCreditoTributario)s,
                    %(idGuia)s,
                    %(idImovel)s,
                    %(idReceitaDiversaLanctos)s,
                    %(idTransfImoveis)s,                    
                    %(idContribuicaoMelhorias)s,
                    %(idContribuicaoMelhoriasImoveis)s,
                    %(idPessoas)s,
                    %(dataVctoOriginal)s,
                    %(complementar)s,
                    %(valorAnistiadoCorrecao)s,
                    %(valorPagoIndexador)s,
                    %(valorAnistiadoMulta)s,
                    %(valorAnistiadoLancado)s,                    
                    %(valorAnistiadoJuros)s,
                    %(valorAnistiadoMulta)s,                    
                    %(valorDescontoConcedidoCorrecao)s,
                    %(valorDescontoConcedidoJuros)s,
                    %(valorDescontoConcedidoLancado)s,
                    %(valorDescontoConcedidoMulta)s,
                    %(valorDescontoCorrecao)s,
                    %(ano)s,
                    %(valorDescontoJuros)s,
                    %(valorDescontoLancado)s,
                    %(valorDescontoMulta)s,
                    %(valorDevidoCorrecao)s,                    
                    %(idContribuicaoMelhoria)s,
                    %(valorDevidoJuros)s,
                    %(valorDevidoLancado)s,
                    %(valorDevidoMulta)s,
                    %(valorDiferencaCorrecao)s,
                    %(valorDiferencaJuros)s,
                    %(idNotaAvulsa)s,
                    %(valorDiferencaMulta)s,
                    %(idReceitasDiversa)s,
                    %(valorDiferencaTributo)s,                    
                    %(idObras)s,
                    %(idDivida)s,
                    %(valorPagoCorrecao)s,
                    %(valorPagoCorrecaoParcelada)s,
                    %(valorPagoJuros)s,
                    %(valorPagoJurosParcelado)s,
                    %(valorPagoLancado)s, 
                    %(valorPagoMulta)s, 
                    %(valorPagoMultaParcelada)s, 
                    %(valorRemidoCorrecao)s, 
                    %(valorRemidoJuros)s, 
                    %(valorRemidoLancado)s, 
                    %(valorRemidoMulta)s, 
                    %(valorDevidoJuroParcelado)s, 
                    %(valorDevidoMultaParcelado)s, 
                    %(valorDevidoCorrecaoParcelado)s, 
                    %(outrosDescCorrecao)s, 
                    %(outrosDescJuros)s, 
                    %(outrosDescMulta)s, 
                    %(outrosDescLancado)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idPagamento = idPagamento,
                tipoReceitaPagamento = tipoReceitaPagamento,
                idParcelamentoParcela = idParcelamentoParcela,                               
                idEconomico = idEconomico,
                idCreditoTributario = idCreditoTributario,
                idGuia = idGuia,                               
                idImovel = idImovel,
                idReceitaDiversaLanctos = idReceitaDiversaLanctos,
                idTransfImoveis = idTransfImoveis,                                               
                idContribuicaoMelhorias = idContribuicaoMelhorias,
                idContribuicaoMelhoriasImoveis = idContribuicaoMelhoriasImoveis,                               
                idPessoas = idPessoas,
                dataVctoOriginal = dataVctoOriginal,
                complementar = complementar,                               
                valorAnistiadoCorrecao = valorAnistiadoCorrecao,
                valorPagoIndexador = valorPagoIndexador,
                valorAnistiadoMulta = valorAnistiadoMulta,
                valorAnistiadoLancado = valorAnistiadoLancado,
                valorAnistiadoJuros = valorAnistiadoJuros,
                valorDescontoConcedidoCorrecao = valorDescontoConcedidoCorrecao,
                valorDescontoConcedidoJuros = valorDescontoConcedidoJuros, 
                valorDescontoConcedidoLancado = valorDescontoConcedidoLancado, 
                valorDescontoConcedidoMulta = valorDescontoConcedidoMulta, 
                valorDescontoCorrecao = valorDescontoCorrecao, 
                ano = ano, 
                valorDescontoJuros = valorDescontoJuros, 
                valorDescontoLancado = valorDescontoLancado, 
                valorDescontoMulta = valorDescontoMulta, 
                valorDevidoCorrecao = valorDevidoCorrecao, 
                idContribuicaoMelhoria = idContribuicaoMelhoria, 
                valorDevidoJuros = valorDevidoJuros, 
                valorDevidoLancado = valorDevidoLancado, 
                valorDevidoMulta = valorDevidoMulta,   
                valorDiferencaCorrecao = valorDiferencaCorrecao, 
                valorDiferencaJuros = valorDiferencaJuros, 
                idNotaAvulsa = idNotaAvulsa, 
                valorDiferencaMulta = valorDiferencaMulta, 
                idReceitasDiversa = idReceitasDiversa, 
                valorDiferencaTributo = valorDiferencaTributo, 
                idObras = idObras, 
                idDivida = idDivida, 
                valorPagoCorrecao = valorPagoCorrecao, 
                valorPagoCorrecaoParcelada = valorPagoCorrecaoParcelada, 
                valorPagoJuros = valorPagoJuros, 
                valorPagoJurosParcelado = valorPagoJurosParcelado,
                valorPagoLancado = valorPagoLancado, 
                valorPagoMulta = valorPagoMulta, 
                valorPagoMultaParcelada = valorPagoMultaParcelada, 
                valorRemidoCorrecao = valorRemidoCorrecao, 
                valorRemidoJuros = valorRemidoJuros, 
                valorRemidoLancado = valorRemidoLancado, 
                valorRemidoMulta = valorRemidoMulta, 
                valorDevidoJuroParcelado = valorDevidoJuroParcelado, 
                valorDevidoMultaParcelado = valorDevidoMultaParcelado, 
                valorDevidoCorrecaoParcelado = valorDevidoCorrecaoParcelado, 
                outrosDescCorrecao = outrosDescCorrecao, 
                outrosDescJuros = outrosDescJuros, 
                outrosDescMulta = outrosDescMulta, 
                outrosDescLancado = outrosDescLancado
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {pagamentosDetalhados} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao inserir o anistias {pagamentosDetalhados}. {contribuintesr}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM pagamentosDetalhados"
            if not self.query(sql_s):
                send_log_warning(f"pagamentosDetalhados não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM pagamentosDetalhados WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de exclusão do atividades econômicas. {contribuintesr}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM pagamentosDetalhados WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    pagamentosDetalhados 
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
            sql = f"SELECT * FROM pagamentosDetalhados WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def db_list(self):
        try:
            sql = "SELECT * FROM pagamentosDetalhados WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM pagamentosDetalhados WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def send_post(self, id, idPagamento, tipoReceitaPagamento, idParcelamentoParcela, idEconomico, idCreditoTributario, idReceitaDiversaLanctos, idGuia, idImovel, 
                  idTransfImoveis, idContribuicaoMelhorias, idContribuicaoMelhoriasImoveis, idPessoas, dataVctoOriginal, complementar, valorAnistiadoCorrecao, valorPagoIndexador, valorAnistiadoJuros, valorAnistiadoLancado,
                  valorAnistiadoMulta, valorDescontoConcedidoCorrecao, valorDescontoConcedidoJuros, valorDescontoConcedidoLancado, valorDescontoConcedidoMulta, valorDescontoCorrecao, ano, valorDescontoJuros, valorDescontoLancado, valorDescontoMulta, valorDevidoCorrecao, idContribuicaoMelhoria, 
                  valorDevidoJuros, valorDevidoLancado, valorDevidoMulta, valorDiferencaCorrecao, valorDiferencaJuros, idNotaAvulsa, valorDiferencaMulta, idReceitasDiversa, valorDiferencaTributo, idObras, idDivida, valorPagoCorrecao,
                  valorPagoCorrecaoParcelada, valorPagoJuros, valorPagoJurosParcelado, valorPagoLancado, valorPagoMulta, valorPagoMultaParcelada, valorRemidoCorrecao, valorRemidoJuros, valorRemidoLancado, 
                  valorRemidoMulta, valorDevidoJuroParcelado, valorDevidoMultaParcelado, valorDevidoCorrecaoParcelado, outrosDescCorrecao, outrosDescJuros, outrosDescMulta, 
                  outrosDescLancado):
        objeto = {
            "idIntegracao": f"Atos{id}",
            "content": {}
        }
        if valorDevidoCorrecaoParcelado:
            objeto["content"]["valorDevidoCorrecaoParcelado"] = f"{valorDevidoCorrecaoParcelado}"

        if outrosDescCorrecao:
            objeto["content"]["outrosDescCorrecao"] = f"{outrosDescCorrecao}"

        if outrosDescJuros:
            objeto["content"]["outrosDescJuros"] = f"{outrosDescJuros}"

        if outrosDescMulta:
            objeto["content"]["outrosDescMulta"] = f"{outrosDescMulta}" 

        if valorPagoLancado:
            objeto["content"]["valorPagoLancado"] = f"{valorPagoLancado}"

        if valorPagoMulta:
            objeto["content"]["valorPagoMulta"] = f"{valorPagoMulta}"

        if valorPagoMultaParcelada:
            objeto["content"]["valorPagoMultaParcelada"] = f"{valorPagoMultaParcelada}"

        if valorRemidoCorrecao:
            objeto["content"]["valorRemidoCorrecao"] = f"{valorRemidoCorrecao}"     

        if valorRemidoJuros:
            objeto["content"]["valorRemidoJuros"] = f"{valorRemidoJuros}"    

        if valorRemidoMulta:
            objeto["content"]["valorRemidoMulta"] = f"{valorRemidoMulta}"

        if valorDevidoJuroParcelado:
            objeto["content"]["valorDevidoJuroParcelado"] = f"{valorDevidoJuroParcelado}"

        if valorDevidoMultaParcelado:
            objeto["content"]["valorDevidoMultaParcelado"] = f"{valorDevidoMultaParcelado}"  

        if idPagamento:
            objeto["content"]["VctoFeriado"] = { "id": int(idPagamento)}
        
        if idParcelamentoParcela:
            objeto["content"]["idParcelamentoParcela"] = { "id": int(idParcelamentoParcela)}
        
        if tipoReceitaPagamento:
            objeto["content"]["tipoReceitaPagamento"] = { "id": int(tipoReceitaPagamento)}
        
        if idEconomico:
            objeto["content"]["idEconomico"] = { "id": int(idEconomico)}
        
        if valorAnistiadoCorrecao:
            objeto["content"]["valorAnistiadoCorrecao"] = f"{valorAnistiadoCorrecao}"
        
        if valorPagoIndexador:
            objeto["content"]["valorPagoIndexador"] = f"{valorPagoIndexador}"
        
        if idCreditoTributario:
            objeto["content"]["idCreditoTributario"] = { "id": int(idCreditoTributario)}
        
        if idGuia:
            objeto["content"]["idGuia"] = { "id": int(idGuia)}
        
        if valorAnistiadoJuros:
            objeto["content"]["valorAnistiadoJuros"] = f"{valorAnistiadoJuros}"       

        if valorDescontoConcedidoCorrecao:
            objeto["content"]["valorDescontoConcedidoCorrecao"] = { "id": int(valorDescontoConcedidoCorrecao) }
        
        if complementar:
            objeto["content"]["complementar"] = f"{complementar}" 

        if valorAnistiadoLancado:
            objeto["content"]["valorAnistiadoLancado"] = f"{valorAnistiadoLancado}"

        if valorAnistiadoMulta:
            objeto["content"]["valorAnistiadoMulta"] = f"{valorAnistiadoMulta}"

        if idReceitaDiversaLanctos:
            objeto["content"]["idReceitaDiversaLanctos"] = { "id": int(idReceitaDiversaLanctos)}     

        if idImovel:
            objeto["content"]["idImovel"] = { "id": int(idImovel)}    

        if idTransfImoveis:
            objeto["content"]["idTransfImoveis"] = f"{idTransfImoveis}"

        if idContribuicaoMelhorias:
            objeto["content"]["idContribuicaoMelhorias"] = f"{idContribuicaoMelhorias}"

        if idContribuicaoMelhoriasImoveis:
            objeto["content"]["idContribuicaoMelhoriasImoveis"] = f"{idContribuicaoMelhoriasImoveis}"

        if valorDescontoConcedidoJuros:
            objeto["content"]["valorDescontoConcedidoJuros"] = f"{valorDescontoConcedidoJuros}"     

        if valorDescontoConcedidoLancado:
            objeto["content"]["valorDescontoConcedidoLancado"] = f"{valorDescontoConcedidoLancado}"    

        if valorDescontoConcedidoMulta:
            objeto["content"]["valorDescontoConcedidoMulta"] = f"{valorDescontoConcedidoMulta}"

        if valorDescontoCorrecao:
            objeto["content"]["valorDescontoCorrecao"] = f"{valorDescontoCorrecao}"

        if ano:
            objeto["content"]["ano"] = f"{ano}"  

        if valorDescontoJuros:
            objeto["content"]["valorDescontoJuros"] = { "id": int(valorDescontoJuros)}

        if valorDescontoLancado:
            objeto["content"]["valorDescontoLancado"] = f"{valorDescontoLancado}"

        if valorDescontoMulta:
            objeto["content"]["valorDescontoMulta"] = f"{valorDescontoMulta}"

        if valorDevidoCorrecao:
            objeto["content"]["valorDevidoCorrecao"] = f"{valorDevidoCorrecao}"             
        
        if idContribuicaoMelhoria:
            objeto["content"]["idContribuicaoMelhoria"] = { "id": int(idContribuicaoMelhoria)}
        
        if valorDevidoJuros:
            objeto["content"]["valorDevidoJuros"] = f"{valorDevidoJuros}"

        if valorDevidoLancado:
            objeto["content"]["valorDevidoLancado"] = f"{valorDevidoLancado}"    

        if valorDevidoMulta:
            objeto["content"]["valorDevidoMulta"] = f"{valorDevidoMulta}"

        if valorDiferencaCorrecao:
            objeto["content"]["valorDiferencaCorrecao"] = f"{valorDiferencaCorrecao}"

        if valorDiferencaJuros:
            objeto["content"]["valorDiferencaJuros"] = f"{valorDiferencaJuros}"  

        if idNotaAvulsa:
            objeto["content"]["idNotaAvulsa"] = { "id": int(idNotaAvulsa)}

        if valorDiferencaMulta:
            objeto["content"]["valorDiferencaMulta"] = { "id": int(valorDiferencaMulta)}

        if idReceitasDiversa:
            objeto["content"]["idReceitasDiversa"] = { "id": int(idReceitasDiversa)}

        if valorDiferencaTributo:
            objeto["content"]["valorDiferencaTributo"] = { "id": int(valorDiferencaTributo)}             
        
        if idObras:
            objeto["content"]["idObras"] = { "id": int(idObras)}
        
        if idDivida:
            objeto["content"]["valorDescontoConcedidoLancado0"] = { "id": int(idDivida)}            
        
        if valorPagoCorrecao:
            objeto["content"]["valorPagoCorrecao"] = f"{valorPagoCorrecao}"
        
        if valorPagoCorrecaoParcelada:
            objeto["content"]["valorPagoCorrecaoParcelada"] = f"{valorPagoCorrecaoParcelada}"      
        
        if valorPagoJuros:
            objeto["content"]["valorPagoJuros"] = f"{valorPagoJuros}",
        
        if valorPagoJurosParcelado:
            objeto["content"]["valorPagoJurosParcelado"] = f"{valorPagoJurosParcelado}"
        
        if dataVctoOriginal != None:
            objeto[0]["calculotributario"]["creditotributario"] = f"{dataVctoOriginal}"  
        
        if idPessoas:
            objeto["content"]["idPessoas"] = f"{idPessoas}"   

        envio = api_post("pagamentosDetalhados", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

pagamentosDetalhados = pagamentosDetalhados()