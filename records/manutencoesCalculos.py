from samples import *
import json

class manutencoesCalculos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idBeneficioFiscal, idManutencoesCalculos, idMotivos, idRequerente, abrangencia, anoVigencia,
                 classificacaoRevisaoCalculo, dtRequerimento, dtIniVigencia, dtFimVigencia, justificativa, nroProcesso, observacao, processandoReferentes,
                 situacao, tipoRequerimento, tipoSolicitacao, tipoVigencia, tipoSelecaoCreditos, percLancadoReq, 
                 percLancado, percCorrecao, percCorrecaoReq, percJuros, percJurosReq, percMulta, percMultaReq):
        try:
            sql = """
                INSERT INTO manutencoesCalculos (                    
                    idIntegracao,                   
                    id_cloud, 
                    idBeneficioFiscal,
                    idManutencoesCalculos,                                               
                    idMotivos, 
                    idRequerente,
                    abrangencia,
                    anoVigencia,
                    classificacaoRevisaoCalculo,
                    dtRequerimento,
                    dtIniVigencia,                    
                    dtFimVigencia,
                    justificativa,
                    nroProcesso,
                    observacao,
                    processandoReferentes,
                    situacao,
                    tipoRequerimento,
                    tipoSolicitacao,
                    tipoVigencia,
                    tipoSelecaoCreditos,
                    percLancadoReq, 
                    percLancado, 
                    percCorrecao, 
                    percCorrecaoReq, 
                    percJuros, 
                    percJurosReq, 
                    percMulta, 
                    percMultaReq, 
                    exibirParece,
                    nroConvenio                  
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idBeneficioFiscal)s,
                    %(idManutencoesCalculos)s,
                    %(idMotivos)s,
                    %(idRequerente)s,
                    %(abrangencia)s,
                    %(anoVigencia)s,
                    %(classificacaoRevisaoCalculo)s,
                    %(dtRequerimento)s,
                    %(dtIniVigencia)s,                    
                    %(dtFimVigencia)s,
                    %(justificativa)s,
                    %(nroProcesso)s,
                    %(observacao)s,
                    %(processandoReferentes)s,
                    %(situacao)s,
                    %(tipoRequerimento)s,
                    %(tipoSelecaoCreditos)s,
                    %(tipoVigencia)s,                    
                    %(tipoSolicitacao)s,
                    %(percLancadoReq)s,
                    %(percLancado)s,
                    %(percCorrecao)s,
                    %(percCorrecaoReq)s,
                    %(percJuros)s,
                    %(percJurosReq)s,
                    %(percMulta)s,
                    %(percMultaReq)s,                    
                    %(exibirParece)s,
                    %(nroConvenio)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idBeneficioFiscal = idBeneficioFiscal,
                idManutencoesCalculos = idManutencoesCalculos,
                idMotivos = idMotivos,                               
                idRequerente = idRequerente,
                abrangencia = abrangencia,
                anoVigencia = anoVigencia,                               
                classificacaoRevisaoCalculo = classificacaoRevisaoCalculo,
                dtRequerimento = dtRequerimento,
                dtIniVigencia = dtIniVigencia,                                               
                dtFimVigencia = dtFimVigencia,
                justificativa = justificativa,                               
                nroProcesso = nroProcesso,
                observacao = observacao,
                processandoReferentes = processandoReferentes,                               
                situacao = situacao,
                tipoRequerimento = tipoRequerimento,
                tipoSelecaoCreditos = tipoSelecaoCreditos,
                tipoVigencia = tipoVigencia,
                tipoSolicitacao = tipoSolicitacao,
                percLancadoReq = percLancadoReq, 
                percLancado = percLancado, 
                percCorrecao = percCorrecao, 
                percCorrecaoReq = percCorrecaoReq, 
                percJuros = percJuros, 
                percJurosReq = percJurosReq, 
                percMulta = percMulta, 
                percMultaReq = percMultaReq

            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {manutencoesCalculos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao inserir o anistias {manutencoesCalculos}. {intervaloFimr}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM manutencoesCalculos"
            if not self.query(sql_s):
                send_log_warning(f"manutencoesCalculos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM manutencoesCalculos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao executar a operação de exclusão do atividades econômicas. {intervaloFimr}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM manutencoesCalculos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    manutencoesCalculos 
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
            sql = f"SELECT * FROM manutencoesCalculos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao executar a operação de busca. {intervaloFimr}")

    def db_list(self):
        try:
            sql = "SELECT * FROM manutencoesCalculos WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM manutencoesCalculos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao executar a operação de busca. {intervaloFimr}")

    def send_post(self, id, idBeneficioFiscal, idManutencoesCalculos, idMotivos, idRequerente, abrangencia, dtRequerimento, anoVigencia, classificacaoRevisaoCalculo, dtIniVigencia, dtFimVigencia, 
                 justificativa, nroProcesso, observacao, processandoReferentes, situacao, tipoRequerimento, tipoSolicitacao, tipoVigencia, 
                 tipoSelecaoCreditos, percLancadoReq, percLancado, percCorrecao, 
                 percCorrecaoReq, percJuros, percJurosReq, percMulta, percMultaReq):
        objeto = {
                    "idIntegracao": f"Atos{id}",
                    "content": {}
        }

        if percCorrecaoReq:
            objeto["content"]["percCorrecaoReq"] = { "id": int(percCorrecaoReq)}

        if percJurosReq:
            objeto["content"]["percJurosReq"] = f"{percJurosReq}"

        if percMulta:
            objeto["content"]["percMulta"] = { "id": int(percMulta)}

        if percMultaReq:
            objeto["content"]["percMultaReq"] = { "id": int(percMultaReq)}    

        if percJuros:
            objeto["content"]["idAgenciaMedida"] = { "id": int(percJuros) }

        if idBeneficioFiscal:
            objeto["content"]["idBeneficioFiscal"] = { "id": int(idBeneficioFiscal)}

        if percCorrecao:
            objeto["content"]["percCorrecao"] = { "id": int(percCorrecao)}

        if percLancadoReq:
            objeto["content"]["percLancadoReq"] = f"{percLancadoReq}"

        if percLancado:
            objeto["content"]["percLancado"] = f"{percLancado}"

        if dtRequerimento:
            objeto["content"]["dtRequerimento"] = f"{dtRequerimento}"

        if classificacaoRevisaoCalculo:
            objeto["content"]["compartilhadoContribuinteMelhorias"] = f"{classificacaoRevisaoCalculo}"

        if dtFimVigencia:
            objeto["content"]["dtFimVigencia"] = f"{dtFimVigencia}"     

        if justificativa:
            objeto["content"]["justificativa"] = f"{justificativa}"

        if nroProcesso:
            objeto["content"]["nroProcesso"] = f"{nroProcesso}"

        if tipoSelecaoCreditos:
            objeto["content"]["tipoSelecaoCreditos"] = f"{tipoSelecaoCreditos}"

        if dtIniVigencia:
            objeto["content"]["dtIniVigencia"] = f"{dtIniVigencia}"             
        
        if idRequerente:
            objeto["content"]["idRequerente"] = { "id": int(idRequerente)}
        
        if observacao:
            objeto["content"]["observacao"] = f"{observacao}"
        
        if idManutencoesCalculos:
            objeto["content"]["idManutencoesCalculos"] = { "id": int(idManutencoesCalculos)}
        
        if idMotivos:
            objeto["content"]["idMotivos"] = { "id": int(idMotivos)}
        
        if situacao:
            objeto["content"]["CasasDecimais"] = f"{situacao}"
        
        if tipoRequerimento:
            objeto["content"]["MaximoDigitos"] = f"{tipoRequerimento}"
        
        if abrangencia:
            objeto["content"]["abrangencias"] = f"{abrangencia}"
        
        if anoVigencia:
            objeto["content"]["CompartilhadoCondominio"] = f"{anoVigencia}"
        
        if tipoSolicitacao:
            objeto["content"]["tipoSolicitacao"] = f"{tipoSolicitacao}"
        
        if processandoReferentes:
            objeto["content"]["LivroEletronico"] = f"{processandoReferentes}"
        
        if tipoVigencia:
            objeto["content"]["tipoVigencia"] = f"{tipoVigencia}"

        envio = api_post("manutencoesCalculos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

manutencoesCalculos = manutencoesCalculos()