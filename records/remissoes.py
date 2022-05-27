from samples import *
import json

class remissoes(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idDividas, idDividasMovtos, idDividasReceitas, idHomologManutencao, percRemissao):
        try:
            sql = """
                INSERT INTO remissoes (                    
                    idIntegracao,                   
                    id_cloud, 
                    idDividas,
                    idDividasMovtos,                                               
                    idDividasReceitas, 
                    idHomologManutencao,
                    percRemissao                
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idDividas)s,
                    %(idDividasMovtos)s,
                    %(idDividasReceitas)s,
                    %(idHomologManutencao)s,
                    %(percRemissao)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idDividas = idDividas,
                idDividasMovtos = idDividasMovtos,
                idDividasReceitas = idDividasReceitas,                               
                idHomologManutencao = idHomologManutencao,
                percRemissao = percRemissao
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {remissoes} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {remissoes}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM remissoes"
            if not self.query(sql_s):
                send_log_warning(f"remissoes não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM remissoes WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM remissoes WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    remissoes 
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
            sql = f"SELECT * FROM remissoes WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM remissoes WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM remissoes WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idDividas, idDividasMovtos, idDividasReceitas, idHomologManutencao, percRemissao):
        objeto = {
            "idIntegracao": f"remissoes{id}",
            "content": {}                                 
        }
        if idDividas:
            objeto["content"]["idDividas"] = { "id": int(idDividas)}

        if idDividasMovtos:
            objeto["content"]["idDividasMovtos"] = { "id": int(idDividasMovtos)}        
       
        if idHomologManutencao:
            objeto["content"]["idHomologManutencao"] = { "id": int(idHomologManutencao)}       
       
        if percRemissao:
            objeto["content"]["percRemissao"] = f"{percRemissao}"         

        if idDividasReceitas != None:
            objeto[0]["content"]["idDividasReceitas"] = { "id": int(idDividasReceitas)}    
            
        envio = api_post("remissoes", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

remissoes = remissoes()