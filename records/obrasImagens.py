from samples import *
import json

class obrasImagens(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idObra, descricao, nomeArquivo, tipoArquivo, s3Key, s3KeyThumbnail, principal):
        try:
            sql = """
                INSERT INTO obrasImagens (                    
                    idIntegracao,                   
                    id_cloud, 
                    idObra,
                    descricao,                                               
                    nomeArquivo, 
                    tipoArquivo,
                    s3Key,
                    principal,
                    s3KeyThumbnail                
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idObra)s,
                    %(descricao)s,
                    %(nomeArquivo)s,
                    %(tipoArquivo)s,
                    %(s3Key)s,
                    %(principal)s,
                    %(s3KeyThumbnail)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idObra = idObra,
                descricao = descricao,
                nomeArquivo = nomeArquivo,                               
                tipoArquivo = tipoArquivo,
                s3Key = s3Key,
                principal = principal,
                s3KeyThumbnail = s3KeyThumbnail
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {obrasImagens} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {obrasImagens}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM obrasImagens"
            if not self.query(sql_s):
                send_log_warning(f"obrasImagens não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM obrasImagens WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM obrasImagens WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    obrasImagens 
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
            sql = f"SELECT * FROM obrasImagens WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM obrasImagens WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM obrasImagens WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idObra, descricao, nomeArquivo, tipoArquivo, s3Key, s3KeyThumbnail, principal):
        objeto = {
            "idIntegracao": f"obrasImagens{id}",
            "content": {}                                 
        }
        if idObra:
            objeto["content"]["idObra"] = { "id": int(idObra)}

        if descricao:
            objeto["content"]["descricao"] = f"{descricao}"        
       
        if tipoArquivo:
            objeto["content"]["tipoArquivo"] = f"{tipoArquivo}"       
       
        if s3Key:
            objeto["content"]["s3Key"] = f"{s3Key}"

        if principal:
            objeto["content"]["principal"] = f"{principal}"  
        
        if s3KeyThumbnail:
            objeto["content"]["s3KeyThumbnail"] = f"{s3KeyThumbnail}"              

        if nomeArquivo != None:
            objeto[0]["content"]["nomeArquivo"] = f"{nomeArquivo}"    
            
        envio = api_post("obrasImagens", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

obrasImagens = obrasImagens()