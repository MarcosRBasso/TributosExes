from samples import *
import json

class baixaAutomatica(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idAgenciaBancaria, arquivo, baixaRetroativa, idBanco, idConvenio, dataArquivo, dataHoraEstorno, dataPagamento, dataRetroativa, 
                  dhInicio, dhTermino, erros, identificacaoSimples, inconsistencias, idMotivoEstorno, nomeArquivoReduzido, nroArquivo, scriptId, situacao, tempoExecucao, usuarioEstorno):
        try:
            sql = """
                INSERT INTO baixaAutomatica (                    
                    idIntegracao,                   
                    id_cloud, 
                    idAgenciaBancaria,
                    arquivo,                                               
                    baixaRetroativa, 
                    idBanco,
                    idConvenio,
                    dataArquivo,
                    dataHoraEstorno,
                    dataPagamento,
                    dataRetroativa,
                    dhInicio,
                    dhTermino,
                    erros,
                    identificacaoSimples,
                    inconsistencias,
                    idMotivoEstorno,
                    nomeArquivoReduzido,
                    nroArquivo,
                    scriptId,
                    situacao,
                    tempoExecucao,
                    usuarioEstorno                    
                ) VALUES (
                    %(idAgenciaBancaria)s,
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(arquivo)s,
                    %(baixaRetroativa)s,
                    %(idBanco)s,
                    %(idConvenio)s,
                    %(dataArquivo)s,
                    %(dataHoraEstorno)s,
                    %(dataPagamento)s,
                    %(dataRetroativa)s,
                    %(dhInicio)s,
                    %(dhTermino)s,
                    %(erros)s,
                    %(identificacaoSimples)s,
                    %(inconsistencias)s,
                    %(idMotivoEstorno)s,
                    %(nomeArquivoReduzido)s,
                    %(nroArquivo)s,
                    %(scriptId)s,
                    %(situacao)s,
                    %(tempoExecucao)s,
                    %(usuarioEstorno)s                                        
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idAgenciaBancaria = idAgenciaBancaria,
                arquivo = arquivo,
                baixaRetroativa = baixaRetroativa,                               
                idBanco = idBanco,
                idConvenio = idConvenio,
                dataArquivo = dataArquivo,                               
                dataHoraEstorno = dataHoraEstorno,
                dataPagamento = dataPagamento,
                dataRetroativa = dataRetroativa,                               
                dhInicio = dhInicio,
                dhTermino = dhTermino,
                erros = erros,                               
                identificacaoSimples = identificacaoSimples,
                inconsistencias = inconsistencias,
                idMotivoEstorno = idMotivoEstorno,                               
                nomeArquivoReduzido = nomeArquivoReduzido,
                nroArquivo = nroArquivo,
                scriptId = scriptId,                               
                situacao = situacao,
                tempoExecucao = tempoExecucao,                               
                usuarioEstorno = usuarioEstorno
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {baixaAutomatica} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {baixaAutomatica}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM baixaAutomatica"
            if not self.query(sql_s):
                send_log_warning(f"baixaAutomatica não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM baixaAutomatica WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM baixaAutomatica WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    baixaAutomatica 
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
            sql = f"SELECT * FROM baixaAutomatica WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM baixaAutomatica WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM baixaAutomatica WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idAgenciaBancaria, arquivo, baixaRetroativa, idBanco, idConvenio, dataArquivo, dataHoraEstorno, dataPagamento, dataRetroativa, 
                  dhInicio, dhTermino, erros, identificacaoSimples, inconsistencias, idMotivoEstorno, nomeArquivoReduzido, nroArquivo, scriptId, situacao, tempoExecucao, usuarioEstorno):
        objeto = {
            "idIntegracao": f"baixaAutomatica{id}",
            "content": {}                                 
        }
        if dataHoraEstorno:
            objeto["content"]["dataHoraEstorno"] = f"{dataHoraEstorno}"
        
        if identificacaoSimples:
            objeto["content"]["identificacaoSimples"] = f"{identificacaoSimples}"
        
        if inconsistencias:
            objeto["content"]["inconsistencias"] = f"{inconsistencias}"
        
        if dataArquivo:
            objeto["content"]["dataArquivo"] = f"{dataArquivo}"
        
        if nroArquivo:
            objeto["content"]["nroArquivo"] = f"{nroArquivo}" 

        if dataPagamento:
            objeto["content"]["dataPagamento"] = f"{dataPagamento}"  

        if dataRetroativa:
            objeto["content"]["dataRetroativa"] = f"{dataRetroativa}"
        
        if baixaRetroativa:
            objeto["content"]["baixaRetroativa"] = f"{baixaRetroativa}"
        
        if situacao:
            objeto["content"]["situacao"] = f"{situacao}"
        
        if tempoExecucao:
            objeto["content"]["tempoExecucao"] = f"{tempoExecucao}"
        
        if usuarioEstorno:
            objeto["content"]["usuarioEstorno"] = f"{usuarioEstorno}" 

        if arquivo:
            objeto["content"]["arquivo"] = f"{arquivo}"
        
        if baixaRetroativa:
            objeto["content"]["baixaRetroativa"] = f"{baixaRetroativa}"
        
        if nomeArquivoReduzido:
            objeto["content"]["nomeArquivoReduzido"] = f"{nomeArquivoReduzido}"
        
        if dhInicio:
            objeto["content"]["dhInicio"] = f"{dhInicio}"
        
        if dhTermino:
            objeto["content"]["dhTermino"] = f"{dhTermino}" 

        if erros:
            objeto["content"]["erros"] = f"{erros}"    

        if idAgenciaBancaria != None:
            objeto[0]["content"]["AgenciaBancaria"] = { "id": int(idAgenciaBancaria) }               

        if idBanco != None:
            objeto[0]["content"]["Banco"] = { "id": int(idBanco) }

        if idConvenio != None:
            objeto[0]["content"]["Convenio"] = { "id": int(idConvenio) }
                    
        if idMotivoEstorno != None:
            objeto[0]["content"]["MotivoEstorno"] = { "id": int(idMotivoEstorno) }

        if scriptId != None:
            objeto[0]["content"]["scriptId"] = { "id": int(scriptId) }  

        envio = api_post("baixaAutomatica", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

baixaAutomatica = baixaAutomatica()