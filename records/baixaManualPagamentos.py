from samples import *
import json

class baixaManualPagamentos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idConvenio, idMotivo, idContribuinte, idBaixaManual, dhTerminoHomologacao, formaPagamento, dtCredito, 
                dtPagamento, situacao, idMotivoEstorno, usuarioEstorno, dhEstorno, dhInicioEstorno, dhFimEstorno, erro, lancamentos ):
        try:
            sql = """
                INSERT INTO baixaManualPagamentos (                    
                    idIntegracao,                   
                    id_cloud, 
                    idConvenio,
                    idMotivo,                                                                    
                    idContribuinte,
                    idBaixaManual,
                    formaPagamento,
                    dtCredito,
                    dhTerminoHomologacao,
                    dtPagamento,                    
                    situacao,
                    idMotivoEstorno,
                    usuarioEstorno,
                    dhEstorno,
                    dhInicioEstorno,                    
                    dhFimEstorno,
                    erro,
                    lancamentos                   
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idConvenio)s,
                    %(idMotivo)s,
                    %(idContribuinte)s,
                    %(idBaixaManual)s,
                    %(formaPagamento)s,
                    %(dtCredito)s,
                    %(dhTerminoHomologacao)s,
                    %(dtPagamento)s,                    
                    %(situacao)s,
                    %(idMotivoEstorno)s,
                    %(usuarioEstorno)s,
                    %(dhEstorno)s,
                    %(dhInicioEstorno)s,
                    %(dhFimEstorno)s,
                    %(erro)s,                      
                    %(lancamentos)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idConvenio = idConvenio,
                idMotivo = idMotivo,                
                idContribuinte = idContribuinte,
                idBaixaManual = idBaixaManual,
                formaPagamento = formaPagamento,                               
                dtCredito = dtCredito,
                dhTerminoHomologacao = dhTerminoHomologacao,
                dtPagamento = dtPagamento,                                               
                situacao = situacao,                              
                idMotivoEstorno = idMotivoEstorno,
                usuarioEstorno = usuarioEstorno,                               
                dhEstorno = dhEstorno,
                dhInicioEstorno = dhInicioEstorno,                
                dhFimEstorno = dhFimEstorno,
                lancamentos = lancamentos,
                erro = erro                
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {baixaManualPagamentos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as idBaixaManual:
            send_log_error(f"idMotivoEstorno ao inserir o anistias {baixaManualPagamentos}. {idConvenio}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM baixaManualPagamentos"
            if not self.query(sql_s):
                send_log_warning(f"baixaManualPagamentos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM baixaManualPagamentos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as idBaixaManual:
            send_log_error(f"idMotivoEstorno ao executar a operação de exclusão do atividades econômicas. {idBaixaManual}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM baixaManualPagamentos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    baixaManualPagamentos 
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
        except Exception as idBaixaManual:
            send_log_error(f"idMotivoEstorno ao executar a operação de atualização da atividades Economicas. {idBaixaManual}")

    def db_search(self, id):
        try:
            sql = f"SELECT * FROM baixasAutomaticas WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as idBaixaManual:
            send_log_error(f"idMotivoEstorno ao executar a operação de busca. {idBaixaManual}")

    def db_list(self):
        try:
            sql = "SELECT * FROM baixaManualPagamentos WHERE id_cloud is null"
            data = self.query(sql)
            if data:
                send_log_info("Consulta de todos os atividades Economicas realizada com sucesso.")
                return data
            return None
        except Exception as idBaixaManual:
            send_log_error(f"idMotivoEstorno ao executar a operação de busca. {idBaixaManual}")

    def get_id_cloud(self, id):
        if (id == None):
            return None
        try:
            sql = f"SELECT id_cloud FROM baixaManualPagamentos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as idBaixaManual:
            send_log_error(f"idMotivoEstorno ao executar a operação de busca. {idBaixaManual}")

    def send_post(self, id, idConvenio, idMotivo, idContribuinte, idBaixaManual, dhTerminoHomologacao, formaPagamento, dtCredito, 
                 dtPagamento, situacao, idMotivoEstorno, usuarioEstorno, dhEstorno, dhInicioEstorno, dhFimEstorno, erro, lancamentos):
        objeto = {
            "idIntegracao": f"baixaManualPagamentos{id}",
            "content": {}                                 
        }
        if dhEstorno:
            objeto["content"]["dhEstorno"] = f"{dhEstorno}"
        
        if dhInicioEstorno:
            objeto["content"]["dhInicioEstorno"] = f"{dhInicioEstorno}"

        if formaPagamento:
            objeto["content"]["formaPagamento"] = f"{formaPagamento}"
           
        if situacao:
            objeto["content"]["situacao"] = f"{situacao}"
        
        if usuarioEstorno:
            objeto["content"]["usuarioEstorno"] = f"{usuarioEstorno}"
        
        if dhFimEstorno:
            objeto["content"]["dhFimEstorno"] = f"{dhFimEstorno}" 

        if dhTerminoHomologacao:
            objeto["content"]["dhTerminoHomologacao"] = f"{dhTerminoHomologacao}"  

        if dtCredito:
            objeto["content"]["tipo"] = f"{dtCredito}"       
       
        if dtPagamento:
            objeto["content"]["dtPagamento"] = f"{dtPagamento}"

        if lancamentos:
            objeto["content"]["lancamentos"] = f"{lancamentos}"   

        if erro:
            objeto["content"]["erro"] = f"{erro}"      

        if idConvenio != None:
            objeto[0]["content"]["idConvenio"] = { "id": int(idConvenio) }               

        if idMotivoEstorno != None:
            objeto[0]["content"]["idMotivoEstorno"] = { "id": int(idMotivoEstorno) }

        if idMotivo != None:
            objeto[0]["content"]["idMotivo"] = { "id": int(idMotivo) }

        if idContribuinte != None:
            objeto[0]["content"]["idContribuinte"] = { "id": int(idContribuinte) }               

        if idBaixaManual != None:
            objeto[0]["content"]["idBaixaManual"] = { "id": int(idBaixaManual) }

        if idMotivo != None:
            objeto[0]["content"]["idMotivo"] = { "id": int(idMotivo) }    

        envio = api_post("baixaManualPagamentos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

baixaManualPagamentos = baixaManualPagamentos()