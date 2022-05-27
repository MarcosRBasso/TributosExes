from samples import *
import json

class atualizacaoDividaAtivaSimAm(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idPessoa, idTipoAtualizacaoCredito, nrOperacao, nrAnoOperacao, nrDivida, nrAnoDivida, dtAtualizacao, cdControleLeiAto, 
                vlAtualizacao, chaveUnificada, chave):
        try:
            sql = """
                INSERT INTO atualizacaoDividaAtivaSimAm (                    
                    idIntegracao,                   
                    id_cloud, 
                    idPessoa,
                    idTipoAtualizacaoCredito,                                               
                    nrOperacao, 
                    nrAnoOperacao,
                    nrDivida,
                    dtAtualizacao,
                    cdControleLeiAto,
                    nrAnoDivida,
                    vlAtualizacao,                    
                    chaveUnificada,
                    chave
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idPessoa)s,
                    %(idTipoAtualizacaoCredito)s,
                    %(nrOperacao)s,
                    %(nrAnoOperacao)s,
                    %(nrDivida)s,
                    %(dtAtualizacao)s,
                    %(cdControleLeiAto)s,
                    %(nrAnoDivida)s,
                    %(vlAtualizacao)s,                    
                    %(chaveUnificada)s,
                    %(chave)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idPessoa = idPessoa,
                idTipoAtualizacaoCredito = idTipoAtualizacaoCredito,
                nrOperacao = nrOperacao,                               
                nrAnoOperacao = nrAnoOperacao,
                nrDivida = nrDivida,
                dtAtualizacao = dtAtualizacao,                               
                cdControleLeiAto = cdControleLeiAto,
                nrAnoDivida = nrAnoDivida,
                vlAtualizacao = vlAtualizacao,                                               
                chaveUnificada = chaveUnificada,
                chave = chave
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {atualizacaoDividaAtivaSimAm} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {atualizacaoDividaAtivaSimAm}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM atualizacaoDividaAtivaSimAm"
            if not self.query(sql_s):
                send_log_warning(f"atualizacaoDividaAtivaSimAm não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM atualizacaoDividaAtivaSimAm WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM atualizacaoDividaAtivaSimAm WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    atualizacaoDividaAtivaSimAm 
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
            sql = f"SELECT * FROM atualizacaoDividaAtivaSimAm WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM atualizacaoDividaAtivaSimAm WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM atualizacaoDividaAtivaSimAm WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idPessoa, idTipoAtualizacaoCredito, nrOperacao, nrAnoOperacao, nrDivida, nrAnoDivida, dtAtualizacao, cdControleLeiAto, 
                vlAtualizacao, chaveUnificada, chave):
        objeto = {
            "idIntegracao": f"atualizacaoDividaAtivaSimAm{id}",
            "content": {}                                 
        }
        if idPessoa:
            objeto["content"]["idPessoa"] = { "id": int(idPessoa)}
        
        if cdControleLeiAto:
            objeto["content"]["cdControleLeiAto"] = f"{cdControleLeiAto}"

        if idTipoAtualizacaoCredito:
            objeto["content"]["idTipoAtualizacaoCredito"] = { "id": int(idTipoAtualizacaoCredito)}           
        
        if nrAnoOperacao:
            objeto["content"]["nrAnoOperacao"] = f"{nrAnoOperacao}" 

        if chave:
            objeto["content"]["chave"] = f"{chave}"  

        if nrDivida:
            objeto["content"]["nrDivida"] = f"{nrDivida}"

        if dtAtualizacao:
            objeto["content"]["dtAtualizacao"] = f"{dtAtualizacao}"   

        if chaveUnificada:
            objeto["content"]["chaveUnificada"] = f"{chaveUnificada}"
        
        if vlAtualizacao:
            objeto["content"]["vlAtualizacao"] = f"{vlAtualizacao}"

        if nrAnoDivida:
            objeto["content"]["nrAnoDivida"] = f"{nrAnoDivida}"

        if nrOperacao != None:
            objeto[0]["content"]["nrOperacao"] = f"{nrOperacao}"               

        envio = api_post("atualizacaoDividaAtivaSimAm", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

atualizacaoDividaAtivaSimAm = atualizacaoDividaAtivaSimAm()