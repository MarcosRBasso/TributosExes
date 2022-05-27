from samples import *
import json

class economicosTabaux(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idEconomicos, dtBase, iTabelaAuxiliar, campo1, campo2, campo3, campo4, campo5, 
                campo6, campo7, campo8, campo9, campo10, idTabelaAuxiliar):
        try:
            sql = """
                INSERT INTO economicosTabaux (                    
                    idIntegracao,                   
                    id_cloud, 
                    idEconomicos,
                    dtBase,                                               
                    iTabelaAuxiliar, 
                    campo1,
                    campo2,
                    campo4,
                    campo5,
                    campo3,
                    campo6,                    
                    campo7,
                    campo8,
                    campo9,
                    campo10,
                    idTabelaAuxiliar                  
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idEconomicos)s,
                    %(dtBase)s,
                    %(iTabelaAuxiliar)s,
                    %(campo1)s,
                    %(campo2)s,
                    %(campo4)s,
                    %(campo5)s,
                    %(campo3)s,
                    %(campo6)s,                    
                    %(campo7)s,
                    %(campo8)s,
                    %(campo9)s,
                    %(campo10)s,
                    %(idTabelaAuxiliar)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idEconomicos = idEconomicos,
                dtBase = dtBase,
                iTabelaAuxiliar = iTabelaAuxiliar,                               
                campo1 = campo1,
                campo2 = campo2,
                campo4 = campo4,                               
                campo5 = campo5,
                campo3 = campo3,
                campo6 = campo6,                                               
                campo7 = campo7,
                campo8 = campo8,                               
                campo9 = campo9,
                campo10 = campo10,
                idTabelaAuxiliar = idTabelaAuxiliar
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {economicosTabaux} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {economicosTabaux}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM economicosTabaux"
            if not self.query(sql_s):
                send_log_warning(f"economicosTabaux não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM economicosTabaux WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM economicosTabaux WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    economicosTabaux 
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
            sql = f"SELECT * FROM economicosTabaux WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM economicosTabaux WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM economicosTabaux WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idEconomicos, dtBase, iTabelaAuxiliar, campo1, campo2, campo3, campo4, campo5, 
                campo6, campo7, campo8, campo9, campo10, idTabelaAuxiliar):
        objeto = {
            "idIntegracao": f"economicosTabaux{id}",
            "content": {}                                 
        }
        if idEconomicos:
            objeto["content"]["idEconomicos"] = { "id": int(idEconomicos)}

        if idTabelaAuxiliar:
            objeto["content"]["idTabelaAuxiliar"] = f"{idTabelaAuxiliar}"
        
        if campo5:
            objeto["content"]["campo5"] = f"{campo5}"

        if dtBase:
            objeto["content"]["dtBase"] = f"{dtBase}"
        
        if campo1:
            objeto["content"]["campo1"] = f"{campo1}" 

        if campo8:
            objeto["content"]["campo8"] = f"{campo8}"       
       
        if campo2:
            objeto["content"]["campo2"] = f"{campo2}"

        if campo4:
            objeto["content"]["campo4"] = f"{campo4}"   

        if campo7:
            objeto["content"]["campo7"] = f"{campo7}"
        
        if campo6:
            objeto["content"]["campo6"] = f"{campo6}"
           
        if campo9:
            objeto["content"]["campo9"] = f"{campo9}"
        
        if campo3:
            objeto["content"]["campo3"] = { "id": int(campo3)}

        if iTabelaAuxiliar != None:
            objeto[0]["content"]["iTabelaAuxiliar"] = { "id": int(iTabelaAuxiliar) }               

        if campo10 != None:
            objeto[0]["content"]["campo10"] = f"{campo10}"    
            
        envio = api_post("economicosTabaux", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

economicosTabaux = economicosTabaux()