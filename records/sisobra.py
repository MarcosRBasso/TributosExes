from samples import *
import json

class sisobra(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idObra, area, areaCoberta, areaDescoberta, tipoArea, tipoAreaComplementar, categoria, destinacao, 
                tipoObra):
        try:
            sql = """
                INSERT INTO sisobra (                    
                    idIntegracao,                   
                    id_cloud, 
                    idObra,
                    area,                                               
                    areaCoberta, 
                    areaDescoberta,
                    tipoArea,
                    categoria,
                    destinacao,
                    tipoAreaComplementar,
                    tipoObra
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idObra)s,
                    %(area)s,
                    %(areaCoberta)s,
                    %(areaDescoberta)s,
                    %(tipoArea)s,
                    %(categoria)s,
                    %(destinacao)s,
                    %(tipoAreaComplementar)s,
                    %(tipoObra)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idObra = idObra,
                area = area,
                areaCoberta = areaCoberta,                               
                areaDescoberta = areaDescoberta,
                tipoArea = tipoArea,
                categoria = categoria,                               
                destinacao = destinacao,
                tipoAreaComplementar = tipoAreaComplementar,
                tipoObra = tipoObra
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {sisobra} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {sisobra}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM sisobra"
            if not self.query(sql_s):
                send_log_warning(f"sisobra não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM sisobra WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM sisobra WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    sisobra 
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
            sql = f"SELECT * FROM sisobra WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM sisobra WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM sisobra WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idObra, area, areaCoberta, areaDescoberta, tipoArea, tipoAreaComplementar, categoria, destinacao, 
                tipoObra):
        objeto = {
            "idIntegracao": f"sisobra{id}",
            "content": {}                                 
        }
        if idObra:
            objeto["content"]["idObra"] = { "id": int(idObra)}          
        
        if destinacao:
            objeto["content"]["destinacao"] = f"{destinacao}"

        if area:
            objeto["content"]["area"] = f"{area}"           
        
        if areaDescoberta:
            objeto["content"]["areaDescoberta"] = f"{areaDescoberta}" 

        if tipoArea:
            objeto["content"]["tipoArea"] = f"{tipoArea}"

        if categoria:
            objeto["content"]["categoria"] = f"{categoria}"   
        
        if tipoObra:
            objeto["content"]["tipoObra"] = f"{tipoObra}"
        
        if tipoAreaComplementar:
            objeto["content"]["tipoAreaComplementar"] = f"{tipoAreaComplementar}"

        if areaCoberta != None:
            objeto[0]["content"]["areaCoberta"] = f"{areaCoberta}"               
            
        envio = api_post("sisobra", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

sisobra = sisobra()