from samples import *
import json

class configTaxaExpediente(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idReceitasDebito, idReceitasDivida, idReceitasParcelamento, idReceitasUnico, vlUnico, vlDebito, vlDivida, vlParcelamento, vlTaxa, 
                  definirTaxaPorCredito, acumularTaxas):
        try:
            sql = """
                INSERT INTO configTaxaExpediente (                    
                    idIntegracao,                   
                    id_cloud,                     
                    idReceitasDebito,                                               
                    idReceitasDivida, 
                    idReceitasParcelamento,
                    idReceitasUnico,
                    vlUnico,
                    vlDebito,
                    vlDivida, 
                    vlParcelamento, 
                    vlTaxa, 
                    definirTaxaPorCredito,
                    acumularTaxas                                 
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,                                        
                    %(idReceitasDebito)s,
                    %(idReceitasDivida)s,
                    %(idReceitasParcelamento)s,
                    %(idReceitasUnico)s,
                    %(vlUnico)s,
                    %(vlDebito)s,
                    %(vlDivida)s, 
                    %(vlParcelamento)s, 
                    %(vlTaxa)s, 
                    %(definirTaxaPorCredito)s,
                    %(acumularTaxas)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                                               
                idReceitasDebito = idReceitasDebito,
                idReceitasDivida = idReceitasDivida,                               
                idReceitasParcelamento = idReceitasParcelamento,
                idReceitasUnico = idReceitasUnico,
                vlUnico = vlUnico,                               
                vlDebito = vlDebito,
                vlDivida = vlDivida, 
                vlParcelamento = vlParcelamento, 
                vlTaxa = vlTaxa, 
                definirTaxaPorCredito = definirTaxaPorCredito,
                acumularTaxas = acumularTaxas               
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {configTaxaExpediente} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {configTaxaExpediente}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM configTaxaExpediente"
            if not self.query(sql_s):
                send_log_warning(f"configTaxaExpediente não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM configTaxaExpediente WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM configTaxaExpediente WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    configTaxaExpediente 
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
            sql = f"SELECT * FROM configTaxaExpediente WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM configTaxaExpediente WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM configTaxaExpediente WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idReceitasDebito, idReceitasDivida, idReceitasParcelamento, idReceitasUnico, vlUnico, vlDebito,vlDivida, vlParcelamento, vlTaxa, definirTaxaPorCredito, acumularTaxas):
        objeto = {
            "idIntegracao": f"configTaxaExpediente{id}",
            "content": {}                                 
        }
        if vlDivida:
            objeto["content"]["vlDivida"] = f"{vlDivida}"
           
        if vlParcelamento:
            objeto["content"]["vlParcelamento"] = f"{vlParcelamento}"
        
        if vlTaxa:
            objeto["content"]["vlTaxa"] = f"{vlTaxa}"
            
        if acumularTaxas:
            objeto["content"]["acumularTaxas"] = f"{acumularTaxas}"
        
        if definirTaxaPorCredito:
            objeto["content"]["definirTaxaPorCredito"] = f"{definirTaxaPorCredito}"

        if idReceitasParcelamento:
            objeto["content"]["idReceitasParcelamento"] =  { "id": int(idReceitasParcelamento)}
        
        if idReceitasUnico:
            objeto["content"]["idReceitasUnico"] =  { "id": int(idReceitasUnico)}

        if idReceitasDebito:
            objeto["content"]["idReceitasDebito"] =  { "id": int(idReceitasDebito)}
           
        if idReceitasDivida:
            objeto["content"]["idReceitasDivida"] =  { "id": int(idReceitasDivida)}
        
        if vlDebito:
            objeto["content"]["vlDebito"] =  { "id": int(vlDebito)}
        
        if vlUnico:
            objeto["content"]["vlUnico"] =  { "id": int(vlUnico)}
        envio = api_post("configTaxaExpediente", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

configTaxaExpediente = configTaxaExpediente()