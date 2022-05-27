from samples import *
import json

class atividadesEconomicasInfComplem(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, areaTexto, idCamposAdicionais, id_cloud, idAtividadesEconomicas, 
                  iInformacoesComplementares, dhCampo, dtBase, texto, vlCampo):
        try:
            sql = """
                INSERT INTO atividadesEconomicasInfComplem (                    
                    idIntegracao,
                    areaTexto,
                    idCamposAdicionais,
                    id_cloud,
                    idAtividadesEconomicas,
                    iInformacoesComplementares,
                    dhCampo, 
                    dtBase,
                    texto,
                    vlCampo
                ) VALUES (
                    %(idIntegracao)s,
                    %(areaTexto)s,
                    %(id_cloud)s,
                    %(idCamposAdicionais)s,
                    %(idListaServicos)s,
                    %(idAtividadesEconomicas)s,
                    %(iInformacoesComplementares)s,
                    %(dhCampo)s,
                    %(dtBase)s,
                    %(texto)s,
                    %(vlCampo)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                areaTexto = areaTexto,
                id_cloud = id_cloud,
                idCamposAdicionais = idCamposAdicionais,
                idAtividadesEconomicas = idAtividadesEconomicas,
                iInformacoesComplementares = iInformacoesComplementares,
                dhCampo = dhCampo,
                dtBase = dtBase, 
                texto = texto,
                vlCampo = vlCampo            
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {atividadesEconomicasInfComplem} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {atividadesEconomicasInfComplem}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM atividadesEconomicasInfComplem"
            if not self.query(sql_s):
                send_log_warning(f"anistias não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM atividadesEconomicasInfComplem WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM atividadesEconomicasInfComplem WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    atividadesEconomicasInfComplem 
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
            sql = f"SELECT * FROM atividadesEconomicasInfComplem WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM atividadesEconomicasInfComplem WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM atividadesEconomicasInfComplem WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, areaTexto, idCamposAdicionais, idAtividadesEconomicas, 
                  iInformacoesComplementares, dhCampo, dtBase, texto, vlCampo):
        objeto = {
            "idIntegracao": f"atividadesEconomicasInfComplem{id}",
            "content": {}                                 
        }

        if areaTexto:
            objeto["content"]["areaTexto"] = f"{areaTexto}"

        if iInformacoesComplementares:
            objeto["content"]["InformacoesComplementares"] = f"{iInformacoesComplementares}"
        
        if dtBase:
            objeto["content"]["dtBase"] = f"{dtBase}"      
      
        if idCamposAdicionais != None:
            objeto[0]["content"]["CamposAdicionais"] = { "id": int(idCamposAdicionais) }               

        if idAtividadesEconomicas != None:
            objeto[0]["content"]["AtividadesEconomicas"] = { "id": int(idAtividadesEconomicas) }                  
        
        if dhCampo:
            objeto["content"]["dhCampo"] = f"{dhCampo}"
        
        if texto:
            objeto["content"]["texto"] = f"{texto}"
            
        if vlCampo != None:
            objeto[0]["content"]["vlCampo"] = f"{vlCampo}"   

        envio = api_post("atividadesEconomicasInfComplem", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

atividadesEconomicasInfComplem = atividadesEconomicasInfComplem()