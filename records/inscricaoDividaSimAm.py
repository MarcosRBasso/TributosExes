from samples import *
import json

class inscricaoDividaSimAm(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idPessoa, idTipoNaturezaCredito, idTipoCredito, idTipoOperacaoCredito, nrOperacao, nrCredito, nrAnoOperacao, nrAnoBase, 
                nrAnoInscricao, nrAnoCredito, cdControleLeiAto, vlInscricao, chaveUnificada, chave):
        try:
            sql = """
                INSERT INTO inscricaoDividaSimAm (                    
                    idIntegracao,                   
                    id_cloud, 
                    idPessoa,
                    idTipoNaturezaCredito,                                               
                    idTipoCredito, 
                    idTipoOperacaoCredito,
                    nrOperacao,
                    nrAnoOperacao,
                    nrAnoBase,
                    nrCredito,
                    nrAnoInscricao,                    
                    nrAnoCredito,
                    cdControleLeiAto,
                    vlInscricao,
                    chaveUnificada,
                    chave       
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idPessoa)s,
                    %(idTipoNaturezaCredito)s,
                    %(idTipoCredito)s,
                    %(idTipoOperacaoCredito)s,
                    %(nrOperacao)s,
                    %(nrAnoOperacao)s,
                    %(nrAnoBase)s,
                    %(nrCredito)s,
                    %(nrAnoInscricao)s,                    
                    %(nrAnoCredito)s,
                    %(cdControleLeiAto)s,
                    %(vlInscricao)s,
                    %(chaveUnificada)s,
                    %(chave)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idPessoa = idPessoa,
                idTipoNaturezaCredito = idTipoNaturezaCredito,
                idTipoCredito = idTipoCredito,                               
                idTipoOperacaoCredito = idTipoOperacaoCredito,
                nrOperacao = nrOperacao,
                nrAnoOperacao = nrAnoOperacao,                               
                nrAnoBase = nrAnoBase,
                nrCredito = nrCredito,
                nrAnoInscricao = nrAnoInscricao,                                               
                nrAnoCredito = nrAnoCredito,
                cdControleLeiAto = cdControleLeiAto,                               
                vlInscricao = vlInscricao,
                chaveUnificada = chaveUnificada,
                chave = chave
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {inscricaoDividaSimAm} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {inscricaoDividaSimAm}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM inscricaoDividaSimAm"
            if not self.query(sql_s):
                send_log_warning(f"inscricaoDividaSimAm não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM inscricaoDividaSimAm WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM inscricaoDividaSimAm WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    inscricaoDividaSimAm 
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
            sql = f"SELECT * FROM inscricaoDividaSimAm WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM inscricaoDividaSimAm WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM inscricaoDividaSimAm WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idPessoa, idTipoNaturezaCredito, idTipoCredito, idTipoOperacaoCredito, nrOperacao, nrCredito, nrAnoOperacao, nrAnoBase, 
                nrAnoInscricao, nrAnoCredito, cdControleLeiAto, vlInscricao, chaveUnificada, chave):
        objeto = {
            "idIntegracao": f"inscricaoDividaSimAm{id}",
            "content": {}                                 
        }

        if idPessoa:
            objeto["content"]["idPessoa"] = { "id": int(idPessoa)}
        
        if nrAnoBase:
            objeto["content"]["nrAnoBase"] = f"{nrAnoBase}"

        if idTipoNaturezaCredito:
            objeto["content"]["idTipoNaturezaCredito"] = { "id": int(idTipoNaturezaCredito)}           
        
        if idTipoOperacaoCredito:
            objeto["content"]["idTipoOperacaoCredito"] = { "id": int(idTipoOperacaoCredito)} 

        if cdControleLeiAto:
            objeto["content"]["cdControleLeiAto"] = f"{cdControleLeiAto}"  

        if nrOperacao:
            objeto["content"]["nrOperacao"] = f"{nrOperacao}"

        if nrAnoOperacao:
            objeto["content"]["nrAnoOperacao"] = f"{nrAnoOperacao}"   

        if nrAnoCredito:
            objeto["content"]["nrAnoCredito"] = f"{nrAnoCredito}"
        
        if nrAnoInscricao:
            objeto["content"]["nrAnoInscricao"] = f"{nrAnoInscricao}"
           
        if vlInscricao:
            objeto["content"]["vlInscricao"] = f"{vlInscricao}"
        
        if chave:
            objeto["content"]["chave"] = f"{chave}"
        
        if nrCredito:
            objeto["content"]["nrCredito"] = f"{nrCredito}"

        if idTipoCredito != None:
            objeto[0]["content"]["idTipoCredito"] = { "id": int(idTipoCredito)}               

        if chaveUnificada != None:
            objeto[0]["content"]["chaveUnificada"] = f"{chaveUnificada}"        
            
        envio = api_post("inscricaoDividaSimAm", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

inscricaoDividaSimAm = inscricaoDividaSimAm()