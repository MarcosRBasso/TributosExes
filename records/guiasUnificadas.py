from samples import *
import json

class guiasUnificadas(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, base64, idConvenio, idEconomico, idImobiliaria, idPessoa, idScriptGuiaUnificada, idReceitaTaxaExpediente, idImovel, 
                  nroBaixa, codigoBarras, protocoloExecucao, representacaoNumerica, dtVencimento, possuiDebitos, possuiDividas, possuivlDescontoCorrecaoGuiamento, vlAnistiaCorrecao, vlAnistiaJuros,
                  vlAnistiaMulta, vlAnistiaTributo, vlBeneficios, vlCorrecaoPreFixada, vlDescontoCorrecaoGuia, vlDescontoDebito, vlDescontoJurosGuia, vlDescontoMultaGuia, 
                  vlDescontoParcelamento, vlDescontoTributoGuia, vlGuia, vlJurosFinanciamento, 
                  vlRemissaoTributo, vlSelecionado, vlTaxaExpediente, vlTaxasParcelamento, vlTotalCorrecao, vlTotalDescontos, vlTotalDescontosGuia, vlTotalJuros, vlTotalMulta,
                  vlTributo, criterioFormaPagamento, formaPagamento, situacao):
        try: 
            sql = """
                INSERT INTO guiasUnificadas (                    
                    idIntegracao,                   
                    id_cloud, 
                    base64,
                    idConvenio,                                               
                    idEconomico, 
                    idImobiliaria,
                    idPessoa,
                    idReceitaTaxaExpediente,
                    idImovel,
                    idScriptGuiaUnificada,
                    nroBaixa,                    
                    codigoBarras,
                    protocoloExecucao,
                    representacaoNumerica,
                    dtVencimento,
                    possuiDebitos,
                    possuiDividas,
                    possuivlDescontoCorrecaoGuiamento,
                    vlAnistiaCorrecao,
                    vlAnistiaJuros,
                    vlAnistiaMulta,
                    vlAnistiaTributo,
                    vlBeneficios, 
                    vlCorrecaoPreFixada,
                    vlDescontoCorrecaoGuia, 
                    vlDescontoDebito,
                    vlDescontoJurosGuia,
                    vlDescontoMultaGuia, 
                    vlDescontoParcelamento, 
                    vlDescontoTributoGuia,
                    vlGuia,
                    vlJurosFinanciamento,
                    vlRemissaoTributo,
                    vlSelecionado,
                    vlTaxaExpediente,
                    vlTaxasParcelamento,
                    vlTotalCorrecao,
                    vlTotalDescontos, 
                    vlTotalDescontosGuia, 
                    vlTotalJuros, 
                    vlTotalMulta, 
                    vlTributo, 
                    criterioFormaPagamento, 
                    formaPagamento, 
                    situacao
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(base64)s,
                    %(idConvenio)s,
                    %(idEconomico)s,
                    %(idImobiliaria)s,
                    %(idPessoa)s,
                    %(idReceitaTaxaExpediente)s,
                    %(idImovel)s,
                    %(idScriptGuiaUnificada)s,
                    %(nroBaixa)s,                    
                    %(codigoBarras)s,
                    %(protocoloExecucao)s,
                    %(representacaoNumerica)s,
                    %(dtVencimento)s,
                    %(possuiDebitos)s,
                    %(possuiDividas)s,
                    %(possuivlDescontoCorrecaoGuiamento)s,
                    %(vlAnistiaMulta)s,
                    %(vlAnistiaJuros)s,                    
                    %(vlAnistiaCorrecao)s,
                    %(vlAnistiaMulta)s,                    
                    %(vlAnistiaTributo)s,
                    %(vlBeneficios)s,
                    %(vlCorrecaoPreFixada)s,
                    %(vlDescontoCorrecaoGuia)s,
                    %(vlDescontoDebito)s,
                    %(vlDescontoJurosGuia)s,
                    %(vlDescontoMultaGuia)s,
                    %(vlDescontoParcelamento)s,
                    %(vlDescontoTributoGuia)s,
                    %(vlGuia)s,                    
                    %(vlJurosFinanciamento)s,
                    %(vlRemissaoTributo)s,
                    %(vlSelecionado)s,
                    %(vlTaxaExpediente)s,
                    %(vlTaxasParcelamento)s,
                    %(vlTotalCorrecao)s,
                    %(vlTotalDescontos)s,
                    %(vlTotalDescontosGuia)s,
                    %(vlTotalJuros)s,
                    %(vlTotalMulta)s,                    
                    %(vlTributo)s,
                    %(criterioFormaPagamento)s,
                    %(formaPagamento)s,
                    %(situacao)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                base64 = base64,
                idConvenio = idConvenio,
                idEconomico = idEconomico,                               
                idImobiliaria = idImobiliaria,
                idPessoa = idPessoa,
                idReceitaTaxaExpediente = idReceitaTaxaExpediente,                               
                idImovel = idImovel,
                idScriptGuiaUnificada = idScriptGuiaUnificada,
                nroBaixa = nroBaixa,                                               
                codigoBarras = codigoBarras,
                protocoloExecucao = protocoloExecucao,                               
                representacaoNumerica = representacaoNumerica,
                dtVencimento = dtVencimento,
                possuiDebitos = possuiDebitos,                               
                possuiDividas = possuiDividas,
                possuivlDescontoCorrecaoGuiamento = possuivlDescontoCorrecaoGuiamento,
                vlAnistiaMulta = vlAnistiaMulta,
                vlAnistiaJuros = vlAnistiaJuros,
                vlAnistiaCorrecao = vlAnistiaCorrecao,
                vlAnistiaTributo = vlAnistiaTributo,
                vlBeneficios = vlBeneficios, 
                vlCorrecaoPreFixada = vlCorrecaoPreFixada, 
                vlDescontoCorrecaoGuia = vlDescontoCorrecaoGuia, 
                vlDescontoDebito = vlDescontoDebito, 
                vlDescontoJurosGuia = vlDescontoJurosGuia, 
                vlDescontoMultaGuia = vlDescontoMultaGuia, 
                vlDescontoParcelamento = vlDescontoParcelamento, 
                vlDescontoTributoGuia = vlDescontoTributoGuia, 
                vlGuia = vlGuia, 
                vlJurosFinanciamento = vlJurosFinanciamento, 
                vlRemissaoTributo = vlRemissaoTributo, 
                vlSelecionado = vlSelecionado, 
                vlTaxaExpediente = vlTaxaExpediente,   
                vlTaxasParcelamento = vlTaxasParcelamento, 
                vlTotalCorrecao = vlTotalCorrecao, 
                vlTotalDescontos = vlTotalDescontos, 
                vlTotalDescontosGuia = vlTotalDescontosGuia, 
                vlTotalJuros = vlTotalJuros, 
                vlTotalMulta = vlTotalMulta, 
                vlTributo = vlTributo, 
                criterioFormaPagamento = criterioFormaPagamento, 
                formaPagamento = formaPagamento, 
                situacao = situacao
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {guiasUnificadas} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao inserir o anistias {guiasUnificadas}. {contribuintesr}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM guiasUnificadas"
            if not self.query(sql_s):
                send_log_warning(f"guiasUnificadas não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM guiasUnificadas WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de exclusão do atividades econômicas. {contribuintesr}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM guiasUnificadas WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    guiasUnificadas 
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
            sql = f"SELECT * FROM guiasUnificadas WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def db_list(self):
        try:
            sql = "SELECT * FROM guiasUnificadas WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM guiasUnificadas WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def send_post(self, id, base64, idConvenio, idEconomico, idImobiliaria, idPessoa, idScriptGuiaUnificada, idReceitaTaxaExpediente, idImovel, 
                  nroBaixa, codigoBarras, protocoloExecucao, representacaoNumerica, dtVencimento, possuiDebitos, possuiDividas, possuivlDescontoCorrecaoGuiamento, vlAnistiaCorrecao, vlAnistiaJuros,
                  vlAnistiaMulta, vlAnistiaTributo, vlBeneficios, vlCorrecaoPreFixada, vlDescontoCorrecaoGuia, vlDescontoDebito, vlDescontoJurosGuia, vlDescontoMultaGuia, vlDescontoParcelamento, vlDescontoTributoGuia, vlGuia, vlJurosFinanciamento, 
                  vlRemissaoTributo, vlSelecionado, vlTaxaExpediente, vlTaxasParcelamento, vlTotalCorrecao, vlTotalDescontos, vlTotalDescontosGuia, vlTotalJuros, vlTotalMulta, vlTributo, criterioFormaPagamento, formaPagamento,
                  situacao):
        objeto = {
            "idIntegracao": f"Atos{id}",
            "content": {}
        }
        if base64:
            objeto["content"]["VctoFeriado"] = f"{base64}"
        
        if idEconomico:
            objeto["content"]["idEconomico"] = { "id": int(idEconomico)}
        
        if idConvenio:
            objeto["content"]["idConvenio"] = { "id": int(idConvenio)}
        
        if idImobiliaria:
            objeto["content"]["idImobiliaria"] = { "id": int(idImobiliaria)}
        
        if possuiDividas:
            objeto["content"]["possuiDividas"] = f"{possuiDividas}"
        
        if possuivlDescontoCorrecaoGuiamento:
            objeto["content"]["possuivlDescontoCorrecaoGuiamento"] = f"{possuivlDescontoCorrecaoGuiamento}"
        
        if idPessoa:
            objeto["content"]["idPessoa"] = { "id": int(idPessoa)}
        
        if idReceitaTaxaExpediente:
            objeto["content"]["idReceitaTaxaExpediente"] = { "id": int(idReceitaTaxaExpediente)}
        
        if vlAnistiaCorrecao:
            objeto["content"]["vlAnistiaCorrecao"] = f"{vlAnistiaCorrecao}"       

        if vlAnistiaTributo:
            objeto["content"]["vlAnistiaTributo"] = f"{vlAnistiaTributo}"
        
        if possuiDebitos:
            objeto["content"]["possuiDebitos"] = f"{possuiDebitos}" 

        if vlAnistiaJuros:
            objeto["content"]["vlAnistiaJuros"] = f"{vlAnistiaJuros}"

        if vlAnistiaMulta:
            objeto["content"]["vlAnistiaMulta"] = f"{vlAnistiaMulta}"

        if idScriptGuiaUnificada:
            objeto["content"]["idScriptGuiaUnificada"] = { "id": int(idScriptGuiaUnificada)}     

        if idImovel:
            objeto["content"]["idImovel"] = { "id": int(idImovel)}    

        if nroBaixa:
            objeto["content"]["nroBaixa"] = f"{nroBaixa}"

        if codigoBarras:
            objeto["content"]["codigoBarras"] = f"{codigoBarras}"

        if protocoloExecucao:
            objeto["content"]["protocoloExecucao"] = f"{protocoloExecucao}"

        if vlBeneficios:
            objeto["content"]["vlBeneficios"] = f"{vlBeneficios}"     

        if vlCorrecaoPreFixada:
            objeto["content"]["vlCorrecaoPreFixada"] = f"{vlCorrecaoPreFixada}"    

        if vlDescontoCorrecaoGuia:
            objeto["content"]["vlDescontoCorrecaoGuia"] = f"{vlDescontoCorrecaoGuia}"

        if vlDescontoDebito:
            objeto["content"]["vlDescontoDebito"] = f"{vlDescontoDebito}"

        if vlDescontoJurosGuia:
            objeto["content"]["vlDescontoJurosGuia"] = f"{vlDescontoJurosGuia}"  

        if vlDescontoMultaGuia:
            objeto["content"]["vlDescontoMultaGuia"] = f"{vlDescontoMultaGuia}"

        if vlDescontoParcelamento:
            objeto["content"]["vlDescontoParcelamento"] = f"{vlDescontoParcelamento}"

        if vlDescontoTributoGuia:
            objeto["content"]["vlDescontoTributoGuia"] = f"{vlDescontoTributoGuia}"

        if vlGuia:
            objeto["content"]["vlGuia"] = f"{vlGuia}"             
        
        if vlJurosFinanciamento:
            objeto["content"]["vlJurosFinanciamento"] = f"{vlJurosFinanciamento}"
        
        if vlRemissaoTributo:
            objeto["content"]["vlRemissaoTributo"] = f"{vlRemissaoTributo}"

        if vlSelecionado:
            objeto["content"]["vlSelecionado"] = f"{vlSelecionado}"    

        if vlTaxaExpediente:
            objeto["content"]["vlTaxaExpediente"] = f"{vlTaxaExpediente}"

        if vlTaxasParcelamento:
            objeto["content"]["vlTaxasParcelamento"] = f"{vlTaxasParcelamento}"

        if vlTotalCorrecao:
            objeto["content"]["vlTotalCorrecao"] = f"{vlTotalCorrecao}"  

        if vlTotalDescontos:
            objeto["content"]["vlTotalDescontos"] = f"{vlTotalDescontos}"

        if vlTotalDescontosGuia:
            objeto["content"]["vlTotalDescontosGuia"] = f"{vlTotalDescontosGuia}"

        if vlTotalJuros:
            objeto["content"]["vlTotalJuros"] = f"{vlTotalJuros}"

        if vlTotalMulta:
            objeto["content"]["vlTotalMulta"] = f"{vlTotalMulta}"             
        
        if vlTributo:
            objeto["content"]["vlTributo"] = f"{vlTributo}"
        
        if criterioFormaPagamento:
            objeto["content"]["vlCorrecaoPreFixada0"] = f"{criterioFormaPagamento}"            
        
        if formaPagamento:
            objeto["content"]["formaPagamento"] = f"{formaPagamento}"
        
        if situacao:
            objeto["content"]["situacao"] = f"{situacao}"      
        
        if dtVencimento != None:
            objeto[0]["calculotributario"]["creditotributario"] = f"{dtVencimento}"  
        
        if representacaoNumerica:
            objeto["content"]["representacaoNumerica"] = f"{representacaoNumerica}"   

        envio = api_post("guiasUnificadas", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

guiasUnificadas = guiasUnificadas()