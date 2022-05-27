from samples import *
import json

class parcelamentosParcTaxas(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idParcelas, idCreditosTributarios, vlTaxa, taxaAutomatica):
        try:
            sql = """
                INSERT INTO parcelamentosParcTaxas (                    
                    idIntegracao,                   
                    id_cloud, 
                    idParcelas,
                    idCreditosTributarios,                                               
                    vlTaxa, 
                    taxaAutomatica               
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idParcelas)s,
                    %(idCreditosTributarios)s,
                    %(vlTaxa)s,
                    %(taxaAutomatica)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idParcelas = idParcelas,
                idCreditosTributarios = idCreditosTributarios,
                vlTaxa = vlTaxa,                               
                taxaAutomatica = taxaAutomatica
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {parcelamentosParcTaxas} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {parcelamentosParcTaxas}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM parcelamentosParcTaxas"
            if not self.query(sql_s):
                send_log_warning(f"parcelamentosParcTaxas não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM parcelamentosParcTaxas WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM parcelamentosParcTaxas WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    parcelamentosParcTaxas 
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
            sql = f"SELECT * FROM parcelamentosParcTaxas WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM parcelamentosParcTaxas WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM parcelamentosParcTaxas WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idParcelas, idCreditosTributarios, vlTaxa, taxaAutomatica):
        objeto = {
            "idIntegracao": f"parcelamentosParcTaxas{id}",
            "content": {}                                 
        }
        if idParcelas:
            objeto["content"]["idParcelas"] = { "id": int(idParcelas)}

        if idCreditosTributarios:
            objeto["content"]["idCreditosTributarios"] = { "id": int(idCreditosTributarios)}        
       
        if taxaAutomatica:
            objeto["content"]["taxaAutomatica"] = f"{taxaAutomatica}"                

        if vlTaxa != None:
            objeto[0]["content"]["vlTaxa"] = f"{vlTaxa}"    
            
        envio = api_post("parcelamentosParcTaxas", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

parcelamentosParcTaxas = parcelamentosParcTaxas()