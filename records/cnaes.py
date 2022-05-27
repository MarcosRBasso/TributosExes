from samples import *
import json

class cnaes(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, nivel, ordem, descricao, cnae, secao, grauRisco, visivel, impeditivoSimples, 
                grauRiscoMei):
        try:
            sql = """
                INSERT INTO cnaes (                    
                    idIntegracao,                   
                    id_cloud, 
                    nivel,
                    ordem,                                               
                    descricao, 
                    cnae,
                    secao,
                    visivel,
                    impeditivoSimples,
                    grauRisco,
                    grauRiscoMei     
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(nivel)s,
                    %(ordem)s,
                    %(descricao)s,
                    %(cnae)s,
                    %(secao)s,
                    %(visivel)s,
                    %(impeditivoSimples)s,
                    %(grauRisco)s,
                    %(grauRiscoMei)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                nivel = nivel,
                ordem = ordem,
                descricao = descricao,                               
                cnae = cnae,
                secao = secao,
                visivel = visivel,                               
                impeditivoSimples = impeditivoSimples,
                grauRisco = grauRisco, 
                grauRiscoMei = grauRiscoMei
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {cnaes} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {cnaes}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM cnaes"
            if not self.query(sql_s):
                send_log_warning(f"cnaes não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM cnaes WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM cnaes WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    cnaes 
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
            sql = f"SELECT * FROM cnaes WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM cnaes WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM cnaes WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, nivel, ordem, descricao, cnae, secao, grauRisco, visivel, impeditivoSimples, 
                grauRiscoMei):
        objeto = {
            "idIntegracao": f"cnaes{id}",
            "content": {}                                 
        }
        if nivel:
            objeto["content"]["nivel"] = { "id": int(nivel)}          
        
        if impeditivoSimples:
            objeto["content"]["impeditivoSimples"] = f"{impeditivoSimples}"

        if ordem:
            objeto["content"]["ordem"] = { "id": int(ordem)}           
        
        if cnae:
            objeto["content"]["cnae"] = f"{cnae}" 

        if secao:
            objeto["content"]["secao"] = f"{secao}"

        if visivel:
            objeto["content"]["visivel"] = f"{visivel}"   
        
        if grauRiscoMei:
            objeto["content"]["grauRiscoMei"] = f"{grauRiscoMei}"
        
        if grauRisco:
            objeto["content"]["grauRisco"] = f"{grauRisco}"

        if descricao != None:
            objeto[0]["content"]["descricao"] = f"{descricao}"       
            
        envio = api_post("cnaes", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

cnaes = cnaes()