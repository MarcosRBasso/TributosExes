from samples import *
import json

class restituicoes(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idSaldo, idReceita, idPagamentosDetalhados, vlSaldo, vlRestituir, vlJuro, vlCorrecao):
        try:
            sql = """
                INSERT INTO restituicoes (                    
                    idIntegracao,                   
                    id_cloud, 
                    idSaldo,
                    idReceita,                                               
                    idPagamentosDetalhados, 
                    vlSaldo,
                    vlRestituir,
                    vlCorrecao,
                    vlJuro                
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idSaldo)s,
                    %(idReceita)s,
                    %(idPagamentosDetalhados)s,
                    %(vlSaldo)s,
                    %(vlRestituir)s,
                    %(vlCorrecao)s,
                    %(vlJuro)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idSaldo = idSaldo,
                idReceita = idReceita,
                idPagamentosDetalhados = idPagamentosDetalhados,                               
                vlSaldo = vlSaldo,
                vlRestituir = vlRestituir,
                vlCorrecao = vlCorrecao,
                vlJuro = vlJuro
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {restituicoes} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {restituicoes}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM restituicoes"
            if not self.query(sql_s):
                send_log_warning(f"restituicoes não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM restituicoes WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM restituicoes WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    restituicoes 
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
            sql = f"SELECT * FROM restituicoes WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM restituicoes WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM restituicoes WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idSaldo, idReceita, idPagamentosDetalhados, vlSaldo, vlRestituir, vlJuro, vlCorrecao):
        objeto = {
            "idIntegracao": f"restituicoes{id}",
            "content": {}                                 
        }
        if idSaldo:
            objeto["content"]["idSaldo"] = { "id": int(idSaldo)}

        if idReceita:
            objeto["content"]["idReceita"] = { "id": int(idReceita)}        
       
        if vlSaldo:
            objeto["content"]["vlSaldo"] = f"{vlSaldo}"       
       
        if vlRestituir:
            objeto["content"]["vlRestituir"] = f"{vlRestituir}"

        if vlCorrecao:
            objeto["content"]["vlCorrecao"] = f"{vlCorrecao}"  
        
        if vlJuro:
            objeto["content"]["vlJuro"] = f"{vlJuro}"              

        if idPagamentosDetalhados != None:
            objeto[0]["content"]["idPagamentosDetalhados"] = { "id": int(idPagamentosDetalhados)}    
            
        envio = api_post("restituicoes", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

restituicoes = restituicoes()