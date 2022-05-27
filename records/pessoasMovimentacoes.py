from samples import *
import json

class pessoasMovimentacoes(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idPessoa, nroProcesso, audCriadoPor, audDhCriacao, audAlteradoPor, audDhAlteracao, tipoMovimentacao, situacao, 
                descricao, dhMovimentacao):
        try:
            sql = """
                INSERT INTO pessoasMovimentacoes (                    
                    idIntegracao,                   
                    id_cloud, 
                    idPessoa,
                    nroProcesso,                                               
                    audCriadoPor, 
                    audDhCriacao,
                    audAlteradoPor,
                    tipoMovimentacao,
                    situacao,
                    audDhAlteracao,
                    descricao,                    
                    dhMovimentacao
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idPessoa)s,
                    %(nroProcesso)s,
                    %(audCriadoPor)s,
                    %(audDhCriacao)s,
                    %(audAlteradoPor)s,
                    %(tipoMovimentacao)s,
                    %(situacao)s,
                    %(audDhAlteracao)s,
                    %(descricao)s,                    
                    %(dhMovimentacao)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idPessoa = idPessoa,
                nroProcesso = nroProcesso,
                audCriadoPor = audCriadoPor,                               
                audDhCriacao = audDhCriacao,
                audAlteradoPor = audAlteradoPor,
                tipoMovimentacao = tipoMovimentacao,                               
                situacao = situacao,
                audDhAlteracao = audDhAlteracao,
                descricao = descricao,                                               
                dhMovimentacao = dhMovimentacao
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {pessoasMovimentacoes} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {pessoasMovimentacoes}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM pessoasMovimentacoes"
            if not self.query(sql_s):
                send_log_warning(f"pessoasMovimentacoes não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM pessoasMovimentacoes WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM pessoasMovimentacoes WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    pessoasMovimentacoes 
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
            sql = f"SELECT * FROM pessoasMovimentacoes WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM pessoasMovimentacoes WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM pessoasMovimentacoes WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idPessoa, nroProcesso, audCriadoPor, audDhCriacao, audAlteradoPor, audDhAlteracao, tipoMovimentacao, situacao, 
                descricao, dhMovimentacao):
        objeto = {
            "idIntegracao": f"pessoasMovimentacoes{id}",
            "content": {}                                 
        }
        if idPessoa:
            objeto["content"]["idPessoa"] = { "id": int(idPessoa)}          
        
        if situacao:
            objeto["content"]["situacao"] = f"{situacao}"

        if nroProcesso:
            objeto["content"]["nroProcesso"] = { "id": int(nroProcesso)}           
        
        if audDhCriacao:
            objeto["content"]["audDhCriacao"] = f"{audDhCriacao}" 

        if audAlteradoPor:
            objeto["content"]["audAlteradoPor"] = f"{audAlteradoPor}"

        if tipoMovimentacao:
            objeto["content"]["tipoMovimentacao"] = f"{tipoMovimentacao}"   

        if dhMovimentacao:
            objeto["content"]["dhMovimentacao"] = f"{dhMovimentacao}"
        
        if descricao:
            objeto["content"]["descricao"] = f"{descricao}"
                   
        if audDhAlteracao:
            objeto["content"]["audDhAlteracao"] = f"{audDhAlteracao}"

        if audCriadoPor != None:
            objeto[0]["content"]["audCriadoPor"] = f"{audCriadoPor}"          
            
        envio = api_post("pessoasMovimentacoes", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

pessoasMovimentacoes = pessoasMovimentacoes()