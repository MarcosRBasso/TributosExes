from samples import *
import json

class secoesInfComplem(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, ano, idCamposAdicionais, idCamposAdicionaisFilho, dhCampo, areaTexto, idSecao, texto, vlCampo):
        try:
            sql = """
                INSERT INTO secoesInfComplem (                    
                    idIntegracao,                   
                    id_cloud, 
                    ano,
                    idCamposAdicionais,                                               
                    idCamposAdicionaisFilho, 
                    dhCampo,
                    areaTexto,
                    texto,
                    idSecao,
                    vlCampo                
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(ano)s,
                    %(idCamposAdicionais)s,
                    %(idCamposAdicionaisFilho)s,
                    %(dhCampo)s,
                    %(areaTexto)s,
                    %(texto)s,
                    %(idSecao)s,
                    %(vlCampo)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                ano = ano,
                idCamposAdicionais = idCamposAdicionais,
                idCamposAdicionaisFilho = idCamposAdicionaisFilho,                               
                dhCampo = dhCampo,
                areaTexto = areaTexto,
                texto = texto,
                idSecao = idSecao,
                vlCampo = vlCampo
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {secoesInfComplem} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {secoesInfComplem}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM secoesInfComplem"
            if not self.query(sql_s):
                send_log_warning(f"secoesInfComplem não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM secoesInfComplem WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM secoesInfComplem WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    secoesInfComplem 
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
            sql = f"SELECT * FROM secoesInfComplem WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM secoesInfComplem WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM secoesInfComplem WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, ano, idCamposAdicionais, idCamposAdicionaisFilho, dhCampo, areaTexto, idSecao, texto, vlCampo):
        objeto = {
            "idIntegracao": f"secoesInfComplem{id}",
            "content": {}                                 
        }
        if ano:
            objeto["content"]["ano"] = { "id": int(ano)}

        if idCamposAdicionais:
            objeto["content"]["idCamposAdicionais"] = { "id": int(idCamposAdicionais)}        
       
        if dhCampo:
            objeto["content"]["dhCampo"] = f"{dhCampo}"      

        if dhCampo:
            objeto["content"]["dhCampo"] = f"{dhCampo}"       
       
        if vlCampo:
            objeto["content"]["vlCampo"] = f"{vlCampo}"

        if texto:
            objeto["content"]["texto"] = f"{texto}"  
        
        if idSecao:
            objeto["content"]["idSecao"] = { "id": int(idSecao)}              

        if idCamposAdicionaisFilho != None:
            objeto[0]["content"]["idCamposAdicionaisFilho"] = { "id": int(idCamposAdicionaisFilho)}    
            
        envio = api_post("secoesInfComplem", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

secoesInfComplem = secoesInfComplem()