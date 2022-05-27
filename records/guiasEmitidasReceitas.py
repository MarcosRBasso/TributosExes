from samples import *
import json

class guiasEmitidasReceitas(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idReceita, classificacaoReceita, idGuiaEmitida, valorOriginal, valorDevido, valorDesconto, valorBeneficio, valorCorrecao, 
                valorRemidoCorrecao, valorJuro, valorRemidoJuro, valorMulta, valorRemidoMulta, valorDescontoCorrecao, valorDescontoJuros, valorDescontoMulta):
        try:
            sql = """
                INSERT INTO guiasEmitidasReceitas (                    
                    idIntegracao,                   
                    id_cloud, 
                    idReceita,
                    classificacaoReceita,                                               
                    idGuiaEmitida, 
                    valorOriginal,
                    valorDevido,
                    valorBeneficio,
                    valorCorrecao,
                    valorDesconto,
                    valorRemidoCorrecao,                    
                    valorJuro,
                    valorMulta,
                    valorRemidoJuro,
                    valorRemidoMulta,
                    valorDescontoCorrecao,
                    valorDescontoJuros,
                    valorDescontoMulta                
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idReceita)s,
                    %(classificacaoReceita)s,
                    %(idGuiaEmitida)s,
                    %(valorOriginal)s,
                    %(valorDevido)s,
                    %(valorBeneficio)s,
                    %(valorCorrecao)s,
                    %(valorDesconto)s,
                    %(valorRemidoCorrecao)s,                    
                    %(valorJuro)s,
                    %(valorMulta)s,
                    %(valorRemidoJuro)s,
                    %(valorRemidoMulta)s,
                    %(valorDescontoCorrecao)s,
                    %(valorDescontoJuros)s,
                    %(valorDescontoMulta)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idReceita = idReceita,
                classificacaoReceita = classificacaoReceita,
                idGuiaEmitida = idGuiaEmitida,                               
                valorOriginal = valorOriginal,
                valorDevido = valorDevido,
                valorBeneficio = valorBeneficio,                               
                valorCorrecao = valorCorrecao,
                valorDesconto = valorDesconto,
                valorRemidoCorrecao = valorRemidoCorrecao,                                               
                valorJuro = valorJuro,
                valorMulta = valorMulta,                               
                valorRemidoJuro = valorRemidoJuro,
                valorRemidoMulta = valorRemidoMulta,
                valorDescontoCorrecao = valorDescontoCorrecao,                               
                valorDescontoJuros = valorDescontoJuros,
                valorDescontoMulta = valorDescontoMulta
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {guiasEmitidasReceitas} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {guiasEmitidasReceitas}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM guiasEmitidasReceitas"
            if not self.query(sql_s):
                send_log_warning(f"guiasEmitidasReceitas não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM guiasEmitidasReceitas WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM guiasEmitidasReceitas WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    guiasEmitidasReceitas 
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
            sql = f"SELECT * FROM guiasEmitidasReceitas WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM guiasEmitidasReceitas WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM guiasEmitidasReceitas WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idReceita, classificacaoReceita, idGuiaEmitida, valorOriginal, valorDevido, valorDesconto, valorBeneficio, valorCorrecao, 
                valorRemidoCorrecao, valorJuro, valorRemidoJuro, valorMulta, valorRemidoMulta, valorDescontoCorrecao, valorDescontoJuros, valorDescontoMulta):
        objeto = {
            "idIntegracao": f"guiasEmitidasReceitas{id}",
            "content": {}                                 
        }
        if idReceita:
            objeto["content"]["idReceita"] = { "id": int(idReceita)}
        
        if valorCorrecao:
            objeto["content"]["valorCorrecao"] = f"{valorCorrecao}"

        if classificacaoReceita:
            objeto["content"]["classificacaoReceita"] = f"{classificacaoReceita}"
        
        if valorOriginal:
            objeto["content"]["valorOriginal"] = f"{valorOriginal}" 

        if valorMulta:
            objeto["content"]["valorMulta"] = f"{valorMulta}"  

        if valorDescontoJuros:
            objeto["content"]["valorDescontoJuros"] = f"{valorDescontoJuros}"       
       
        if valorDevido:
            objeto["content"]["valorDevido"] = f"{valorDevido}"

        if valorBeneficio:
            objeto["content"]["valorBeneficio"] = f"{valorBeneficio}"   

        if valorJuro:
            objeto["content"]["valorJuro"] = f"{valorJuro}"
        
        if valorRemidoCorrecao:
            objeto["content"]["valorRemidoCorrecao"] = f"{valorRemidoCorrecao}"
           
        if valorRemidoJuro:
            objeto["content"]["valorRemidoJuro"] = f"{valorRemidoJuro}"
        
        if valorDescontoCorrecao:
            objeto["content"]["valorDescontoCorrecao"] = f"{valorDescontoCorrecao}"

        if valorDesconto:
            objeto["content"]["valorDesconto"] = f"{valorDesconto}"

        if idGuiaEmitida != None:
            objeto[0]["content"]["idGuiaEmitida"] = { "id": int(idGuiaEmitida) }               

        if valorRemidoMulta != None:
            objeto[0]["content"]["valorRemidoMulta"] = f"{valorRemidoMulta}"

        if valorDescontoMulta != None:
            objeto[0]["content"]["valorDescontoMulta"] = f"{valorDescontoMulta}"
            
        envio = api_post("guiasEmitidasReceitas", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

guiasEmitidasReceitas = guiasEmitidasReceitas()