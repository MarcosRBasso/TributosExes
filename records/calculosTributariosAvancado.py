from samples import *
import json

class calculosTributariosAvancado(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idCalculo, idCampoAdicional, texto, vlCampo, dhCampo, operadorComparacao, operadorAcao):
        try:
            sql = """
                INSERT INTO calculosTributariosAvancado (                    
                    idIntegracao,                   
                    id_cloud,                                                           
                    idCalculo, 
                    idCampoAdicional,
                    texto,
                    vlCampo,
                    dhCampo,
                    operadorComparacao,
                    operadorAcao                          
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,                                                            
                    %(idCalculo)s,
                    %(idCampoAdicional)s,
                    %(texto)s,
                    %(vlCampo)s,
                    %(operadorComparacao)s,
                    %(dhCampo)s,
                    %(operadorAcao)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                                                               
                idCalculo = idCalculo,                               
                idCampoAdicional = idCampoAdicional,
                texto = texto,
                vlCampo = vlCampo,
                operadorComparacao = operadorComparacao,                               
                dhCampo = dhCampo,
                operadorAcao = operadorAcao            
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {calculosTributariosAvancado} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {calculosTributariosAvancado}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM calculosTributariosAvancado"
            if not self.query(sql_s):
                send_log_warning(f"calculosTributariosAvancado não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM calculosTributariosAvancado WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, dhCampo):
        try:
            sql_s = f"SELECT * FROM calculosTributariosAvancado WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    calculosTributariosAvancado 
                SET 
                    id_cloud = %(id_cloud)s,
                    json_post = %(json)s,
                    resposta_post = %(dhCampo)s
                WHERE
                    id = %(id)s
                """
            data = dict (
                id = id,
                id_cloud = id_cloud,
                json = json,
                dhCampo = dhCampo
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"atividades Economicas {id} atualizado com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de atualização da atividades Economicas. {error}")

    def db_search(self, id):
        try:
            sql = f"SELECT * FROM calculosTributariosAvancado WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM calculosTributariosAvancado WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM calculosTributariosAvancado WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, idCalculo, idCampoAdicional, texto, vlCampo, dhCampo, operadorComparacao, operadorAcao):
        objeto = {
            "idIntegracao": f"calculosTributariosAvancado{id}",
            "content": {}                                 
        }
        if texto:
            objeto["content"]["texto"] = f"{texto}"
        
        if dhCampo:
            objeto["content"]["dhCampo"] = f"{dhCampo}"

        if vlCampo:
            objeto["content"]["vlCampo"] = f"{vlCampo}"
           
        if operadorAcao:
            objeto["content"]["operadorAcao"] = f"{operadorAcao}"
        
        if operadorComparacao:
            objeto["content"]["operadorComparacao"] = f"{operadorComparacao}"

        if idCampoAdicional != None:
            objeto[0]["content"]["idCampoAdicional"] = { "id": int(idCampoAdicional) }    
               
        if idCalculo != None:
            objeto[0]["camposadicionais"]["Calculo"] = { "id": int(idCalculo) }
        
        envio = api_post("calculosTributariosAvancado", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["dhCampo"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["dhCampo"], ensure_ascii=False))

calculosTributariosAvancado = calculosTributariosAvancado()