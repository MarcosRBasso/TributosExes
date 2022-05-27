from samples import *
import json

class estornoLancamentoCreditoSimAm(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idPessoa, nrOperacao, nrAnoOperacao, nrAnoCredito, dtEstorno, cdControleLeiAto, vlEstorno, dsMotivo, 
                chaveUnificada, chave):
        try:
            sql = """
                INSERT INTO estornoLancamentoCreditoSimAm (                    
                    idIntegracao,                   
                    id_cloud, 
                    idPessoa,
                    nrOperacao,                                               
                    nrAnoOperacao, 
                    nrAnoCredito,
                    dtEstorno,
                    vlEstorno,
                    dsMotivo,
                    cdControleLeiAto,
                    chaveUnificada,                    
                    chave
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idPessoa)s,
                    %(nrOperacao)s,
                    %(nrAnoOperacao)s,
                    %(nrAnoCredito)s,
                    %(dtEstorno)s,
                    %(vlEstorno)s,
                    %(dsMotivo)s,
                    %(cdControleLeiAto)s,
                    %(chaveUnificada)s,                    
                    %(chave)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idPessoa = idPessoa,
                nrOperacao = nrOperacao,
                nrAnoOperacao = nrAnoOperacao,                               
                nrAnoCredito = nrAnoCredito,
                dtEstorno = dtEstorno,
                vlEstorno = vlEstorno,                               
                dsMotivo = dsMotivo,
                cdControleLeiAto = cdControleLeiAto,
                chaveUnificada = chaveUnificada,                                               
                chave = chave
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {estornoLancamentoCreditoSimAm} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {estornoLancamentoCreditoSimAm}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM estornoLancamentoCreditoSimAm"
            if not self.query(sql_s):
                send_log_warning(f"estornoLancamentoCreditoSimAm não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM estornoLancamentoCreditoSimAm WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM estornoLancamentoCreditoSimAm WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    estornoLancamentoCreditoSimAm 
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
            sql = f"SELECT * FROM estornoLancamentoCreditoSimAm WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM estornoLancamentoCreditoSimAm WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM estornoLancamentoCreditoSimAm WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idPessoa, nrOperacao, nrAnoOperacao, nrAnoCredito, dtEstorno, cdControleLeiAto, vlEstorno, dsMotivo, 
                chaveUnificada, chave):
        objeto = {
            "idIntegracao": f"estornoLancamentoCreditoSimAm{id}",
            "content": {}                                 
        } 

        if idPessoa:
            objeto["content"]["idPessoa"] = { "id": int(idPessoa)}   
        
        if dsMotivo:
            objeto["content"]["dsMotivo"] = f"{dsMotivo}"

        if nrOperacao:
            objeto["content"]["nrOperacao"] = f"{nrOperacao}"           
        
        if nrAnoCredito:
            objeto["content"]["nrAnoCredito"] = f"{nrAnoCredito}"  

        if dtEstorno:
            objeto["content"]["dtEstorno"] = f"{dtEstorno}"

        if vlEstorno:
            objeto["content"]["vlEstorno"] = f"{vlEstorno}"   

        if chave:
            objeto["content"]["chave"] = f"{chave}"
        
        if chaveUnificada:
            objeto["content"]["chaveUnificada"] = f"{chaveUnificada}"
        
        if cdControleLeiAto:
            objeto["content"]["cdControleLeiAto"] = f"{cdControleLeiAto}"

        if nrAnoOperacao != None:
            objeto[0]["content"]["nrAnoOperacao"] = f"{nrAnoOperacao}"         
            
        envio = api_post("estornoLancamentoCreditoSimAm", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

estornoLancamentoCreditoSimAm = estornoLancamentoCreditoSimAm()