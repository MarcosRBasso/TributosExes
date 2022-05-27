from samples import *
import json

class atos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, cpfResponsavel, dtCriacao, dtPublicacao, dtResolucao, dtVigorar, 
                   ementa, idNaturezasTextoJurAtos, idTiposAtos, nmResponsavel, nroDiarioOficial, nroOficial, nroProcesso, nroResolucao, id_cloud ):
        try:
            sql = """
                INSERT INTO atos (
                    idIntegracao,                    
                    cpfResponsavel,
                    id_cloud,
                    dtCriacao,
                    dtPublicacao,
                    dtResolucao,
                    dtVigorar,
                    ementa,
                    idNaturezasTextoJurAtos,
                    idTiposAtos,
                    nmResponsavel,
                    nroDiarioOficial,
                    nroOficial,
                    nroProcesso                    
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idCamposAdicionais)s,
                    %(dtPublicacao)s,
                    %(dtResolucao)s,
                    %(dtVigorar)s,
                    %(ementa)s,
                    %(idNaturezasTextoJurAtos)s,
                    %(idTiposAtos)s,
                    %(nmResponsavel)s,  
                    %(nroDiarioOficial)s,
                    %(nroOficial)s,
                    %(nroProcesso)s,
                    %(nroResolucao)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                
                cpfResponsavel = cpfResponsavel,
                dtCriacao = dtCriacao,
                dtPublicacao = dtPublicacao,
                dtResolucao = dtResolucao,
                dtVigorar = dtVigorar,
                ementa = ementa,
                idNaturezasTextoJurAtos = idNaturezasTextoJurAtos,
                idTiposAtos = idTiposAtos, 
                nmResponsavel = nmResponsavel,
                nroDiarioOficial = nroDiarioOficial,
                nroOficial = nroOficial,  
                nroProcesso = nroProcesso,
                nroResolucao = nroResolucao
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {atos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {atos}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM atos"
            if not self.query(sql_s):
                send_log_warning(f"anistias não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM atos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM atos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    atos 
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
            sql = f"SELECT * FROM atos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM atos WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM atos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atos {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, cpfResponsavel, dtCriacao, dtPublicacao, dtResolucao, dtVigorar, 
                   ementa, idNaturezasTextoJurAtos, idTiposAtos, nmResponsavel, nroDiarioOficial, nroOficial, nroProcesso, nroResolucao ):
        objeto = {
            "idIntegracao": f"atos{id}",
            "content": {}                                 
        }

        if cpfResponsavel:
            objeto["content"]["cpfResponsavel"] = f"{cpfResponsavel}"
        
        if dtCriacao:
            objeto["content"]["dtCriacao"] = f"{dtCriacao}"
        
        if dtPublicacao:
            objeto["content"]["dtPublicacao"] = f"{dtPublicacao}"
        
        if dtResolucao:
            objeto["content"]["dtResolucao"] = f"{dtResolucao}"
        
        if dtVigorar:
            objeto["content"]["dtVigorar"] = f"{dtVigorar}" 

        if ementa:
            objeto["content"]["ementa"] = f"{ementa}"    

        if idTiposAtos != None:
            objeto[0]["content"]["TiposAtos"] = { "id": int(idTiposAtos) }               

        if idNaturezasTextoJurAtos != None:
            objeto[0]["content"]["NaturezasTextoJurAtos"] = { "id": int(idNaturezasTextoJurAtos) }

        if nmResponsavel:
            objeto["content"]["nmResponsavel"] = f"{nmResponsavel}"
        
        if nroDiarioOficial:
            objeto["content"]["nroDiarioOficial"] = f"{nroDiarioOficial}"
        
        if nroProcesso:
            objeto["content"]["nroProcesso"] = f"{nroProcesso}" 

        if nroResolucao:
            objeto["content"]["nroResolucao"] = f"{nroResolucao}"   

        if nroOficial:
            objeto["content"]["nroOficial"] = f"{nroOficial}" 
        envio = api_post("atos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

atos = atos()