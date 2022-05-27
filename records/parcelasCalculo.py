from samples import *
import json

class parcelasCalculo(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idCalculosTributarios, dataVcto, parcela, percDesconto, unica):
        try:
            sql = """
                INSERT INTO parcelasCalculo (                    
                    idIntegracao,                   
                    id_cloud,                                                           
                    idCalculosTributarios, 
                    dataVcto,
                    parcela,
                    percDesconto,
                    unica,
                    operadorComparacao,
                    operadorAcao                          
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,                                                            
                    %(idCalculosTributarios)s,
                    %(dataVcto)s,
                    %(parcela)s,
                    %(percDesconto)s,
                    %(operadorComparacao)s,
                    %(unica)s,
                    %(operadorAcao)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                                                               
                idCalculosTributarios = idCalculosTributarios,                               
                dataVcto = dataVcto,
                parcela = parcela,
                percDesconto = percDesconto,                
                unica = unica                           
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {parcelasCalculo} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {parcelasCalculo}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM parcelasCalculo"
            if not self.query(sql_s):
                send_log_warning(f"parcelasCalculo não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM parcelasCalculo WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, unica):
        try:
            sql_s = f"SELECT * FROM parcelasCalculo WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    parcelasCalculo 
                SET 
                    id_cloud = %(id_cloud)s,
                    json_post = %(json)s,
                    resposta_post = %(unica)s
                WHERE
                    id = %(id)s
                """
            data = dict (
                id = id,
                id_cloud = id_cloud,
                json = json,
                unica = unica
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"atividades Economicas {id} atualizado com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de atualização da atividades Economicas. {error}")

    def db_search(self, id):
        try:
            sql = f"SELECT * FROM parcelasCalculo WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM parcelasCalculo WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM parcelasCalculo WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idCalculosTributarios, dataVcto, parcela, percDesconto, unica):
        objeto = {
            "idIntegracao": f"parcelasCalculo{id}",
            "content": {}                                 
        }
        if dataVcto:
            objeto["content"]["dataVcto"] = f"{dataVcto}"
        
        if parcela:
            objeto["content"]["parcela"] = f"{parcela}"

        if percDesconto:
            objeto["content"]["percDesconto"] = f"{percDesconto}"    

        if idCalculosTributarios != None:
            objeto[0]["content"]["idCalculosTributarios"] = { "id": int(idCalculosTributarios) }
        
        if unica != None:
            objeto[0]["content"]["unica"] = f"{unica}"

        envio = api_post("parcelasCalculo", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["unica"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["unica"], ensure_ascii=False))

parcelasCalculo = parcelasCalculo()