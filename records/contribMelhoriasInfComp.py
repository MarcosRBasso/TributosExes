from samples import *
import json

class contribMelhoriasInfComp(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, areaTexto, idCamposAdicionais, idContribuicoesMelhorias, dhCampo, texto, vlCampo):
        try:
            sql = """
                INSERT INTO contribMelhoriasInfComp (                    
                    idIntegracao,                   
                    id_cloud,                     
                    areaTexto,                                               
                    idCamposAdicionais, 
                    idContribuicoesMelhorias,
                    dhCampo,
                    texto,
                    vlCampo                                 
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,                                        
                    %(areaTexto)s,
                    %(idCamposAdicionais)s,
                    %(idContribuicoesMelhorias)s,
                    %(dhCampo)s,
                    %(texto)s,
                    %(vlCampo)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                                               
                areaTexto = areaTexto,
                idCamposAdicionais = idCamposAdicionais,                               
                idContribuicoesMelhorias = idContribuicoesMelhorias,
                dhCampo = dhCampo,
                texto = texto,                               
                vlCampo = vlCampo               
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {contribMelhoriasInfComp} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {contribMelhoriasInfComp}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM contribMelhoriasInfComp"
            if not self.query(sql_s):
                send_log_warning(f"contribMelhoriasInfComp n??o encontrado para excluir.")
                return
            sql_d = f"DELETE FROM contribMelhoriasInfComp WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias exclu??dos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de exclus??o do atividades econ??micas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM contribMelhoriasInfComp WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} n??o encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    contribMelhoriasInfComp 
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
            send_log_error(f"Erro ao executar a opera????o de atualiza????o da atividades Economicas. {error}")

    def db_search(self, id):
        try:
            sql = f"SELECT * FROM contribMelhoriasInfComp WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} n??o encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM contribMelhoriasInfComp WHERE id_cloud is null"
            data = self.query(sql)
            if data:
                send_log_info("Consulta de todos os atividades Economicas realizada com sucesso.")
                return data
            return None
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de busca. {error}")

    def get_id_cloud(self, id):
        if (id == None):
            return None
        try:
            sql = f"SELECT id_cloud FROM contribMelhoriasInfComp WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} n??o encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de busca. {error}")

    def send_post(self, id, areaTexto, idCamposAdicionais, idContribuicoesMelhorias, dhCampo, texto, vlCampo):
        objeto = {
            "idIntegracao": f"contribMelhoriasInfComp{id}",
            "content": {}                                 
        }
        if idContribuicoesMelhorias:
            objeto["content"]["idContribuicoesMelhorias"] =  { "id": int(idContribuicoesMelhorias)}
        
        if dhCampo:
            objeto["content"]["dhCampo"] =  f"{dhCampo}"

        if areaTexto:
            objeto["content"]["areaTexto"] =  f"{areaTexto}"
           
        if idCamposAdicionais:
            objeto["content"]["idCamposAdicionais"] =  { "id": int(idCamposAdicionais)}
        
        if vlCampo:
            objeto["content"]["vlCampo"] =  f"{vlCampo}"
        
        if texto:
            objeto["content"]["texto"] =  f"{texto}"
        envio = api_post("contribMelhoriasInfComp", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

contribMelhoriasInfComp = contribMelhoriasInfComp()