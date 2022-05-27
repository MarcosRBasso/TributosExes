from samples import *
import json

class parcelamentosCompOrigem(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idParcelamentos, idParcelamentosAnt, idGuias, idDividas, idReceitas, valorReceita, valorCorrecao, valorJuro, 
                valorMulta, valorDescontoReceita, valorDescontoCorrecao, valorDescontoJuro, valorDescontoMulta, valorRemissaoReceita, valorAnistiaReceita, valorAnistiaCorrecao, 
                valorAnistiaJuro, valorAnistiaMulta):
        try:
            sql = """
                INSERT INTO parcelamentosCompOrigem (                    
                    idIntegracao,                   
                    id_cloud, 
                    idParcelamentos,
                    idParcelamentosAnt,                                               
                    idGuias, 
                    idDividas,
                    idReceitas,
                    valorCorrecao,
                    valorJuro,
                    valorReceita,
                    valorMulta,                    
                    valorDescontoReceita,
                    valorDescontoCorrecao,
                    valorDescontoJuro,
                    valorDescontoMulta,
                    valorRemissaoReceita,
                    valorAnistiaReceita, 
                    valorAnistiaCorrecao, 
                    valorAnistiaJuro, 
                    valorAnistiaMulta                
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idParcelamentos)s,
                    %(idParcelamentosAnt)s,
                    %(idGuias)s,
                    %(idDividas)s,
                    %(idReceitas)s,
                    %(valorCorrecao)s,
                    %(valorJuro)s,
                    %(valorReceita)s,
                    %(valorMulta)s,                    
                    %(valorDescontoReceita)s,
                    %(valorDescontoCorrecao)s,
                    %(valorDescontoJuro)s,
                    %(valorDescontoMulta)s,
                    %(valorRemissaoReceita)s,
                    %(valorAnistiaReceita)s, 
                    %(valorAnistiaCorrecao)s, 
                    %(valorAnistiaJuro)s, 
                    %(valorAnistiaMulta)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idParcelamentos = idParcelamentos,
                idParcelamentosAnt = idParcelamentosAnt,
                idGuias = idGuias,                               
                idDividas = idDividas,
                idReceitas = idReceitas,
                valorCorrecao = valorCorrecao,                               
                valorJuro = valorJuro,
                valorReceita = valorReceita,
                valorMulta = valorMulta,                                               
                valorDescontoReceita = valorDescontoReceita,
                valorDescontoCorrecao = valorDescontoCorrecao,                               
                valorDescontoJuro = valorDescontoJuro,
                valorDescontoMulta = valorDescontoMulta,
                valorRemissaoReceita = valorRemissaoReceita,
                valorAnistiaReceita = valorAnistiaReceita, 
                valorAnistiaCorrecao = valorAnistiaCorrecao, 
                valorAnistiaJuro = valorAnistiaJuro, 
                valorAnistiaMulta = valorAnistiaMulta
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {parcelamentosCompOrigem} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {parcelamentosCompOrigem}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM parcelamentosCompOrigem"
            if not self.query(sql_s):
                send_log_warning(f"parcelamentosCompOrigem não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM parcelamentosCompOrigem WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM parcelamentosCompOrigem WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    parcelamentosCompOrigem 
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
            sql = f"SELECT * FROM parcelamentosCompOrigem WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM parcelamentosCompOrigem WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM parcelamentosCompOrigem WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idParcelamentos, idParcelamentosAnt, idGuias, idDividas, idReceitas, valorReceita, valorCorrecao, valorJuro, 
                valorMulta, valorDescontoReceita, valorDescontoCorrecao, valorDescontoJuro, valorDescontoMulta, valorRemissaoReceita, valorAnistiaReceita, valorAnistiaCorrecao, valorAnistiaJuro, valorAnistiaMulta):
        objeto = {
            "idIntegracao": f"parcelamentosCompOrigem{id}",
            "content": {}                                 
        }
        if idParcelamentos:
            objeto["content"]["idParcelamentos"] = { "id": int(idParcelamentos)}

        if valorAnistiaReceita:
            objeto["content"]["valorAnistiaReceita"] = f"{valorAnistiaReceita}"   

        if valorAnistiaCorrecao:
            objeto["content"]["valorAnistiaCorrecao"] = f"{valorAnistiaCorrecao}"
        
        if valorAnistiaJuro:
            objeto["content"]["valorAnistiaJuro"] = f"{valorAnistiaJuro}"
           
        if valorAnistiaMulta:
            objeto["content"]["valorAnistiaMulta"] = f"{valorAnistiaMulta}"            
        
        if valorJuro:
            objeto["content"]["valorJuro"] = f"{valorJuro}"

        if idParcelamentosAnt:
            objeto["content"]["idParcelamentosAnt"] = { "id": int(idParcelamentosAnt)}           
        
        if idDividas:
            objeto["content"]["idDividas"] = { "id": int(idDividas)} 

        if valorDescontoCorrecao:
            objeto["content"]["valorDescontoCorrecao"] = f"{valorDescontoCorrecao}"  

        if idReceitas:
            objeto["content"]["idReceitas"] = { "id": int(idReceitas)}

        if valorCorrecao:
            objeto["content"]["valorCorrecao"] = f"{valorCorrecao}"   

        if valorDescontoReceita:
            objeto["content"]["valorDescontoReceita"] = f"{valorDescontoReceita}"
        
        if valorMulta:
            objeto["content"]["valorMulta"] = f"{valorMulta}"
           
        if valorDescontoJuro:
            objeto["content"]["valorDescontoJuro"] = f"{valorDescontoJuro}"
        
        if valorRemissaoReceita:
            objeto["content"]["valorRemissaoReceita"] = f"{valorRemissaoReceita}"
        
        if valorReceita:
            objeto["content"]["valorReceita"] = f"{valorReceita}"

        if idGuias != None:
            objeto[0]["content"]["idGuias"] = { "id": int(idGuias) }               

        if valorDescontoMulta != None:
            objeto[0]["content"]["valorDescontoMulta"] = f"{valorDescontoMulta}"        
            
        envio = api_post("parcelamentosCompOrigem", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

parcelamentosCompOrigem = parcelamentosCompOrigem()