from samples import *
import json

class integracoesContabeis(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idConvenios, dataCreditoFinal, dataCreditoInicial, dataEstornoFinal, dataEstornoInicial, dataMovimentacaoFinal, dataMovimentacaoInicial,
                  dataPagamentoFinal, dataPagamentoInicial, tipoIntegracao, tipoLancamentoIntegrados):
        try:
            sql = """
                INSERT INTO integracoesContabeis (                    
                    idIntegracao,                   
                    id_cloud, 
                    idConvenios,
                    dataCreditoFinal,                                               
                    dataCreditoInicial, 
                    dataEstornoFinal,
                    dataEstornoInicial,
                    dataMovimentacaoInicial,
                    dataPagamentoFinal,
                    dataMovimentacaoFinal,
                    dataPagamentoInicial,                    
                    tipoIntegracao, 
                    tipoLancamentoIntegrados             
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idConvenios)s,
                    %(dataCreditoFinal)s,
                    %(dataCreditoInicial)s,
                    %(dataEstornoFinal)s,
                    %(dataEstornoInicial)s,
                    %(dataMovimentacaoInicial)s,
                    %(dataPagamentoFinal)s,
                    %(dataMovimentacaoFinal)s,
                    %(dataPagamentoInicial)s,                    
                    %(tipoIntegracao)s,
                    %(tipoLancamentoIntegrados)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idConvenios = idConvenios,
                dataCreditoFinal = dataCreditoFinal,
                dataCreditoInicial = dataCreditoInicial,                               
                dataEstornoFinal = dataEstornoFinal,
                dataEstornoInicial = dataEstornoInicial,
                dataMovimentacaoInicial = dataMovimentacaoInicial,                               
                dataPagamentoFinal = dataPagamentoFinal,
                dataMovimentacaoFinal = dataMovimentacaoFinal,
                dataPagamentoInicial = dataPagamentoInicial,                                               
                tipoIntegracao = tipoIntegracao,
                tipoLancamentoIntegrados = tipoLancamentoIntegrados 
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {integracoesContabeis} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {integracoesContabeis}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM integracoesContabeis"
            if not self.query(sql_s):
                send_log_warning(f"integracoesContabeis não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM integracoesContabeis WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM integracoesContabeis WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    integracoesContabeis 
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
            sql = f"SELECT * FROM integracoesContabeis WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM integracoesContabeis WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM integracoesContabeis WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idConvenios, dataCreditoFinal, dataCreditoInicial, dataEstornoFinal, dataEstornoInicial, dataMovimentacaoFinal, dataMovimentacaoInicial, dataPagamentoFinal, 
                dataPagamentoInicial, tipoIntegracao, tipoLancamentoIntegrados):
        objeto = {
            "idIntegracao": f"integracoesContabeis{id}",
            "content": {}                                 
        }
        if idConvenios:
            objeto["content"]["idConvenios"] = { "id": int(idConvenios)}

        if tipoLancamentoIntegrados:
            objeto["content"]["tipoLancamentoIntegrados"] = f"{tipoLancamentoIntegrados}"    
        
        if dataPagamentoFinal:
            objeto["content"]["dataPagamentoFinal"] = f"{dataPagamentoFinal}"

        if dataCreditoFinal:
            objeto["content"]["dataCreditoFinal"] = f"{dataCreditoFinal}"
           
        if dataEstornoFinal:
            objeto["content"]["dataEstornoFinal"] = f"{dataEstornoFinal}"
       
        if dataEstornoInicial:
            objeto["content"]["dataEstornoInicial"] = f"{dataEstornoInicial}"

        if dataMovimentacaoInicial:
            objeto["content"]["dataMovimentacaoInicial"] = f"{dataMovimentacaoInicial}"   

        if tipoIntegracao:
            objeto["content"]["tipoIntegracao"] = f"{tipoIntegracao}"
        
        if dataPagamentoInicial:
            objeto["content"]["dataPagamentoInicial"] = f"{dataPagamentoInicial}"
        if dataMovimentacaoFinal:
            objeto["content"]["dataMovimentacaoFinal"] = f"{dataMovimentacaoFinal}"

        if dataCreditoInicial != None:
            objeto[0]["content"]["dataCreditoInicial"] = f"{dataCreditoInicial}"    
            
        envio = api_post("integracoesContabeis", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

integracoesContabeis = integracoesContabeis()