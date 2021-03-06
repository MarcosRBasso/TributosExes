from samples import *
import json

class configTaxaExpedCredts(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idConfigTaxaExpediente, idCreditosTributarios, idCreditosTributariosRec, vlTaxa):
        try:
            sql = """
                INSERT INTO configTaxaExpedCredts (                    
                    idIntegracao,                   
                    id_cloud,                                                           
                    idConfigTaxaExpediente, 
                    idCreditosTributarios,
                    idCreditosTributariosRec,
                    vlTaxa                                             
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,                                                            
                    %(idConfigTaxaExpediente)s,
                    %(idCreditosTributarios)s,
                    %(idCreditosTributariosRec)s,
                    %(vlTaxa)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                                                               
                idConfigTaxaExpediente = idConfigTaxaExpediente,                               
                idCreditosTributarios = idCreditosTributarios,
                idCreditosTributariosRec = idCreditosTributariosRec,
                vlTaxa = vlTaxa     
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {configTaxaExpedCredts} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {configTaxaExpedCredts}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM configTaxaExpedCredts"
            if not self.query(sql_s):
                send_log_warning(f"configTaxaExpedCredts n??o encontrado para excluir.")
                return
            sql_d = f"DELETE FROM configTaxaExpedCredts WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias exclu??dos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de exclus??o do atividades econ??micas. {error}")

    def db_update(self, id, id_cloud, json, descricao):
        try:
            sql_s = f"SELECT * FROM configTaxaExpedCredts WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} n??o encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    configTaxaExpedCredts 
                SET 
                    id_cloud = %(id_cloud)s,
                    json_post = %(json)s,
                    resposta_post = %(descricao)s
                WHERE
                    id = %(id)s
                """
            data = dict (
                id = id,
                id_cloud = id_cloud,
                json = json,
                descricao = descricao
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"atividades Economicas {id} atualizado com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de atualiza????o da atividades Economicas. {error}")

    def db_search(self, id):
        try:
            sql = f"SELECT * FROM configTaxaExpedCredts WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} n??o encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM configTaxaExpedCredts WHERE id_cloud is null"
            data = self.query(sql)
            if data:
                send_log_info("Consulta de todos os atividades Economicas realizada com sucesso.")
                return data
            return None
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de busca. {error}")

    def get_id_cloud(self, id):
        if (id == None):
            return None
        try:
            sql = f"SELECT id_cloud FROM configTaxaExpedCredts WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} n??o encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de busca. {error}")

    def send_post(self, id, idConfigTaxaExpediente, idCreditosTributarios, idCreditosTributariosRec, vlTaxa):
        objeto = {
            "idIntegracao": f"configTaxaExpedCredts{id}",
            "content": {}                                 
        }

        if idCreditosTributarios != None:
            objeto[0]["content"]["CalculosTributariosAvancado"] = { "id": int(idCreditosTributarios) }    
               
        if idConfigTaxaExpediente != None:
            objeto[0]["camposadicionais"]["idConfigTaxaExpediente"] = { "id": int(idConfigTaxaExpediente) }

        if idCreditosTributariosRec != None:
            objeto[0]["camposadicionais"]["idCreditosTributariosRec"] = { "id": int(idCreditosTributariosRec)}   

        if vlTaxa != None:
            objeto[0]["camposadicionais"]["vlTaxa"] = f"{vlTaxa}"           

        envio = api_post("configTaxaExpedCredts", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["descricao"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["descricao"], ensure_ascii=False))

configTaxaExpedCredts = configTaxaExpedCredts()