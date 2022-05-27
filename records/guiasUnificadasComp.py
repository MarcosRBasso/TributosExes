from samples import *
import json

class guiasUnificadasComp(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idCreditoTributario, idDebito, idDivida, idGuiaUnificada, idReferente, idParcelamento, idParcelamentoParcela, ano, 
                  vlAnistiaJuros, codigoBarras, protocoloExecucao, representacaoNumerica, dtVencimento, possuiDebitos, possuiDividas, possuivlDescontoCorrecaoGuiamento, vlAnistiaCorrecao, 
                  vlAnistiaMulta, vlAnistiaTributo, vlBeneficios, vlCorrecaoPreFixada, vlDescontoCorrecaoGuia, vlDescontoDebito, vlDescontoJurosGuia, vlDescontoMultaGuia, 
                  vlDescontoParcelamento, vlDescontoTributoGuia, vlBeneficioCorrecao, vlJurosFinanciamento, 
                  vlRemissaoTributo, vlJuros, vlMulta, vlTaxasParcelamento, tipoLancamento):
        try: 
            sql = """
                INSERT INTO guiasUnificadasComp (                    
                    idIntegracao,                   
                    id_cloud, 
                    idCreditoTributario,
                    idDebito,                                               
                    idDivida, 
                    idGuiaUnificada,
                    idReferente,
                    idParcelamentoParcela,
                    ano,
                    idParcelamento,
                    vlAnistiaJuros,                    
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
                    vlBeneficioCorrecao,
                    vlJurosFinanciamento,
                    vlRemissaoTributo,
                    vlJuros,
                    vlMulta,
                    vlTaxasParcelamento,
                    tipoLancamento
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idCreditoTributario)s,
                    %(idDebito)s,
                    %(idDivida)s,
                    %(idGuiaUnificada)s,
                    %(idReferente)s,
                    %(idParcelamentoParcela)s,
                    %(ano)s,
                    %(idParcelamento)s,
                    %(vlAnistiaJuros)s,                    
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
                    %(vlBeneficioCorrecao)s,                    
                    %(vlJurosFinanciamento)s,
                    %(vlRemissaoTributo)s,
                    %(vlJuros)s,
                    %(vlMulta)s,
                    %(vlTaxasParcelamento)s,
                    %(tipoLancamento)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idCreditoTributario = idCreditoTributario,
                idDebito = idDebito,
                idDivida = idDivida,                               
                idGuiaUnificada = idGuiaUnificada,
                idReferente = idReferente,
                idParcelamentoParcela = idParcelamentoParcela,                               
                ano = ano,
                idParcelamento = idParcelamento,
                vlAnistiaJuros = vlAnistiaJuros,                                               
                codigoBarras = codigoBarras,
                protocoloExecucao = protocoloExecucao,                               
                representacaoNumerica = representacaoNumerica,
                dtVencimento = dtVencimento,
                possuiDebitos = possuiDebitos,                               
                possuiDividas = possuiDividas,
                possuivlDescontoCorrecaoGuiamento = possuivlDescontoCorrecaoGuiamento,
                vlAnistiaMulta = vlAnistiaMulta,
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
                vlBeneficioCorrecao = vlBeneficioCorrecao, 
                vlJurosFinanciamento = vlJurosFinanciamento, 
                vlRemissaoTributo = vlRemissaoTributo, 
                vlJuros = vlJuros, 
                vlMulta = vlMulta,   
                vlTaxasParcelamento = vlTaxasParcelamento, 
                tipoLancamento = tipoLancamento
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {guiasUnificadasComp} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao inserir o anistias {guiasUnificadasComp}. {contribuintesr}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM guiasUnificadasComp"
            if not self.query(sql_s):
                send_log_warning(f"guiasUnificadasComp não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM guiasUnificadasComp WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de exclusão do atividades econômicas. {contribuintesr}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM guiasUnificadasComp WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    guiasUnificadasComp 
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
            sql = f"SELECT * FROM guiasUnificadasComp WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def db_list(self):
        try:
            sql = "SELECT * FROM guiasUnificadasComp WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM guiasUnificadasComp WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def send_post(self, id, idCreditoTributario, idDebito, idDivida, idGuiaUnificada, idReferente, idParcelamento, idParcelamentoParcela, ano, 
                   codigoBarras, protocoloExecucao, representacaoNumerica, dtVencimento, possuiDebitos, possuiDividas, possuivlDescontoCorrecaoGuiamento, vlAnistiaCorrecao, vlAnistiaJuros,
                  vlAnistiaMulta, vlAnistiaTributo, vlBeneficios, vlCorrecaoPreFixada, vlDescontoCorrecaoGuia, vlDescontoDebito, vlDescontoJurosGuia, vlDescontoMultaGuia, vlDescontoParcelamento, vlDescontoTributoGuia, vlBeneficioCorrecao, vlJurosFinanciamento, 
                  vlRemissaoTributo, vlJuros, vlMulta, vlTaxasParcelamento, tipoLancamento):
        objeto = {
            "idIntegracao": f"Atos{id}",
            "content": {}
        }
        if idCreditoTributario:
            objeto["content"]["VctoFeriado"] = { "id": int(idCreditoTributario)}
        
        if idDivida:
            objeto["content"]["idDivida"] = { "id": int(idDivida)}
        
        if idDebito:
            objeto["content"]["idDebito"] = { "id": int(idDebito)}
        
        if idGuiaUnificada:
            objeto["content"]["idGuiaUnificada"] = { "id": int(idGuiaUnificada)}
        
        if possuiDividas:
            objeto["content"]["possuiDividas"] = f"{possuiDividas}"
        
        if possuivlDescontoCorrecaoGuiamento:
            objeto["content"]["possuivlDescontoCorrecaoGuiamento"] = f"{possuivlDescontoCorrecaoGuiamento}"
        
        if idReferente:
            objeto["content"]["idReferente"] = { "id": int(idReferente)}
        
        if idParcelamentoParcela:
            objeto["content"]["idParcelamentoParcela"] = { "id": int(idParcelamentoParcela)}
        
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

        if idParcelamento:
            objeto["content"]["idParcelamento"] = { "id": int(idParcelamento)}     

        if ano:
            objeto["content"]["ano"] = { "id": int(ano)}    

        if vlAnistiaJuros:
            objeto["content"]["vlAnistiaJuros"] = f"{vlAnistiaJuros}"

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

        if vlBeneficioCorrecao:
            objeto["content"]["vlBeneficioCorrecao"] = f"{vlBeneficioCorrecao}"             
        
        if vlJurosFinanciamento:
            objeto["content"]["vlJurosFinanciamento"] = f"{vlJurosFinanciamento}"
        
        if vlRemissaoTributo:
            objeto["content"]["vlRemissaoTributo"] = f"{vlRemissaoTributo}"

        if vlJuros:
            objeto["content"]["vlJuros"] = f"{vlJuros}"    

        if vlMulta:
            objeto["content"]["vlMulta"] = f"{vlMulta}"

        if vlTaxasParcelamento:
            objeto["content"]["vlTaxasParcelamento"] = f"{vlTaxasParcelamento}"

        if tipoLancamento:
            objeto["content"]["tipoLancamento"] = f"{tipoLancamento}"    
        
        if dtVencimento != None:
            objeto[0]["calculotributario"]["creditotributario"] = f"{dtVencimento}"  
        
        if representacaoNumerica:
            objeto["content"]["representacaoNumerica"] = f"{representacaoNumerica}"   

        envio = api_post("guiasUnificadasComp", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

guiasUnificadasComp = guiasUnificadasComp()