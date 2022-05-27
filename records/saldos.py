from samples import *
import json

class saldos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idSaldoOrigem, idSaldo, idPessoa, idPagamentos, comentario, idManutencaoPagamento, nroProcesso, observacoes, 
                dtSaldo, dtValidade, vlSaldoTotal, vlSaldoUtilizado, situacao, tipoInconsistencia, tipoSaldo, tipoUtilizacaoSaldo, utilizado):
        try:
            sql = """
                INSERT INTO saldos (                    
                    idIntegracao,                   
                    id_cloud, 
                    idSaldoOrigem,
                    idSaldo,                                               
                    idPessoa, 
                    idPagamentos,
                    comentario,
                    nroProcesso,
                    observacoes,
                    idManutencaoPagamento,
                    dtSaldo,                    
                    dtValidade,
                    vlSaldoTotal,
                    vlSaldoUtilizado,
                    situacao,
                    tipoInconsistencia,
                    tipoSaldo, 
                    tipoUtilizacaoSaldo, 
                    utilizado        
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idSaldoOrigem)s,
                    %(idSaldo)s,
                    %(idPessoa)s,
                    %(idPagamentos)s,
                    %(comentario)s,
                    %(nroProcesso)s,
                    %(observacoes)s,
                    %(idManutencaoPagamento)s,
                    %(dtSaldo)s,                    
                    %(dtValidade)s,
                    %(vlSaldoTotal)s,
                    %(vlSaldoUtilizado)s,
                    %(situacao)s,
                    %(tipoInconsistencia)s,
                    %(tipoSaldo)s, 
                    %(tipoUtilizacaoSaldo)s, 
                    %(utilizado)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idSaldoOrigem = idSaldoOrigem,
                idSaldo = idSaldo,
                idPessoa = idPessoa,                               
                idPagamentos = idPagamentos,
                comentario = comentario,
                nroProcesso = nroProcesso,                               
                observacoes = observacoes,
                idManutencaoPagamento = idManutencaoPagamento,
                dtSaldo = dtSaldo,                                               
                dtValidade = dtValidade,
                vlSaldoTotal = vlSaldoTotal,                               
                vlSaldoUtilizado = vlSaldoUtilizado,
                situacao = situacao,
                tipoInconsistencia = tipoInconsistencia,
                tipoSaldo = tipoSaldo, 
                tipoUtilizacaoSaldo = tipoUtilizacaoSaldo, 
                utilizado = utilizado
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {saldos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {saldos}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM saldos"
            if not self.query(sql_s):
                send_log_warning(f"saldos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM saldos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM saldos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    saldos 
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
            sql = f"SELECT * FROM saldos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM saldos WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM saldos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idSaldoOrigem, idSaldo, idPessoa, idPagamentos, comentario, idManutencaoPagamento, nroProcesso, observacoes, 
                dtSaldo, dtValidade, vlSaldoTotal, vlSaldoUtilizado, situacao, tipoInconsistencia, 
                tipoSaldo, tipoUtilizacaoSaldo, utilizado):
        objeto = {
            "idIntegracao": f"saldos{id}",
            "content": {}                                 
        }

        if idSaldoOrigem:
            objeto["content"]["idSaldoOrigem"] = { "id": int(idSaldoOrigem)}

        if tipoSaldo:
            objeto["content"]["tipoSaldo"] = f"{tipoSaldo}"   

        if tipoUtilizacaoSaldo:
            objeto["content"]["tipoUtilizacaoSaldo"] = f"{tipoUtilizacaoSaldo}"
        
        if utilizado:
            objeto["content"]["utilizado"] = f"{utilizado}"
                   
        if observacoes:
            objeto["content"]["observacoes"] = f"{observacoes}"

        if idSaldo:
            objeto["content"]["idSaldo"] = { "id": int(idSaldo)}           
        
        if idPagamentos:
            objeto["content"]["idPagamentos"] = { "id": int(idPagamentos)} 

        if vlSaldoTotal:
            objeto["content"]["vlSaldoTotal"] = f"{vlSaldoTotal}"  

        if comentario:
            objeto["content"]["comentario"] = f"{comentario}"

        if nroProcesso:
            objeto["content"]["nroProcesso"] = { "id": int(nroProcesso)}   

        if dtValidade:
            objeto["content"]["dtValidade"] = f"{dtValidade}"
        
        if dtSaldo:
            objeto["content"]["dtSaldo"] = f"{dtSaldo}"
           
        if vlSaldoUtilizado:
            objeto["content"]["vlSaldoUtilizado"] = f"{vlSaldoUtilizado}"
        
        if tipoInconsistencia:
            objeto["content"]["tipoInconsistencia"] = f"{tipoInconsistencia}"
        
        if idManutencaoPagamento:
            objeto["content"]["idManutencaoPagamento"] = { "id": int(idManutencaoPagamento)}

        if idPessoa != None:
            objeto[0]["content"]["idPessoa"] = { "id": int(idPessoa)}               

        if situacao != None:
            objeto[0]["content"]["situacao"] = f"{situacao}"        
            
        envio = api_post("saldos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

saldos = saldos()