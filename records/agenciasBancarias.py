from samples import *
import json

class agenciasBancarias(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao,  cep, digAgencia, id_cloud, idBairros, idBancos, idLogradouros, idMunicipios, nome, nroAgencia, numero):
        try:
            sql = """
                INSERT INTO agenciasBancarias (
                    idIntegracao,                    
                    cep,
                    id_cloud,
                    digAgencia,
                    idBairros,
                    idBancos,
                    idLogradouros,
                    idMunicipios,
                    nome,
                    nroAgencia,
                    numero
                ) VALUES (
                    %(idIntegracao)s,
                    %(cep)s,
                    %(id_cloud)s,
                    %(digAgencia)s,
                    %(idBairros)s,
                    %(idBancos)s,
                    %(idLogradouros)s,
                    %(idMunicipios)s,
                    %(nome)s,
                    %(nroAgencia)s,
                    %(numero)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,               
                cep = cep,
                digAgencia = digAgencia,
                id_cloud = id_cloud,
                idBairros = idBairros,
                idBancos = idBancos,
                idLogradouros = idLogradouros,
                idMunicipios = idMunicipios,
                nome = nome,
                nroAgencia = nroAgencia,
                numero = numero
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {nome} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o agrupamento {nome}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM agenciasBancarias"
            if not self.query(sql_s):
                send_log_warning(f"Agências Bancarias não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM agenciasBancarias WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"Agências Bancarias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do agrupamentos. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM agenciasBancarias WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"Agências Bancarias {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    agenciasBancarias 
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
            send_log_info(f"Agências Bancarias {id} atualizado com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de atualização da Agências Bancarias. {error}")

    def db_search(self, id):
        try:
            sql = f"SELECT * FROM agenciasBancarias WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"Agências Bancarias {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM agenciasBancarias WHERE id_cloud is null"
            data = self.query(sql)
            if data:
                send_log_info("Consulta de todas as Agências Bancarias realizada com sucesso.")
                return data
            return None
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def get_id_cloud(self, id):
        if (id == None):
            return None
        try:
            sql = f"SELECT id_cloud FROM agenciasBancarias WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"agrupamentos {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, cep, digAgencia, id_cloud, idBairros, idBancos, idLogradouros, idMunicipios, nome, nroAgencia, numero):
        objeto = {
             "idIntegracao": f"agenciasBancarias{id}",
              "content": {} 
            }                    
                                                      
        if numero:
            objeto["content"]["numero"] = f"{numero}"
        
        if cep:
            objeto["content"]["cep"] = f"{cep}"
        
        if digAgencia:
            objeto["content"]["digitoagencia"] = f"{digAgencia}"
        
        if nome:
            objeto["content"]["nome"] = f"{nome}"
        
        if nroAgencia:
            objeto["content"]["numeroAgencias"] = f"{nroAgencia}"    

        if idLogradouros != None:
            objeto[0]["content"]["logradouros"] = { "id": int(idLogradouros) }

        if idBancos != None:
            objeto[0]["content"]["Bancos"] = { "id": int(idBancos) }
                    
        if idMunicipios != None:
            objeto[0]["content"]["municipios"] = { "id": int(idMunicipios) }

        if idBairros != None:
            objeto[0]["content"]["bairros"] = { "id": int(idBairros) }

        envio = api_post("agenciasBancarias", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

agenciasBancarias = agenciasBancarias()