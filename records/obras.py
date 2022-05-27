from samples import *
import json

class obras(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idAgrupamentos, idSolicitantes, idImoveis, codigo, dataEntrada, descricao, nroProcesso, observacao, 
                  situacao, solicitanteProprietario, unidadeMedida, medida):
        try:
            sql = """
                INSERT INTO obras (                    
                    idIntegracao,                   
                    id_cloud, 
                    idAgrupamentos,
                    idSolicitantes,                                               
                    idImoveis, 
                    codigo,
                    dataEntrada,
                    nroProcesso,
                    observacao,
                    descricao,
                    situacao,                    
                    solicitanteProprietario,
                    unidadeMedida,
                    medida         
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idAgrupamentos)s,
                    %(idSolicitantes)s,
                    %(idImoveis)s,
                    %(codigo)s,
                    %(dataEntrada)s,
                    %(nroProcesso)s,
                    %(observacao)s,
                    %(descricao)s,
                    %(situacao)s,                    
                    %(solicitanteProprietario)s,
                    %(unidadeMedida)s,
                    %(medida)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idAgrupamentos = idAgrupamentos,
                idSolicitantes = idSolicitantes,
                idImoveis = idImoveis,                               
                codigo = codigo,
                dataEntrada = dataEntrada,
                nroProcesso = nroProcesso,                               
                observacao = observacao,
                descricao = descricao,
                situacao = situacao,                                               
                solicitanteProprietario = solicitanteProprietario,
                unidadeMedida = unidadeMedida,                               
                medida = medida
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {obras} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {obras}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM obras"
            if not self.query(sql_s):
                send_log_warning(f"obras não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM obras WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM obras WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    obras 
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
            sql = f"SELECT * FROM obras WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM obras WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM obras WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idAgrupamentos, idSolicitantes, idImoveis, codigo, dataEntrada, descricao, nroProcesso, observacao, 
                situacao, solicitanteProprietario, unidadeMedida, medida):
        objeto = {
            "idIntegracao": f"obras{id}",
            "content": {}                                 
        }
        if idAgrupamentos:
            objeto["content"]["idAgrupamentos"] = { "id": int(idAgrupamentos)}
        if observacao:
            objeto["content"]["observacao"] = f"{observacao}"

        if idSolicitantes:
            objeto["content"]["idSolicitantes"] = { "id": int(idSolicitantes)} 
        
        if codigo:
            objeto["content"]["codigo"] = f"{codigo}" 

        if unidadeMedida:
            objeto["content"]["unidadeMedida"] = f"{unidadeMedida}"  

        if dataEntrada:
            objeto["content"]["dataEntrada"] = f"{dataEntrada}"

        if nroProcesso:
            objeto["content"]["nroProcesso"] = f"{nroProcesso}"   

        if solicitanteProprietario:
            objeto["content"]["solicitanteProprietario"] = f"{solicitanteProprietario}"
        
        if situacao:
            objeto["content"]["situacao"] = f"{situacao}"
           
        if medida:
            objeto["content"]["medida"] = f"{medida}"
        
        if descricao:
            objeto["content"]["descricao"] = f"{descricao}"

        if idImoveis != None:
            objeto[0]["content"]["idImoveis"] = { "id": int(idImoveis) }  
            
        envio = api_post("obras", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

obras = obras()