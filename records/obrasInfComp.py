from samples import *
import json

class obrasInfComp(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idObras, idAgrupamentos, idCamposAdicionais, idCamposAdicionaisFilho, ano, vlCampo, texto, areaTexto, dhCampo):
        try:
            sql = """
                INSERT INTO obrasInfComp (                    
                    idIntegracao,                   
                    id_cloud, 
                    idObras,
                    idAgrupamentos,                                               
                    idCamposAdicionais, 
                    idCamposAdicionaisFilho,
                    ano,
                    texto,
                    vlCampo,
                    areaTexto,
                    dhCampo                
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idObras)s,
                    %(idAgrupamentos)s,
                    %(idCamposAdicionais)s,
                    %(idCamposAdicionaisFilho)s,
                    %(ano)s,
                    %(texto)s,
                    %(vlCampo)s,
                    %(areaTexto)s,
                    %(dhCampo)s    
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idObras = idObras,
                idAgrupamentos = idAgrupamentos,
                idCamposAdicionais = idCamposAdicionais,                               
                idCamposAdicionaisFilho = idCamposAdicionaisFilho,
                ano = ano,
                texto = texto,
                vlCampo = vlCampo,
                areaTexto = areaTexto,
                dhCampo = dhCampo    
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {obrasInfComp} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {obrasInfComp}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM obrasInfComp"
            if not self.query(sql_s):
                send_log_warning(f"obrasInfComp não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM obrasInfComp WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM obrasInfComp WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    obrasInfComp 
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
            sql = f"SELECT * FROM obrasInfComp WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM obrasInfComp WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM obrasInfComp WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idObras, idAgrupamentos, idCamposAdicionais, idCamposAdicionaisFilho, ano, vlCampo, texto, areaTexto, dhCampo):
        objeto = {
            "idIntegracao": f"obrasInfComp{id}",
            "content": {}                                 
        }
        if idObras:
            objeto["content"]["idObras"] = { "id": int(idObras)}

        if idAgrupamentos:
            objeto["content"]["idAgrupamentos"] = { "id": int(idAgrupamentos)}        
       
        if idCamposAdicionaisFilho:
            objeto["content"]["idCamposAdicionaisFilho"] = { "id": int(idCamposAdicionaisFilho)}

        if areaTexto:
            objeto["content"]["areaTexto"] = f"{areaTexto}"

        if dhCampo:
            objeto["content"]["dhCampo"] = f"{dhCampo}"           
       
        if ano:
            objeto["content"]["ano"] = f"{ano}"

        if texto:
            objeto["content"]["texto"] = f"{texto}"  
        
        if vlCampo:
            objeto["content"]["vlCampo"] = f"{vlCampo}"              

        if idCamposAdicionais != None:
            objeto[0]["content"]["idCamposAdicionais"] = { "id": int(idCamposAdicionais)}    
            
        envio = api_post("obrasInfComp", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

obrasInfComp = obrasInfComp()