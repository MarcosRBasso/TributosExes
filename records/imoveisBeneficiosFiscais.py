from samples import *
import json

class imoveisBeneficiosFiscais(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idCalculo, idImovel):
        try:
            sql = """
                INSERT INTO imoveisBeneficiosFiscais (                    
                    idIntegracao,                   
                    id_cloud,                                                           
                    idCalculo, 
                    idImovel                                 
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,                                                            
                    %(idCalculo)s,
                    %(idImovel)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                                                               
                idCalculo = idCalculo,                               
                idImovel = idImovel
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {imoveisBeneficiosFiscais} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {imoveisBeneficiosFiscais}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM imoveisBeneficiosFiscais"
            if not self.query(sql_s):
                send_log_warning(f"imoveisBeneficiosFiscais não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM imoveisBeneficiosFiscais WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, descricao):
        try:
            sql_s = f"SELECT * FROM imoveisBeneficiosFiscais WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    imoveisBeneficiosFiscais 
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
            send_log_error(f"Erro ao executar a operação de atualização da atividades Economicas. {error}")

    def db_search(self, id):
        try:
            sql = f"SELECT * FROM imoveisBeneficiosFiscais WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM imoveisBeneficiosFiscais WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM imoveisBeneficiosFiscais WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idCalculo, idImovel):
        objeto = {
            "idIntegracao": f"imoveisBeneficiosFiscais{id}",
            "content": {}                                 
        }
        if idImovel != None:
            objeto[0]["content"]["idImovel"] = { "id": int(idImovel)}    
               
        if idCalculo != None:
            objeto[0]["camposadicionais"]["idCalculo"] = { "id": int(idCalculo)}

        envio = api_post("imoveisBeneficiosFiscais", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["descricao"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["descricao"], ensure_ascii=False))

imoveisBeneficiosFiscais = imoveisBeneficiosFiscais()