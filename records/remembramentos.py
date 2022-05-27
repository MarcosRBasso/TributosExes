from samples import *
import json

class remembramentos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idPessoas, idAgrupamentos, idEngenheirosArquitetos, situacao, codArtRrt, nroProcesso, nroProcessoCancelamento, observacao, 
                dhAprovacao, dhCancelamento):
        try:
            sql = """
                INSERT INTO remembramentos (                    
                    idIntegracao,                   
                    id_cloud, 
                    idPessoas,
                    idAgrupamentos,                                               
                    idEngenheirosArquitetos, 
                    situacao,
                    codArtRrt,
                    nroProcessoCancelamento,
                    observacao,
                    nroProcesso,
                    dhAprovacao,                    
                    dhCancelamento       
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idPessoas)s,
                    %(idAgrupamentos)s,
                    %(idEngenheirosArquitetos)s,
                    %(situacao)s,
                    %(codArtRrt)s,
                    %(nroProcessoCancelamento)s,
                    %(observacao)s,
                    %(nroProcesso)s,
                    %(dhAprovacao)s,                    
                    %(dhCancelamento)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idPessoas = idPessoas,
                idAgrupamentos = idAgrupamentos,
                idEngenheirosArquitetos = idEngenheirosArquitetos,                               
                situacao = situacao,
                codArtRrt = codArtRrt,
                nroProcessoCancelamento = nroProcessoCancelamento,                               
                observacao = observacao,
                nroProcesso = nroProcesso,
                dhAprovacao = dhAprovacao,                                               
                dhCancelamento = dhCancelamento
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {remembramentos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {remembramentos}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM remembramentos"
            if not self.query(sql_s):
                send_log_warning(f"remembramentos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM remembramentos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM remembramentos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    remembramentos 
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
            sql = f"SELECT * FROM remembramentos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM remembramentos WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM remembramentos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idPessoas, idAgrupamentos, idEngenheirosArquitetos, situacao, codArtRrt, nroProcesso, nroProcessoCancelamento, observacao, 
                dhAprovacao, dhCancelamento):
        objeto = {
            "idIntegracao": f"remembramentos{id}",
            "content": {}                                 
        }
        if idPessoas:
            objeto["content"]["idPessoas"] = { "id": int(idPessoas)}          
        
        if observacao:
            objeto["content"]["observacao"] = f"{observacao}"

        if idAgrupamentos:
            objeto["content"]["idAgrupamentos"] = { "id": int(idAgrupamentos)}           
        
        if situacao:
            objeto["content"]["situacao"] = f"{situacao}"  

        if codArtRrt:
            objeto["content"]["codArtRrt"] = f"{codArtRrt}"

        if nroProcessoCancelamento:
            objeto["content"]["nroProcessoCancelamento"] = f"{nroProcessoCancelamento}"   

        if dhCancelamento:
            objeto["content"]["dhCancelamento"] = f"{dhCancelamento}"
        
        if dhAprovacao:
            objeto["content"]["dhAprovacao"] = f"{dhAprovacao}"
        
        if nroProcesso:
            objeto["content"]["nroProcesso"] = f"{nroProcesso}"

        if idEngenheirosArquitetos != None:
            objeto[0]["content"]["idEngenheirosArquitetos"] = { "id": int(idEngenheirosArquitetos) }  
            
        envio = api_post("remembramentos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

remembramentos = remembramentos()