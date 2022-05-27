from samples import *
import json

class contribMelhoriasImoveis(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idContribuicaoMelhorias, dtAdesao, idImoveis, intervalo, percValorizacao, qtdParcelas, tipoIntervalo, usaSaldoDevedor, 
                vlPrevio, vlValorizacao, vlVenal, situacaoImovelMelhoria, custoMelhoriaImovel):
        try:
            sql = """
                INSERT INTO contribMelhoriasImoveis (                    
                    idIntegracao,                   
                    id_cloud, 
                    idContribuicaoMelhorias,
                    dtAdesao,                                               
                    idImoveis, 
                    intervalo,
                    percValorizacao,
                    tipoIntervalo,
                    usaSaldoDevedor,
                    qtdParcelas,
                    vlPrevio,                    
                    vlValorizacao,
                    vlVenal,
                    situacaoImovelMelhoria,
                    custoMelhoriaImovel                  
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idContribuicaoMelhorias)s,
                    %(dtAdesao)s,
                    %(idImoveis)s,
                    %(intervalo)s,
                    %(percValorizacao)s,
                    %(tipoIntervalo)s,
                    %(usaSaldoDevedor)s,
                    %(qtdParcelas)s,
                    %(vlPrevio)s,                    
                    %(vlValorizacao)s,
                    %(vlVenal)s,
                    %(situacaoImovelMelhoria)s,
                    %(custoMelhoriaImovel)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idContribuicaoMelhorias = idContribuicaoMelhorias,
                dtAdesao = dtAdesao,
                idImoveis = idImoveis,                               
                intervalo = intervalo,
                percValorizacao = percValorizacao,
                tipoIntervalo = tipoIntervalo,                               
                usaSaldoDevedor = usaSaldoDevedor,
                qtdParcelas = qtdParcelas,
                vlPrevio = vlPrevio,                                               
                vlValorizacao = vlValorizacao,
                vlVenal = vlVenal,                               
                situacaoImovelMelhoria = situacaoImovelMelhoria,
                custoMelhoriaImovel = custoMelhoriaImovel
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {contribMelhoriasImoveis} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {contribMelhoriasImoveis}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM contribMelhoriasImoveis"
            if not self.query(sql_s):
                send_log_warning(f"contribMelhoriasImoveis não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM contribMelhoriasImoveis WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM contribMelhoriasImoveis WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    contribMelhoriasImoveis 
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
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de atualização da atividades Economicas. {error}")

    def db_search(self, id):
        try:
            sql = f"SELECT * FROM contribMelhoriasImoveis WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM contribMelhoriasImoveis WHERE id_cloud is null"
            data = self.query(sql)
            if data:
                send_log_info("Consulta de todos os atividades Economicas realizada com sucesso.")
                return data
            return None
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def get_id_cloud(self, id):
        if (id == None):
            return None
        try:
            sql = f"SELECT id_cloud FROM contribMelhoriasImoveis WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idContribuicaoMelhorias, dtAdesao, idImoveis, intervalo, percValorizacao, qtdParcelas, tipoIntervalo, usaSaldoDevedor, 
                vlPrevio, vlValorizacao, vlVenal, situacaoImovelMelhoria, custoMelhoriaImovel):
        objeto = {
            "idIntegracao": f"contribMelhoriasImoveis{id}",
            "content": {}                                 
        }
        if idContribuicaoMelhorias:
            objeto["content"]["idContribuicaoMelhorias"] = { "id": int(idContribuicaoMelhorias)}
        
        if usaSaldoDevedor:
            objeto["content"]["usaSaldoDevedor"] = f"{usaSaldoDevedor}"

        if dtAdesao:
            objeto["content"]["dtAdesao"] = f"{dtAdesao}"
        
        if intervalo:
            objeto["content"]["intervalo"] = f"{intervalo}" 

        if vlVenal:
            objeto["content"]["vlVenal"] = f"{vlVenal}"       
       
        if percValorizacao:
            objeto["content"]["percValorizacao"] = f"{percValorizacao}"

        if tipoIntervalo:
            objeto["content"]["tipoIntervalo"] = f"{tipoIntervalo}"   

        if vlValorizacao:
            objeto["content"]["vlValorizacao"] = f"{vlValorizacao}"
        
        if vlPrevio:
            objeto["content"]["vlPrevio"] = f"{vlPrevio}"
           
        if situacaoImovelMelhoria:
            objeto["content"]["situacaoImovelMelhoria"] = f"{situacaoImovelMelhoria}"
        
        if qtdParcelas:
            objeto["content"]["qtdParcelas"] = { "id": int(qtdParcelas)}

        if idImoveis != None:
            objeto[0]["content"]["idImoveis"] = { "id": int(idImoveis) }               

        if custoMelhoriaImovel != None:
            objeto[0]["content"]["custoMelhoriaImovel"] = f"{custoMelhoriaImovel}"    
            
        envio = api_post("contribMelhoriasImoveis", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

contribMelhoriasImoveis = contribMelhoriasImoveis()