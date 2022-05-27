from samples import *
import json

class configTransfImoveis(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idCreditosTributariosRecRural, idCreditosTributariosRecUrbano, idCreditosTributariosRural, idCreditosTributariosUrbano, numeroDias, 
                  percAliqAvistaRur, percAliqAvistaUrb, percAliqBenfeitoriaRur, percAliqBenfeitoriaUrb, percAliqFinanciadaRur, percAliqFinanciadaUrb, percAliqOutrosRur, 
                  percAliqOutrosUrb, formaTransf, transfIsentoAutomatico, incluirImoRurAutomatico, benfeitoriaValorDeclarado, alterarDescricaoOutros, alterarValorDeclarado, 
                  dataCadastro, dataTransferencia, situacao, formaCobranca, imovel, endereco, inscImobiliaIncra, areaTotalTerreno, areaTotalConstruida, valorVenalTerritorial, 
                  valorVenalConstruido, valorVenal, valorVenalBenfeitorias, motivo, tipoVenda, cartorio, unidadeFutura, financiado, outros, benfeitorias, nomeVendedor, terrenoVendido,
                  construidoVendido, percVenda, nomeComprador, terrenoComprado, construidoComprado, percCompra, numImoveisIncluido, reiniciarSequencial, valorTotalItbi, tipoDias,
                  descricaoOutros):
        try:
            sql = """
                INSERT INTO configTransfImoveis (                    
                    idIntegracao,                   
                    id_cloud, 
                    idCreditosTributariosRecRural,
                    idCreditosTributariosRecUrbano,                                               
                    idCreditosTributariosRural, 
                    idCreditosTributariosUrbano,
                    numeroDias,
                    percAliqAvistaRur,
                    percAliqAvistaUrb,
                    percAliqBenfeitoriaRur,
                    percAliqBenfeitoriaUrb,                    
                    percAliqFinanciadaRur,
                    percAliqFinanciadaUrb,
                    percAliqOutrosRur,
                    percAliqOutrosUrb,
                    formaTransf,
                    transfIsentoAutomatico,
                    incluirImoRurAutomatico,
                    benfeitoriaValorDeclarado,
                    alterarDescricaoOutros,
                    alterarValorDeclarado,
                    dataCadastro, 
                    dataTransferencia, 
                    situacao, 
                    formaCobranca, 
                    imovel, 
                    endereco, 
                    inscImobiliaIncra, 
                    areaTotalTerreno, 
                    exibirParece,
                    valorVenalTerritorial, 
                    valorVenalConstruido, 
                    valorVenal, 
                    valorVenalBenfeitorias,
                    motivo,
                    tipoVenda,
                    cartorio,
                    unidadeFutura,
                    financiado,
                    outros,
                    benfeitorias,
                    nomeVendedor,
                    terrenoVendido,
                    construidoVendido,
                    percVenda,
                    nomeComprador,
                    terrenoComprado,
                    construidoComprado,
                    percCompra,
                    numImoveisIncluido,
                    reiniciarSequencial,
                    valorTotalItbi,
                    tipoDias,
                    descricaoOutros                   
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idCreditosTributariosRecRural)s,
                    %(idCreditosTributariosRecUrbano)s,
                    %(idCreditosTributariosRural)s,
                    %(idCreditosTributariosUrbano)s,
                    %(numeroDias)s,
                    %(percAliqAvistaRur)s,
                    %(percAliqAvistaUrb)s,
                    %(percAliqBenfeitoriaRur)s,
                    %(percAliqBenfeitoriaUrb)s,                    
                    %(percAliqFinanciadaRur)s,
                    %(percAliqFinanciadaUrb)s,
                    %(percAliqOutrosRur)s,
                    %(percAliqOutrosUrb)s,
                    %(formaTransf)s,
                    %(transfIsentoAutomatico)s,
                    %(incluirImoRurAutomatico)s,
                    %(alterarValorDeclarado)s,
                    %(alterarDescricaoOutros)s,                    
                    %(benfeitoriaValorDeclarado)s,
                    %(dataCadastro)s,
                    %(dataTransferencia)s,
                    %(situacao)s,
                    %(formaCobranca)s,
                    %(imovel)s,
                    %(endereco)s,
                    %(inscImobiliaIncra)s,
                    %(areaTotalTerreno)s,                    
                    %(exibirParece)s,
                    %(valorVenalTerritorial)s, 
                    %(valorVenalConstruido)s, 
                    %(valorVenal)s, 
                    %(valorVenalBenfeitorias)s,
					%(motivo)s,
					%(tipoVenda)s,
					%(cartorio)s,
					%(unidadeFutura)s,
					%(financiado)s,
					%(outros)s,
					%(benfeitorias)s,
					%(nomeVendedor)s,
					%(terrenoVendido)s,
					%(construidoVendido)s,
					%(percVenda)s,
					%(nomeComprador)s,
					%(terrenoComprado)s,
					%(construidoComprado)s,
					%(percCompra)s,
					%(numImoveisIncluido)s,
					%(reiniciarSequencial)s,
					%(valorTotalItbi)s,
					%(tipoDias)s,
					%(descricaoOutros)s                    
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idCreditosTributariosRecRural = idCreditosTributariosRecRural,
                idCreditosTributariosRecUrbano = idCreditosTributariosRecUrbano,
                idCreditosTributariosRural = idCreditosTributariosRural,                               
                idCreditosTributariosUrbano = idCreditosTributariosUrbano,
                numeroDias = numeroDias,
                percAliqAvistaRur = percAliqAvistaRur,                               
                percAliqAvistaUrb = percAliqAvistaUrb,
                percAliqBenfeitoriaRur = percAliqBenfeitoriaRur,
                percAliqBenfeitoriaUrb = percAliqBenfeitoriaUrb,                                               
                percAliqFinanciadaRur = percAliqFinanciadaRur,
                percAliqFinanciadaUrb = percAliqFinanciadaUrb,                               
                percAliqOutrosRur = percAliqOutrosRur,
                percAliqOutrosUrb = percAliqOutrosUrb,
                formaTransf = formaTransf,                               
                transfIsentoAutomatico = transfIsentoAutomatico,
                incluirImoRurAutomatico = incluirImoRurAutomatico,
                alterarValorDeclarado = alterarValorDeclarado,
                alterarDescricaoOutros = alterarDescricaoOutros,
                benfeitoriaValorDeclarado = benfeitoriaValorDeclarado,
                dataCadastro = dataCadastro, 
                dataTransferencia = dataTransferencia, 
                situacao = situacao, 
                formaCobranca = formaCobranca, 
                imovel = imovel, 
                endereco = endereco, 
                inscImobiliaIncra = inscImobiliaIncra, 
                areaTotalTerreno = areaTotalTerreno, 
                areaTotalConstruida = areaTotalConstruida,
                valorVenalTerritorial = valorVenalTerritorial, 
                valorVenalConstruido = valorVenalConstruido, 
                valorVenal = valorVenal, 
                valorVenalBenfeitorias = valorVenalBenfeitorias,
				motivo = motivo,
				tipoVenda = tipoVenda,
				cartorio = cartorio,
				unidadeFutura = unidadeFutura,
				financiado = financiado,
				outros = outros,
				benfeitorias = benfeitorias,
				nomeVendedor = nomeVendedor,
				terrenoVendido = terrenoVendido,
				construidoVendido = construidoVendido,
				percVenda = percVenda,
				nomeComprador = nomeComprador,
				terrenoComprado = terrenoComprado,
				construidoComprado = construidoComprado,
				percCompra = percCompra,
				numImoveisIncluido = numImoveisIncluido,
				reiniciarSequencial = reiniciarSequencial,
				valorTotalItbi = valorTotalItbi,
				tipoDias = tipoDias,
				descricaoOutros = descricaoOutros                

            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {configTransfImoveis} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as nomeRequerenter:
            send_log_error(f"nomeRequerente ao inserir o anistias {configTransfImoveis}. {nomeRequerenter}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM configTransfImoveis"
            if not self.query(sql_s):
                send_log_warning(f"configTransfImoveis não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM configTransfImoveis WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as nomeRequerenter:
            send_log_error(f"nomeRequerente ao executar a operação de exclusão do atividades econômicas. {nomeRequerenter}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM configTransfImoveis WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    configTransfImoveis 
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
        except Exception as nomeRequerenter:
            send_log_error(f"nomeRequerente ao executar a operação de atualização da atividades Economicas. {nomeRequerenter}")

    def db_search(self, id):
        try:
            sql = f"SELECT * FROM configTransfImoveis WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as nomeRequerenter:
            send_log_error(f"nomeRequerente ao executar a operação de busca. {nomeRequerenter}")

    def db_list(self):
        try:
            sql = "SELECT * FROM configTransfImoveis WHERE id_cloud is null"
            data = self.query(sql)
            if data:
                send_log_info("Consulta de todos os atividades Economicas realizada com sucesso.")
                return data
            return None
        except Exception as nomeRequerenter:
            send_log_error(f"nomeRequerente ao executar a operação de busca. {nomeRequerenter}")

    def get_id_cloud(self, id):
        if (id == None):
            return None
        try:
            sql = f"SELECT id_cloud FROM configTransfImoveis WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as nomeRequerenter:
            send_log_error(f"nomeRequerente ao executar a operação de busca. {nomeRequerenter}")

    def send_post(self, id, idCreditosTributariosRecRural, idCreditosTributariosRecUrbano, idCreditosTributariosRural, idCreditosTributariosUrbano, numeroDias, percAliqBenfeitoriaRur, percAliqAvistaRur, percAliqAvistaUrb, percAliqBenfeitoriaUrb, percAliqFinanciadaRur, 
                 percAliqFinanciadaUrb, percAliqOutrosRur, percAliqOutrosUrb, formaTransf, transfIsentoAutomatico, incluirImoRurAutomatico, benfeitoriaValorDeclarado, 
                 alterarDescricaoOutros, alterarValorDeclarado, dataCadastro, dataTransferencia, situacao, formaCobranca, imovel, endereco, inscImobiliaIncra, areaTotalTerreno, 
                 areaTotalConstruida, valorVenalTerritorial, valorVenalConstruido, valorVenal, valorVenalBenfeitorias, motivo, tipoVenda, cartorio, unidadeFutura, financiado, outros,
                 benfeitorias, nomeVendedor, terrenoVendido, construidoVendido, percVenda, nomeComprador, terrenoComprado, construidoComprado, percCompra, numImoveisIncluido,
                 reiniciarSequencial, valorTotalItbi, tipoDias, descricaoOutros):
        objeto = {
                    "idIntegracao": f"Atos{id}",
                    "content": {}
        }
        if terrenoComprado:
            objeto["content"]["terrenoComprado"] = f"{terrenoComprado}"

        if construidoComprado:
            objeto["content"]["construidoComprado"] = f"{construidoComprado}"

        if percCompra:
            objeto["content"]["percCompra"] = f"{percCompra}"     

        if numImoveisIncluido:
            objeto["content"]["numImoveisIncluido"] = f"{numImoveisIncluido}"

        if reiniciarSequencial:
            objeto["content"]["reiniciarSequencial"] = f"{reiniciarSequencial}"

        if valorTotalItbi:
            objeto["content"]["valorTotalItbi"] = f"{valorTotalItbi}"

        if tipoDias:
            objeto["content"]["tipoDias"] = f"{tipoDias}"     

        if descricaoOutros:
            objeto["content"]["descricaoOutros"] = f"{descricaoOutros}"
       
        if financiado:
            objeto["content"]["financiado"] = f"{financiado}"

        if outros:
            objeto["content"]["outros"] = f"{outros}"

        if benfeitorias:
            objeto["content"]["benfeitorias"] = f"{benfeitorias}"     

        if nomeVendedor:
            objeto["content"]["nomeVendedor"] = f"{nomeVendedor}"

        if terrenoVendido:
            objeto["content"]["terrenoVendido"] = f"{terrenoVendido}"

        if construidoVendido:
            objeto["content"]["construidoVendido"] = f"{construidoVendido}"

        if percVenda:
            objeto["content"]["percVenda"] = f"{percVenda}"     

        if nomeComprador:
            objeto["content"]["nomeComprador"] = f"{nomeComprador}"

        if motivo:
            objeto["content"]["motivo"] = f"{motivo}"

        if tipoVenda:
            objeto["content"]["tipoVenda"] = f"{tipoVenda}"

        if cartorio:
            objeto["content"]["cartorio"] = f"{cartorio}"     

        if unidadeFutura:
            objeto["content"]["unidadeFutura"] = f"{unidadeFutura}"

        if valorVenalTerritorial:
            objeto["content"]["valorVenalTerritorial"] = f"{valorVenalTerritorial}"

        if valorVenalConstruido:
            objeto["content"]["valorVenalConstruido"] = f"{valorVenalConstruido}"

        if valorVenal:
            objeto["content"]["valorVenal"] = f"{valorVenal}"     

        if valorVenalBenfeitorias:
            objeto["content"]["valorVenalBenfeitorias"] = f"{valorVenalBenfeitorias}"  

        if formaCobranca:
            objeto["content"]["formaCobranca"] = { "id": int(formaCobranca)}

        if endereco:
            objeto["content"]["endereco"] = { "id": int(endereco)}

        if inscImobiliaIncra:
            objeto["content"]["inscImobiliaIncra"] = { "id": int(inscImobiliaIncra)}

        if areaTotalTerreno:
            objeto["content"]["areaTotalTerreno"] = { "id": int(areaTotalTerreno)}    

        if areaTotalConstruida:
            objeto["content"]["areaTotalConstruida"] = f"{areaTotalConstruida}"

        if imovel:
            objeto["content"]["UnidadeMedida"] = { "id": int(imovel) }

        if idCreditosTributariosRecRural:
            objeto["content"]["idCreditosTributariosRecRural"] = { "id": int(idCreditosTributariosRecRural)}

        if situacao:
            objeto["content"]["situacao"] = { "id": int(situacao)}

        if dataCadastro:
            objeto["content"]["dataCadastro"] = { "id": int(dataCadastro)}

        if dataTransferencia:
            objeto["content"]["dataTransferencia"] = { "id": int(dataTransferencia)}

        if percAliqBenfeitoriaRur:
            objeto["content"]["percAliqBenfeitoriaRur"] = f"{percAliqBenfeitoriaRur}"

        if percAliqAvistaUrb:
            objeto["content"]["compartilhadoContribuinteMelhorias"] = { "id": int(percAliqAvistaUrb)}

        if percAliqFinanciadaRur:
            objeto["content"]["percAliqFinanciadaRur"] = f"{percAliqFinanciadaRur}"     

        if percAliqFinanciadaUrb:
            objeto["content"]["percAliqFinanciadaUrb"] = f"{percAliqFinanciadaUrb}"

        if percAliqOutrosRur:
            objeto["content"]["percAliqOutrosRur"] = f"{percAliqOutrosRur}"

        if alterarValorDeclarado:
            objeto["content"]["alterarValorDeclarado"] = { "id": int(alterarValorDeclarado)}

        if percAliqBenfeitoriaUrb:
            objeto["content"]["percAliqBenfeitoriaUrb"] = f"{percAliqBenfeitoriaUrb}"             
        
        if idCreditosTributariosUrbano:
            objeto["content"]["idCreditosTributariosUrbano"] = { "id": int(idCreditosTributariosUrbano)}
        
        if percAliqOutrosUrb:
            objeto["content"]["percAliqOutrosUrb"] = f"{percAliqOutrosUrb}"
        
        if idCreditosTributariosRecUrbano:
            objeto["content"]["idCreditosTributariosRecUrbano"] = { "id": int(idCreditosTributariosRecUrbano)}
        
        if idCreditosTributariosRural:
            objeto["content"]["idCreditosTributariosRural"] = { "id": int(idCreditosTributariosRural)}
        
        if transfIsentoAutomatico:
            objeto["content"]["CasasDecimais"] = { "id": int(transfIsentoAutomatico) }
        
        if incluirImoRurAutomatico:
            objeto["content"]["MaximoDigitos"] = { "id": int(incluirImoRurAutomatico) }
        
        if numeroDias:
            objeto["content"]["numeroDiass"] = { "id": int(numeroDias) }
        
        if percAliqAvistaRur:
            objeto["content"]["CompartilhadoCondominio"] = { "id": int(percAliqAvistaRur)}
        
        if benfeitoriaValorDeclarado:
            objeto["content"]["benfeitoriaValorDeclarado"] = { "id": int(benfeitoriaValorDeclarado)}
        
        if formaTransf:
            objeto["content"]["LivroEletronico"] = f"{formaTransf}"
        
        if alterarDescricaoOutros:
            objeto["content"]["alterarDescricaoOutros"] = { "id": int(alterarDescricaoOutros)}

        envio = api_post("configTransfImoveis", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

configTransfImoveis = configTransfImoveis()