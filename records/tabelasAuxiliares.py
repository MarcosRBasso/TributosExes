from samples import *
import json

class tabelasAuxiliares(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idTabelaAuxiliar, descricao, campos, desativadaConfigEconomico, inseridaConfigEconomico):
        try:
            sql = """
                INSERT INTO tabelasAuxiliares (                    
                    idIntegracao,                   
                    id_cloud, 
                    idTabelaAuxiliar,
                    descricao,                                               
                    campos, 
                    desativadaConfigEconomico,
                    inseridaConfigEconomico              
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idTabelaAuxiliar)s,
                    %(descricao)s,
                    %(campos)s,
                    %(desativadaConfigEconomico)s,
                    %(inseridaConfigEconomico)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idTabelaAuxiliar = idTabelaAuxiliar,
                descricao = descricao,
                campos = campos,                               
                desativadaConfigEconomico = desativadaConfigEconomico,
                inseridaConfigEconomico = inseridaConfigEconomico
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {tabelasAuxiliares} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {tabelasAuxiliares}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM tabelasAuxiliares"
            if not self.query(sql_s):
                send_log_warning(f"tabelasAuxiliares não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM tabelasAuxiliares WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM tabelasAuxiliares WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    tabelasAuxiliares 
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
            sql = f"SELECT * FROM tabelasAuxiliares WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM tabelasAuxiliares WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM tabelasAuxiliares WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idTabelaAuxiliar, descricao, campos, desativadaConfigEconomico, inseridaConfigEconomico):
        objeto = {
            "idIntegracao": f"tabelasAuxiliares{id}",
            "content": {}                                 
        }
        if idTabelaAuxiliar:
            objeto["content"]["idTabelaAuxiliar"] = { "id": int(idTabelaAuxiliar)}

        if descricao:
            objeto["content"]["descricao"] = f"{descricao}"        
       
        if desativadaConfigEconomico:
            objeto["content"]["desativadaConfigEconomico"] = f"{desativadaConfigEconomico}"       
       
        if inseridaConfigEconomico:
            objeto["content"]["inseridaConfigEconomico"] = f"{inseridaConfigEconomico}"             

        if campos != None:
            objeto[0]["content"]["campos"] = f"{campos}"    
            
        envio = api_post("tabelasAuxiliares", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

tabelasAuxiliares = tabelasAuxiliares()