from samples import *
import json

class notificacoesDividasDados(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idNotificacoesDividas, idContribuinte, idEnderecoContribuinte, idTelefoneContribuinte, idImovel, idEconomico, idReceitaDiversa, 
                  idContribuicaoMelhoria, idTransferenciaImovel, idanoLivro, unidadeImovel, nomeCorresponsavel, idEnderecoCorresponsavel, idAtividade, idServico, idCreditoTributario,
                  idReceitas, apartamentoReferente, idBairroReferente, cepReferente, complementoReferente, idCondominioReferente, idDistritoReferente, inscricaoIncraReferente, 
                  idLocalidadeReferente, idLogradouroReferente, loteReferente, idLoteamentoReferente, quadraReferente, idDivida, numeroInscricao, campo1, campo2, campo3, campo4, 
                  campo5, campo6, campo7, campo8, campo9, campo10, ano, dataInscricao, dataVencimento, numero, anoLivro, folha, posicao, parcela, valorTributoInscritoMoedaOriginal, 
                  valorTributoInscritoMoedaCorrente, valorSaldoMoedaOriginal, valorSaldoMoedaCorrente, valorCorrecaoAtual, valorJurosAtual, valorMultaAtual, 
                  valorSaldoTotalMoedaCorrente, valorTributoReceitaInscritoMoedaOriginal, valorTributoReceitaInscritoMoedaCorrente, valorSaldoReceitaMoedaOriginal, 
                  valorSaldoReceitaMoedaCorrente, valorCorrecaoReceitaAtual, valorJurosReceitaAtual, valorMultaReceitaAtual, valorSaldoTotalReceitaMoedaCorrente, situacaoDivida,
                  mesesCobrancaAcrescimos):
        try: 
            sql = """
                INSERT INTO notificacoesDividasDados (                    
                    idIntegracao,                   
                    id_cloud, 
                    idNotificacoesDividas,
                    idContribuinte,                                               
                    idEnderecoContribuinte, 
                    idTelefoneContribuinte,
                    idImovel,
                    idReceitaDiversa,
                    idContribuicaoMelhoria,
                    idEconomico,
                    idTransferenciaImovel,                    
                    idanoLivro,
                    unidadeImovel,
                    nomeCorresponsavel,
                    idEnderecoCorresponsavel,
                    idAtividade,
                    idServico,
                    idCreditoTributario,
                    idReceitas,
                    apartamentoReferente,
                    idBairroReferente,
                    cepReferente,
                    complementoReferente, 
                    idCondominioReferente,
                    idDistritoReferente, 
                    inscricaoIncraReferente,
                    idLocalidadeReferente,
                    idLogradouroReferente, 
                    loteReferente, 
                    idLoteamentoReferente,
                    quadraReferente,
                    idDivida,
                    numeroInscricao,
                    campo1,
                    campo2,
                    campo3,
                    campo4,
                    campo5, 
                    campo6, 
                    campo7, 
                    campo8, 
                    campo9, 
                    campo10, 
                    ano, 
                    dataInscricao, 
                    dataVencimento, 
                    numero, 
                    anoLivro, 
                    folha, 
                    posicao, 
                    parcela, 
                    valorTributoInscritoMoedaOriginal, 
                    valorTributoInscritoMoedaCorrente, 
                    valorSaldoMoedaOriginal, 
                    valorSaldoMoedaCorrente, 
                    valorCorrecaoAtual, 
                    valorJurosAtual, 
                    valorMultaAtual, 
                    valorSaldoTotalMoedaCorrente, 
                    valorTributoReceitaInscritoMoedaOriginal, 
                    valorTributoReceitaInscritoMoedaCorrente,
                    valorSaldoReceitaMoedaOriginal, 
                    valorSaldoReceitaMoedaCorrente, 
                    valorCorrecaoReceitaAtual, 
                    valorJurosReceitaAtual, 
                    valorMultaReceitaAtual, 
                    valorSaldoTotalReceitaMoedaCorrente, 
                    situacaoDivida,
                    mesesCobrancaAcrescimos
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idNotificacoesDividas)s,
                    %(idContribuinte)s,
                    %(idEnderecoContribuinte)s,
                    %(idTelefoneContribuinte)s,
                    %(idImovel)s,
                    %(idReceitaDiversa)s,
                    %(idContribuicaoMelhoria)s,
                    %(idEconomico)s,
                    %(idTransferenciaImovel)s,                    
                    %(idanoLivro)s,
                    %(unidadeImovel)s,
                    %(nomeCorresponsavel)s,
                    %(idEnderecoCorresponsavel)s,
                    %(idAtividade)s,
                    %(idServico)s,
                    %(idCreditoTributario)s,
                    %(idBairroReferente)s,
                    %(apartamentoReferente)s,                    
                    %(idReceitas)s,
                    %(idBairroReferente)s,                    
                    %(cepReferente)s,
                    %(complementoReferente)s,
                    %(idCondominioReferente)s,
                    %(idDistritoReferente)s,
                    %(inscricaoIncraReferente)s,
                    %(idLocalidadeReferente)s,
                    %(idLogradouroReferente)s,
                    %(loteReferente)s,
                    %(idLoteamentoReferente)s,
                    %(quadraReferente)s,                    
                    %(idDivida)s,
                    %(numeroInscricao)s,
                    %(campo1)s,
                    %(campo2)s,
                    %(campo3)s,
                    %(campo4)s,
                    %(campo5)s,
                    %(campo6)s,
                    %(campo7)s,
                    %(campo8)s,                    
                    %(campo9)s,
                    %(campo10)s,
                    %(ano)s,
                    %(dataInscricao)s,
                    %(dataVencimento)s,
                    %(numero)s,
                    %(anoLivro)s,
                    %(folha)s,
                    %(posicao)s,                    
                    %(parcela)s,
                    %(valorTributoInscritoMoedaOriginal)s,
                    %(valorTributoInscritoMoedaCorrente)s,
                    %(valorSaldoMoedaOriginal)s,
                    %(valorSaldoMoedaCorrente)s,
                    %(valorCorrecaoAtual)s,
                    %(valorJurosAtual)s,
                    %(valorMultaAtual)s,                    
                    %(valorSaldoTotalMoedaCorrente)s,
                    %(valorTributoReceitaInscritoMoedaOriginal)s,                    
                    %(valorTributoReceitaInscritoMoedaCorrente)s,
                    %(valorSaldoReceitaMoedaOriginal)s, 
                    %(valorSaldoReceitaMoedaCorrente)s, 
                    %(valorCorrecaoReceitaAtual)s, 
                    %(valorJurosReceitaAtual)s, 
                    %(valorMultaReceitaAtual)s, 
                    %(valorSaldoTotalReceitaMoedaCorrente)s, 
                    %(situacaoDivida)s,
                    %(mesesCobrancaAcrescimos)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idNotificacoesDividas = idNotificacoesDividas,
                idContribuinte = idContribuinte,
                idEnderecoContribuinte = idEnderecoContribuinte,                               
                idTelefoneContribuinte = idTelefoneContribuinte,
                idImovel = idImovel,
                idReceitaDiversa = idReceitaDiversa,                               
                idContribuicaoMelhoria = idContribuicaoMelhoria,
                idEconomico = idEconomico,
                idTransferenciaImovel = idTransferenciaImovel,                                               
                idanoLivro = idanoLivro,
                unidadeImovel = unidadeImovel,                               
                nomeCorresponsavel = nomeCorresponsavel,
                idEnderecoCorresponsavel = idEnderecoCorresponsavel,
                idAtividade = idAtividade,                               
                idServico = idServico,
                idCreditoTributario = idCreditoTributario,
                idBairroReferente = idBairroReferente,
                apartamentoReferente = apartamentoReferente,
                idReceitas = idReceitas,
                cepReferente = cepReferente,
                complementoReferente = complementoReferente, 
                idCondominioReferente = idCondominioReferente, 
                idDistritoReferente = idDistritoReferente, 
                inscricaoIncraReferente = inscricaoIncraReferente, 
                idLocalidadeReferente = idLocalidadeReferente, 
                idLogradouroReferente = idLogradouroReferente, 
                loteReferente = loteReferente, 
                idLoteamentoReferente = idLoteamentoReferente, 
                quadraReferente = quadraReferente, 
                idDivida = idDivida, 
                numeroInscricao = numeroInscricao, 
                campo1 = campo1, 
                campo2 = campo2,   
                campo3 = campo3, 
                campo4 = campo4, 
                campo5 = campo5, 
                campo6 = campo6, 
                campo7 = campo7, 
                campo8 = campo8, 
                campo9 = campo9, 
                campo10 = campo10, 
                ano = ano, 
                dataInscricao = dataInscricao, 
                dataVencimento = dataVencimento, 
                numero = numero, 
                anoLivro = anoLivro, 
                folha = folha, 
                posicao = posicao, 
                parcela = parcela, 
                valorTributoInscritoMoedaOriginal =valorTributoInscritoMoedaOriginal, 
                valorTributoInscritoMoedaCorrente = valorTributoInscritoMoedaCorrente, 
                valorSaldoMoedaOriginal = valorSaldoMoedaOriginal, 
                valorSaldoMoedaCorrente = valorSaldoMoedaCorrente, 
                valorCorrecaoAtual = valorCorrecaoAtual, 
                valorJurosAtual = valorJurosAtual, 
                valorMultaAtual = valorMultaAtual, 
                valorSaldoTotalMoedaCorrente = valorSaldoTotalMoedaCorrente, 
                valorTributoReceitaInscritoMoedaOriginal = valorTributoReceitaInscritoMoedaOriginal, 
                valorTributoReceitaInscritoMoedaCorrente = valorTributoReceitaInscritoMoedaCorrente,
                valorSaldoReceitaMoedaOriginal = valorSaldoReceitaMoedaOriginal, 
                valorSaldoReceitaMoedaCorrente = valorSaldoReceitaMoedaCorrente, 
                valorCorrecaoReceitaAtual = valorCorrecaoReceitaAtual, 
                valorJurosReceitaAtual = valorJurosReceitaAtual, 
                valorMultaReceitaAtual = valorMultaReceitaAtual, 
                valorSaldoTotalReceitaMoedaCorrente = valorSaldoTotalReceitaMoedaCorrente, 
                situacaoDivida = situacaoDivida,
                mesesCobrancaAcrescimos = mesesCobrancaAcrescimos
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {notificacoesDividasDados} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao inserir o anistias {notificacoesDividasDados}. {contribuintesr}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM notificacoesDividasDados"
            if not self.query(sql_s):
                send_log_warning(f"notificacoesDividasDados não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM notificacoesDividasDados WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de exclusão do atividades econômicas. {contribuintesr}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM notificacoesDividasDados WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    notificacoesDividasDados 
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
            sql = f"SELECT * FROM notificacoesDividasDados WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def db_list(self):
        try:
            sql = "SELECT * FROM notificacoesDividasDados WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM notificacoesDividasDados WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def send_post(self, id, idNotificacoesDividas, idContribuinte, idEnderecoContribuinte, idTelefoneContribuinte, idImovel, idEconomico, idReceitaDiversa, idContribuicaoMelhoria, 
                  idTransferenciaImovel, idanoLivro, unidadeImovel, nomeCorresponsavel, idEnderecoCorresponsavel, idAtividade, idServico, idCreditoTributario, idReceitas, apartamentoReferente,
                  idBairroReferente, cepReferente, complementoReferente, idCondominioReferente, idDistritoReferente, inscricaoIncraReferente, idLocalidadeReferente, idLogradouroReferente, loteReferente, idLoteamentoReferente, quadraReferente, idDivida, 
                  numeroInscricao, campo1, campo2, campo3, campo4, campo5, campo6, campo7, campo8, campo9, campo10, ano, dataInscricao, dataVencimento, numero, anoLivro, 
                  folha, posicao, parcela, valorTributoInscritoMoedaOriginal, valorTributoInscritoMoedaCorrente, valorSaldoMoedaOriginal, valorSaldoMoedaCorrente, valorCorrecaoAtual, valorJurosAtual, valorMultaAtual, 
                  valorSaldoTotalMoedaCorrente, valorTributoReceitaInscritoMoedaOriginal, valorTributoReceitaInscritoMoedaCorrente,valorSaldoReceitaMoedaOriginal, 
                  valorSaldoReceitaMoedaCorrente, valorCorrecaoReceitaAtual, valorJurosReceitaAtual, valorMultaReceitaAtual, valorSaldoTotalReceitaMoedaCorrente, situacaoDivida,
                  mesesCobrancaAcrescimos):
        objeto = {
            "idIntegracao": f"Atos{id}",
            "content": {}
        }
        if valorSaldoReceitaMoedaOriginal:
            objeto["content"]["valorSaldoReceitaMoedaOriginal"] = f"{valorSaldoReceitaMoedaOriginal}"
        
        if valorSaldoReceitaMoedaCorrente:
            objeto["content"]["valorSaldoReceitaMoedaCorrente"] = f"{valorSaldoReceitaMoedaCorrente}"
        
        if valorCorrecaoReceitaAtual:
            objeto["content"]["valorCorrecaoReceitaAtual"] = f"{valorCorrecaoReceitaAtual}"
        
        if valorJurosReceitaAtual:
            objeto["content"]["valorJurosReceitaAtual"] = f"{valorJurosReceitaAtual}"
        
        if valorMultaReceitaAtual:
            objeto["content"]["valorMultaReceitaAtual"] = f"{valorMultaReceitaAtual}"
        
        if valorSaldoTotalReceitaMoedaCorrente:
            objeto["content"]["valorSaldoTotalReceitaMoedaCorrente"] = f"{valorSaldoTotalReceitaMoedaCorrente}"
        
        if situacaoDivida:
            objeto["content"]["situacaoDivida"] = f"{situacaoDivida}"
        
        if mesesCobrancaAcrescimos:
            objeto["content"]["mesesCobrancaAcrescimos"] = f"{mesesCobrancaAcrescimos}"

        if idNotificacoesDividas:
            objeto["content"]["VctoFeriado"] = { "id": int(idNotificacoesDividas)}
        
        if idEnderecoContribuinte:
            objeto["content"]["idEnderecoContribuinte"] = { "id": int(idEnderecoContribuinte)}
        
        if idContribuinte:
            objeto["content"]["idContribuinte"] = { "id": int(idContribuinte)}
        
        if idTelefoneContribuinte:
            objeto["content"]["idTelefoneContribuinte"] = { "id": int(idTelefoneContribuinte)}
        
        if idServico:
            objeto["content"]["idServico"] = { "id": int(idServico)}
        
        if idCreditoTributario:
            objeto["content"]["idCreditoTributario"] = { "id": int(idCreditoTributario)}
        
        if idImovel:
            objeto["content"]["idImovel"] = { "id": int(idImovel)}
        
        if idReceitaDiversa:
            objeto["content"]["idReceitaDiversa"] = { "id": int(idReceitaDiversa)}
        
        if idReceitas:
            objeto["content"]["idReceitas"] = { "id": int(idReceitas)}       

        if cepReferente:
            objeto["content"]["cepReferente"] = { "id": int(cepReferente) }
        
        if idAtividade:
            objeto["content"]["idAtividade"] = { "id": int(idAtividade)} 

        if apartamentoReferente:
            objeto["content"]["apartamentoReferente"] = f"{apartamentoReferente}"

        if idBairroReferente:
            objeto["content"]["idBairroReferente"] = { "id": int(idBairroReferente)}

        if idEconomico:
            objeto["content"]["idEconomico"] = { "id": int(idEconomico)}     

        if idContribuicaoMelhoria:
            objeto["content"]["idContribuicaoMelhoria"] = { "id": int(idContribuicaoMelhoria)}    

        if idTransferenciaImovel:
            objeto["content"]["idTransferenciaImovel"] = { "id": int(idTransferenciaImovel)}

        if folha:
            objeto["content"]["folha"] = { "id": int(folha) }

        if idanoLivro:
            objeto["content"]["idanoLivro"] = { "id": int(idanoLivro)}

        if complementoReferente:
            objeto["content"]["complementoReferente"] = f"{complementoReferente}"     

        if idCondominioReferente:
            objeto["content"]["idCondominioReferente"] = { "id": int(idCondominioReferente)}    

        if idDistritoReferente:
            objeto["content"]["idDistritoReferente"] = { "id": int(idDistritoReferente)}

        if inscricaoIncraReferente:
            objeto["content"]["inscricaoIncraReferente"] = f"{inscricaoIncraReferente}"

        if idLocalidadeReferente:
            objeto["content"]["idLocalidadeReferente"] = { "id": int(idLocalidadeReferente)}  

        if idLogradouroReferente:
            objeto["content"]["idLogradouroReferente"] = { "id": int(idLogradouroReferente)}

        if loteReferente:
            objeto["content"]["loteReferente"] = f"{loteReferente}"

        if idLoteamentoReferente:
            objeto["content"]["idLoteamentoReferente"] = { "id": int(idLoteamentoReferente)}

        if quadraReferente:
            objeto["content"]["quadraReferente"] = f"{quadraReferente}"             
        
        if idDivida:
            objeto["content"]["idDivida"] = { "id": int(idDivida)}
        
        if numeroInscricao:
            objeto["content"]["numeroInscricao"] = f"{numeroInscricao}"

        if campo1:
            objeto["content"]["campo1"] = f"{campo1}"    

        if campo2:
            objeto["content"]["campo2"] = f"{campo2}"

        if campo3:
            objeto["content"]["campo3"] = f"{campo3}"

        if campo4:
            objeto["content"]["campo4"] = f"{campo4}"  

        if campo5:
            objeto["content"]["campo5"] = f"{campo5}"

        if campo6:
            objeto["content"]["campo6"] = f"{campo6}"

        if campo7:
            objeto["content"]["campo7"] = f"{campo7}"

        if campo8:
            objeto["content"]["campo8"] = f"{campo8}"             
        
        if campo9:
            objeto["content"]["campo9"] = f"{campo9}"
        
        if campo10:
            objeto["content"]["idCondominioReferente0"] = f"{campo10}"            
        
        if ano:
            objeto["content"]["ano"] = f"{ano}"
        
        if dataInscricao:
            objeto["content"]["dataInscricao"] = f"{dataInscricao}"
        
        if posicao:
            objeto["content"]["posicao"] = { "id": int(posicao) }
        
        if parcela:
            objeto["content"]["parcela"] = { "id": int(parcela) }
        
        if valorTributoInscritoMoedaOriginal:
            objeto["content"]["valorTributoInscritoMoedaOriginal"] = f"{valorTributoInscritoMoedaOriginal}"

        if valorTributoInscritoMoedaCorrente:
            objeto["content"]["valorTributoInscritoMoedaCorrente"] = f"{valorTributoInscritoMoedaCorrente}"

        if valorSaldoMoedaCorrente:
            objeto["content"]["valorSaldoMoedaCorrente"] = f"{valorSaldoMoedaCorrente}"

        if valorSaldoMoedaOriginal:
            objeto["content"]["CodCaracteristicas"] = f"{valorSaldoMoedaOriginal}"
        
        if dataVencimento:
            objeto["content"]["dataVencimento"] = f"{dataVencimento}",
        
        if numero:
            objeto["content"]["numero"] = f"{numero}"
        
        if anoLivro:
            objeto["content"]["anoLivro"] = f"{anoLivro}"
        
        if unidadeImovel:
            objeto["content"]["unidadeImovel"] = f"{unidadeImovel}"       

        if idEnderecoCorresponsavel != None:
            objeto[0]["calculotributario"]["creditotributario"] = { "id": int(idEnderecoCorresponsavel) }   
        
        if valorCorrecaoAtual:
            objeto["content"]["valorCorrecaoAtual"] = f"{valorCorrecaoAtual}",
        
        if valorJurosAtual:
            objeto["content"]["valorJurosAtual"] = f"{valorJurosAtual}"
        
        if valorMultaAtual:
            objeto["content"]["valorMultaAtual"] = f"{valorMultaAtual}"
        
        if valorSaldoTotalMoedaCorrente:
            objeto["content"]["valorSaldoTotalMoedaCorrente"] = f"{valorSaldoTotalMoedaCorrente}"                       
        
        if valorTributoReceitaInscritoMoedaOriginal:
            objeto["content"]["valorTributoReceitaInscritoMoedaOriginal"] = f"{valorTributoReceitaInscritoMoedaOriginal}"
        
        if valorTributoReceitaInscritoMoedaCorrente:
            objeto["content"]["valorTributoReceitaInscritoMoedaCorrente"] = f"{valorTributoReceitaInscritoMoedaCorrente}"
        
        if nomeCorresponsavel:
            objeto["content"]["nomeCorresponsavel"] = f"{nomeCorresponsavel}"   

        envio = api_post("notificacoesDividasDados", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

notificacoesDividasDados = notificacoesDividasDados()