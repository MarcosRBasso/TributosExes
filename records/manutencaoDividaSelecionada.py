from samples import *
import json

class manutencaoDividaSelecionada(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idDivida, idManutencaoDivida, idContribuinte, idCredito, idPagamento, anoCredito, valorPrestacaoDiversa):
        try:
            sql = """
                INSERT INTO manutencaoDividaSelecionada (                    
                    idIntegracao,                   
                    id_cloud, 
                    idDivida,
                    idManutencaoDivida,                                               
                    idContribuinte, 
                    idCredito,
                    idPagamento,
                    valorPrestacaoDiversa,
                    anoCredito                
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idDivida)s,
                    %(idManutencaoDivida)s,
                    %(idContribuinte)s,
                    %(idCredito)s,
                    %(idPagamento)s,
                    %(valorPrestacaoDiversa)s,
                    %(anoCredito)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idDivida = idDivida,
                idManutencaoDivida = idManutencaoDivida,
                idContribuinte = idContribuinte,                               
                idCredito = idCredito,
                idPagamento = idPagamento,
                valorPrestacaoDiversa = valorPrestacaoDiversa,
                anoCredito = anoCredito
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {manutencaoDividaSelecionada} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {manutencaoDividaSelecionada}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM manutencaoDividaSelecionada"
            if not self.query(sql_s):
                send_log_warning(f"manutencaoDividaSelecionada não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM manutencaoDividaSelecionada WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM manutencaoDividaSelecionada WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    manutencaoDividaSelecionada 
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
            sql = f"SELECT * FROM manutencaoDividaSelecionada WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM manutencaoDividaSelecionada WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM manutencaoDividaSelecionada WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idDivida, idManutencaoDivida, idContribuinte, idCredito, idPagamento, anoCredito, valorPrestacaoDiversa):
        objeto = {
            "idIntegracao": f"manutencaoDividaSelecionada{id}",
            "content": {}                                 
        }
        if idDivida:
            objeto["content"]["idDivida"] = { "id": int(idDivida)}

        if idManutencaoDivida:
            objeto["content"]["idManutencaoDivida"] = { "id": int(idManutencaoDivida)}        
       
        if idCredito:
            objeto["content"]["idCredito"] = { "id": int(idCredito)}       
       
        if idPagamento:
            objeto["content"]["idPagamento"] = { "id": int(idPagamento)}

        if valorPrestacaoDiversa:
            objeto["content"]["valorPrestacaoDiversa"] = f"{valorPrestacaoDiversa}"  
        
        if anoCredito:
            objeto["content"]["anoCredito"] = f"{anoCredito}"              

        if idContribuinte != None:
            objeto[0]["content"]["idContribuinte"] = { "id": int(idContribuinte)}   
            
        envio = api_post("manutencaoDividaSelecionada", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

manutencaoDividaSelecionada = manutencaoDividaSelecionada()