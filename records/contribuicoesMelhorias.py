from samples import *
import json

class contribuicoesMelhorias(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idAgrupamento, anoEdital, anoProposta, descMelhoria, dtEmissaoEdital, dtInicio,
                 dtProposta, dtTermino, edital, extensaoLogradouro, idContribuicoes, intervaloFim, intervaloIni, larguraLogradouro, idLogradouro, memorialDescritivo, percJurosFim,
                 percJurosIni, percParticipFim, percParticipIni, proposta, 
                 qtdImoveis, qtdParcFim, qtdParcIni, situacao, tipoIntervaloFim, 
                 tipoIntervaloIni, unidade, vlMelhoria, vlMinAmortFim, vlMinAmortIni, vlParticipacao, vlUnidade, lancamentoGerado):
        try:
            sql = """
                INSERT INTO contribuicoesMelhorias (                    
                    idIntegracao,                   
                    id_cloud, 
                    idAgrupamento,
                    anoEdital,                                               
                    anoProposta, 
                    descMelhoria,
                    dtEmissaoEdital,
                    dtInicio,
                    dtProposta,
                    dtTermino,
                    edital,                    
                    extensaoLogradouro,
                    idContribuicoes,
                    intervaloFim,
                    intervaloIni,
                    larguraLogradouro,
                    idLogradouro,
                    memorialDescritivo,
                    percJurosFim,
                    percJurosIni,
                    percParticipFim,
                    percParticipIni, 
                    proposta, 
                    qtdImoveis, 
                    qtdParcFim, 
                    qtdParcIni, 
                    situacao, 
                    tipoIntervaloFim, 
                    tipoIntervaloIni, 
                    exibirParece,
                    vlMelhoria, 
                    vlMinAmortFim, 
                    vlMinAmortIni, 
                    vlParticipacao,
                    vlUnidade, 
                    lancamentoGerado                   
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idAgrupamento)s,
                    %(anoEdital)s,
                    %(anoProposta)s,
                    %(descMelhoria)s,
                    %(dtEmissaoEdital)s,
                    %(dtInicio)s,
                    %(dtProposta)s,
                    %(dtTermino)s,
                    %(edital)s,                    
                    %(extensaoLogradouro)s,
                    %(idContribuicoes)s,
                    %(intervaloFim)s,
                    %(intervaloIni)s,
                    %(larguraLogradouro)s,
                    %(idLogradouro)s,
                    %(memorialDescritivo)s,
                    %(percParticipFim)s,
                    %(percJurosIni)s,                    
                    %(percJurosFim)s,
                    %(percParticipIni)s,
                    %(proposta)s,
                    %(qtdImoveis)s,
                    %(qtdParcFim)s,
                    %(qtdParcIni)s,
                    %(situacao)s,
                    %(tipoIntervaloFim)s,
                    %(tipoIntervaloIni)s,                    
                    %(exibirParece)s,
                    %(vlMelhoria)s, 
                    %(vlMinAmortFim)s, 
                    %(vlMinAmortIni)s, 
                    %(vlParticipacao)s,
                    %(vlUnidade)s, 
                    %(lancamentoGerado)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idAgrupamento = idAgrupamento,
                anoEdital = anoEdital,
                anoProposta = anoProposta,                               
                descMelhoria = descMelhoria,
                dtEmissaoEdital = dtEmissaoEdital,
                dtInicio = dtInicio,                               
                dtProposta = dtProposta,
                dtTermino = dtTermino,
                edital = edital,                                               
                extensaoLogradouro = extensaoLogradouro,
                idContribuicoes = idContribuicoes,                               
                intervaloFim = intervaloFim,
                intervaloIni = intervaloIni,
                larguraLogradouro = larguraLogradouro,                               
                idLogradouro = idLogradouro,
                memorialDescritivo = memorialDescritivo,
                percParticipFim = percParticipFim,
                percJurosIni = percJurosIni,
                percJurosFim = percJurosFim,
                percParticipIni = percParticipIni, 
                proposta = proposta, 
                qtdImoveis = qtdImoveis, 
                qtdParcFim = qtdParcFim, 
                qtdParcIni = qtdParcIni, 
                situacao = situacao, 
                tipoIntervaloFim = tipoIntervaloFim, 
                tipoIntervaloIni = tipoIntervaloIni, 
                unidade = unidade,
                vlMelhoria = vlMelhoria, 
                vlMinAmortFim = vlMinAmortFim, 
                vlMinAmortIni = vlMinAmortIni, 
                vlParticipacao = vlParticipacao,
                vlUnidade = vlUnidade, 
                lancamentoGerado = lancamentoGerado

            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {contribuicoesMelhorias} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao inserir o anistias {contribuicoesMelhorias}. {intervaloFimr}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM contribuicoesMelhorias"
            if not self.query(sql_s):
                send_log_warning(f"contribuicoesMelhorias não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM contribuicoesMelhorias WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao executar a operação de exclusão do atividades econômicas. {intervaloFimr}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM contribuicoesMelhorias WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    contribuicoesMelhorias 
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
            sql = f"SELECT * FROM contribuicoesMelhorias WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao executar a operação de busca. {intervaloFimr}")

    def db_list(self):
        try:
            sql = "SELECT * FROM contribuicoesMelhorias WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM contribuicoesMelhorias WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao executar a operação de busca. {intervaloFimr}")

    def send_post(self, id, idAgrupamento, anoEdital, anoProposta, descMelhoria, dtEmissaoEdital, dtTermino, dtInicio, dtProposta, edital, extensaoLogradouro, 
                 idContribuicoes, intervaloFim, intervaloIni, larguraLogradouro, idLogradouro, memorialDescritivo, percJurosFim, percJurosIni, 
                 percParticipFim, percParticipIni, proposta, qtdImoveis, 
                 qtdParcFim, qtdParcIni, situacao, tipoIntervaloFim, tipoIntervaloIni, 
                 unidade, vlMelhoria, vlMinAmortFim, vlMinAmortIni, vlParticipacao, vlUnidade, lancamentoGerado):
        objeto = {
                    "idIntegracao": f"Atos{id}",
                    "content": {}
        }
        if vlUnidade:
            objeto["content"]["vlUnidade"] = f"{vlUnidade}"

        if lancamentoGerado:
            objeto["content"]["lancamentoGerado"] = f"{lancamentoGerado}"

        if vlMelhoria:
            objeto["content"]["vlMelhoria"] = f"{vlMelhoria}"

        if vlMinAmortFim:
            objeto["content"]["vlMinAmortFim"] = f"{vlMinAmortFim}"

        if vlMinAmortIni:
            objeto["content"]["vlMinAmortIni"] = f"{vlMinAmortIni}"     

        if vlParticipacao:
            objeto["content"]["vlParticipacao"] = f"{vlParticipacao}"  

        if qtdParcFim:
            objeto["content"]["qtdParcFim"] = { "id": int(qtdParcFim)}

        if situacao:
            objeto["content"]["situacao"] = f"{situacao}"

        if tipoIntervaloFim:
            objeto["content"]["tipoIntervaloFim"] = f"{tipoIntervaloFim}"

        if tipoIntervaloIni:
            objeto["content"]["tipoIntervaloIni"] = f"{tipoIntervaloIni}"    

        if unidade:
            objeto["content"]["unidade"] = f"{unidade}"

        if qtdParcIni:
            objeto["content"]["UnidadeMedida"] = { "id": int(qtdParcIni) }

        if idAgrupamento:
            objeto["content"]["idAgrupamento"] = { "id": int(idAgrupamento)}

        if qtdImoveis:
            objeto["content"]["qtdImoveis"] = { "id": int(qtdImoveis)}

        if percParticipIni:
            objeto["content"]["percParticipIni"] = f"{percParticipIni}"

        if proposta:
            objeto["content"]["proposta"] = f"{proposta}"

        if dtTermino:
            objeto["content"]["dtTermino"] = f"{dtTermino}"

        if dtProposta:
            objeto["content"]["compartilhadoContribuinteMelhorias"] = f"{dtProposta}"

        if extensaoLogradouro:
            objeto["content"]["extensaoLogradouro"] = f"{extensaoLogradouro}"     

        if idContribuicoes:
            objeto["content"]["idContribuicoes"] = { "id": int(idContribuicoes)}

        if intervaloFim:
            objeto["content"]["intervaloFim"] = f"{intervaloFim}"

        if percParticipFim:
            objeto["content"]["percParticipFim"] = { "id": int(percParticipFim)}

        if edital:
            objeto["content"]["edital"] = f"{edital}"             
        
        if descMelhoria:
            objeto["content"]["descMelhoria"] = f"{descMelhoria}"
        
        if intervaloIni:
            objeto["content"]["intervaloIni"] = f"{intervaloIni}"
        
        if anoEdital:
            objeto["content"]["anoEdital"] = { "id": int(anoEdital)}
        
        if anoProposta:
            objeto["content"]["anoProposta"] = { "id": int(anoProposta)}
        
        if idLogradouro:
            objeto["content"]["CasasDecimais"] = { "id": int(idLogradouro) }
        
        if memorialDescritivo:
            objeto["content"]["MaximoDigitos"] = f"{memorialDescritivo}"
        
        if dtEmissaoEdital:
            objeto["content"]["dtEmissaoEditals"] = f"{dtEmissaoEdital}"
        
        if dtInicio:
            objeto["content"]["CompartilhadoCondominio"] = f"{dtInicio}"
        
        if percJurosFim:
            objeto["content"]["percJurosFim"] = { "id": int(percJurosFim)}
        
        if larguraLogradouro:
            objeto["content"]["LivroEletronico"] = f"{larguraLogradouro}"
        
        if percJurosIni:
            objeto["content"]["percJurosIni"] = f"{percJurosIni}"

        envio = api_post("contribuicoesMelhorias", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

contribuicoesMelhorias = contribuicoesMelhorias()