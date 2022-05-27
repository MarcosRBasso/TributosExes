from samples import *
import json

class condominios(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idLogradouro, codigo, idBairro, idBanco, tipoCondominio, nome, numero, cep, latitude, 
                  longitude, idPessoa, anoConstrucao, utilizacao, nroPavimentos, nroBlocos, nroApartamentos, nroGaragens, nroElevadores, nroSalas, areaComum, areaEdificada):
        try:
            sql = """
                INSERT INTO condominios (                    
                    idIntegracao,                   
                    id_cloud, 
                    idLogradouro,
                    codigo,                                               
                    idBairro, 
                    idBanco,
                    tipoCondominio,
                    nome,
                    numero,
                    cep,
                    latitude,
                    longitude,
                    idPessoa,
                    anoConstrucao,
                    utilizacao,
                    nroPavimentos,
                    nroBlocos,
                    nroApartamentos,
                    nroGaragens,
                    nroElevadores,
                    nroSalas,
                    areaComum,
                    areaEdificada                    
                ) VALUES (
                    %(idLogradouro)s,
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(codigo)s,
                    %(idBairro)s,
                    %(idBanco)s,
                    %(tipoCondominio)s,
                    %(nome)s,
                    %(numero)s,
                    %(cep)s,
                    %(latitude)s,
                    %(longitude)s,
                    %(idPessoa)s,
                    %(anoConstrucao)s,
                    %(utilizacao)s,
                    %(nroPavimentos)s,
                    %(nroBlocos)s,
                    %(nroApartamentos)s,
                    %(nroGaragens)s,
                    %(nroElevadores)s,
                    %(nroSalas)s,
                    %(areaComum)s,
                    %(areaEdificada)s                                        
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idLogradouro = idLogradouro,
                codigo = codigo,
                idBairro = idBairro,                               
                idBanco = idBanco,
                tipoCondominio = tipoCondominio,
                nome = nome,                               
                numero = numero,
                cep = cep,
                latitude = latitude,                               
                longitude = longitude,
                idPessoa = idPessoa,
                anoConstrucao = anoConstrucao,                               
                utilizacao = utilizacao,
                nroPavimentos = nroPavimentos,
                nroBlocos = nroBlocos,                               
                nroApartamentos = nroApartamentos,
                nroGaragens = nroGaragens,
                nroElevadores = nroElevadores,                               
                nroSalas = nroSalas,
                areaComum = areaComum,                               
                areaEdificada = areaEdificada
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {condominios} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {condominios}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM condominios"
            if not self.query(sql_s):
                send_log_warning(f"condominios não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM condominios WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM condominios WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    condominios 
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
            sql = f"SELECT * FROM condominios WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM condominios WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM condominios WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idLogradouro, codigo, idBairro, idBanco, tipoCondominio, nome, numero, cep, latitude, 
                  longitude, idPessoa, anoConstrucao, utilizacao, nroPavimentos, nroBlocos, nroApartamentos, nroGaragens, nroElevadores, nroSalas, areaComum, areaEdificada):
        objeto = {
            "idIntegracao": f"condominios{id}",
            "content": {}                                 
        }
        if numero:
            objeto["content"]["numero"] = f"{numero}"
        
        if utilizacao:
            objeto["content"]["utilizacao"] = f"{utilizacao}"
        
        if nroPavimentos:
            objeto["content"]["nroPavimentos"] = f"{nroPavimentos}"
        
        if nome:
            objeto["content"]["nome"] = f"{nome}"
        
        if nroGaragens:
            objeto["content"]["nroGaragens"] = f"{nroGaragens}" 

        if cep:
            objeto["content"]["cep"] = f"{cep}"  

        if latitude:
            objeto["content"]["latitude"] = f"{latitude}"
        
        if nroSalas:
            objeto["content"]["nroSalas"] = f"{nroSalas}"
        
        if areaComum:
            objeto["content"]["areaComum"] = f"{areaComum}"
        
        if areaEdificada:
            objeto["content"]["areaEdificada"] = f"{areaEdificada}" 

        if codigo:
            objeto["content"]["codigo"] = f"{codigo}"
        
        if idBairro:
            objeto["content"]["idBairro"] = { "id": int(idBairro)}
        
        if nroApartamentos:
            objeto["content"]["nroApartamentos"] = f"{nroApartamentos}"
        
        if longitude:
            objeto["content"]["longitude"] = f"{longitude}"
        
        if idPessoa:
            objeto["content"]["idPessoa"] = { "id": int(idPessoa)} 

        if anoConstrucao:
            objeto["content"]["anoConstrucao"] = f"{anoConstrucao}"    

        if idLogradouro != None:
            objeto[0]["content"]["AgenciaBancaria"] = { "id": int(idLogradouro) }               

        if idBanco != None:
            objeto[0]["content"]["Banco"] = { "id": int(idBanco) }

        if tipoCondominio != None:
            objeto[0]["content"]["Convenio"] = f"{tipoCondominio}"
                    
        if nroBlocos != None:
            objeto[0]["content"]["MotivoEstorno"] = { "id": int(nroBlocos) }

        if nroElevadores != None:
            objeto[0]["content"]["nroElevadores"] = { "id": int(nroElevadores) }  

        envio = api_post("condominios", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

condominios = condominios()