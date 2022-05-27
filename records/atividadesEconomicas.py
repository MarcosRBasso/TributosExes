from samples import *
import json

class atividadesEconomicas(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao,  idCnaes, idListaServicos, id_cloud, risco, riscoMei, classificacao):
        try:
            sql = """
                INSERT INTO atividadesEconomicas (                    
                    idIntegracao,
                    idCnaes,
                    idListaServicos,
                    id_cloud,
                    riscoMei,
                    classificacao,
                    risco
                ) VALUES (                  
                    %(idIntegracao)s,
                    %(idCnaes)s,
                    %(id_cloud)s,
                    %(risco)s,
                    %(idListaServicos)s,
                    %(riscoMei)s,
                    %(classificacao)s                    
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                idCnaes = idCnaes,
                id_cloud = id_cloud,
                idListaServicos = idListaServicos,
                riscoMei = riscoMei,
                classificacao = classificacao,
                risco = risco            
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {atividadesEconomicas} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {atividadesEconomicas}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM atividadesEconomicas"
            if not self.query(sql_s):
                send_log_warning(f"anistias não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM atividadesEconomicas WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do agrupamentos. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM atividadesEconomicas WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividadesEconomicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    atividadesEconomicas 
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
            sql = f"SELECT * FROM atividadesEconomicas WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM atividadesEconomicas WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM atividadesEconomicas WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idCnaes, idListaServicos, risco, riscoMei, classificacao):
        objeto = {
            "idIntegracao": f"atividadesEconomicas{id}",
            "content": {}                                 
        }

        if risco:
            objeto["content"]["risco"] = f"{risco}"
        
        if riscoMei:
            objeto["content"]["riscoMei"] = f"{riscoMei}"
        
        if classificacao:
            objeto["content"]["classificacao"] = f"{classificacao}"
      
      
        if idCnaes != None:
            objeto[0]["content"]["Cnaes"] = { "id": int(idCnaes) }               

        if idListaServicos != None:
            objeto[0]["content"]["ListaServicos"] = { "id": int(idListaServicos) }        

        envio = api_post("atividadesEconomicas", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

atividadesEconomicas = atividadesEconomicas()