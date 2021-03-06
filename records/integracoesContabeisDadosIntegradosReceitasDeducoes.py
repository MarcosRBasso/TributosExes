from samples import *
import json

class integracoesContabeisDadosIntegradosReceitasDeducoes(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idIntegracoesContabeisDadosIntegradosReceitas, tipoDevolucao, valor):
        try:
            sql = """
                INSERT INTO integracoesContabeisDadosIntegradosReceitasDeducoes (                    
                    idIntegracao,                   
                    id_cloud,                                                           
                    idIntegracoesContabeisDadosIntegradosReceitas, 
                    tipoDevolucao,
                    valor                                             
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,                                                            
                    %(idIntegracoesContabeisDadosIntegradosReceitas)s,
                    %(tipoDevolucao)s,
                    %(valor)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                                                               
                idIntegracoesContabeisDadosIntegradosReceitas = idIntegracoesContabeisDadosIntegradosReceitas,                               
                tipoDevolucao = tipoDevolucao,
                valor = valor
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {integracoesContabeisDadosIntegradosReceitasDeducoes} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {integracoesContabeisDadosIntegradosReceitasDeducoes}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM integracoesContabeisDadosIntegradosReceitasDeducoes"
            if not self.query(sql_s):
                send_log_warning(f"integracoesContabeisDadosIntegradosReceitasDeducoes n??o encontrado para excluir.")
                return
            sql_d = f"DELETE FROM integracoesContabeisDadosIntegradosReceitasDeducoes WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias exclu??dos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de exclus??o do atividades econ??micas. {error}")

    def db_update(self, id, id_cloud, json, descricao):
        try:
            sql_s = f"SELECT * FROM integracoesContabeisDadosIntegradosReceitasDeducoes WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} n??o encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    integracoesContabeisDadosIntegradosReceitasDeducoes 
                SET 
                    id_cloud = %(id_cloud)s,
                    json_post = %(json)s,
                    resposta_post = %(descricao)s
                WHERE
                    id = %(id)s
                """
            data = dict (
                id = id,
                id_cloud = id_cloud,
                json = json,
                descricao = descricao
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"atividades Economicas {id} atualizado com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de atualiza????o da atividades Economicas. {error}")

    def db_search(self, id):
        try:
            sql = f"SELECT * FROM integracoesContabeisDadosIntegradosReceitasDeducoes WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} n??o encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM integracoesContabeisDadosIntegradosReceitasDeducoes WHERE id_cloud is null"
            data = self.query(sql)
            if data:
                send_log_info("Consulta de todos os atividades Economicas realizada com sucesso.")
                return data
            return None
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de busca. {error}")

    def get_id_cloud(self, id):
        if (id == None):
            return None
        try:
            sql = f"SELECT id_cloud FROM integracoesContabeisDadosIntegradosReceitasDeducoes WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} n??o encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de busca. {error}")

    def send_post(self, id, idIntegracoesContabeisDadosIntegradosReceitas, tipoDevolucao, valor):
        objeto = {
            "idIntegracao": f"integracoesContabeisDadosIntegradosReceitasDeducoes{id}",
            "content": {}                                 
        }
        if valor != None:
            objeto[0]["content"]["valor"] = f"{valor}"  

        if tipoDevolucao != None:
            objeto[0]["content"]["tipoDevolucao"] = f"{tipoDevolucao}"    
               
        if idIntegracoesContabeisDadosIntegradosReceitas != None:
            objeto[0]["camposadicionais"]["idIntegracoesContabeisDadosIntegradosReceitas"] = { "id": int(idIntegracoesContabeisDadosIntegradosReceitas)}

        envio = api_post("integracoesContabeisDadosIntegradosReceitasDeducoes", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["descricao"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["descricao"], ensure_ascii=False))

integracoesContabeisDadosIntegradosReceitasDeducoes = integracoesContabeisDadosIntegradosReceitasDeducoes()