from samples import *
import json

class irrfAliquotas(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idIrrf, aliquota, valorDeducao, valorBaseFinal, valorBaseInicial, baseInicial, baseFinal):
        try:
            sql = """
                INSERT INTO irrfAliquotas (                    
                    idIntegracao,                   
                    id_cloud, 
                    idIrrf,
                    aliquota,                                               
                    valorDeducao, 
                    valorBaseFinal,
                    valorBaseInicial,
                    baseFinal,
                    baseInicial                
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idIrrf)s,
                    %(aliquota)s,
                    %(valorDeducao)s,
                    %(valorBaseFinal)s,
                    %(valorBaseInicial)s,
                    %(baseFinal)s,
                    %(baseInicial)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idIrrf = idIrrf,
                aliquota = aliquota,
                valorDeducao = valorDeducao,                               
                valorBaseFinal = valorBaseFinal,
                valorBaseInicial = valorBaseInicial,
                baseFinal = baseFinal,
                baseInicial = baseInicial
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {irrfAliquotas} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {irrfAliquotas}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM irrfAliquotas"
            if not self.query(sql_s):
                send_log_warning(f"irrfAliquotas não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM irrfAliquotas WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM irrfAliquotas WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    irrfAliquotas 
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
            sql = f"SELECT * FROM irrfAliquotas WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM irrfAliquotas WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM irrfAliquotas WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idIrrf, aliquota, valorDeducao, valorBaseFinal, valorBaseInicial, baseInicial, baseFinal):
        objeto = {
            "idIntegracao": f"irrfAliquotas{id}",
            "content": {}                                 
        }
        if idIrrf:
            objeto["content"]["idIrrf"] = { "id": int(idIrrf)}

        if aliquota:
            objeto["content"]["aliquota"] = { "id": int(aliquota)}        
       
        if valorBaseFinal:
            objeto["content"]["valorBaseFinal"] = f"{valorBaseFinal}"       
       
        if valorBaseInicial:
            objeto["content"]["valorBaseInicial"] = f"{valorBaseInicial}"

        if baseFinal:
            objeto["content"]["baseFinal"] = f"{baseFinal}"  
        
        if baseInicial:
            objeto["content"]["baseInicial"] = f"{baseInicial}"              

        if valorDeducao != None:
            objeto[0]["content"]["valorDeducao"] = f"{valorDeducao}"    
            
        envio = api_post("irrfAliquotas", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

irrfAliquotas = irrfAliquotas()