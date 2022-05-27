from samples import *
import json

class guiasReceitas(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idGuias, idReceitasCreditos, valorLancado, valorDesconto, valorBeneficio, valorPago, percBeneficioCorrecao, percBeneficioJuros, 
                percBeneficioMulta, percBeneficioReceita):
        try:
            sql = """
                INSERT INTO guiasReceitas (                    
                    idIntegracao,                   
                    id_cloud, 
                    idGuias,
                    idReceitasCreditos,                                               
                    valorLancado, 
                    valorDesconto,
                    valorBeneficio,
                    percBeneficioCorrecao,
                    percBeneficioJuros,
                    valorPago,
                    percBeneficioMulta,                    
                    percBeneficioReceita             
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idGuias)s,
                    %(idReceitasCreditos)s,
                    %(valorLancado)s,
                    %(valorDesconto)s,
                    %(valorBeneficio)s,
                    %(percBeneficioCorrecao)s,
                    %(percBeneficioJuros)s,
                    %(valorPago)s,
                    %(percBeneficioMulta)s,                    
                    %(percBeneficioReceita)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idGuias = idGuias,
                idReceitasCreditos = idReceitasCreditos,
                valorLancado = valorLancado,                               
                valorDesconto = valorDesconto,
                valorBeneficio = valorBeneficio,
                percBeneficioCorrecao = percBeneficioCorrecao,                               
                percBeneficioJuros = percBeneficioJuros,
                valorPago = valorPago,
                percBeneficioMulta = percBeneficioMulta,                                               
                percBeneficioReceita = percBeneficioReceita
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {guiasReceitas} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {guiasReceitas}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM guiasReceitas"
            if not self.query(sql_s):
                send_log_warning(f"guiasReceitas não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM guiasReceitas WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM guiasReceitas WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    guiasReceitas 
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
            sql = f"SELECT * FROM guiasReceitas WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM guiasReceitas WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM guiasReceitas WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idGuias, idReceitasCreditos, valorLancado, valorDesconto, valorBeneficio, valorPago, percBeneficioCorrecao, percBeneficioJuros, 
                percBeneficioMulta, percBeneficioReceita):
        objeto = {
            "idIntegracao": f"guiasReceitas{id}",
            "content": {}                                 
        }
        if idGuias:
            objeto["content"]["idGuias"] = { "id": int(idGuias)}
        
        if percBeneficioJuros:
            objeto["content"]["percBeneficioJuros"] = f"{percBeneficioJuros}"

        if idReceitasCreditos:
            objeto["content"]["idReceitasCreditos"] = { "id": int(idReceitasCreditos)}
           
        if valorDesconto:
            objeto["content"]["valorDesconto"] = f"{valorDesconto}"
       
        if valorBeneficio:
            objeto["content"]["valorBeneficio"] = f"{valorBeneficio}"

        if percBeneficioCorrecao:
            objeto["content"]["percBeneficioCorrecao"] = f"{percBeneficioCorrecao}"   

        if percBeneficioReceita:
            objeto["content"]["percBeneficioReceita"] = f"{percBeneficioReceita}"
        
        if percBeneficioMulta:
            objeto["content"]["percBeneficioMulta"] = f"{percBeneficioMulta}"
        if valorPago:
            objeto["content"]["valorPago"] = f"{valorPago}"

        if valorLancado != None:
            objeto[0]["content"]["valorLancado"] = f"{valorLancado}"    
            
        envio = api_post("guiasReceitas", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

guiasReceitas = guiasReceitas()