from samples import *
import json

class obrasAnexos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idObra, descricao, nomeArquivo, tipoArquivo, s3Key):
        try:
            sql = """
                INSERT INTO obrasAnexos (                    
                    idIntegracao,                   
                    id_cloud, 
                    idObra,
                    descricao,                                               
                    nomeArquivo, 
                    tipoArquivo,
                    s3Key               
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idObra)s,
                    %(descricao)s,
                    %(nomeArquivo)s,
                    %(tipoArquivo)s,
                    %(s3Key)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idObra = idObra,
                descricao = descricao,
                nomeArquivo = nomeArquivo,                               
                tipoArquivo = tipoArquivo,
                s3Key = s3Key
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {obrasAnexos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {obrasAnexos}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM obrasAnexos"
            if not self.query(sql_s):
                send_log_warning(f"obrasAnexos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM obrasAnexos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM obrasAnexos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    obrasAnexos 
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
            sql = f"SELECT * FROM obrasAnexos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM obrasAnexos WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM obrasAnexos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idObra, descricao, nomeArquivo, tipoArquivo, s3Key):
        objeto = {
            "idIntegracao": f"obrasAnexos{id}",
            "content": {}                                 
        }
        if idObra:
            objeto["content"]["idObra"] = { "id": int(idObra)}

        if s3Key:
            objeto["content"]["s3Key"] = f"{s3Key}"      

        if descricao:
            objeto["content"]["descricao"] = f"{descricao}"        
       
        if tipoArquivo:
            objeto["content"]["tipoArquivo"] = f"{tipoArquivo}"                

        if nomeArquivo != None:
            objeto[0]["content"]["nomeArquivo"] = f"{nomeArquivo}"    
            
        envio = api_post("obrasAnexos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

obrasAnexos = obrasAnexos()