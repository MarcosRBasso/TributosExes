from samples import *
import json

class imoveisMovimentacoes(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idTransferenciaImoveis, idImoveis, idAlteracaoCadastral, audCriadoPor, audDhCriacao, audAlteradoPor, audDhAlteracao, descricao, 
                nroProcesso, situacao, tipoMovimentacao):
        try:
            sql = """
                INSERT INTO imoveisMovimentacoes (                    
                    idIntegracao,                   
                    id_cloud, 
                    idTransferenciaImoveis,
                    idImoveis,                                               
                    idAlteracaoCadastral, 
                    audCriadoPor,
                    audDhCriacao,
                    audDhAlteracao,
                    descricao,
                    audAlteradoPor,
                    nroProcesso,                    
                    situacao,
                    tipoMovimentacao             
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idTransferenciaImoveis)s,
                    %(idImoveis)s,
                    %(idAlteracaoCadastral)s,
                    %(audCriadoPor)s,
                    %(audDhCriacao)s,
                    %(audDhAlteracao)s,
                    %(descricao)s,
                    %(audAlteradoPor)s,
                    %(nroProcesso)s,                    
                    %(situacao)s,
                    %(tipoMovimentacao)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idTransferenciaImoveis = idTransferenciaImoveis,
                idImoveis = idImoveis,
                idAlteracaoCadastral = idAlteracaoCadastral,                               
                audCriadoPor = audCriadoPor,
                audDhCriacao = audDhCriacao,
                audDhAlteracao = audDhAlteracao,                               
                descricao = descricao,
                audAlteradoPor = audAlteradoPor,
                nroProcesso = nroProcesso,                                               
                situacao = situacao,
                tipoMovimentacao = tipoMovimentacao
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {imoveisMovimentacoes} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {imoveisMovimentacoes}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM imoveisMovimentacoes"
            if not self.query(sql_s):
                send_log_warning(f"imoveisMovimentacoes não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM imoveisMovimentacoes WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM imoveisMovimentacoes WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    imoveisMovimentacoes 
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
            sql = f"SELECT * FROM imoveisMovimentacoes WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM imoveisMovimentacoes WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM imoveisMovimentacoes WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idTransferenciaImoveis, idImoveis, idAlteracaoCadastral, audCriadoPor, audDhCriacao, audAlteradoPor, audDhAlteracao, descricao, 
                nroProcesso, situacao, tipoMovimentacao):
        objeto = {
            "idIntegracao": f"imoveisMovimentacoes{id}",
            "content": {}                                 
        }
        if idTransferenciaImoveis:
            objeto["content"]["idTransferenciaImoveis"] = { "id": int(idTransferenciaImoveis)}

        if descricao:
            objeto["content"]["descricao"] = f"{descricao}"    
        
        if tipoMovimentacao:
            objeto["content"]["tipoMovimentacao"] = f"{tipoMovimentacao}"

        if idImoveis:
            objeto["content"]["idImoveis"] = { "id": int(idImoveis)}
           
        if audCriadoPor:
            objeto["content"]["audCriadoPor"] = f"{audCriadoPor}"
       
        if audDhCriacao:
            objeto["content"]["audDhCriacao"] = f"{audDhCriacao}"

        if audDhAlteracao:
            objeto["content"]["audDhAlteracao"] = f"{audDhAlteracao}"   

        if situacao:
            objeto["content"]["situacao"] = f"{situacao}"
        
        if nroProcesso:
            objeto["content"]["nroProcesso"] = f"{nroProcesso}"
        if audAlteradoPor:
            objeto["content"]["audAlteradoPor"] = f"{audAlteradoPor}"

        if idAlteracaoCadastral != None:
            objeto[0]["content"]["idAlteracaoCadastral"] = { "id": int(idAlteracaoCadastral)}    
            
        envio = api_post("imoveisMovimentacoes", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

imoveisMovimentacoes = imoveisMovimentacoes()