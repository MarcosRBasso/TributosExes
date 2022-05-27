from samples import *
import json

class economicosCnaesMovtos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idEconomicosCnae, dtInicio, dtFinal, observacao):
        try:
            sql = """
                INSERT INTO economicosCnaesMovtos (                    
                    idIntegracao,                   
                    id_cloud, 
                    idEconomicosCnae,                                              
                    dtInicio, 
                    dtFinal,
                    observacao                
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idEconomicosCnae)s,
                    %(dtInicio)s,
                    %(dtFinal)s,
                    %(observacao)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idEconomicosCnae = idEconomicosCnae,
                dtInicio = dtInicio,                               
                dtFinal = dtFinal,
                observacao = observacao
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {economicosCnaesMovtos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {economicosCnaesMovtos}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM economicosCnaesMovtos"
            if not self.query(sql_s):
                send_log_warning(f"economicosCnaesMovtos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM economicosCnaesMovtos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM economicosCnaesMovtos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    economicosCnaesMovtos 
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
            sql = f"SELECT * FROM economicosCnaesMovtos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM economicosCnaesMovtos WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM economicosCnaesMovtos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idEconomicosCnae, dtInicio, dtFinal, observacao):
        objeto = {
            "idIntegracao": f"economicosCnaesMovtos{id}",
            "content": {}                                 
        }
        if idEconomicosCnae:
            objeto["content"]["idEconomicosCnae"] = { "id": int(idEconomicosCnae)}
           
        if dtFinal:
            objeto["content"]["dtFinal"] = f"{dtFinal}"       
       
        if observacao:
            objeto["content"]["observacao"] = f"{observacao}"            

        if dtInicio != None:
            objeto[0]["content"]["dtInicio"] = f"{dtInicio}"    
            
        envio = api_post("economicosCnaesMovtos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

economicosCnaesMovtos = economicosCnaesMovtos()