from samples import *
import json

class manutencaoDivida(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idAto, idMotivo, qtdDividas, vlPrestacaoDiversa, nroProcesso, formasPagamentoPrestacaoDiversa, especificacoes, observacoes, 
                obsHomologManutencao, situacao, tiposManutencoesDividas, dtValidade, dhManutencao):
        try:
            sql = """
                INSERT INTO manutencaoDivida (                    
                    idIntegracao,                   
                    id_cloud, 
                    idAto,
                    idMotivo,                                               
                    qtdDividas, 
                    vlPrestacaoDiversa,
                    nroProcesso,
                    especificacoes,
                    observacoes,
                    formasPagamentoPrestacaoDiversa,
                    obsHomologManutencao,                    
                    situacao,
                    dtValidade,
                    tiposManutencoesDividas,
                    dhManutencao              
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idAto)s,
                    %(idMotivo)s,
                    %(qtdDividas)s,
                    %(vlPrestacaoDiversa)s,
                    %(nroProcesso)s,
                    %(especificacoes)s,
                    %(observacoes)s,
                    %(formasPagamentoPrestacaoDiversa)s,
                    %(obsHomologManutencao)s,                    
                    %(situacao)s,
                    %(dtValidade)s,
                    %(tiposManutencoesDividas)s,
                    %(dhManutencao)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idAto = idAto,
                idMotivo = idMotivo,
                qtdDividas = qtdDividas,                               
                vlPrestacaoDiversa = vlPrestacaoDiversa,
                nroProcesso = nroProcesso,
                especificacoes = especificacoes,                               
                observacoes = observacoes,
                formasPagamentoPrestacaoDiversa = formasPagamentoPrestacaoDiversa,
                obsHomologManutencao = obsHomologManutencao,                                               
                situacao = situacao,
                dtValidade = dtValidade,                               
                tiposManutencoesDividas = tiposManutencoesDividas,
                dhManutencao = dhManutencao
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {manutencaoDivida} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {manutencaoDivida}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM manutencaoDivida"
            if not self.query(sql_s):
                send_log_warning(f"manutencaoDivida não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM manutencaoDivida WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM manutencaoDivida WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    manutencaoDivida 
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
            sql = f"SELECT * FROM manutencaoDivida WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM manutencaoDivida WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM manutencaoDivida WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idAto, idMotivo, qtdDividas, vlPrestacaoDiversa, nroProcesso, formasPagamentoPrestacaoDiversa, especificacoes, observacoes, 
                obsHomologManutencao, situacao, tiposManutencoesDividas, dtValidade, dhManutencao):
        objeto = {
            "idIntegracao": f"manutencaoDivida{id}",
            "content": {}                                 
        }
        if idAto:
            objeto["content"]["idAto"] = { "id": int(idAto)}
        
        if observacoes:
            objeto["content"]["observacoes"] = f"{observacoes}"

        if idMotivo:
            objeto["content"]["idMotivo"] = { "id": int(idMotivo)}
        
        if vlPrestacaoDiversa:
            objeto["content"]["vlPrestacaoDiversa"] = f"{vlPrestacaoDiversa}" 

        if dtValidade:
            objeto["content"]["dtValidade"] = f"{dtValidade}"       
       
        if nroProcesso:
            objeto["content"]["nroProcesso"] = f"{nroProcesso}"

        if especificacoes:
            objeto["content"]["especificacoes"] = f"{especificacoes}"   

        if situacao:
            objeto["content"]["situacao"] = f"{situacao}"
        
        if obsHomologManutencao:
            objeto["content"]["obsHomologManutencao"] = f"{obsHomologManutencao}"
           
        if tiposManutencoesDividas:
            objeto["content"]["tiposManutencoesDividas"] = f"{tiposManutencoesDividas}"
        
        if formasPagamentoPrestacaoDiversa:
            objeto["content"]["formasPagamentoPrestacaoDiversa"] = f"{formasPagamentoPrestacaoDiversa}"

        if qtdDividas != None:
            objeto[0]["content"]["qtdDividas"] = { "id": int(qtdDividas) }               

        if dhManutencao != None:
            objeto[0]["content"]["dhManutencao"] = f"{dhManutencao}"
            
        envio = api_post("manutencaoDivida", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

manutencaoDivida = manutencaoDivida()