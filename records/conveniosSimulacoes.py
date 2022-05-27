from samples import *
import json

class conveniosSimulacoes(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idConvenio, idSimulacao, valor, nroBaixa, nossoNumero, codigoBarras, linhaDigitavel, dtVencimento):
        try:
            sql = """
                INSERT INTO conveniosSimulacoes (                    
                    idIntegracao,                   
                    id_cloud, 
                    idConvenio,
                    idSimulacao,                                               
                    valor, 
                    nroBaixa,
                    nossoNumero,
                    linhaDigitavel,
                    dtVencimento                 
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idConvenio)s,
                    %(idSimulacao)s,
                    %(valor)s,
                    %(nroBaixa)s,
                    %(nossoNumero)s,
                    %(linhaDigitavel)s,
                    %(dtVencimento)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idConvenio = idConvenio,
                idSimulacao = idSimulacao,
                valor = valor,                               
                nroBaixa = nroBaixa,
                nossoNumero = nossoNumero,
                linhaDigitavel = linhaDigitavel,                               
                dtVencimento = dtVencimento,
                codigoBarras = codigoBarras
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {conveniosSimulacoes} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {conveniosSimulacoes}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM conveniosSimulacoes"
            if not self.query(sql_s):
                send_log_warning(f"conveniosSimulacoes não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM conveniosSimulacoes WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM conveniosSimulacoes WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    conveniosSimulacoes 
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
            sql = f"SELECT * FROM conveniosSimulacoes WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM conveniosSimulacoes WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM conveniosSimulacoes WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idConvenio, idSimulacao, valor, nroBaixa, nossoNumero, codigoBarras, linhaDigitavel, dtVencimento):
        objeto = {
            "idIntegracao": f"conveniosSimulacoes{id}",
            "content": {}                                 
        }
        if idConvenio:
            objeto["content"]["idConvenio"] = { "id": int(idConvenio)}
        
        if dtVencimento:
            objeto["content"]["dtVencimento"] = f"{dtVencimento}"

        if idSimulacao:
            objeto["content"]["idSimulacao"] = { "id": int(idSimulacao)}        
       
        if nroBaixa:
            objeto["content"]["nroBaixa"] = { "id": int(nroBaixa)}       
       
        if nossoNumero:
            objeto["content"]["nossoNumero"] = { "id": int(nossoNumero)}

        if linhaDigitavel:
            objeto["content"]["linhaDigitavel"] = f"{linhaDigitavel}"  
        
        if codigoBarras:
            objeto["content"]["codigoBarras"] = f"{codigoBarras}"              

        if valor != None:
            objeto[0]["content"]["valor"] = f"{valor}"    
            
        envio = api_post("conveniosSimulacoes", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

conveniosSimulacoes = conveniosSimulacoes()