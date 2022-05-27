from samples import *
import json

class deducaoDividaSimAm(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idPessoa, nrOperacao, nrAnoOperacao, nrDivida, nrAnoDivida, dtOperacao, cdControleLeiAto, vlOperacao, 
                tipoDeducao, dsMotivo, chaveUnificada, chave):
        try:
            sql = """
                INSERT INTO deducaoDividaSimAm (                    
                    idIntegracao,                   
                    id_cloud, 
                    idPessoa,
                    nrOperacao,                                               
                    nrAnoOperacao, 
                    nrDivida,
                    nrAnoDivida,
                    cdControleLeiAto,
                    vlOperacao,
                    dtOperacao,
                    tipoDeducao,                    
                    dsMotivo,
                    chaveUnificada,
                    chave     
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idPessoa)s,
                    %(nrOperacao)s,
                    %(nrAnoOperacao)s,
                    %(nrDivida)s,
                    %(nrAnoDivida)s,
                    %(cdControleLeiAto)s,
                    %(vlOperacao)s,
                    %(dtOperacao)s,
                    %(tipoDeducao)s,                    
                    %(dsMotivo)s,
                    %(chaveUnificada)s,
                    %(chave)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idPessoa = idPessoa,
                nrOperacao = nrOperacao,
                nrAnoOperacao = nrAnoOperacao,                               
                nrDivida = nrDivida,
                nrAnoDivida = nrAnoDivida,
                cdControleLeiAto = cdControleLeiAto,                               
                vlOperacao = vlOperacao,
                dtOperacao = dtOperacao,
                tipoDeducao = tipoDeducao,                                               
                dsMotivo = dsMotivo,
                chaveUnificada = chaveUnificada,                               
                chave = chave
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {deducaoDividaSimAm} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {deducaoDividaSimAm}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM deducaoDividaSimAm"
            if not self.query(sql_s):
                send_log_warning(f"deducaoDividaSimAm não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM deducaoDividaSimAm WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM deducaoDividaSimAm WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    deducaoDividaSimAm 
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
            sql = f"SELECT * FROM deducaoDividaSimAm WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM deducaoDividaSimAm WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM deducaoDividaSimAm WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idPessoa, nrOperacao, nrAnoOperacao, nrDivida, nrAnoDivida, dtOperacao, cdControleLeiAto, vlOperacao, 
                tipoDeducao, dsMotivo, chaveUnificada, chave):
        objeto = {
            "idIntegracao": f"deducaoDividaSimAm{id}",
            "content": {}                                 
        }

        if idPessoa:
            objeto["content"]["idPessoa"] = { "id": int(idPessoa)}
        
        if vlOperacao:
            objeto["content"]["vlOperacao"] = f"{vlOperacao}"

        if nrOperacao:
            objeto["content"]["nrOperacao"] = f"{nrOperacao}"           
        
        if nrDivida:
            objeto["content"]["nrDivida"] = f"{nrDivida}" 

        if chaveUnificada:
            objeto["content"]["chaveUnificada"] = f"{chaveUnificada}"  

        if nrAnoDivida:
            objeto["content"]["nrAnoDivida"] = f"{nrAnoDivida}"

        if cdControleLeiAto:
            objeto["content"]["cdControleLeiAto"] = f"{cdControleLeiAto}"   

        if dsMotivo:
            objeto["content"]["dsMotivo"] = f"{dsMotivo}"
        
        if tipoDeducao:
            objeto["content"]["tipoDeducao"] = f"{tipoDeducao}"
           
        if chave:
            objeto["content"]["chave"] = f"{chave}"
                        
        if dtOperacao:
            objeto["content"]["dtOperacao"] = f"{dtOperacao}"

        if nrAnoOperacao != None:
            objeto[0]["content"]["nrAnoOperacao"] = f"{nrAnoOperacao}"               

                    
        envio = api_post("deducaoDividaSimAm", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

deducaoDividaSimAm = deducaoDividaSimAm()