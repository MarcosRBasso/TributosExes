from samples import *
import json

class anistias(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, idDividas, idDividasMovtos, id_cloud, idDividasReceitas, dtValidade, idHomologManutencao, idScriptManutencao):
        try:
            sql = """
                INSERT INTO anistias (                    
                    idIntegracao,
                    idDividas,
                    idDividasMovtos,
                    id_cloud,
                    idDividasReceitas,
                    idHomologManutencao,
                    idScriptManutencao,
                    dtValidade
                ) VALUES (
                    %(idIntegracao)s,
                    %(idDividas)s,
                    %(id_cloud)s,
                    %(dtValidade)s,
                    %(idDividasMovtos)s,
                    %(idDividasReceitas)s,
                    %(idHomologManutencao)s,
                    %(idScriptManutencao)s    
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                idDividas = idDividas,
                dtValidade = dtValidade,
                id_cloud = id_cloud,
                idDividasMovtos = idDividasMovtos,
                idDividasReceitas = idDividasReceitas,
                idHomologManutencao = idHomologManutencao,
                idScriptManutencao = idScriptManutencao            
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {anistias} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {anistias}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM anistias"
            if not self.query(sql_s):
                send_log_warning(f"anistias não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM anistias WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do agrupamentos. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM anistias WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"anistias {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    anistias 
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
            send_log_info(f"anistias {id} atualizado com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de atualização da anistias. {error}")

    def db_search(self, id):
        try:
            sql = f"SELECT * FROM anistias WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"anistias {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM anistias WHERE id_cloud is null"
            data = self.query(sql)
            if data:
                send_log_info("Consulta de todos os anistias realizada com sucesso.")
                return data
            return None
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def get_id_cloud(self, id):
        if (id == None):
            return None
        try:
            sql = f"SELECT id_cloud FROM anistias WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"alvaras {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, idIntegracao, id, idDividas, idDividasMovtos, id_cloud, idDividasReceitas, dtValidade, idHomologManutencao, idScriptManutencao):
        objeto = {
            "idIntegracao": f"anistias{id}",
            "content": {}                                 
        }
        
        if idDividas != None:
            objeto[0]["content"]["Dividas"] = { "id": int(idDividas) }               

        if idDividasMovtos != None:
            objeto[0]["content"]["DividasMovtos"] = { "id": int(idDividasMovtos) }

        if idDividasReceitas != None:
            objeto[0]["content"]["DividasReceitas"] = { "id": int(idDividasReceitas) }
                    
        if idHomologManutencao != None:
            objeto[0]["content"]["HomologManutencao"] = { "id": int(idHomologManutencao) }

        if idScriptManutencao != None:
            objeto[0]["content"]["ScriptManutencao"] = { "id": int(idScriptManutencao) } 

        envio = api_post("anistias", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

anistias = anistias()