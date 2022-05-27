from samples import *
import json

class guiasReceitasManutencoes(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idGuiasReceitas, idManutencaoRevogacao, idManutencoesCalculos, percCorrecao, percIncentivo, percIsencao, percJuros, percMulta, 
                percRemissao, valorIncentivo, valorIsencao, valorRemissao, tipoSolicitacao):
        try:
            sql = """
                INSERT INTO guiasReceitasManutencoes (                    
                    idIntegracao,                   
                    id_cloud, 
                    idGuiasReceitas,
                    idManutencaoRevogacao,                                               
                    idManutencoesCalculos, 
                    percCorrecao,
                    percIncentivo,
                    percJuros,
                    percMulta,
                    percIsencao,
                    percRemissao,                    
                    valorIncentivo,
                    valorIsencao,
                    valorRemissao,
                    tipoSolicitacao                
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idGuiasReceitas)s,
                    %(idManutencaoRevogacao)s,
                    %(idManutencoesCalculos)s,
                    %(percCorrecao)s,
                    %(percIncentivo)s,
                    %(percJuros)s,
                    %(percMulta)s,
                    %(percIsencao)s,
                    %(percRemissao)s,                    
                    %(valorIncentivo)s,
                    %(valorIsencao)s,
                    %(valorRemissao)s,
                    %(tipoSolicitacao)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idGuiasReceitas = idGuiasReceitas,
                idManutencaoRevogacao = idManutencaoRevogacao,
                idManutencoesCalculos = idManutencoesCalculos,                               
                percCorrecao = percCorrecao,
                percIncentivo = percIncentivo,
                percJuros = percJuros,                               
                percMulta = percMulta,
                percIsencao = percIsencao,
                percRemissao = percRemissao,                                               
                valorIncentivo = valorIncentivo,
                valorIsencao = valorIsencao,                               
                valorRemissao = valorRemissao,
                tipoSolicitacao = tipoSolicitacao
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {guiasReceitasManutencoes} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {guiasReceitasManutencoes}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM guiasReceitasManutencoes"
            if not self.query(sql_s):
                send_log_warning(f"guiasReceitasManutencoes não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM guiasReceitasManutencoes WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM guiasReceitasManutencoes WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    guiasReceitasManutencoes 
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
            sql = f"SELECT * FROM guiasReceitasManutencoes WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM guiasReceitasManutencoes WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM guiasReceitasManutencoes WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idGuiasReceitas, idManutencaoRevogacao, idManutencoesCalculos, percCorrecao, percIncentivo, percIsencao, percJuros, percMulta, 
                percRemissao, valorIncentivo, valorIsencao, valorRemissao, tipoSolicitacao):
        objeto = {
            "idIntegracao": f"guiasReceitasManutencoes{id}",
            "content": {}                                 
        }
        if idGuiasReceitas:
            objeto["content"]["idGuiasReceitas"] = { "id": int(idGuiasReceitas)}
        
        if percMulta:
            objeto["content"]["percMulta"] = f"{percMulta}"

        if idManutencaoRevogacao:
            objeto["content"]["idManutencaoRevogacao"] = { "id": int(idManutencaoRevogacao)}
        
        if percCorrecao:
            objeto["content"]["percCorrecao"] = f"{percCorrecao}" 

        if valorIsencao:
            objeto["content"]["valorIsencao"] = f"{valorIsencao}"  
       
        if percIncentivo:
            objeto["content"]["percIncentivo"] = f"{percIncentivo}"

        if percJuros:
            objeto["content"]["percJuros"] = f"{percJuros}"   

        if valorIncentivo:
            objeto["content"]["valorIncentivo"] = f"{valorIncentivo}"
        
        if percRemissao:
            objeto["content"]["percRemissao"] = f"{percRemissao}"
           
        if valorRemissao:
            objeto["content"]["valorRemissao"] = f"{valorRemissao}"

        if percIsencao:
            objeto["content"]["percIsencao"] = f"{percIsencao}"

        if idManutencoesCalculos != None:
            objeto[0]["content"]["idManutencoesCalculos"] = { "id": int(idManutencoesCalculos) }               

        if tipoSolicitacao != None:
            objeto[0]["content"]["tipoSolicitacao"] = f"{tipoSolicitacao}"        
            
        envio = api_post("guiasReceitasManutencoes", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

guiasReceitasManutencoes = guiasReceitasManutencoes()