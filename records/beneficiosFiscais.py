from samples import *
import json

class beneficiosFiscais(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, descricao, idAto, tipoBeneficio, fundamentacaoLegal, dtValidadeInicial, dtValidadeFinal):
        try:
            sql = """
                INSERT INTO beneficiosFiscais (                    
                    idIntegracao,                   
                    id_cloud,                                                           
                    descricao, 
                    idAto,
                    tipoBeneficio,
                    fundamentacaoLegal,
                    dtValidadeInicial,
                    dtValidadeFinal                                 
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,                                                            
                    %(descricao)s,
                    %(idAto)s,
                    %(tipoBeneficio)s,
                    %(fundamentacaoLegal)s,
                    %(dtValidadeFinal)s,
                    %(dtValidadeInicial)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                                                               
                descricao = descricao,                               
                idAto = idAto,
                tipoBeneficio = tipoBeneficio,
                fundamentacaoLegal = fundamentacaoLegal,
                dtValidadeFinal = dtValidadeFinal,                               
                dtValidadeInicial = dtValidadeInicial                
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {beneficiosFiscais} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {beneficiosFiscais}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM beneficiosFiscais"
            if not self.query(sql_s):
                send_log_warning(f"beneficiosFiscais n??o encontrado para excluir.")
                return
            sql_d = f"DELETE FROM beneficiosFiscais WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias exclu??dos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de exclus??o do atividades econ??micas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM beneficiosFiscais WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} n??o encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    beneficiosFiscais 
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
            sql = f"SELECT * FROM beneficiosFiscais WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} n??o encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM beneficiosFiscais WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM beneficiosFiscais WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} n??o encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de busca. {error}")

    def send_post(self, id, descricao,  idAto, tipoBeneficio, fundamentacaoLegal, dtValidadeInicial, dtValidadeFinal):
        objeto = {
            "idIntegracao": f"beneficiosFiscais{id}",
            "content": {}                                 
        }
        if tipoBeneficio:
            objeto["content"]["tipoBeneficio"] = f"{tipoBeneficio}"
        
        if descricao:
            objeto["content"]["descricao"] = f"{descricao}"

        if dtValidadeInicial:
            objeto["content"]["dtValidadeInicial"] = f"{dtValidadeInicial}"
           
        if fundamentacaoLegal:
            objeto["content"]["fundamentacaoLegal"] = f"{fundamentacaoLegal}"
        
        if dtValidadeFinal:
            objeto["content"]["dtValidadeFinal"] = f"{dtValidadeFinal}"
        
        if idAto != None:
            objeto[0]["content"]["idAto"] = { "id": int(idAto) }

        envio = api_post("beneficiosFiscais", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

beneficiosFiscais = beneficiosFiscais()