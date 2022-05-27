from samples import *
import json

class certidoesITBI(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idBairroEndereco, idCondominioEndereco, idComprador, idVendedor, idCorresponsavel, idCreditosTributarios,
                 idDistritoEndereco, idDividas, idModelo, idImoveis, idImoveisInfComplem, idLogradouroEndereco, idLoteamentoEndereco, idMunicipios, idReceitas, idTransfImoveisItens,
                 idTransfImoveisItensCompra, idTransfImoveisItensProcessos, idTransfImoveisItensVenda, idTransferenciaImoveis, dtVencimento, apartamentoEndereco, blocoEndereco, 
                 cepEndereco, lote, numeroEndereco, numeroTelefone, quadra, nroDocumento, valorCorrecao, valorJuro, valorLancado, valorMulta, valorTotal, vlDeclarado, 
                 principalEndereco, situacaoDivida, situacaoLancamento, situacaoParcela, tipoCertidaoITBI, situacaoCertidaoITBI, formaPagamento):
        try:
            sql = """
                INSERT INTO certidoesITBI (                    
                    idIntegracao,                   
                    id_cloud, 
                    idBairroEndereco,
                    idCondominioEndereco,                                               
                    idComprador, 
                    idVendedor,
                    idCorresponsavel,
                    idCreditosTributarios,
                    idDistritoEndereco,
                    idDividas,
                    idModelo,                    
                    idImoveis,
                    idImoveisInfComplem,
                    idLogradouroEndereco,
                    idLoteamentoEndereco,
                    idMunicipios,
                    idReceitas,
                    idTransfImoveisItens,
                    idTransfImoveisItensCompra,
                    idTransfImoveisItensProcessos,
                    idTransfImoveisItensVenda,
                    idTransferenciaImoveis, 
                    dtVencimento, 
                    apartamentoEndereco, 
                    blocoEndereco, 
                    cepEndereco, 
                    lote, 
                    numeroEndereco, 
                    numeroTelefone, 
                    exibirParece,
                    nroDocumento, 
                    valorCorrecao, 
                    valorJuro, 
                    valorLancado, 
                    valorMulta, 
                    valorTotal, 
                    vlDeclarado, 
                    principalEndereco, 
                    situacaoDivida, 
                    situacaoLancamento, 
                    situacaoParcela, 
                    tipoCertidaoITBI, 
                    situacaoCertidaoITBI, 
                    formaPagamento                   
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idBairroEndereco)s,
                    %(idCondominioEndereco)s,
                    %(idComprador)s,
                    %(idVendedor)s,
                    %(idCorresponsavel)s,
                    %(idCreditosTributarios)s,
                    %(idDistritoEndereco)s,
                    %(idDividas)s,
                    %(idModelo)s,                    
                    %(idImoveis)s,
                    %(idImoveisInfComplem)s,
                    %(idLogradouroEndereco)s,
                    %(idLoteamentoEndereco)s,
                    %(idMunicipios)s,
                    %(idReceitas)s,
                    %(idTransfImoveisItens)s,
                    %(idTransfImoveisItensVenda)s,
                    %(idTransfImoveisItensProcessos)s,                    
                    %(idTransfImoveisItensCompra)s,
                    %(idTransferenciaImoveis)s,
                    %(dtVencimento)s,
                    %(apartamentoEndereco)s,
                    %(blocoEndereco)s,
                    %(cepEndereco)s,
                    %(lote)s,
                    %(numeroEndereco)s,
                    %(numeroTelefone)s,                    
                    %(exibirParece)s,
                    %(nroDocumento)s, 
                    %(valorCorrecao)s, 
                    %(valorJuro)s, 
                    %(valorLancado)s, 
                    %(valorMulta)s, 
                    %(valorTotal)s, 
                    %(vlDeclarado)s, 
                    %(principalEndereco)s, 
                    %(situacaoDivida)s, 
                    %(situacaoLancamento)s, 
                    %(situacaoParcela)s, 
                    %(tipoCertidaoITBI)s, 
                    %(situacaoCertidaoITBI)s, 
                    %(formaPagamento)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idBairroEndereco = idBairroEndereco,
                idCondominioEndereco = idCondominioEndereco,
                idComprador = idComprador,                               
                idVendedor = idVendedor,
                idCorresponsavel = idCorresponsavel,
                idCreditosTributarios = idCreditosTributarios,                               
                idDistritoEndereco = idDistritoEndereco,
                idDividas = idDividas,
                idModelo = idModelo,                                               
                idImoveis = idImoveis,
                idImoveisInfComplem = idImoveisInfComplem,                               
                idLogradouroEndereco = idLogradouroEndereco,
                idLoteamentoEndereco = idLoteamentoEndereco,
                idMunicipios = idMunicipios,                               
                idReceitas = idReceitas,
                idTransfImoveisItens = idTransfImoveisItens,
                idTransfImoveisItensVenda = idTransfImoveisItensVenda,
                idTransfImoveisItensProcessos = idTransfImoveisItensProcessos,
                idTransfImoveisItensCompra = idTransfImoveisItensCompra,
                idTransferenciaImoveis = idTransferenciaImoveis, 
                dtVencimento = dtVencimento, 
                apartamentoEndereco = apartamentoEndereco, 
                blocoEndereco = blocoEndereco, 
                cepEndereco = cepEndereco, 
                lote = lote, 
                numeroEndereco = numeroEndereco, 
                numeroTelefone = numeroTelefone, 
                quadra = quadra,
                nroDocumento = nroDocumento,                  
                valorCorrecao = valorCorrecao, 
                valorJuro = valorJuro,  
                valorLancado = valorLancado, 
                valorMulta = valorMulta, 
                valorTotal = valorTotal, 
                vlDeclarado = vlDeclarado, 
                principalEndereco = principalEndereco, 
                situacaoDivida = situacaoDivida, 
                situacaoLancamento = situacaoLancamento, 
                situacaoParcela = situacaoParcela, 
                tipoCertidaoITBI = tipoCertidaoITBI, 
                situacaoCertidaoITBI = situacaoCertidaoITBI, 
                formaPagamento = formaPagamento
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {certidoesITBI} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as idLogradouroEnderecor:
            send_log_error(f"idLogradouroEndereco ao inserir o anistias {certidoesITBI}. {idLogradouroEnderecor}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM certidoesITBI"
            if not self.query(sql_s):
                send_log_warning(f"certidoesITBI não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM certidoesITBI WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as idLogradouroEnderecor:
            send_log_error(f"idLogradouroEndereco ao executar a operação de exclusão do atividades econômicas. {idLogradouroEnderecor}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM certidoesITBI WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    certidoesITBI 
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
        except Exception as idLogradouroEnderecor:
            send_log_error(f"idLogradouroEndereco ao executar a operação de atualização da atividades Economicas. {idLogradouroEnderecor}")

    def db_search(self, id):
        try:
            sql = f"SELECT * FROM certidoesITBI WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as idLogradouroEnderecor:
            send_log_error(f"idLogradouroEndereco ao executar a operação de busca. {idLogradouroEnderecor}")

    def db_list(self):
        try:
            sql = "SELECT * FROM certidoesITBI WHERE id_cloud is null"
            data = self.query(sql)
            if data:
                send_log_info("Consulta de todos os atividades Economicas realizada com sucesso.")
                return data
            return None
        except Exception as idLogradouroEnderecor:
            send_log_error(f"idLogradouroEndereco ao executar a operação de busca. {idLogradouroEnderecor}")

    def get_id_cloud(self, id):
        if (id == None):
            return None
        try:
            sql = f"SELECT id_cloud FROM certidoesITBI WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as idLogradouroEnderecor:
            send_log_error(f"idLogradouroEndereco ao executar a operação de busca. {idLogradouroEnderecor}")

    def send_post(self, id, idBairroEndereco, idCondominioEndereco, idComprador, idVendedor, idCorresponsavel, idDividas, idCreditosTributarios, idDistritoEndereco, idModelo, 
                  idImoveis, idImoveisInfComplem, idLogradouroEndereco, idLoteamentoEndereco, idMunicipios, idReceitas, idTransfImoveisItens, idTransfImoveisItensCompra, 
                  idTransfImoveisItensProcessos, idTransfImoveisItensVenda, idTransferenciaImoveis, dtVencimento, apartamentoEndereco, blocoEndereco, cepEndereco, lote, numeroEndereco, 
                  numeroTelefone, quadra, nroDocumento, valorCorrecao, valorJuro, valorLancado, valorMulta, valorTotal, vlDeclarado, principalEndereco, situacaoDivida, situacaoLancamento, 
                  situacaoParcela, tipoCertidaoITBI, situacaoCertidaoITBI, formaPagamento):
        objeto = {
                    "idIntegracao": f"Atos{id}",
                    "content": {}
        }
        if principalEndereco:
            objeto["content"]["principalEndereco"] = f"{principalEndereco}"

        if situacaoDivida:
            objeto["content"]["situacaoDivida"] = f"{situacaoDivida}"

        if situacaoLancamento:
            objeto["content"]["situacaoLancamento"] = f"{situacaoLancamento}"     

        if situacaoParcela:
            objeto["content"]["situacaoParcela"] = f"{situacaoParcela}"    

        if tipoCertidaoITBI:
            objeto["content"]["tipoCertidaoITBI"] = f"{tipoCertidaoITBI}"

        if situacaoCertidaoITBI:
            objeto["content"]["situacaoCertidaoITBI"] = f"{situacaoCertidaoITBI}"

        if formaPagamento:
            objeto["content"]["formaPagamento"] = f"{formaPagamento}"

        if vlDeclarado:
            objeto["content"]["vlDeclarado"] = f"{vlDeclarado}"

        if valorTotal:
            objeto["content"]["valorTotal"] = f"{valorTotal}"

        if valorMulta:
            objeto["content"]["valorMulta"] = f"{valorMulta}"

        if valorLancado:
            objeto["content"]["valorLancado"] = f"{valorLancado}"     

        if valorJuro:
            objeto["content"]["valorJuro"] = f"{valorJuro}"    

        if valorCorrecao:
            objeto["content"]["valorCorrecao"] = f"{valorCorrecao}"

        if nroDocumento:
            objeto["content"]["nroDocumento"] = f"{nroDocumento}"

        if blocoEndereco:
            objeto["content"]["blocoEndereco"] = f"{blocoEndereco}"

        if lote:
            objeto["content"]["lote"] = f"{lote}"

        if numeroEndereco:
            objeto["content"]["numeroEndereco"] = f"{numeroEndereco}"     

        if numeroTelefone:
            objeto["content"]["numeroTelefone"] = f"{numeroTelefone}"    

        if quadra:
            objeto["content"]["quadra"] = f"{quadra}"

        if cepEndereco:
            objeto["content"]["UnidadeMedida"] = f"{cepEndereco}"

        if idBairroEndereco:
            objeto["content"]["idBairroEndereco"] = { "id": int(idBairroEndereco)}

        if apartamentoEndereco:
            objeto["content"]["apartamentoEndereco"] = f"{apartamentoEndereco}"

        if idTransferenciaImoveis:
            objeto["content"]["idTransferenciaImoveis"] = { "id": int(idTransferenciaImoveis)}

        if dtVencimento:
            objeto["content"]["dtVencimento"] = f"{dtVencimento}"    

        if idDividas:
            objeto["content"]["idDividas"] = { "id": int(idDividas)}

        if idDistritoEndereco:
            objeto["content"]["compartilhadoContribuinteMelhorias"] = { "id": int(idDistritoEndereco)}

        if idImoveis:
            objeto["content"]["idImoveis"] = { "id": int(idImoveis)}     

        if idImoveisInfComplem:
            objeto["content"]["idImoveisInfComplem"] = { "id": int(idImoveisInfComplem)}

        if idLogradouroEndereco:
            objeto["content"]["idLogradouroEndereco"] = { "id": int(idLogradouroEndereco)}

        if idTransfImoveisItensVenda:
            objeto["content"]["idTransfImoveisItensVenda"] = { "id": int(idTransfImoveisItensVenda)}

        if idModelo:
            objeto["content"]["idModelo"] = { "id": int(idModelo)}
        
        if idComprador:
            objeto["content"]["idComprador"] = { "id": int(idComprador)}
        
        if idLoteamentoEndereco:
            objeto["content"]["idLoteamentoEndereco"] = { "id": int(idLoteamentoEndereco)}
        
        if idCondominioEndereco:
            objeto["content"]["idCondominioEndereco"] ={ "id": int(idCondominioEndereco)}
        
        if idVendedor:
            objeto["content"]["idVendedor"] = { "id": int(idVendedor)}
        
        if idReceitas:
            objeto["content"]["CasasDecimais"] = { "id": int(idReceitas) }
        
        if idTransfImoveisItens:
            objeto["content"]["MaximoDigitos"] = { "id": int(idTransfImoveisItens) }
        
        if idCorresponsavel:
            objeto["content"]["idCorresponsavels"] = { "id": int(idCorresponsavel) }
        
        if idCreditosTributarios:
            objeto["content"]["CompartilhadoCondominio"] = { "id": int(idCreditosTributarios)}
        
        if idTransfImoveisItensCompra:
            objeto["content"]["idTransfImoveisItensCompra"] = { "id": int(idTransfImoveisItensCompra)}
        
        if idMunicipios:
            objeto["content"]["LivroEletronico"] = { "id": int(idMunicipios)}
        
        if idTransfImoveisItensProcessos:
            objeto["content"]["idTransfImoveisItensProcessos"] = { "id": int(idTransfImoveisItensProcessos)}

        envio = api_post("certidoesITBI", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

certidoesITBI = certidoesITBI()