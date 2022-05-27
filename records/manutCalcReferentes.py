from samples import *
import json

class manutCalcReferentes(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idManutencoesCalculos, idLancamentos, idImoveis, idPessoas, idContribuicoes, idReceitasDiversas, idReceitasDiversasLanctos,
                    idEconomicos, 
                idTransferenciaImoveis, idNotasAvulsas, idObras, descricao):
        try:
            sql = """
                INSERT INTO manutCalcReferentes (                    
                    idIntegracao,                   
                    id_cloud, 
                    idManutencoesCalculos,
                    idLancamentos,                                               
                    idImoveis, 
                    idPessoas,
                    idContribuicoes,
                    idReceitasDiversasLanctos,
                    idEconomicos,
                    idReceitasDiversas,
                    idTransferenciaImoveis,                    
                    idNotasAvulsas,
                    descricao,
                    idObras
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idManutencoesCalculos)s,
                    %(idLancamentos)s,
                    %(idImoveis)s,
                    %(idPessoas)s,
                    %(idContribuicoes)s,
                    %(idReceitasDiversasLanctos)s,
                    %(idEconomicos)s,
                    %(idReceitasDiversas)s,
                    %(idTransferenciaImoveis)s,                    
                    %(idNotasAvulsas)s,
                    %(descricao)s,
                    %(idObras)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idManutencoesCalculos = idManutencoesCalculos,
                idLancamentos = idLancamentos,
                idImoveis = idImoveis,                               
                idPessoas = idPessoas,
                idContribuicoes = idContribuicoes,
                idReceitasDiversasLanctos = idReceitasDiversasLanctos,                               
                idEconomicos = idEconomicos,
                idReceitasDiversas = idReceitasDiversas,
                idTransferenciaImoveis = idTransferenciaImoveis,                                               
                idNotasAvulsas = idNotasAvulsas,
                descricao = descricao,                               
                idObras = idObras
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {manutCalcReferentes} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {manutCalcReferentes}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM manutCalcReferentes"
            if not self.query(sql_s):
                send_log_warning(f"manutCalcReferentes não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM manutCalcReferentes WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM manutCalcReferentes WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    manutCalcReferentes 
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
            sql = f"SELECT * FROM manutCalcReferentes WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM manutCalcReferentes WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM manutCalcReferentes WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idManutencoesCalculos, idLancamentos, idImoveis, idPessoas, idContribuicoes, idReceitasDiversas, idReceitasDiversasLanctos, idEconomicos, 
                idTransferenciaImoveis, idNotasAvulsas, idObras, descricao):
        objeto = {
            "idIntegracao": f"manutCalcReferentes{id}",
            "content": {}                                 
        }
        if idManutencoesCalculos:
            objeto["content"]["idManutencoesCalculos"] = { "id": int(idManutencoesCalculos)}
        
        if idEconomicos:
            objeto["content"]["idEconomicos"] = { "id": int(idEconomicos)}

        if idLancamentos:
            objeto["content"]["idLancamentos"] = { "id": int(idLancamentos)}
        
        if idPessoas:
            objeto["content"]["idPessoas"] = { "id": int(idPessoas)} 

        if descricao:
            objeto["content"]["descricao"] = f"{descricao}"      
       
        if idContribuicoes:
            objeto["content"]["idContribuicoes"] = { "id": int(idContribuicoes)}

        if idReceitasDiversasLanctos:
            objeto["content"]["idReceitasDiversasLanctos"] = { "id": int(idReceitasDiversasLanctos)}   

        if idNotasAvulsas:
            objeto["content"]["idNotasAvulsas"] = { "id": int(idNotasAvulsas)}
        
        if idTransferenciaImoveis:
            objeto["content"]["idTransferenciaImoveis"] = { "id": int(idTransferenciaImoveis)}
           
        if idObras:
            objeto["content"]["idObras"] = { "id": int(idObras)}

        if idReceitasDiversas:
            objeto["content"]["idReceitasDiversas"] = { "id": int(idReceitasDiversas)}

        if idImoveis != None:
            objeto[0]["content"]["idImoveis"] = { "id": int(idImoveis) }               

        envio = api_post("manutCalcReferentes", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

manutCalcReferentes = manutCalcReferentes()