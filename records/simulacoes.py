from samples import *
import json

class simulacoes(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, anoInicial, anoFinal, nroDiasVencidos, nroLivro, nroFolha, nroPosicao,
                 anoLivro, qtdTotalCreditos, qtdInconsistentes, filtroCreditos, filtroPessoas, filtroImoveis, filtroEconomicos, filtroReceitasDiversas,
                 filtroContribMelhorias, filtroNotasAvulsas, filtroSerieNotas, ordemInscricao, dhSimulacao, dtVctoInicial, 
                 dtVctoFinal, dtInscricao, vlTotalCreditos, situacao, tipoIntervalo, criterioFormaPagamento, novoLivro):
        try:
            sql = """
                INSERT INTO simulacoes (                    
                    idIntegracao,                   
                    id_cloud, 
                    anoInicial,
                    anoFinal,                                               
                    nroDiasVencidos, 
                    nroLivro,
                    nroFolha,
                    nroPosicao,
                    anoLivro,
                    qtdTotalCreditos,
                    qtdInconsistentes,                    
                    filtroCreditos,
                    filtroPessoas,
                    filtroImoveis,
                    filtroEconomicos,
                    filtroReceitasDiversas,
                    filtroContribMelhorias,
                    filtroNotasAvulsas,
                    filtroSerieNotas,
                    ordemInscricao,
                    dhSimulacao,
                    dtVctoInicial, 
                    dtVctoFinal, 
                    dtInscricao, 
                    vlTotalCreditos, 
                    situacao, 
                    tipoIntervalo, 
                    criterioFormaPagamento, 
                    novoLivro, 
                    exibirParece,
                    nroConvenio                  
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(anoInicial)s,
                    %(anoFinal)s,
                    %(nroDiasVencidos)s,
                    %(nroLivro)s,
                    %(nroFolha)s,
                    %(nroPosicao)s,
                    %(anoLivro)s,
                    %(qtdTotalCreditos)s,
                    %(qtdInconsistentes)s,                    
                    %(filtroCreditos)s,
                    %(filtroPessoas)s,
                    %(filtroImoveis)s,
                    %(filtroEconomicos)s,
                    %(filtroReceitasDiversas)s,
                    %(filtroContribMelhorias)s,
                    %(filtroNotasAvulsas)s,
                    %(dhSimulacao)s,
                    %(ordemInscricao)s,                    
                    %(filtroSerieNotas)s,
                    %(dtVctoInicial)s,
                    %(dtVctoFinal)s,
                    %(dtInscricao)s,
                    %(vlTotalCreditos)s,
                    %(situacao)s,
                    %(tipoIntervalo)s,
                    %(criterioFormaPagamento)s,
                    %(novoLivro)s,                    
                    %(exibirParece)s,
                    %(nroConvenio)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                anoInicial = anoInicial,
                anoFinal = anoFinal,
                nroDiasVencidos = nroDiasVencidos,                               
                nroLivro = nroLivro,
                nroFolha = nroFolha,
                nroPosicao = nroPosicao,                               
                anoLivro = anoLivro,
                qtdTotalCreditos = qtdTotalCreditos,
                qtdInconsistentes = qtdInconsistentes,                                               
                filtroCreditos = filtroCreditos,
                filtroPessoas = filtroPessoas,                               
                filtroImoveis = filtroImoveis,
                filtroEconomicos = filtroEconomicos,
                filtroReceitasDiversas = filtroReceitasDiversas,                               
                filtroContribMelhorias = filtroContribMelhorias,
                filtroNotasAvulsas = filtroNotasAvulsas,
                dhSimulacao = dhSimulacao,
                ordemInscricao = ordemInscricao,
                filtroSerieNotas = filtroSerieNotas,
                dtVctoInicial = dtVctoInicial, 
                dtVctoFinal = dtVctoFinal, 
                dtInscricao = dtInscricao, 
                vlTotalCreditos = vlTotalCreditos, 
                situacao = situacao, 
                tipoIntervalo = tipoIntervalo, 
                criterioFormaPagamento = criterioFormaPagamento, 
                novoLivro = novoLivro

            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {simulacoes} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao inserir o anistias {simulacoes}. {intervaloFimr}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM simulacoes"
            if not self.query(sql_s):
                send_log_warning(f"simulacoes não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM simulacoes WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao executar a operação de exclusão do atividades econômicas. {intervaloFimr}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM simulacoes WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    simulacoes 
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
            sql = f"SELECT * FROM simulacoes WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao executar a operação de busca. {intervaloFimr}")

    def db_list(self):
        try:
            sql = "SELECT * FROM simulacoes WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM simulacoes WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao executar a operação de busca. {intervaloFimr}")

    def send_post(self, id, anoInicial, anoFinal, nroDiasVencidos, nroLivro, nroFolha, qtdTotalCreditos, nroPosicao, anoLivro, qtdInconsistentes, filtroCreditos, 
                 filtroPessoas, filtroImoveis, filtroEconomicos, filtroReceitasDiversas, filtroContribMelhorias, filtroNotasAvulsas, filtroSerieNotas, ordemInscricao, 
                 dhSimulacao, dtVctoInicial, dtVctoFinal, dtInscricao, 
                 vlTotalCreditos, situacao, tipoIntervalo, criterioFormaPagamento, novoLivro):
        objeto = {
                    "idIntegracao": f"Atos{id}",
                    "content": {}
        }

        if vlTotalCreditos:
            objeto["content"]["vlTotalCreditos"] = f"{vlTotalCreditos}"

        if tipoIntervalo:
            objeto["content"]["tipoIntervalo"] = f"{tipoIntervalo}"

        if criterioFormaPagamento:
            objeto["content"]["criterioFormaPagamento"] = f"{criterioFormaPagamento}"

        if novoLivro:
            objeto["content"]["novoLivro"] = { "id": int(novoLivro)}    

        if situacao:
            objeto["content"]["idAgenciaMedida"] = f"{situacao}"

        if anoInicial:
            objeto["content"]["anoInicial"] = { "id": int(anoInicial)}

        if dtInscricao:
            objeto["content"]["dtInscricao"] = { "id": int(dtInscricao)}

        if dtVctoInicial:
            objeto["content"]["dtVctoInicial"] = f"{dtVctoInicial}"

        if dtVctoFinal:
            objeto["content"]["dtVctoFinal"] = f"{dtVctoFinal}"

        if qtdTotalCreditos:
            objeto["content"]["qtdTotalCreditos"] = f"{qtdTotalCreditos}"

        if anoLivro:
            objeto["content"]["compartilhadoContribuinteMelhorias"] = f"{anoLivro}"

        if filtroCreditos:
            objeto["content"]["filtroCreditos"] = f"{filtroCreditos}"     

        if filtroPessoas:
            objeto["content"]["filtroPessoas"] = f"{filtroPessoas}"

        if filtroImoveis:
            objeto["content"]["filtroImoveis"] = f"{filtroImoveis}"

        if dhSimulacao:
            objeto["content"]["dhSimulacao"] = f"{dhSimulacao}"

        if qtdInconsistentes:
            objeto["content"]["qtdInconsistentes"] = f"{qtdInconsistentes}"             
        
        if nroLivro:
            objeto["content"]["nroLivro"] = { "id": int(nroLivro)}
        
        if filtroEconomicos:
            objeto["content"]["filtroEconomicos"] = f"{filtroEconomicos}"
        
        if anoFinal:
            objeto["content"]["anoFinal"] = { "id": int(anoFinal)}
        
        if nroDiasVencidos:
            objeto["content"]["nroDiasVencidos"] = { "id": int(nroDiasVencidos)}
        
        if filtroContribMelhorias:
            objeto["content"]["CasasDecimais"] = f"{filtroContribMelhorias}"
        
        if filtroNotasAvulsas:
            objeto["content"]["MaximoDigitos"] = f"{filtroNotasAvulsas}"
        
        if nroFolha:
            objeto["content"]["nroFolhas"] = f"{nroFolha}"
        
        if nroPosicao:
            objeto["content"]["CompartilhadoCondominio"] = f"{nroPosicao}"
        
        if filtroSerieNotas:
            objeto["content"]["filtroSerieNotas"] = f"{filtroSerieNotas}"
        
        if filtroReceitasDiversas:
            objeto["content"]["LivroEletronico"] = f"{filtroReceitasDiversas}"
        
        if ordemInscricao:
            objeto["content"]["ordemInscricao"] = f"{ordemInscricao}"

        envio = api_post("simulacoes", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

simulacoes = simulacoes()