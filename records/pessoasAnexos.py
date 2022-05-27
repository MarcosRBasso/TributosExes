from samples import *
import json

class pessoasAnexos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idPessoas, descricao, nomeArquivo, tipoArquivo, idPessoasMovimentacoes):
        try:
            sql = """
                INSERT INTO pessoasAnexos (                    
                    idIntegracao,                   
                    id_cloud, 
                    idPessoas,
                    descricao,                                               
                    nomeArquivo, 
                    tipoArquivo,
                    idPessoasMovimentacoes             
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idPessoas)s,
                    %(descricao)s,
                    %(nomeArquivo)s,
                    %(tipoArquivo)s,
                    %(idPessoasMovimentacoes)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idPessoas = idPessoas,
                descricao = descricao,
                nomeArquivo = nomeArquivo,                               
                tipoArquivo = tipoArquivo,
                idPessoasMovimentacoes = idPessoasMovimentacoes
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {pessoasAnexos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {pessoasAnexos}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM pessoasAnexos"
            if not self.query(sql_s):
                send_log_warning(f"pessoasAnexos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM pessoasAnexos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM pessoasAnexos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    pessoasAnexos 
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
            sql = f"SELECT * FROM pessoasAnexos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM pessoasAnexos WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM pessoasAnexos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idPessoas, descricao, nomeArquivo, tipoArquivo, idPessoasMovimentacoes):
        objeto = {
            "idIntegracao": f"pessoasAnexos{id}",
            "content": {}                                 
        }
        if idPessoas:
            objeto["content"]["idPessoas"] = { "id": int(idPessoas)}

        if descricao:
            objeto["content"]["descricao"] = f"{descricao}"        
       
        if tipoArquivo:
            objeto["content"]["tipoArquivo"] = f"{tipoArquivo}"       
       
        if idPessoasMovimentacoes:
            objeto["content"]["idPessoasMovimentacoes"] = { "id": int(idPessoasMovimentacoes)}

        if nomeArquivo != None:
            objeto[0]["content"]["nomeArquivo"] = f"{nomeArquivo}"    
            
        envio = api_post("pessoasAnexos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

pessoasAnexos = pessoasAnexos()