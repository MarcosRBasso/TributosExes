from samples import *
import json

class bairros(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idMunicipio, codigo, nome, zonaRural):
        try:
            sql = """
                INSERT INTO bairros (                    
                    idIntegracao,                   
                    id_cloud,                                                           
                    idMunicipio, 
                    codigo,
                    nome,
                    zonaRural                                             
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,                                                            
                    %(idMunicipio)s,
                    %(codigo)s,
                    %(nome)s,
                    %(zonaRural)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                                                               
                idMunicipio = idMunicipio,                               
                codigo = codigo,
                nome = nome,
                zonaRural = zonaRural
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {bairros} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {bairros}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM bairros"
            if not self.query(sql_s):
                send_log_warning(f"bairros não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM bairros WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, descricao):
        try:
            sql_s = f"SELECT * FROM bairros WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    bairros 
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
            sql = f"SELECT * FROM bairros WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM bairros WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM bairros WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idMunicipio, codigo, nome, zonaRural):
        objeto = {
            "idIntegracao": f"bairros{id}",
            "content": {}                                 
        }
        if zonaRural != None:
            objeto[0]["content"]["zonaRural"] = f"{zonaRural}" 

        if nome != None:
            objeto[0]["content"]["nome"] = f"{nome}"  

        if codigo != None:
            objeto[0]["content"]["codigo"] = { "id": int(codigo)}    
               
        if idMunicipio != None:
            objeto[0]["camposadicionais"]["idMunicipio"] = { "id": int(idMunicipio)}

        envio = api_post("bairros", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["descricao"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["descricao"], ensure_ascii=False))

bairros = bairros()