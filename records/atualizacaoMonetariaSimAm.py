from samples import *
import json

class atualizacaoMonetariaSimAm(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, nrOperacao, idPessoa, nrAnoOperacao, nrCredito, nrAnoCredito, dtOperacao, cdControleLeiAto, vlOperacao, 
                idTipoAtualizacaoCredito, chaveUnificada, chave):
        try:
            sql = """
                INSERT INTO atualizacaoMonetariaSimAm (                    
                    idIntegracao,                   
                    id_cloud, 
                    nrOperacao,
                    idPessoa,                                               
                    nrAnoOperacao, 
                    nrCredito,
                    nrAnoCredito,
                    cdControleLeiAto,
                    vlOperacao,
                    dtOperacao,
                    idTipoAtualizacaoCredito,                    
                    chaveUnificada,
                    chave   
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(nrOperacao)s,
                    %(idPessoa)s,
                    %(nrAnoOperacao)s,
                    %(nrCredito)s,
                    %(nrAnoCredito)s,
                    %(cdControleLeiAto)s,
                    %(vlOperacao)s,
                    %(dtOperacao)s,
                    %(idTipoAtualizacaoCredito)s,                    
                    %(chaveUnificada)s,
                    %(chave)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                nrOperacao = nrOperacao,
                idPessoa = idPessoa,
                nrAnoOperacao = nrAnoOperacao,                               
                nrCredito = nrCredito,
                nrAnoCredito = nrAnoCredito,
                cdControleLeiAto = cdControleLeiAto,                               
                vlOperacao = vlOperacao,
                dtOperacao = dtOperacao,
                idTipoAtualizacaoCredito = idTipoAtualizacaoCredito,                                               
                chaveUnificada = chaveUnificada,
                chave = chave
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {atualizacaoMonetariaSimAm} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {atualizacaoMonetariaSimAm}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM atualizacaoMonetariaSimAm"
            if not self.query(sql_s):
                send_log_warning(f"atualizacaoMonetariaSimAm n??o encontrado para excluir.")
                return
            sql_d = f"DELETE FROM atualizacaoMonetariaSimAm WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias exclu??dos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de exclus??o do atividades econ??micas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM atualizacaoMonetariaSimAm WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} n??o encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    atualizacaoMonetariaSimAm 
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
            send_log_error(f"Erro ao executar a opera????o de atualiza????o da atividades Economicas. {error}")

    def db_search(self, id):
        try:
            sql = f"SELECT * FROM atualizacaoMonetariaSimAm WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} n??o encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM atualizacaoMonetariaSimAm WHERE id_cloud is null"
            data = self.query(sql)
            if data:
                send_log_info("Consulta de todos os atividades Economicas realizada com sucesso.")
                return data
            return None
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de busca. {error}")

    def get_id_cloud(self, id):
        if (id == None):
            return None
        try:
            sql = f"SELECT id_cloud FROM atualizacaoMonetariaSimAm WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} n??o encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de busca. {error}")

    def send_post(self, id, nrOperacao, idPessoa, nrAnoOperacao, nrCredito, nrAnoCredito, dtOperacao, cdControleLeiAto, vlOperacao, 
                idTipoAtualizacaoCredito, chaveUnificada, chave):
        objeto = {
            "idIntegracao": f"atualizacaoMonetariaSimAm{id}",
            "content": {}                                 
        }  

        if nrOperacao:
            objeto["content"]["nrOperacao"] = { "id": int(nrOperacao)}
        
        if vlOperacao:
            objeto["content"]["vlOperacao"] = f"{vlOperacao}"

        if idPessoa:
            objeto["content"]["idPessoa"] =  { "id": int(idPessoa)}           
        
        if nrCredito:
            objeto["content"]["nrCredito"] = f"{nrCredito}" 

        if chave:
            objeto["content"]["chave"] = f"{chave}"  

        if nrAnoCredito:
            objeto["content"]["nrAnoCredito"] = f"{nrAnoCredito}"

        if cdControleLeiAto:
            objeto["content"]["cdControleLeiAto"] = f"{cdControleLeiAto}"   

        if chaveUnificada:
            objeto["content"]["chaveUnificada"] = f"{chaveUnificada}"
        
        if idTipoAtualizacaoCredito:
            objeto["content"]["idTipoAtualizacaoCredito"] =  { "id": int(idTipoAtualizacaoCredito)}
        
        if dtOperacao:
            objeto["content"]["dtOperacao"] = f"{dtOperacao}"

        if nrAnoOperacao != None:
            objeto[0]["content"]["nrAnoOperacao"] = f"{nrAnoOperacao}"            
            
        envio = api_post("atualizacaoMonetariaSimAm", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

atualizacaoMonetariaSimAm = atualizacaoMonetariaSimAm()