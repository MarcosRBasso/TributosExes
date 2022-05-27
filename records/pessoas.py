from samples import *
import json

class pessoas(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idPessoas, idEnderecoPrincipal, cpfCnpj, inscricaoMunicipal, nome, nomeFantasia, site, situacao, 
                  tipoPessoa):
        try:
            sql = """
                INSERT INTO pessoas (                    
                    idIntegracao,                   
                    id_cloud, 
                    idPessoas,
                    idEnderecoPrincipal,                                               
                    cpfCnpj, 
                    inscricaoMunicipal,
                    nome,
                    site,
                    situacao,
                    nomeFantasia,
                    tipoPessoa
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idPessoas)s,
                    %(idEnderecoPrincipal)s,
                    %(cpfCnpj)s,
                    %(inscricaoMunicipal)s,
                    %(nome)s,
                    %(site)s,
                    %(situacao)s,
                    %(nomeFantasia)s,
                    %(tipoPessoa)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idPessoas = idPessoas,
                idEnderecoPrincipal = idEnderecoPrincipal,
                cpfCnpj = cpfCnpj,                               
                inscricaoMunicipal = inscricaoMunicipal,
                nome = nome,
                site = site,                               
                situacao = situacao,
                nomeFantasia = nomeFantasia,
                tipoPessoa = tipoPessoa
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {pessoas} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {pessoas}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM pessoas"
            if not self.query(sql_s):
                send_log_warning(f"pessoas não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM pessoas WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM pessoas WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    pessoas 
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
            sql = f"SELECT * FROM pessoas WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM pessoas WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM pessoas WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idPessoas, idEnderecoPrincipal, cpfCnpj, inscricaoMunicipal, nome, nomeFantasia, site, situacao, 
                tipoPessoa):
        objeto = {
            "idIntegracao": f"pessoas{id}",
            "content": {}                                 
        }
        if idPessoas:
            objeto["content"]["idPessoas"] = { "id": int(idPessoas)}          
        
        if situacao:
            objeto["content"]["situacao"] = f"{situacao}"

        if idEnderecoPrincipal:
            objeto["content"]["idEnderecoPrincipal"] = { "id": int(idEnderecoPrincipal)}           
        
        if inscricaoMunicipal:
            objeto["content"]["inscricaoMunicipal"] = f"{inscricaoMunicipal}"

        if nome:
            objeto["content"]["nome"] = f"{nome}"

        if site:
            objeto["content"]["site"] = f"{site}"   
        
        if tipoPessoa:
            objeto["content"]["tipoPessoa"] = f"{tipoPessoa}"
        
        if nomeFantasia:
            objeto["content"]["nomeFantasia"] = f"{nomeFantasia}"

        if cpfCnpj != None:
            objeto[0]["content"]["cpfCnpj"] = { "id": int(cpfCnpj) }          
            
        envio = api_post("pessoas", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

pessoas = pessoas()