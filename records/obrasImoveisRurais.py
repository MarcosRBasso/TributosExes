from samples import *
import json

class obrasImoveisRurais(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idLogradouro, idCondominio, idBairro, idDistrito, idFace, idLocalidade, idLoteamento, idSecao, apartamento, 
                  bloco, cep, complemento, denominacao, latitude, longitude, lote, matricula, quadra, setor):
        try:
            sql = """
                INSERT INTO obrasImoveisRurais (                    
                    idIntegracao,                   
                    id_cloud, 
                    idLogradouro,
                    idCondominio,                                               
                    idBairro, 
                    idDistrito,
                    idFace,
                    idLocalidade,
                    idLoteamento,
                    idSecao,
                    apartamento,
                    bloco,
                    cep,
                    complemento,
                    denominacao,
                    latitude,
                    longitude,
                    lote,
                    matricula,
                    quadra,
                    setor                   
                ) VALUES (
                    %(idLogradouro)s,
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idCondominio)s,
                    %(idBairro)s,
                    %(idDistrito)s,
                    %(idFace)s,
                    %(idLocalidade)s,
                    %(idLoteamento)s,
                    %(idSecao)s,
                    %(apartamento)s,
                    %(bloco)s,
                    %(cep)s,
                    %(complemento)s,
                    %(denominacao)s,
                    %(latitude)s,
                    %(longitude)s,
                    %(lote)s,
                    %(matricula)s,
                    %(quadra)s,
                    %(setor)s                                       
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idLogradouro = idLogradouro,
                idCondominio = idCondominio,
                idBairro = idBairro,                               
                idDistrito = idDistrito,
                idFace = idFace,
                idLocalidade = idLocalidade,                               
                idLoteamento = idLoteamento,
                idSecao = idSecao,
                apartamento = apartamento,                               
                bloco = bloco,
                cep = cep,
                complemento = complemento,                               
                denominacao = denominacao,
                latitude = latitude,
                longitude = longitude,                               
                lote = lote,
                matricula = matricula,
                quadra = quadra,                               
                setor = setor,
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {obrasImoveisRurais} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {obrasImoveisRurais}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM obrasImoveisRurais"
            if not self.query(sql_s):
                send_log_warning(f"obrasImoveisRurais não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM obrasImoveisRurais WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM obrasImoveisRurais WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    obrasImoveisRurais 
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
            sql = f"SELECT * FROM obrasImoveisRurais WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM obrasImoveisRurais WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM obrasImoveisRurais WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idLogradouro, idCondominio, idBairro, idDistrito, idFace, idLocalidade, idLoteamento, idSecao, apartamento, 
                  bloco, cep, complemento, denominacao, latitude, longitude, lote, matricula, quadra, setor):
        objeto = {
            "idIntegracao": f"obrasImoveisRurais{id}",
            "content": {}                                 
        }
        if idLoteamento:
            objeto["content"]["idLoteamento"] = { "id": int(idLoteamento)}
        
        if denominacao:
            objeto["content"]["denominacao"] = f"{denominacao}"
        
        if latitude:
            objeto["content"]["latitude"] = f"{latitude}"
        
        if idLocalidade:
            objeto["content"]["idLocalidade"] = { "id": int(idLocalidade)}
        
        if matricula:
            objeto["content"]["matricula"] = f"{matricula}" 

        if idSecao:
            objeto["content"]["idSecao"] = { "id": int(idSecao)}  

        if apartamento:
            objeto["content"]["apartamento"] = f"{apartamento}"
        
        if setor:
            objeto["content"]["setor"] = f"{setor}"

        if idCondominio:
            objeto["content"]["idCondominio"] = { "id": int(idCondominio)}
        
        if idBairro:
            objeto["content"]["idBairro"] = { "id": int(idBairro)}
        
        if lote:
            objeto["content"]["lote"] = f"{lote}"
        
        if bloco:
            objeto["content"]["bloco"] = f"{bloco}"
        
        if cep:
            objeto["content"]["cep"] = { "id": int(cep)} 

        if complemento:
            objeto["content"]["complemento"] = f"{complemento}"    

        if idLogradouro != None:
            objeto[0]["content"]["AgenciaBancaria"] = { "id": int(idLogradouro) }               

        if idDistrito != None:
            objeto[0]["content"]["Banco"] = { "id": int(idDistrito) }

        if idFace != None:
            objeto[0]["content"]["Convenio"] = { "id": int(idFace)}
                    
        if longitude != None:
            objeto[0]["content"]["MotivoEstorno"] = f"{longitude}"

        if quadra != None:
            objeto[0]["content"]["quadra"] = f"{quadra}" 

        envio = api_post("obrasImoveisRurais", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

obrasImoveisRurais = obrasImoveisRurais()