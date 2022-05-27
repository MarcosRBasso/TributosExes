from samples import *
import json

class condominiosInfComplem(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idCamposAdicionais, idCamposAdicionaisFilho, idCondominio, dhCampo, texto, vlCampo, areaTexto, ano):
        try:
            sql = """
                INSERT INTO condominiosInfComplem (                    
                    idIntegracao,                   
                    id_cloud, 
                    idCamposAdicionais,
                    idCamposAdicionaisFilho,                                               
                    idCondominio, 
                    dhCampo,
                    texto,
                    areaTexto,
                    vlCampo,
                    ano                
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idCamposAdicionais)s,
                    %(idCamposAdicionaisFilho)s,
                    %(idCondominio)s,
                    %(dhCampo)s,
                    %(texto)s,
                    %(areaTexto)s,
                    %(vlCampo)s,
                    %(ano)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idCamposAdicionais = idCamposAdicionais,
                idCamposAdicionaisFilho = idCamposAdicionaisFilho,
                idCondominio = idCondominio,                               
                dhCampo = dhCampo,
                texto = texto,
                areaTexto = areaTexto,
                vlCampo = vlCampo,
                ano = ano
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {condominiosInfComplem} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {condominiosInfComplem}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM condominiosInfComplem"
            if not self.query(sql_s):
                send_log_warning(f"condominiosInfComplem não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM condominiosInfComplem WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM condominiosInfComplem WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    condominiosInfComplem 
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
            sql = f"SELECT * FROM condominiosInfComplem WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM condominiosInfComplem WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM condominiosInfComplem WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idCamposAdicionais, idCamposAdicionaisFilho, idCondominio, dhCampo, texto, vlCampo, areaTexto, ano):
        objeto = {
            "idIntegracao": f"condominiosInfComplem{id}",
            "content": {}                                 
        }
        if idCamposAdicionais:
            objeto["content"]["idCamposAdicionais"] = { "id": int(idCamposAdicionais)}

        if idCamposAdicionaisFilho:
            objeto["content"]["idCamposAdicionaisFilho"] = { "id": int(idCamposAdicionaisFilho)}  

        if ano:
            objeto["content"]["ano"] = { "id": int(ano)}           
       
        if dhCampo:
            objeto["content"]["dhCampo"] = f"{dhCampo}"       
       
        if texto:
            objeto["content"]["texto"] = f"{texto}"

        if areaTexto:
            objeto["content"]["areaTexto"] = f"{areaTexto}"  
        
        if vlCampo:
            objeto["content"]["vlCampo"] = f"{vlCampo}"              

        if idCondominio != None:
            objeto[0]["content"]["idCondominio"] = { "id": int(idCondominio)}    
            
        envio = api_post("condominiosInfComplem", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

condominiosInfComplem = condominiosInfComplem()