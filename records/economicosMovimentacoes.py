from samples import *
import json

class economicosMovimentacoes(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idEconomico, audCriadoPor, audDhCriacao, audAlteradoPor, audDhAlteracao, dataValidadeAlvara, descricao, dhMovimentacao, 
                dtSituacao, nroDocumento, nroProcesso, tipoMovimentacao, situacaoEconomico):
        try:
            sql = """
                INSERT INTO economicosMovimentacoes (                    
                    idIntegracao,                   
                    id_cloud, 
                    idEconomico,
                    audCriadoPor,                                               
                    audDhCriacao, 
                    audAlteradoPor,
                    audDhAlteracao,
                    descricao,
                    dhMovimentacao,
                    dataValidadeAlvara,
                    dtSituacao,                    
                    nroDocumento,
                    nroProcesso,
                    tipoMovimentacao,
                    situacaoEconomico                  
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idEconomico)s,
                    %(audCriadoPor)s,
                    %(audDhCriacao)s,
                    %(audAlteradoPor)s,
                    %(audDhAlteracao)s,
                    %(descricao)s,
                    %(dhMovimentacao)s,
                    %(dataValidadeAlvara)s,
                    %(dtSituacao)s,                    
                    %(nroDocumento)s,
                    %(nroProcesso)s,
                    %(tipoMovimentacao)s,
                    %(situacaoEconomico)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idEconomico = idEconomico,
                audCriadoPor = audCriadoPor,
                audDhCriacao = audDhCriacao,                               
                audAlteradoPor = audAlteradoPor,
                audDhAlteracao = audDhAlteracao,
                descricao = descricao,                               
                dhMovimentacao = dhMovimentacao,
                dataValidadeAlvara = dataValidadeAlvara,
                dtSituacao = dtSituacao,                                               
                nroDocumento = nroDocumento,
                nroProcesso = nroProcesso,                               
                tipoMovimentacao = tipoMovimentacao,
                situacaoEconomico = situacaoEconomico
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {economicosMovimentacoes} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {economicosMovimentacoes}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM economicosMovimentacoes"
            if not self.query(sql_s):
                send_log_warning(f"economicosMovimentacoes não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM economicosMovimentacoes WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM economicosMovimentacoes WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    economicosMovimentacoes 
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
            sql = f"SELECT * FROM economicosMovimentacoes WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM economicosMovimentacoes WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM economicosMovimentacoes WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idEconomico, audCriadoPor, audDhCriacao, audAlteradoPor, audDhAlteracao, dataValidadeAlvara, descricao, dhMovimentacao, 
                dtSituacao, nroDocumento, nroProcesso, tipoMovimentacao, situacaoEconomico):
        objeto = {
            "idIntegracao": f"economicosMovimentacoes{id}",
            "content": {}                                 
        }
        if idEconomico:
            objeto["content"]["idEconomico"] = { "id": int(idEconomico)}
        
        if dhMovimentacao:
            objeto["content"]["dhMovimentacao"] = f"{dhMovimentacao}"

        if audCriadoPor:
            objeto["content"]["audCriadoPor"] = f"{audCriadoPor}"
        
        if audAlteradoPor:
            objeto["content"]["audAlteradoPor"] = f"{audAlteradoPor}" 

        if nroProcesso:
            objeto["content"]["nroProcesso"] = { "id": int(nroProcesso)}       
       
        if audDhAlteracao:
            objeto["content"]["audDhAlteracao"] = f"{audDhAlteracao}"

        if descricao:
            objeto["content"]["descricao"] = f"{descricao}"   

        if nroDocumento:
            objeto["content"]["nroDocumento"] = f"{nroDocumento}"
        
        if dtSituacao:
            objeto["content"]["dtSituacao"] = f"{dtSituacao}"
           
        if tipoMovimentacao:
            objeto["content"]["tipoMovimentacao"] = f"{tipoMovimentacao}"
        
        if dataValidadeAlvara:
            objeto["content"]["dataValidadeAlvara"] = f"{dataValidadeAlvara}"

        if audDhCriacao != None:
            objeto[0]["content"]["audDhCriacao"] = f"{audDhCriacao}"               

        if situacaoEconomico != None:
            objeto[0]["content"]["situacaoEconomico"] = f"{situacaoEconomico}"    
            
        envio = api_post("economicosMovimentacoes", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

economicosMovimentacoes = economicosMovimentacoes()