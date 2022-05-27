from samples import *
import json

class economicosListaServicosValores(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idEconomicosListaServico, valorAlvara, percIssqn, dtAlvara, dtAliquotaIss, dtIssFixo, valorIssFixo):
        try:
            sql = """
                INSERT INTO economicosListaServicosValores (                    
                    idIntegracao,                   
                    id_cloud, 
                    idEconomicosListaServico,
                    valorAlvara,                                               
                    dtAlvara, 
                    dtAliquotaIss,
                    dtIssFixo,
                    percIssqn,
                    valorIssFixo                
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idEconomicosListaServico)s,
                    %(valorAlvara)s,
                    %(dtAlvara)s,
                    %(dtAliquotaIss)s,
                    %(dtIssFixo)s,
                    %(percIssqn)s,
                    %(valorIssFixo)s 
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idEconomicosListaServico = idEconomicosListaServico,
                valorAlvara = valorAlvara,
                dtAlvara = dtAlvara,                               
                dtAliquotaIss = dtAliquotaIss,
                dtIssFixo = dtIssFixo,
                percIssqn = percIssqn,
                valorIssFixo = valorIssFixo 
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {economicosListaServicosValores} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {economicosListaServicosValores}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM economicosListaServicosValores"
            if not self.query(sql_s):
                send_log_warning(f"economicosListaServicosValores não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM economicosListaServicosValores WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM economicosListaServicosValores WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    economicosListaServicosValores 
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
            sql = f"SELECT * FROM economicosListaServicosValores WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM economicosListaServicosValores WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM economicosListaServicosValores WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idEconomicosListaServico, valorAlvara, dtAlvara, dtAliquotaIss, dtIssFixo, percIssqn, valorIssFixo):
        objeto = {
            "idIntegracao": f"economicosListaServicosValores{id}",
            "content": {}                                 
        }
        if percIssqn:
            objeto["content"]["percIssqn"] = { "id": int(percIssqn)}

        if valorIssFixo:
            objeto["content"]["valorIssFixo"] = f"{valorIssFixo}"     

        if idEconomicosListaServico:
            objeto["content"]["idEconomicosListaServico"] = { "id": int(idEconomicosListaServico)}

        if valorAlvara:
            objeto["content"]["valorAlvara"] = f"{valorAlvara}"        
       
        if dtAliquotaIss:
            objeto["content"]["dtAliquotaIss"] = f"{dtAliquotaIss}"       
       
        if dtIssFixo:
            objeto["content"]["dtIssFixo"] = f"{dtIssFixo}"

        if dtAlvara != None:
            objeto[0]["content"]["dtAlvara"] = f"{dtAlvara}"    
            
        envio = api_post("economicosListaServicosValores", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

economicosListaServicosValores = economicosListaServicosValores()