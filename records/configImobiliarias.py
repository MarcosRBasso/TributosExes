from samples import *
import json

class configImobiliarias(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, descricaoUnidade, controleSecoes, inscricaoDuplicada, inscricaoIncraDuplicada, usarCampoUnidade):
        try:
            sql = """
                INSERT INTO configImobiliarias (                    
                    idIntegracao,                   
                    id_cloud,                     
                    descricaoUnidade,                                               
                    controleSecoes, 
                    inscricaoDuplicada,
                    inscricaoIncraDuplicada,
                    usarCampoUnidade,                          
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,                                        
                    %(descricaoUnidade)s,
                    %(controleSecoes)s,
                    %(inscricaoDuplicada)s,
                    %(inscricaoIncraDuplicada)s,
                    %(usarCampoUnidade)s,
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                                               
                descricaoUnidade = descricaoUnidade,
                controleSecoes = controleSecoes,                               
                inscricaoDuplicada = inscricaoDuplicada,
                inscricaoIncraDuplicada = inscricaoIncraDuplicada,
                usarCampoUnidade = usarCampoUnidade,           
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {configImobiliarias} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {configImobiliarias}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM configImobiliarias"
            if not self.query(sql_s):
                send_log_warning(f"configImobiliarias n??o encontrado para excluir.")
                return
            sql_d = f"DELETE FROM configImobiliarias WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias exclu??dos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de exclus??o do atividades econ??micas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM configImobiliarias WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} n??o encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    configImobiliarias 
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
            send_log_error(f"Erro ao executar a opera????o de atualiza????o da atividades Economicas. {error}")

    def db_search(self, id):
        try:
            sql = f"SELECT * FROM configImobiliarias WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} n??o encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM configImobiliarias WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM configImobiliarias WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} n??o encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de busca. {error}")

    def send_post(self, id, descricaoUnidade, controleSecoes, inscricaoDuplicada, inscricaoIncraDuplicada, usarCampoUnidade):
        objeto = {
            "idIntegracao": f"configImobiliarias{id}",
            "content": {}                                 
        }
        if inscricaoDuplicada:
            objeto["content"]["inscricaoDuplicada"] =  { "id": int(inscricaoDuplicada)}
        
        if inscricaoIncraDuplicada:
            objeto["content"]["inscricaoIncraDuplicada"] =  { "id": int(inscricaoIncraDuplicada)}

        if descricaoUnidade:
            objeto["content"]["descricaoUnidade"] =  { "id": int(descricaoUnidade)}
           
        if controleSecoes:
            objeto["content"]["controleSecoes"] =  { "id": int(controleSecoes)}
            
        if usarCampoUnidade:
            objeto["content"]["usarCampoUnidade"] =  { "id": int(usarCampoUnidade)}
        envio = api_post("configImobiliarias", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

configImobiliarias = configImobiliarias()