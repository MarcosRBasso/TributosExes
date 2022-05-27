from samples import *
import json

class atosFontesDivulgacoes(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, idAtos, idFontesDivulgacoesAtos, numeroPublicacao, id_cloud ):
        try:
            sql = """
                INSERT INTO atosFontesDivulgacoes (                   
                    idIntegracao,                    
                    idAtos,
                    id_cloud,
                    idFontesDivulgacoesAtos,
                    numeroPublicacao                                 
                ) VALUES (             
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(numeroPublicacao)s,
                    %(idFontesDivulgacoesAtos)s,
                    %(idAtos)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                            
                idAtos = idAtos,
                numeroPublicacao = numeroPublicacao,
                idFontesDivulgacoesAtos = idFontesDivulgacoesAtos
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {atosFontesDivulgacoes} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {atosFontesDivulgacoes}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM atos"
            if not self.query(sql_s):
                send_log_warning(f"atosFontesDivulgacoes não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM atosFontesDivulgacoes WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM atosFontesDivulgacoes WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    atosFontesDivulgacoes 
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
            sql = f"SELECT * FROM atosFontesDivulgacoes WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM atosFontesDivulgacoes WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM atosFontesDivulgacoes WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idAtos, idFontesDivulgacoesAtos, numeroPublicacao ):
        objeto = {
            "idIntegracao": f"atosFontesDivulgacoes{id}",
            "content": {}                                 
        }
        if numeroPublicacao:
            objeto["content"]["numeroPublicacao"] = f"{numeroPublicacao}"    

        if idAtos != None:
            objeto[0]["content"]["Atos"] = { "id": int(idAtos) }               

        if idFontesDivulgacoesAtos != None:
            objeto[0]["content"]["FontesDivulgacoesAtos"] = { "id": int(idFontesDivulgacoesAtos) }
        
        envio = api_post("atosFontesDivulgacoes", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

atosFontesDivulgacoes = atosFontesDivulgacoes()