from samples import *
import json

class baixasAutomaticas(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, baixaAutomatica, baixaRetroativa, idConvenio, dataArquivo, dataHoraEstorno, dataPagamento, dataPagamentoRetroativo, dhInicioEstorno, 
                dhInicioHomologacao, dhTerminoEstorno, dhTerminoHomologacao, erro, idMotivoEstorno, nomeArquivo, nroArquivo, scriptId, situacao, tempoExecucao, usuarioEstorno):
        try:
            sql = """
                INSERT INTO baixasAutomaticas (                    
                    idIntegracao,                   
                    id_cloud, 
                    baixaAutomatica,
                    baixaRetroativa,                                               
                    idConvenio, 
                    dataArquivo,
                    dataHoraEstorno,
                    dataPagamentoRetroativo,
                    dhInicioEstorno,
                    dataPagamento,
                    dhInicioHomologacao,                    
                    dhTerminoEstorno,
                    dhTerminoHomologacao,
                    erro,
                    idMotivoEstorno,
                    nomeArquivo,
                    nroArquivo,
                    scriptId,
                    situacao,
                    tempoExecucao,
                    usuarioEstorno                   
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(baixaAutomatica)s,
                    %(baixaRetroativa)s,
                    %(idConvenio)s,
                    %(dataArquivo)s,
                    %(dataHoraEstorno)s,
                    %(dataPagamentoRetroativo)s,
                    %(dhInicioEstorno)s,
                    %(dataPagamento)s,
                    %(dhInicioHomologacao)s,                    
                    %(dhTerminoEstorno)s,
                    %(dhTerminoHomologacao)s,
                    %(erro)s,
                    %(idMotivoEstorno)s,
                    %(nomeArquivo)s,
                    %(nroArquivo)s,
                    %(scriptId)s,
                    %(usuarioEstorno)s,
                    %(tempoExecucao)s,                    
                    %(situacao)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                baixaAutomatica = baixaAutomatica,
                baixaRetroativa = baixaRetroativa,
                idConvenio = idConvenio,                               
                dataArquivo = dataArquivo,
                dataHoraEstorno = dataHoraEstorno,
                dataPagamentoRetroativo = dataPagamentoRetroativo,                               
                dhInicioEstorno = dhInicioEstorno,
                dataPagamento = dataPagamento,
                dhInicioHomologacao = dhInicioHomologacao,                                               
                dhTerminoEstorno = dhTerminoEstorno,
                dhTerminoHomologacao = dhTerminoHomologacao,                               
                erro = erro,
                idMotivoEstorno = idMotivoEstorno,
                nomeArquivo = nomeArquivo,                               
                nroArquivo = nroArquivo,
                scriptId = scriptId,
                usuarioEstorno = usuarioEstorno,
                tempoExecucao = tempoExecucao,
                situacao = situacao
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {baixasAutomaticas} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {baixasAutomaticas}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM baixasAutomaticas"
            if not self.query(sql_s):
                send_log_warning(f"baixasAutomaticas não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM baixasAutomaticas WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM baixasAutomaticas WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    baixasAutomaticas 
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
            sql = f"SELECT * FROM baixasAutomaticas WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM baixasAutomaticas WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM baixasAutomaticas WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, baixaAutomatica, baixaRetroativa, idConvenio, dataArquivo, dataHoraEstorno, dataPagamento, dataPagamentoRetroativo, dhInicioEstorno, 
                dhInicioHomologacao, dhTerminoEstorno, dhTerminoHomologacao, erro, idMotivoEstorno, nomeArquivo, nroArquivo, scriptId, situacao, tempoExecucao, usuarioEstorno):
        objeto = {
            "idIntegracao": f"baixasAutomaticas{id}",
            "content": {}                                 
        }
        if baixaAutomatica:
            objeto["content"]["baixaAutomatica"] = f"{baixaAutomatica}"
        
        if dhInicioEstorno:
            objeto["content"]["dhInicioEstorno"] = f"{dhInicioEstorno}"

        if baixaRetroativa:
            objeto["content"]["baixaRetroativa"] = f"{baixaRetroativa}"
           
        if situacao:
            objeto["content"]["situacao"] = f"{situacao}"
        
        if usuarioEstorno:
            objeto["content"]["usuarioEstorno"] = f"{usuarioEstorno}"
        
        if dataArquivo:
            objeto["content"]["dataArquivo"] = f"{dataArquivo}" 

        if dhTerminoHomologacao:
            objeto["content"]["dhTerminoHomologacao"] = f"{dhTerminoHomologacao}"  

        if nroArquivo:
            objeto["content"]["nroArquivo"] = f"{nroArquivo}"       
       
        if dataHoraEstorno:
            objeto["content"]["dataHoraEstorno"] = f"{dataHoraEstorno}"

        if dataPagamentoRetroativo:
            objeto["content"]["dataPagamentoRetroativo"] = f"{dataPagamentoRetroativo}"   

        if dhTerminoEstorno:
            objeto["content"]["dhTerminoEstorno"] = f"{dhTerminoEstorno}"
        
        if dhInicioHomologacao:
            objeto["content"]["dhInicioHomologacao"] = f"{dhInicioHomologacao}"
           
        if erro:
            objeto["content"]["erro"] = f"{erro}"
        
        if nomeArquivo:
            objeto["content"]["nomeArquivo"] = f"{nomeArquivo}"
        
        if tempoExecucao:
            objeto["content"]["tempoExecucao"] = f"{tempoExecucao}"  

        if dataPagamento:
            objeto["content"]["dataPagamento"] = f"{dataPagamento}"

        if idConvenio != None:
            objeto[0]["content"]["idConvenio"] = { "id": int(idConvenio) }               

        if idMotivoEstorno != None:
            objeto[0]["content"]["idMotivoEstorno"] = { "id": int(idMotivoEstorno) }        

        if scriptId != None:
            objeto[0]["content"]["scriptId"] = { "id": int(scriptId) }
            
        envio = api_post("baixasAutomaticas", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

baixasAutomaticas = baixasAutomaticas()