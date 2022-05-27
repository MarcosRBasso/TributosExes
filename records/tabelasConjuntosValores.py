from samples import *
import json

class tabelasConjuntosValores(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idTabelasCalculos, idTabelasConjuntos, idCamposAdicionais, idTabelasConjuntosCampos, valor, operadorAcao, operadorComparacao):
        try:
            sql = """
                INSERT INTO tabelasConjuntosValores (                    
                    idIntegracao,                   
                    id_cloud, 
                    idTabelasCalculos,
                    idTabelasConjuntos,                                               
                    idCamposAdicionais, 
                    idTabelasConjuntosCampos,
                    valor,
                    operadorComparacao      
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idTabelasCalculos)s,
                    %(idTabelasConjuntos)s,
                    %(idCamposAdicionais)s,
                    %(idTabelasConjuntosCampos)s,
                    %(valor)s,
                    %(operadorComparacao)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idTabelasCalculos = idTabelasCalculos,
                idTabelasConjuntos = idTabelasConjuntos,
                idCamposAdicionais = idCamposAdicionais,                               
                idTabelasConjuntosCampos = idTabelasConjuntosCampos,
                valor = valor,
                operadorComparacao = operadorComparacao,                     
                operadorAcao = operadorAcao
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {tabelasConjuntosValores} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {tabelasConjuntosValores}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM tabelasConjuntosValores"
            if not self.query(sql_s):
                send_log_warning(f"tabelasConjuntosValores não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM tabelasConjuntosValores WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM tabelasConjuntosValores WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    tabelasConjuntosValores 
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
            sql = f"SELECT * FROM tabelasConjuntosValores WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM tabelasConjuntosValores WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM tabelasConjuntosValores WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idTabelasCalculos, idTabelasConjuntos, idCamposAdicionais, idTabelasConjuntosCampos, valor, operadorAcao, operadorComparacao):
        objeto = {
            "idIntegracao": f"tabelasConjuntosValores{id}",
            "content": {}                                 
        }
        if idTabelasCalculos:
            objeto["content"]["idTabelasCalculos"] = { "id": int(idTabelasCalculos)} 
        if idTabelasConjuntos:
            objeto["content"]["idTabelasConjuntos"] = { "id": int(idTabelasConjuntos)}           
        
        if idTabelasConjuntosCampos:
            objeto["content"]["idTabelasConjuntosCampos"] = { "id": int(idTabelasConjuntosCampos)} 

        if valor:
            objeto["content"]["valor"] = f"{valor}"

        if operadorComparacao:
            objeto["content"]["operadorComparacao"] = f"{operadorComparacao}"   
        
        if operadorAcao:
            objeto["content"]["operadorAcao"] = f"{operadorAcao}"

        if idCamposAdicionais != None:
            objeto[0]["content"]["idCamposAdicionais"] = { "id": int(idCamposAdicionais) }      
            
        envio = api_post("tabelasConjuntosValores", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

tabelasConjuntosValores = tabelasConjuntosValores()