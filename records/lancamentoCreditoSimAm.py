from samples import *
import json

class lancamentoCreditoSimAm(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idPessoa, idTipoNaturezaCredito, idTipoCredito, idTipoOperacaoCredito, dtLancamento, nrMesBase, nrAnoBase, cdControleLeiAto, 
                vlLancamento, nrAnoOperacao, nrOperacao, chaveUnificada, chave):
        try:
            sql = """
                INSERT INTO lancamentoCreditoSimAm (                    
                    idIntegracao,                   
                    id_cloud, 
                    idPessoa,
                    idTipoNaturezaCredito,                                               
                    idTipoCredito, 
                    idTipoOperacaoCredito,
                    dtLancamento,
                    nrAnoBase,
                    cdControleLeiAto,
                    nrMesBase,
                    vlLancamento,                    
                    nrAnoOperacao,
                    nrOperacao,
                    chaveUnificada,
                    chave      
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idPessoa)s,
                    %(idTipoNaturezaCredito)s,
                    %(idTipoCredito)s,
                    %(idTipoOperacaoCredito)s,
                    %(dtLancamento)s,
                    %(nrAnoBase)s,
                    %(cdControleLeiAto)s,
                    %(nrMesBase)s,
                    %(vlLancamento)s,                    
                    %(nrAnoOperacao)s,
                    %(nrOperacao)s,
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
                dtLancamento = dtLancamento,
                nrAnoBase = nrAnoBase,                               
                cdControleLeiAto = cdControleLeiAto,
                nrMesBase = nrMesBase,
                vlLancamento = vlLancamento,                                               
                nrAnoOperacao = nrAnoOperacao,
                nrOperacao = nrOperacao,                               
                chaveUnificada = chaveUnificada,
                chave = chave
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {lancamentoCreditoSimAm} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {lancamentoCreditoSimAm}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM lancamentoCreditoSimAm"
            if not self.query(sql_s):
                send_log_warning(f"lancamentoCreditoSimAm não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM lancamentoCreditoSimAm WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM lancamentoCreditoSimAm WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    lancamentoCreditoSimAm 
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
            sql = f"SELECT * FROM lancamentoCreditoSimAm WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM lancamentoCreditoSimAm WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM lancamentoCreditoSimAm WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idPessoa, idTipoNaturezaCredito, idTipoCredito, idTipoOperacaoCredito, dtLancamento, nrMesBase, nrAnoBase, cdControleLeiAto, 
                vlLancamento, nrAnoOperacao, nrOperacao, chaveUnificada, chave):
        objeto = {
            "idIntegracao": f"lancamentoCreditoSimAm{id}",
            "content": {}                                 
        }

        if idPessoa:
            objeto["content"]["idPessoa"] = { "id": int(idPessoa)}
        
        if cdControleLeiAto:
            objeto["content"]["cdControleLeiAto"] = f"{cdControleLeiAto}"

        if idTipoNaturezaCredito:
            objeto["content"]["idTipoNaturezaCredito"] = { "id": int(idTipoNaturezaCredito)}           
        
        if idTipoOperacaoCredito:
            objeto["content"]["idTipoOperacaoCredito"] = { "id": int(idTipoOperacaoCredito)} 

        if nrOperacao:
            objeto["content"]["nrOperacao"] = f"{nrOperacao}"  

        if dtLancamento:
            objeto["content"]["dtLancamento"] = f"{dtLancamento}"

        if nrAnoBase:
            objeto["content"]["nrAnoBase"] = f"{nrAnoBase}"   

        if nrAnoOperacao:
            objeto["content"]["nrAnoOperacao"] = f"{nrAnoOperacao}"
        
        if vlLancamento:
            objeto["content"]["vlLancamento"] = f"{vlLancamento}"
           
        if chaveUnificada:
            objeto["content"]["chaveUnificada"] = f"{chaveUnificada}"
        
        if nrMesBase:
            objeto["content"]["nrMesBase"] = f"{nrMesBase}"

        if idTipoCredito != None:
            objeto[0]["content"]["idTipoCredito"] = { "id": int(idTipoCredito)}               

        if chave != None:
            objeto[0]["content"]["chave"] = f"{chave}"        
            
        envio = api_post("lancamentoCreditoSimAm", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

lancamentoCreditoSimAm = lancamentoCreditoSimAm()