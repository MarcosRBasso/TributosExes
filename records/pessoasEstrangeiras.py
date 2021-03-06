from samples import *
import json

class pessoasEstrangeiras(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idPessoas, dtChegada, dtExpedicao, dtValidade, nroIdentidade, orgaoEmissor, tipoVisto):
        try:
            sql = """
                INSERT INTO pessoasEstrangeiras (                    
                    idIntegracao,                   
                    id_cloud, 
                    idPessoas,
                    dtChegada,                                               
                    dtExpedicao, 
                    dtValidade,
                    nroIdentidade,
                    tipoVisto,
                    orgaoEmissor                
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idPessoas)s,
                    %(dtChegada)s,
                    %(dtExpedicao)s,
                    %(dtValidade)s,
                    %(nroIdentidade)s,
                    %(tipoVisto)s,
                    %(orgaoEmissor)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idPessoas = idPessoas,
                dtChegada = dtChegada,
                dtExpedicao = dtExpedicao,                               
                dtValidade = dtValidade,
                nroIdentidade = nroIdentidade,
                tipoVisto = tipoVisto,
                orgaoEmissor = orgaoEmissor
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {pessoasEstrangeiras} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {pessoasEstrangeiras}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM pessoasEstrangeiras"
            if not self.query(sql_s):
                send_log_warning(f"pessoasEstrangeiras n??o encontrado para excluir.")
                return
            sql_d = f"DELETE FROM pessoasEstrangeiras WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias exclu??dos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de exclus??o do atividades econ??micas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM pessoasEstrangeiras WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} n??o encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    pessoasEstrangeiras 
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
            sql = f"SELECT * FROM pessoasEstrangeiras WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} n??o encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM pessoasEstrangeiras WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM pessoasEstrangeiras WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} n??o encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de busca. {error}")

    def send_post(self, id, idPessoas, dtChegada, dtExpedicao, dtValidade, nroIdentidade, orgaoEmissor, tipoVisto):
        objeto = {
            "idIntegracao": f"pessoasEstrangeiras{id}",
            "content": {}                                 
        }
        if idPessoas:
            objeto["content"]["idPessoas"] = { "id": int(idPessoas)}

        if dtChegada:
            objeto["content"]["dtChegada"] = f"{dtChegada}"        
       
        if dtValidade:
            objeto["content"]["dtValidade"] = f"{dtValidade}"       
       
        if nroIdentidade:
            objeto["content"]["nroIdentidade"] = f"{nroIdentidade}"

        if tipoVisto:
            objeto["content"]["tipoVisto"] = f"{tipoVisto}"  
        
        if orgaoEmissor:
            objeto["content"]["orgaoEmissor"] = f"{orgaoEmissor}"              

        if dtExpedicao != None:
            objeto[0]["content"]["dtExpedicao"] = f"{dtExpedicao}"    
            
        envio = api_post("pessoasEstrangeiras", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

pessoasEstrangeiras = pessoasEstrangeiras()