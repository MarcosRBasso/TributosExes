from samples import *
import json

class transfImoveisItensProcessos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idTransfImoveisItens, nroProcesso, comentario):
        try:
            sql = """
                INSERT INTO transfImoveisItensProcessos (                    
                    idIntegracao,                   
                    id_cloud, 
                    idTransfImoveisItens,
                    nroProcesso,                                               
                    comentario             
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idTransfImoveisItens)s,
                    %(nroProcesso)s,
                    %(comentario)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idTransfImoveisItens = idTransfImoveisItens,
                nroProcesso = nroProcesso,
                comentario = comentario
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {transfImoveisItensProcessos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {transfImoveisItensProcessos}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM transfImoveisItensProcessos"
            if not self.query(sql_s):
                send_log_warning(f"transfImoveisItensProcessos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM transfImoveisItensProcessos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM transfImoveisItensProcessos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    transfImoveisItensProcessos 
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
            sql = f"SELECT * FROM transfImoveisItensProcessos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM transfImoveisItensProcessos WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM transfImoveisItensProcessos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idTransfImoveisItens, nroProcesso, comentario):
        objeto = {
            "idIntegracao": f"transfImoveisItensProcessos{id}",
            "content": {}                                 
        }
        if idTransfImoveisItens:
            objeto["content"]["idTransfImoveisItens"] = { "id": int(idTransfImoveisItens)}

        if nroProcesso:
            objeto["content"]["nroProcesso"] = { "id": int(nroProcesso)}                  

        if comentario != None:
            objeto[0]["content"]["comentario"] = f"{comentario}"    
            
        envio = api_post("transfImoveisItensProcessos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

transfImoveisItensProcessos = transfImoveisItensProcessos()