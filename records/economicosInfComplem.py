from samples import *
import json

class economicosInfComplem(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idAgrupamentos, idCamposAdicionais, areaTexto, idCamposAdicionaisFilho, dhCampo, dtBase, texto,vlCampo, idEconomico):
        try:
            sql = """
                INSERT INTO economicosInfComplem (                    
                    idIntegracao,                   
                    id_cloud, 
                    idAgrupamentos,
                    idCamposAdicionais,                                               
                    areaTexto, 
                    idCamposAdicionaisFilho,
                    dhCampo,
                    texto,
                    dtBase,
                    vlCampo, 
                    idEconomico                
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idAgrupamentos)s,
                    %(idCamposAdicionais)s,
                    %(areaTexto)s,
                    %(idCamposAdicionaisFilho)s,
                    %(dhCampo)s,
                    %(texto)s,
                    %(dtBase)s,
                    %(vlCampo)s, 
                    %(idEconomico)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idAgrupamentos = idAgrupamentos,
                idCamposAdicionais = idCamposAdicionais,
                areaTexto = areaTexto,                               
                idCamposAdicionaisFilho = idCamposAdicionaisFilho,
                dhCampo = dhCampo,
                texto = texto,
                dtBase = dtBase,
                vlCampo = vlCampo, 
                idEconomico = idEconomico
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {economicosInfComplem} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {economicosInfComplem}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM economicosInfComplem"
            if not self.query(sql_s):
                send_log_warning(f"economicosInfComplem não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM economicosInfComplem WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM economicosInfComplem WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    economicosInfComplem 
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
            sql = f"SELECT * FROM economicosInfComplem WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM economicosInfComplem WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM economicosInfComplem WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idAgrupamentos, idCamposAdicionais, areaTexto, idCamposAdicionaisFilho, dhCampo, dtBase, texto, vlCampo, idEconomico):
        objeto = {
            "idIntegracao": f"economicosInfComplem{id}",
            "content": {}                                 
        }
        if idEconomico:
            objeto["content"]["idEconomico"] = { "id": int(idEconomico)}

        if idAgrupamentos:
            objeto["content"]["idAgrupamentos"] = { "id": int(idAgrupamentos)}

        if idCamposAdicionais:
            objeto["content"]["idCamposAdicionais"] = { "id": int(idCamposAdicionais)}        
       
        if idCamposAdicionaisFilho:
            objeto["content"]["idCamposAdicionaisFilho"] = { "id": int(idCamposAdicionaisFilho)}       
       
        if vlCampo:
            objeto["content"]["vlCampo"] = f"{vlCampo}"

        if dhCampo:
            objeto["content"]["dhCampo"] = f"{dhCampo}"    

        if texto:
            objeto["content"]["texto"] = f"{texto}"  
        
        if dtBase:
            objeto["content"]["dtBase"] = f"{dtBase}"              

        if areaTexto != None:
            objeto[0]["content"]["areaTexto"] = f"{areaTexto}"    
            
        envio = api_post("economicosInfComplem", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

economicosInfComplem = economicosInfComplem()