from samples import *
import json

class pessoasEnderecos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idPessoa, idLogradouro, idCondominio, idLoteamento, idBairro, idDistrito, idMunicipio, idEstado, 
                principal, ordem, descricao, cep, numero, complemento, bloco, apartamento, observacao, 
                longitude, latitude):
        try:
            sql = """
                INSERT INTO pessoasEnderecos (                    
                    idIntegracao,                   
                    id_cloud, 
                    idPessoa,
                    idLogradouro,                                               
                    idCondominio, 
                    idLoteamento,
                    idBairro,
                    idMunicipio,
                    idEstado,
                    idDistrito,
                    principal,                    
                    ordem,
                    descricao,
                    cep,
                    numero,
                    complemento,
                    bloco, 
                    apartamento, 
                    observacao, 
                    longitude, 
                    latitude         
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idPessoa)s,
                    %(idLogradouro)s,
                    %(idCondominio)s,
                    %(idLoteamento)s,
                    %(idBairro)s,
                    %(idMunicipio)s,
                    %(idEstado)s,
                    %(idDistrito)s,
                    %(principal)s,                    
                    %(ordem)s,
                    %(descricao)s,
                    %(cep)s,
                    %(numero)s,
                    %(complemento)s,
                    %(bloco)s, 
                    %(apartamento)s, 
                    %(observacao)s, 
                    %(longitude)s, 
                    %(latitude)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idPessoa = idPessoa,
                idLogradouro = idLogradouro,
                idCondominio = idCondominio,                               
                idLoteamento = idLoteamento,
                idBairro = idBairro,
                idMunicipio = idMunicipio,                               
                idEstado = idEstado,
                idDistrito = idDistrito,
                principal = principal,                                               
                ordem = ordem,
                descricao = descricao,                               
                cep = cep,
                numero = numero,
                complemento = complemento,
                bloco = bloco, 
                apartamento = apartamento, 
                observacao = observacao, 
                longitude = longitude, 
                latitude = latitude
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {pessoasEnderecos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {pessoasEnderecos}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM pessoasEnderecos"
            if not self.query(sql_s):
                send_log_warning(f"pessoasEnderecos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM pessoasEnderecos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM pessoasEnderecos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    pessoasEnderecos 
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
            sql = f"SELECT * FROM pessoasEnderecos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM pessoasEnderecos WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM pessoasEnderecos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idPessoa, idLogradouro, idCondominio, idLoteamento, idBairro, idDistrito, idMunicipio, idEstado, 
                principal, ordem, descricao, cep, numero, complemento, 
                bloco, apartamento, observacao, longitude, latitude):
        objeto = {
            "idIntegracao": f"pessoasEnderecos{id}",
            "content": {}                                 
        }
        if latitude:
            objeto["content"]["latitude"] = f"{latitude}"   

        if idPessoa:
            objeto["content"]["idPessoa"] = { "id": int(idPessoa)}

        if bloco:
            objeto["content"]["bloco"] = f"{bloco}"   

        if apartamento:
            objeto["content"]["apartamento"] = f"{apartamento}"
        
        if observacao:
            objeto["content"]["observacao"] = { "id": int(observacao)}
           
        if longitude:
            objeto["content"]["longitude"] = f"{longitude}"            
        
        if idEstado:
            objeto["content"]["idEstado"] = { "id": int(idEstado)}

        if idLogradouro:
            objeto["content"]["idLogradouro"] = { "id": int(idLogradouro)}           
        
        if idLoteamento:
            objeto["content"]["idLoteamento"] = { "id": int(idLoteamento)} 

        if descricao:
            objeto["content"]["descricao"] = f"{descricao}"  

        if idBairro:
            objeto["content"]["idBairro"] = { "id": int(idBairro)}

        if idMunicipio:
            objeto["content"]["idMunicipio"] = { "id": int(idMunicipio)}  

        if ordem:
            objeto["content"]["ordem"] = f"{ordem}"
        
        if principal:
            objeto["content"]["principal"] = f"{principal}"
           
        if cep:
            objeto["content"]["cep"] = f"{cep}"
        
        if complemento:
            objeto["content"]["complemento"] = f"{complemento}"
        
        if idDistrito:
            objeto["content"]["idDistrito"] = { "id": int(idDistrito)}

        if idCondominio != None:
            objeto[0]["content"]["idCondominio"] = { "id": int(idCondominio)}  

        if numero != None:
            objeto[0]["content"]["numero"] = f"{numero}"        
            
        envio = api_post("pessoasEnderecos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

pessoasEnderecos = pessoasEnderecos()