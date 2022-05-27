from samples import *
import json

class obrasResponsaveisTecnicos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idEngenheirosArquitetos, idObras, nroDocumento, observacao, responsabilidade, tipoDocumento):
        try:
            sql = """
                INSERT INTO obrasResponsaveisTecnicos (                    
                    idIntegracao,                   
                    id_cloud, 
                    idEngenheirosArquitetos,
                    idObras,                                               
                    nroDocumento, 
                    observacao,
                    responsabilidade,
                    tipoDocumento                
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idEngenheirosArquitetos)s,
                    %(idObras)s,
                    %(nroDocumento)s,
                    %(observacao)s,
                    %(responsabilidade)s,
                    %(tipoDocumento)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idEngenheirosArquitetos = idEngenheirosArquitetos,
                idObras = idObras,
                nroDocumento = nroDocumento,                               
                observacao = observacao,
                responsabilidade = responsabilidade,
                tipoDocumento = tipoDocumento
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {obrasResponsaveisTecnicos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {obrasResponsaveisTecnicos}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM obrasResponsaveisTecnicos"
            if not self.query(sql_s):
                send_log_warning(f"obrasResponsaveisTecnicos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM obrasResponsaveisTecnicos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM obrasResponsaveisTecnicos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    obrasResponsaveisTecnicos 
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
            sql = f"SELECT * FROM obrasResponsaveisTecnicos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM obrasResponsaveisTecnicos WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM obrasResponsaveisTecnicos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idEngenheirosArquitetos, idObras, nroDocumento, observacao, responsabilidade, tipoDocumento):
        objeto = {
            "idIntegracao": f"obrasResponsaveisTecnicos{id}",
            "content": {}                                 
        }
        if idEngenheirosArquitetos:
            objeto["content"]["idEngenheirosArquitetos"] = { "id": int(idEngenheirosArquitetos)}

        if idObras:
            objeto["content"]["idObras"] = { "id": int(idObras)}        
       
        if observacao:
            objeto["content"]["observacao"] = f"{observacao}"       
       
        if responsabilidade:
            objeto["content"]["responsabilidade"] = f"{responsabilidade}"
        
        if tipoDocumento:
            objeto["content"]["tipoDocumento"] = f"{tipoDocumento}"              

        if nroDocumento != None:
            objeto[0]["content"]["nroDocumento"] = f"{nroDocumento}"    
            
        envio = api_post("obrasResponsaveisTecnicos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

obrasResponsaveisTecnicos = obrasResponsaveisTecnicos()