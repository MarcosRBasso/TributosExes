from samples import *
import json

class atividadesEconomicasRelacionadas(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, idAtividadesEconomicasCnae, idAtividadesEconomicasServico, id_cloud ):
        try:
            sql = """
                INSERT INTO atividadesEconomicasRelacionadas (
                    idIntegracao,
                    idAtividadesEconomicasCnae,
                    idAtividadesEconomicasServico,
                    id_cloud
                ) VALUES (
                    %(idIntegracao)s,
                    %(idAtividadesEconomicasCnae)s,
                    %(id_cloud)s,
                    %(idCamposAdicionais)s,
                    %(idAtividadesEconomicasServico)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                idAtividadesEconomicasCnae = idAtividadesEconomicasCnae,
                id_cloud = id_cloud,
                idAtividadesEconomicasServico = idAtividadesEconomicasServico
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {atividadesEconomicasRelacionadas} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {atividadesEconomicasRelacionadas}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM atividadesEconomicasInfCompOp"
            if not self.query(sql_s):
                send_log_warning(f"anistias não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM atividadesEconomicasInfCompOp WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM atividadesEconomicasInfCompOp WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    atividadesEconomicasInfCompOp 
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
            sql = f"SELECT * FROM atividadesEconomicasInfCompOp WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM atividadesEconomicasInfCompOp WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM atividadesEconomicasInfCompOp WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idAtividadesEconomicasCnae, idAtividadesEconomicasServico):
        objeto = {
            "idIntegracao": f"atividadesEconomicasRelacionadas{id}",
            "content": {}                                 
        }         

        if idAtividadesEconomicasCnae != None:
            objeto[0]["content"]["AtividadesEconomicasCnae"] = { "id": int(idAtividadesEconomicasCnae) }               

        if idAtividadesEconomicasServico != None:
            objeto[0]["content"]["AtividadesEconomicasServico"] = { "id": int(idAtividadesEconomicasServico) }        

        envio = api_post("atividadesEconomicasRelacionadas", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

atividadesEconomicasRelacionadas = atividadesEconomicasRelacionadas()