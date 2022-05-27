from samples import *
import json

class paises(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idTemplate, sigla2C, sigla3C, sigla3D, codigoBacen, versionTemplate):
        try:
            sql = """
                INSERT INTO paises (                    
                    idIntegracao,                   
                    id_cloud, 
                    idTemplate,                                            
                    sigla2C, 
                    sigla3C,
                    sigla3D,
                    versionTemplate,
                    codigoBacen                
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idTemplate)s,
                    %(sigla2C)s,
                    %(sigla3C)s,
                    %(sigla3D)s,
                    %(versionTemplate)s,
                    %(codigoBacen)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idTemplate = idTemplate,
                sigla2C = sigla2C,                               
                sigla3C = sigla3C,
                sigla3D = sigla3D,
                versionTemplate = versionTemplate,
                codigoBacen = codigoBacen
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {paises} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {paises}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM paises"
            if not self.query(sql_s):
                send_log_warning(f"paises não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM paises WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM paises WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    paises 
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
            sql = f"SELECT * FROM paises WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM paises WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM paises WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idTemplate,  sigla2C, sigla3C, sigla3D, codigoBacen, versionTemplate):
        objeto = {
            "idIntegracao": f"paises{id}",
            "content": {}                                 
        }
        if idTemplate:
            objeto["content"]["idTemplate"] = { "id": int(idTemplate)}
       
        if sigla3C:
            objeto["content"]["sigla3C"] = f"{sigla3C}"       
       
        if sigla3D:
            objeto["content"]["sigla3D"] = f"{sigla3D}"

        if versionTemplate:
            objeto["content"]["versionTemplate"] = f"{versionTemplate}"  
        
        if codigoBacen:
            objeto["content"]["codigoBacen"] = f"{codigoBacen}"              

        if sigla2C != None:
            objeto[0]["content"]["sigla2C"] = f"{sigla2C}"    
            
        envio = api_post("paises", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

paises = paises()