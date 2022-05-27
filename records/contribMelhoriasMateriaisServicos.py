from samples import *
import json

class contribMelhoriasMateriaisServicos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idContribuicoesMelhorias, idMateriaisServicos, quantidade, idUnidadesMedidas, valorUnitario, valorTotal):
        try:
            sql = """
                INSERT INTO contribMelhoriasMateriaisServicos (                    
                    idIntegracao,                   
                    id_cloud,                     
                    idContribuicoesMelhorias,                                               
                    idMateriaisServicos, 
                    quantidade,
                    idUnidadesMedidas,
                    valorUnitario,
                    valorTotal                                
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,                                        
                    %(idContribuicoesMelhorias)s,
                    %(idMateriaisServicos)s,
                    %(quantidade)s,
                    %(idUnidadesMedidas)s,
                    %(valorUnitario)s,
                    %(valorTotal)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                                               
                idContribuicoesMelhorias = idContribuicoesMelhorias,
                idMateriaisServicos = idMateriaisServicos,                               
                quantidade = quantidade,
                idUnidadesMedidas = idUnidadesMedidas,
                valorUnitario = valorUnitario,                               
                valorTotal = valorTotal               
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {contribMelhoriasMateriaisServicos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {contribMelhoriasMateriaisServicos}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM contribMelhoriasMateriaisServicos"
            if not self.query(sql_s):
                send_log_warning(f"contribMelhoriasMateriaisServicos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM contribMelhoriasMateriaisServicos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM contribMelhoriasMateriaisServicos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    contribMelhoriasMateriaisServicos 
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
            sql = f"SELECT * FROM contribMelhoriasMateriaisServicos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM contribMelhoriasMateriaisServicos WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM contribMelhoriasMateriaisServicos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idContribuicoesMelhorias, idMateriaisServicos, quantidade, idUnidadesMedidas, valorUnitario, valorTotal):
        objeto = {
            "idIntegracao": f"contribMelhoriasMateriaisServicos{id}",
            "content": {}                                 
        }
        if quantidade:
            objeto["content"]["quantidade"] =  { "id": int(quantidade)}
        
        if idUnidadesMedidas:
            objeto["content"]["idUnidadesMedidas"] =  { "id": int(idUnidadesMedidas)}

        if idContribuicoesMelhorias:
            objeto["content"]["idContribuicoesMelhorias"] =  { "id": int(idContribuicoesMelhorias)}
           
        if idMateriaisServicos:
            objeto["content"]["idMateriaisServicos"] =  { "id": int(idMateriaisServicos)}
        
        if valorTotal:
            objeto["content"]["valorTotal"] =  f"{valorTotal}"
        
        if valorUnitario:
            objeto["content"]["valorUnitario"] =  f"{valorUnitario}"
        envio = api_post("contribMelhoriasMateriaisServicos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

contribMelhoriasMateriaisServicos = contribMelhoriasMateriaisServicos()