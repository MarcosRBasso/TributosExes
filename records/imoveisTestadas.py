from samples import *
import json

class imoveisTestadas(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idImovel, idBairro, idFace, idLogradouro, idSecao, anoBase, anoDesativacao, extensao, 
                numero, testadaPrincipal):
        try:
            sql = """
                INSERT INTO imoveisTestadas (                    
                    idIntegracao,                   
                    id_cloud, 
                    idImovel,
                    idBairro,                                               
                    idFace, 
                    idLogradouro,
                    idSecao,
                    anoDesativacao,
                    extensao,
                    anoBase,
                    numero,                    
                    testadaPrincipal             
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idImovel)s,
                    %(idBairro)s,
                    %(idFace)s,
                    %(idLogradouro)s,
                    %(idSecao)s,
                    %(anoDesativacao)s,
                    %(extensao)s,
                    %(anoBase)s,
                    %(numero)s,                    
                    %(testadaPrincipal)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idImovel = idImovel,
                idBairro = idBairro,
                idFace = idFace,                               
                idLogradouro = idLogradouro,
                idSecao = idSecao,
                anoDesativacao = anoDesativacao,                               
                extensao = extensao,
                anoBase = anoBase,
                numero = numero,                                               
                testadaPrincipal = testadaPrincipal
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {imoveisTestadas} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {imoveisTestadas}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM imoveisTestadas"
            if not self.query(sql_s):
                send_log_warning(f"imoveisTestadas não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM imoveisTestadas WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM imoveisTestadas WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    imoveisTestadas 
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
            sql = f"SELECT * FROM imoveisTestadas WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM imoveisTestadas WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM imoveisTestadas WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idImovel, idBairro, idFace, idLogradouro, idSecao, anoBase, anoDesativacao, extensao, 
                numero, testadaPrincipal):
        objeto = {
            "idIntegracao": f"imoveisTestadas{id}",
            "content": {}                                 
        }
        if idImovel:
            objeto["content"]["idImovel"] = { "id": int(idImovel)}
        
        if extensao:
            objeto["content"]["extensao"] = f"{extensao}"

        if idBairro:
            objeto["content"]["idBairro"] = { "id": int(idBairro)}
           
        if idLogradouro:
            objeto["content"]["idLogradouro"] = { "id": int(idLogradouro)}
       
        if idSecao:
            objeto["content"]["idSecao"] = { "id": int(idSecao)}

        if anoDesativacao:
            objeto["content"]["anoDesativacao"] = f"{anoDesativacao}"   

        if testadaPrincipal:
            objeto["content"]["testadaPrincipal"] = f"{testadaPrincipal}"
        
        if numero:
            objeto["content"]["numero"] = f"{numero}"
        if anoBase:
            objeto["content"]["anoBase"] = f"{anoBase}"

        if idFace != None:
            objeto[0]["content"]["idFace"] = { "id": int(idFace)}    
            
        envio = api_post("imoveisTestadas", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

imoveisTestadas = imoveisTestadas()