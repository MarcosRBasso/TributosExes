from samples import *
import json

class logradouros(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idLogradouro, idTipoLogradouro, idMunicipio, cep, nome, epigrafe, extensao, lei, zonaFiscal):
        try:
            sql = """
                INSERT INTO logradouros (                    
                    idIntegracao,                   
                    id_cloud, 
                    idLogradouro,
                    idTipoLogradouro,                                               
                    idMunicipio, 
                    cep,
                    nome,
                    extensao,
                    epigrafe,
                    lei, 
                    zonaFiscal                
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idLogradouro)s,
                    %(idTipoLogradouro)s,
                    %(idMunicipio)s,
                    %(cep)s,
                    %(nome)s,
                    %(extensao)s,
                    %(epigrafe)s,
                    %(lei)s, 
                    %(zonaFiscal)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idLogradouro = idLogradouro,
                idTipoLogradouro = idTipoLogradouro,
                idMunicipio = idMunicipio,                               
                cep = cep,
                nome = nome,
                extensao = extensao,
                epigrafe = epigrafe,
                lei = lei, 
                zonaFiscal = zonaFiscal
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {logradouros} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {logradouros}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM logradouros"
            if not self.query(sql_s):
                send_log_warning(f"logradouros não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM logradouros WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM logradouros WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    logradouros 
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
            sql = f"SELECT * FROM logradouros WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM logradouros WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM logradouros WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idLogradouro, idTipoLogradouro, idMunicipio, cep, nome, epigrafe, extensao, lei, zonaFiscal):
        objeto = {
            "idIntegracao": f"logradouros{id}",
            "content": {}                                 
        }
        if idLogradouro:
            objeto["content"]["idLogradouro"] = { "id": int(idLogradouro)}

        if idTipoLogradouro:
            objeto["content"]["idTipoLogradouro"] = { "id": int(idTipoLogradouro)}   

        if lei:
            objeto["content"]["lei"] = f"{lei}"       
       
        if zonaFiscal:
            objeto["content"]["zonaFiscal"] = f"{zonaFiscal}"         
       
        if cep:
            objeto["content"]["cep"] = f"{cep}"       
       
        if nome:
            objeto["content"]["nome"] = f"{nome}"

        if extensao:
            objeto["content"]["extensao"] = f"{extensao}"  
        
        if epigrafe:
            objeto["content"]["epigrafe"] = f"{epigrafe}"              

        if idMunicipio != None:
            objeto[0]["content"]["idMunicipio"] = { "id": int(idMunicipio)}    
            
        envio = api_post("logradouros", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

logradouros = logradouros()