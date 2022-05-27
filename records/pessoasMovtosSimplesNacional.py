from samples import *
import json

class pessoasMovtosSimplesNacional(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idPessoaJuridica, idMotivos, optante, dtInicio, dtEfeito, comentario, orgao):
        try:
            sql = """
                INSERT INTO pessoasMovtosSimplesNacional (                    
                    idIntegracao,                   
                    id_cloud, 
                    idPessoaJuridica,
                    idMotivos,                                               
                    optante, 
                    dtInicio,
                    dtEfeito,
                    orgao,
                    comentario                
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idPessoaJuridica)s,
                    %(idMotivos)s,
                    %(optante)s,
                    %(dtInicio)s,
                    %(dtEfeito)s,
                    %(orgao)s,
                    %(comentario)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idPessoaJuridica = idPessoaJuridica,
                idMotivos = idMotivos,
                optante = optante,                               
                dtInicio = dtInicio,
                dtEfeito = dtEfeito,
                orgao = orgao,
                comentario = comentario
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {pessoasMovtosSimplesNacional} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {pessoasMovtosSimplesNacional}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM pessoasMovtosSimplesNacional"
            if not self.query(sql_s):
                send_log_warning(f"pessoasMovtosSimplesNacional não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM pessoasMovtosSimplesNacional WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM pessoasMovtosSimplesNacional WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    pessoasMovtosSimplesNacional 
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
            sql = f"SELECT * FROM pessoasMovtosSimplesNacional WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM pessoasMovtosSimplesNacional WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM pessoasMovtosSimplesNacional WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idPessoaJuridica, idMotivos, optante, dtInicio, dtEfeito, comentario, orgao):
        objeto = {
            "idIntegracao": f"pessoasMovtosSimplesNacional{id}",
            "content": {}                                 
        }
        if idPessoaJuridica:
            objeto["content"]["idPessoaJuridica"] = { "id": int(idPessoaJuridica)}

        if idMotivos:
            objeto["content"]["idMotivos"] = { "id": int(idMotivos)}        
       
        if dtInicio:
            objeto["content"]["dtInicio"] = f"{dtInicio}"       
       
        if dtEfeito:
            objeto["content"]["dtEfeito"] = f"{dtEfeito}"

        if orgao:
            objeto["content"]["orgao"] = f"{orgao}"  
        
        if comentario:
            objeto["content"]["comentario"] = f"{comentario}"              

        if optante != None:
            objeto[0]["content"]["optante"] = f"{optante}"    
            
        envio = api_post("pessoasMovtosSimplesNacional", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

pessoasMovtosSimplesNacional = pessoasMovtosSimplesNacional()