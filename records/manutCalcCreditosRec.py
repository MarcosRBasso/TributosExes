from samples import *
import json

class manutCalcCreditosRec(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idCreditosTributariosRec, idManutencoesCalculos, idManutCalcReferentes, idMotivo, selecionada, deferida,
                 classificacaoRevisaoCalculo, valorLancado, valorCorrecao, valorBeneficioLancado, valorJuros, valorBeneficioCorrecao, valorBeneficioJuros, valorBeneficioMulta, 
                 classificacaoRevisaoCalculoCorrecao, classificacaoRevisaoCalculoJuros,
                 valorBeneficioLancadoReq,
                 valorBeneficioCorrecaoReq, valorBeneficioJurosReq, valorBeneficioMultaReq, percLancadoReq, 
                 percLancado, percCorrecao, percCorrecaoReq, percJuros, percJurosReq, 
                 percMulta, percMultaReq, percReqAlterado, percAlterado, anosVigencia):
        try:
            sql = """
                INSERT INTO manutCalcCreditosRec (                    
                    idIntegracao,                   
                    id_cloud, 
                    idCreditosTributariosRec,
                    idManutencoesCalculos,                                               
                    idManutCalcReferentes, 
                    idMotivo,
                    selecionada,
                    deferida,
                    classificacaoRevisaoCalculo,
                    valorLancado,
                    valorCorrecao,                    
                    valorBeneficioLancado,
                    valorJuros,
                    valorBeneficioCorrecao,
                    valorBeneficioJuros,
                    valorBeneficioMulta,
                    classificacaoRevisaoCalculoCorrecao,
                    classificacaoRevisaoCalculoJuros,
                    valorBeneficioLancadoReq,
                    valorBeneficioCorrecaoReq,
                    valorBeneficioJurosReq,
                    valorBeneficioMultaReq, 
                    percLancadoReq, 
                    percLancado, 
                    percCorrecao, 
                    percCorrecaoReq, 
                    percJuros, 
                    percJurosReq, 
                    percMulta, 
                    exibirParece,
                    percReqAlterado, 
                    percAlterado, 
                    anosVigencia                  
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idCreditosTributariosRec)s,
                    %(idManutencoesCalculos)s,
                    %(idManutCalcReferentes)s,
                    %(idMotivo)s,
                    %(selecionada)s,
                    %(deferida)s,
                    %(classificacaoRevisaoCalculo)s,
                    %(valorLancado)s,
                    %(valorCorrecao)s,                    
                    %(valorBeneficioLancado)s,
                    %(valorJuros)s,
                    %(valorBeneficioCorrecao)s,
                    %(valorBeneficioJuros)s,
                    %(valorBeneficioMulta)s,
                    %(classificacaoRevisaoCalculoCorrecao)s,
                    %(classificacaoRevisaoCalculoJuros)s,
                    %(valorBeneficioJurosReq)s,
                    %(valorBeneficioCorrecaoReq)s,                    
                    %(valorBeneficioLancadoReq)s,
                    %(valorBeneficioMultaReq)s,
                    %(percLancadoReq)s,
                    %(percLancado)s,
                    %(percCorrecao)s,
                    %(percCorrecaoReq)s,
                    %(percJuros)s,
                    %(percJurosReq)s,
                    %(percMulta)s,                    
                    %(exibirParece)s,
                    %(percReqAlterado)s,
                    %(percAlterado)s, 
                    %(anosVigencia)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idCreditosTributariosRec = idCreditosTributariosRec,
                idManutencoesCalculos = idManutencoesCalculos,
                idManutCalcReferentes = idManutCalcReferentes,                               
                idMotivo = idMotivo,
                selecionada = selecionada,
                deferida = deferida,                               
                classificacaoRevisaoCalculo = classificacaoRevisaoCalculo,
                valorLancado = valorLancado,
                valorCorrecao = valorCorrecao,                                               
                valorBeneficioLancado = valorBeneficioLancado,
                valorJuros = valorJuros,                               
                valorBeneficioCorrecao = valorBeneficioCorrecao,
                valorBeneficioJuros = valorBeneficioJuros,
                valorBeneficioMulta = valorBeneficioMulta,                               
                classificacaoRevisaoCalculoCorrecao = classificacaoRevisaoCalculoCorrecao,
                classificacaoRevisaoCalculoJuros = classificacaoRevisaoCalculoJuros,
                valorBeneficioJurosReq = valorBeneficioJurosReq,
                valorBeneficioCorrecaoReq = valorBeneficioCorrecaoReq,
                valorBeneficioLancadoReq = valorBeneficioLancadoReq,
                valorBeneficioMultaReq = valorBeneficioMultaReq, 
                percLancadoReq = percLancadoReq, 
                percLancado = percLancado, 
                percCorrecao = percCorrecao, 
                percCorrecaoReq = percCorrecaoReq, 
                percJuros = percJuros, 
                percJurosReq = percJurosReq, 
                percMulta = percMulta, 
                percMultaReq = percMultaReq,
                percReqAlterado = percReqAlterado,
                percAlterado = percAlterado, 
                anosVigencia = anosVigencia
                 

            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {manutCalcCreditosRec} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao inserir o anistias {manutCalcCreditosRec}. {intervaloFimr}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM manutCalcCreditosRec"
            if not self.query(sql_s):
                send_log_warning(f"manutCalcCreditosRec não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM manutCalcCreditosRec WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao executar a operação de exclusão do atividades econômicas. {intervaloFimr}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM manutCalcCreditosRec WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    manutCalcCreditosRec 
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
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao executar a operação de atualização da atividades Economicas. {intervaloFimr}")

    def db_search(self, id):
        try:
            sql = f"SELECT * FROM manutCalcCreditosRec WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao executar a operação de busca. {intervaloFimr}")

    def db_list(self):
        try:
            sql = "SELECT * FROM manutCalcCreditosRec WHERE id_cloud is null"
            data = self.query(sql)
            if data:
                send_log_info("Consulta de todos os atividades Economicas realizada com sucesso.")
                return data
            return None
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao executar a operação de busca. {intervaloFimr}")

    def get_id_cloud(self, id):
        if (id == None):
            return None
        try:
            sql = f"SELECT id_cloud FROM manutCalcCreditosRec WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao executar a operação de busca. {intervaloFimr}")

    def send_post(self, id, idCreditosTributariosRec, idManutencoesCalculos, idManutCalcReferentes, idMotivo, selecionada, valorLancado, deferida, classificacaoRevisaoCalculo, valorCorrecao, valorBeneficioLancado, 
                 valorJuros, valorBeneficioCorrecao, valorBeneficioJuros, valorBeneficioMulta, classificacaoRevisaoCalculoCorrecao, classificacaoRevisaoCalculoJuros, valorBeneficioLancadoReq, valorBeneficioCorrecaoReq, 
                 valorBeneficioJurosReq, valorBeneficioMultaReq, percLancadoReq, percLancado, 
                 percCorrecao, percCorrecaoReq, percJuros, percJurosReq, percMulta, 
                 percMultaReq, percReqAlterado, percAlterado, anosVigencia):
        objeto = {
                    "idIntegracao": f"Atos{id}",
                    "content": {}
        }
        if percAlterado:
            objeto["content"]["percAlterado"] = f"{percAlterado}"

        if anosVigencia:
            objeto["content"]["anosVigencia"] = f"{anosVigencia}"

        if percReqAlterado:
            objeto["content"]["percReqAlterado"] = f"{percReqAlterado}"

        if percCorrecao:
            objeto["content"]["percCorrecao"] = { "id": int(percCorrecao)}

        if percJuros:
            objeto["content"]["percJuros"] = f"{percJuros}"

        if percJurosReq:
            objeto["content"]["percJurosReq"] = { "id": int(percJurosReq)}

        if percMulta:
            objeto["content"]["percMulta"] = { "id": int(percMulta)}    

        if percMultaReq:
            objeto["content"]["percMultaReq"] = { "id": int(percMultaReq)}

        if percCorrecaoReq:
            objeto["content"]["percMultaReqMedida"] = { "id": int(percCorrecaoReq) }

        if idCreditosTributariosRec:
            objeto["content"]["idCreditosTributariosRec"] = { "id": int(idCreditosTributariosRec)}

        if percLancado:
            objeto["content"]["percLancado"] = { "id": int(percLancado)}

        if valorBeneficioMultaReq:
            objeto["content"]["valorBeneficioMultaReq"] = f"{valorBeneficioMultaReq}"

        if percLancadoReq:
            objeto["content"]["percLancadoReq"] = f"{percLancadoReq}"

        if valorLancado:
            objeto["content"]["valorLancado"] = f"{valorLancado}"

        if classificacaoRevisaoCalculo:
            objeto["content"]["compartilhadoContribuinteMelhorias"] = f"{classificacaoRevisaoCalculo}"

        if valorBeneficioLancado:
            objeto["content"]["valorBeneficioLancado"] = f"{valorBeneficioLancado}"     

        if valorJuros:
            objeto["content"]["valorJuros"] = f"{valorJuros}"

        if valorBeneficioCorrecao:
            objeto["content"]["valorBeneficioCorrecao"] = f"{valorBeneficioCorrecao}"

        if valorBeneficioJurosReq:
            objeto["content"]["valorBeneficioJurosReq"] = f"{valorBeneficioJurosReq}"

        if valorCorrecao:
            objeto["content"]["valorCorrecao"] = f"{valorCorrecao}"             
        
        if idMotivo:
            objeto["content"]["idMotivo"] = { "id": int(idMotivo)}
        
        if valorBeneficioJuros:
            objeto["content"]["valorBeneficioJuros"] = f"{valorBeneficioJuros}"
        
        if idManutencoesCalculos:
            objeto["content"]["idManutencoesCalculos"] = { "id": int(idManutencoesCalculos)}
        
        if idManutCalcReferentes:
            objeto["content"]["idManutCalcReferentes"] = { "id": int(idManutCalcReferentes)}
        
        if classificacaoRevisaoCalculoCorrecao:
            objeto["content"]["CasasDecimais"] = f"{classificacaoRevisaoCalculoCorrecao}"
        
        if classificacaoRevisaoCalculoJuros:
            objeto["content"]["MaximoDigitos"] = f"{classificacaoRevisaoCalculoJuros}"
        
        if selecionada:
            objeto["content"]["selecionadas"] = f"{selecionada}"
        
        if deferida:
            objeto["content"]["CompartilhadoCondominio"] = f"{deferida}"
        
        if valorBeneficioLancadoReq:
            objeto["content"]["valorBeneficioLancadoReq"] = f"{valorBeneficioLancadoReq}"
        
        if valorBeneficioMulta:
            objeto["content"]["LivroEletronico"] = f"{valorBeneficioMulta}"
        
        if valorBeneficioCorrecaoReq:
            objeto["content"]["valorBeneficioCorrecaoReq"] = f"{valorBeneficioCorrecaoReq}"

        envio = api_post("manutCalcCreditosRec", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

manutCalcCreditosRec = manutCalcCreditosRec()