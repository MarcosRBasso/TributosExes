from samples import *
import json

class plantasValores(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idBairros, idDistritos, idFaces, idIndexadores, idLogradouros, idSecoes, idAtos, ano, vlMetroQuadrado):
        try:
            sql = """
                INSERT INTO plantasValores (                    
                    idIntegracao,                   
                    id_cloud, 
                    idBairros,
                    idDistritos,                                               
                    idFaces, 
                    idIndexadores,
                    idLogradouros,
                    idAtos,
                    idSecoes, 
                    ano, 
                    vlMetroQuadrado                
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idBairros)s,
                    %(idDistritos)s,
                    %(idFaces)s,
                    %(idIndexadores)s,
                    %(idLogradouros)s,
                    %(idAtos)s,
                    %(idSecoes)s,
                    %(ano)s,
                    %(vlMetroQuadrado)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idBairros = idBairros,
                idDistritos = idDistritos,
                idFaces = idFaces,                               
                idIndexadores = idIndexadores,
                idLogradouros = idLogradouros,
                idAtos = idAtos,
                idSecoes = idSecoes,
                ano = ano,
                vlMetroQuadrado = vlMetroQuadrado

            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {plantasValores} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {plantasValores}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM plantasValores"
            if not self.query(sql_s):
                send_log_warning(f"plantasValores não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM plantasValores WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM plantasValores WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    plantasValores 
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
            sql = f"SELECT * FROM plantasValores WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM plantasValores WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM plantasValores WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idBairros, idDistritos, idFaces, idIndexadores, idLogradouros, idSecoes, idAtos, ano, vlMetroQuadrado):
        objeto = {
            "idIntegracao": f"plantasValores{id}",
            "content": {}                                 
        }
        if ano:
            objeto["content"]["ano"] = f"{ano}"

        if vlMetroQuadrado:
            objeto["content"]["vlMetroQuadrado"] = f"{vlMetroQuadrado}"        

        if idBairros:
            objeto["content"]["idBairros"] = { "id": int(idBairros)}

        if idDistritos:
            objeto["content"]["idDistritos"] = { "id": int(idDistritos)}        
       
        if idIndexadores:
            objeto["content"]["idIndexadores"] = { "id": int(idIndexadores)}       
       
        if idLogradouros:
            objeto["content"]["idLogradouros"] = { "id": int(idLogradouros)}

        if idAtos:
            objeto["content"]["idAtos"] = { "id": int(idAtos)}  
        
        if idSecoes:
            objeto["content"]["idSecoes"] = { "id": int(idSecoes)}              

        if idFaces != None:
            objeto[0]["content"]["idFaces"] = { "id": int(idFaces)}    
            
        envio = api_post("plantasValores", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

plantasValores = plantasValores()