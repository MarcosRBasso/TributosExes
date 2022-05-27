from samples import *
import json

class notasAvulsas(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idEconomicoPrestador, idEconomicoTomador, idPrestador, idRequerente, idTomador, idMotivo, numeroNota, apartamentoTomador, 
                  bairroTomador, blocoTomador, cepTomador, complementoTomador, condominioTomador, cpfCnpjPrestador, cpfCnpjTomador, descricaoEnderecoTomador, distritoTomador, 
                  enderecoObsTomador,
                  inscricaoMunicipalPrestador, inscricaoMunicipalTomador, logradouroTomador, loteamentoTomador, municipioTomador, nomePrestador, nomeRequerente, nomeTomador, 
                  numeroTomador, serie, modelo, 
                  numeroEmpenho, dataEmissao, dataEmpenho, outrasDeducoes, qtdDependentes, totalDeducoes, totalNotaFiscal, baseCalcIrrf, valorCofins, valorCsll, 
                  valorInss, valorInssRecolher, valorInssRecolhido, valorIrrf, valorIssqn, valorLiquido, valorPisPasep, valorSestSenat, valorTotalReducao, valorTotalServicos, 
                  vlPorDependente, vlPorPensaoAlimenticia, vlTotalDependentes, lancamentoGerado, situacaoNota):
        try: 
            sql = """
                INSERT INTO notasAvulsas (                    
                    idIntegracao,                   
                    id_cloud, 
                    idEconomicoPrestador,
                    idEconomicoTomador,                                               
                    idPrestador, 
                    idRequerente,
                    idTomador,
                    numeroNota,
                    apartamentoTomador,
                    idMotivo,
                    bairroTomador,                    
                    blocoTomador,
                    cepTomador,
                    complementoTomador,
                    condominioTomador,
                    cpfCnpjPrestador,
                    cpfCnpjTomador,
                    descricaoEnderecoTomador,
                    distritoTomador,
                    enderecoObsTomador,
                    inscricaoMunicipalPrestador,
                    inscricaoMunicipalTomador,
                    logradouroTomador, 
                    loteamentoTomador,
                    municipioTomador, 
                    nomePrestador,
                    nomeRequerente,
                    nomeTomador, 
                    numeroTomador, 
                    serie,
                    modelo,
                    numeroEmpenho,
                    dataEmissao,
                    dataEmpenho,
                    outrasDeducoes,
                    qtdDependentes,
                    totalDeducoes,
                    totalNotaFiscal, 
                    baseCalcIrrf, 
                    valorCofins, 
                    valorCsll, 
                    valorInss, 
                    valorInssRecolher, 
                    valorInssRecolhido, 
                    valorIrrf, 
                    valorIssqn,
                    valorLiquido,
                    valorPisPasep, 
                    valorSestSenat, 
                    valorTotalReducao, 
                    valorTotalServicos, 
                    vlPorDependente, 
                    vlPorPensaoAlimenticia, 
                    vlTotalDependentes, 
                    lancamentoGerado, 
                    situacaoNota
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idEconomicoPrestador)s,
                    %(idEconomicoTomador)s,
                    %(idPrestador)s,
                    %(idRequerente)s,
                    %(idTomador)s,
                    %(numeroNota)s,
                    %(apartamentoTomador)s,
                    %(idMotivo)s,
                    %(bairroTomador)s,                    
                    %(blocoTomador)s,
                    %(cepTomador)s,
                    %(complementoTomador)s,
                    %(condominioTomador)s,
                    %(cpfCnpjPrestador)s,
                    %(cpfCnpjTomador)s,
                    %(descricaoEnderecoTomador)s,
                    %(inscricaoMunicipalPrestador)s,
                    %(enderecoObsTomador)s,                    
                    %(distritoTomador)s,                  
                    %(inscricaoMunicipalTomador)s,
                    %(logradouroTomador)s,
                    %(loteamentoTomador)s,
                    %(municipioTomador)s,
                    %(nomePrestador)s,
                    %(nomeRequerente)s,
                    %(nomeTomador)s,
                    %(numeroTomador)s,
                    %(serie)s,
                    %(modelo)s,                    
                    %(numeroEmpenho)s,
                    %(dataEmissao)s,
                    %(dataEmpenho)s,
                    %(outrasDeducoes)s,
                    %(qtdDependentes)s,
                    %(totalDeducoes)s,
                    %(totalNotaFiscal)s,
                    %(baseCalcIrrf)s,
                    %(valorCofins)s,
                    %(valorCsll)s,                    
                    %(valorInss)s,
                    %(valorInssRecolher)s,
                    %(valorInssRecolhido)s,
                    %(valorIrrf)s,
                    %(valorIssqn)s,
                    %(valorLiquido)s,
                    %(valorPisPasep)s, 
                    %(valorSestSenat)s, 
                    %(valorTotalReducao)s, 
                    %(valorTotalServicos)s, 
                    %(vlPorDependente)s, 
                    %(vlPorPensaoAlimenticia)s, 
                    %(vlTotalDependentes)s, 
                    %(lancamentoGerado)s, 
                    %(situacaoNota)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idEconomicoPrestador = idEconomicoPrestador,
                idEconomicoTomador = idEconomicoTomador,
                idPrestador = idPrestador,                               
                idRequerente = idRequerente,
                idTomador = idTomador,
                numeroNota = numeroNota,                               
                apartamentoTomador = apartamentoTomador,
                idMotivo = idMotivo,
                bairroTomador = bairroTomador,                                               
                blocoTomador = blocoTomador,
                cepTomador = cepTomador,                               
                complementoTomador = complementoTomador,
                condominioTomador = condominioTomador,
                cpfCnpjPrestador = cpfCnpjPrestador,                               
                cpfCnpjTomador = cpfCnpjTomador,
                descricaoEnderecoTomador = descricaoEnderecoTomador,
                inscricaoMunicipalPrestador = inscricaoMunicipalPrestador,
                enderecoObsTomador = enderecoObsTomador,
                distritoTomador = distritoTomador,
                inscricaoMunicipalTomador = inscricaoMunicipalTomador,
                logradouroTomador = logradouroTomador, 
                loteamentoTomador = loteamentoTomador, 
                municipioTomador = municipioTomador, 
                nomePrestador = nomePrestador, 
                nomeRequerente = nomeRequerente, 
                nomeTomador = nomeTomador, 
                numeroTomador = numeroTomador, 
                serie = serie, 
                modelo = modelo, 
                numeroEmpenho = numeroEmpenho, 
                dataEmissao = dataEmissao, 
                dataEmpenho = dataEmpenho, 
                outrasDeducoes = outrasDeducoes,   
                qtdDependentes = qtdDependentes, 
                totalDeducoes = totalDeducoes, 
                totalNotaFiscal = totalNotaFiscal, 
                baseCalcIrrf = baseCalcIrrf, 
                valorCofins = valorCofins, 
                valorCsll = valorCsll, 
                valorInss = valorInss, 
                valorInssRecolher = valorInssRecolher, 
                valorInssRecolhido = valorInssRecolhido, 
                valorIrrf = valorIrrf, 
                valorIssqn = valorIssqn, 
                valorLiquido = valorLiquido,
                valorPisPasep = valorPisPasep, 
                valorSestSenat = valorSestSenat, 
                valorTotalReducao = valorTotalReducao, 
                valorTotalServicos = valorTotalServicos, 
                vlPorDependente = vlPorDependente, 
                vlPorPensaoAlimenticia = vlPorPensaoAlimenticia, 
                vlTotalDependentes = vlTotalDependentes, 
                lancamentoGerado = lancamentoGerado, 
                situacaoNota = situacaoNota
             )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {notasAvulsas} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao inserir o anistias {notasAvulsas}. {contribuintesr}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM notasAvulsas"
            if not self.query(sql_s):
                send_log_warning(f"notasAvulsas não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM notasAvulsas WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de exclusão do atividades econômicas. {contribuintesr}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM notasAvulsas WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    notasAvulsas 
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
            sql = f"SELECT * FROM notasAvulsas WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def db_list(self):
        try:
            sql = "SELECT * FROM notasAvulsas WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM notasAvulsas WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def send_post(self, id, idEconomicoPrestador, idEconomicoTomador, idPrestador, idRequerente, idTomador, idMotivo, numeroNota, apartamentoTomador, 
                  bairroTomador, blocoTomador, cepTomador, complementoTomador, condominioTomador, cpfCnpjPrestador, cpfCnpjTomador, descricaoEnderecoTomador, distritoTomador, enderecoObsTomador,
                  inscricaoMunicipalPrestador, inscricaoMunicipalTomador, logradouroTomador, loteamentoTomador, municipioTomador, nomePrestador, nomeRequerente, nomeTomador, numeroTomador, serie, modelo, numeroEmpenho, 
                  dataEmissao, dataEmpenho, outrasDeducoes, qtdDependentes, totalDeducoes, totalNotaFiscal, baseCalcIrrf, valorCofins, valorCsll, valorInss, valorInssRecolher, valorInssRecolhido,
                  valorIrrf, valorIssqn, valorLiquido,valorPisPasep, valorSestSenat, valorTotalReducao, valorTotalServicos, 
                  vlPorDependente, vlPorPensaoAlimenticia, vlTotalDependentes, lancamentoGerado, situacaoNota):
        objeto = {
            "idIntegracao": f"Atos{id}",
            "content": {}
        }
        if situacaoNota:
            objeto["content"]["situacaoNota"] = f"{situacaoNota}"

        if valorPisPasep:
            objeto["content"]["valorPisPasep"] = f"{valorPisPasep}"

        if valorSestSenat:
            objeto["content"]["valorSestSenat"] = f"{valorSestSenat}"

        if valorTotalReducao:
            objeto["content"]["valorTotalReducao"] = f"{valorTotalReducao}"

        if valorTotalServicos:
            objeto["content"]["valorTotalServicos"] = f"{valorTotalServicos}"     

        if vlPorDependente:
            objeto["content"]["vlPorDependente"] = f"{vlPorDependente}"    

        if vlPorPensaoAlimenticia:
            objeto["content"]["vlPorPensaoAlimenticia"] = f"{vlPorPensaoAlimenticia}"

        if vlTotalDependentes:
            objeto["content"]["vlTotalDependentes"] = f"{vlTotalDependentes}"

        if lancamentoGerado:
            objeto["content"]["lancamentoGerado"] = f"{lancamentoGerado}"  

        if idEconomicoPrestador:
            objeto["content"]["VctoFeriado"] = { "id": int(idEconomicoPrestador)}
        
        if idPrestador:
            objeto["content"]["idPrestador"] = { "id": int(idPrestador)}
        
        if idEconomicoTomador:
            objeto["content"]["idEconomicoTomador"] = { "id": int(idEconomicoTomador)}
        
        if idRequerente:
            objeto["content"]["idRequerente"] = { "id": int(idRequerente)}
        
        if cpfCnpjTomador:
            objeto["content"]["cpfCnpjTomador"] = f"{cpfCnpjTomador}"
        
        if descricaoEnderecoTomador:
            objeto["content"]["descricaoEnderecoTomador"] = f"{descricaoEnderecoTomador}"
        
        if idTomador:
            objeto["content"]["idTomador"] = { "id": int(idTomador)}
        
        if numeroNota:
            objeto["content"]["numeroNota"] = { "id": int(numeroNota)}
        
        if distritoTomador:
            objeto["content"]["distritoTomador"] = f"{distritoTomador}"       

        if inscricaoMunicipalTomador:
            objeto["content"]["inscricaoMunicipalTomador"] = { "id": int(inscricaoMunicipalTomador) }
        
        if cpfCnpjPrestador:
            objeto["content"]["cpfCnpjPrestador"] = f"{cpfCnpjPrestador}" 

        if enderecoObsTomador:
            objeto["content"]["enderecoObsTomador"] = f"{enderecoObsTomador}"

        if inscricaoMunicipalPrestador:
            objeto["content"]["inscricaoMunicipalPrestador"] = f"{inscricaoMunicipalPrestador}"

        if idMotivo:
            objeto["content"]["idMotivo"] = { "id": int(idMotivo)}     

        if apartamentoTomador:
            objeto["content"]["apartamentoTomador"] = f"{apartamentoTomador}"    

        if bairroTomador:
            objeto["content"]["bairroTomador"] = f"{bairroTomador}"

        if blocoTomador:
            objeto["content"]["blocoTomador"] = f"{blocoTomador}"

        if cepTomador:
            objeto["content"]["cepTomador"] = f"{cepTomador}"

        if logradouroTomador:
            objeto["content"]["logradouroTomador"] = f"{logradouroTomador}"     

        if loteamentoTomador:
            objeto["content"]["loteamentoTomador"] = f"{loteamentoTomador}"    

        if municipioTomador:
            objeto["content"]["municipioTomador"] = f"{municipioTomador}"

        if nomePrestador:
            objeto["content"]["nomePrestador"] = f"{nomePrestador}"

        if nomeRequerente:
            objeto["content"]["nomeRequerente"] = f"{nomeRequerente}"  

        if nomeTomador:
            objeto["content"]["nomeTomador"] = f"{nomeTomador}"

        if numeroTomador:
            objeto["content"]["numeroTomador"] = f"{numeroTomador}"

        if serie:
            objeto["content"]["serie"] = f"{serie}"

        if modelo:
            objeto["content"]["modelo"] = f"{modelo}"             
        
        if numeroEmpenho:
            objeto["content"]["numeroEmpenho"] = { "id": int(numeroEmpenho)}
        
        if dataEmissao:
            objeto["content"]["dataEmissao"] = f"{dataEmissao}"

        if dataEmpenho:
            objeto["content"]["dataEmpenho"] = f"{dataEmpenho}"    

        if outrasDeducoes:
            objeto["content"]["outrasDeducoes"] = f"{outrasDeducoes}"

        if qtdDependentes:
            objeto["content"]["qtdDependentes"] = f"{qtdDependentes}"

        if totalDeducoes:
            objeto["content"]["totalDeducoes"] = f"{totalDeducoes}"  

        if totalNotaFiscal:
            objeto["content"]["totalNotaFiscal"] = { "id": int(totalNotaFiscal)}

        if baseCalcIrrf:
            objeto["content"]["baseCalcIrrf"] = { "id": int(baseCalcIrrf)}

        if valorCofins:
            objeto["content"]["valorCofins"] = f"{valorCofins}"

        if valorCsll:
            objeto["content"]["valorCsll"] = f"{valorCsll}"
        
        if valorInss:
            objeto["content"]["valorInss"] = f"{valorInss}"
        
        if valorInssRecolher:
            objeto["content"]["divida"] = f"{valorInssRecolher}"            
        
        if valorInssRecolhido:
            objeto["content"]["valorInssRecolhido"] = f"{valorInssRecolhido}"
        
        if valorIrrf:
            objeto["content"]["valorIrrf"] = f"{valorIrrf}"      
        
        if valorIssqn:
            objeto["content"]["valorIssqn"] = f"{valorIssqn}",
        
        if valorLiquido:
            objeto["content"]["valorLiquido"] = f"{valorLiquido}"
        
        if condominioTomador != None:
            objeto[0]["calculotributario"]["creditotributario"] = f"{condominioTomador}"  
        
        if complementoTomador:
            objeto["content"]["complementoTomador"] = f"{complementoTomador}"   

        envio = api_post("notasAvulsas", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

notasAvulsas = notasAvulsas()