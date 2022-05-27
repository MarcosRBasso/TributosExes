from samples import *
import json

class desmembramentosImoveis(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idDesmembramento, unidade, idImovel, matricula, setor, quadra, lote, campo1, 
                campo2, campo3, campo4, campo5, campo6, campo7, campo8, campo9, campo10, copiarCaracteristicas, situacaoImovel):
        try:
            sql = """
                INSERT INTO desmembramentosImoveis (                    
                    idIntegracao,                   
                    id_cloud, 
                    idDesmembramento,
                    unidade,                                               
                    idImovel, 
                    matricula,
                    setor,
                    lote,
                    campo1,
                    quadra,
                    campo2,                    
                    campo3,
                    campo4,
                    campo5,
                    campo6,
                    campo7,
                    campo8, 
                    campo9, 
                    campo10, 
                    copiarCaracteristicas, 
                    situacaoImovel                 
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idDesmembramento)s,
                    %(unidade)s,
                    %(idImovel)s,
                    %(matricula)s,
                    %(setor)s,
                    %(lote)s,
                    %(campo1)s,
                    %(quadra)s,
                    %(campo2)s,                    
                    %(campo3)s,
                    %(campo4)s,
                    %(campo5)s,
                    %(campo6)s,
                    %(campo7)s,
                    %(campo8)s, 
                    %(campo9)s, 
                    %(campo10)s, 
                    %(copiarCaracteristicas)s, 
                    %(situacaoImovel)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idDesmembramento = idDesmembramento,
                unidade = unidade,
                idImovel = idImovel,                               
                matricula = matricula,
                setor = setor,
                lote = lote,                               
                campo1 = campo1,
                quadra = quadra,
                campo2 = campo2,                                               
                campo3 = campo3,
                campo4 = campo4,                               
                campo5 = campo5,
                campo6 = campo6,
                campo7 = campo7,
                campo8 = campo8, 
                campo9 = campo9, 
                campo10 = campo10, 
                copiarCaracteristicas = copiarCaracteristicas, 
                situacaoImovel = situacaoImovel
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {desmembramentosImoveis} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {desmembramentosImoveis}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM desmembramentosImoveis"
            if not self.query(sql_s):
                send_log_warning(f"desmembramentosImoveis não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM desmembramentosImoveis WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM desmembramentosImoveis WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    desmembramentosImoveis 
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
            sql = f"SELECT * FROM desmembramentosImoveis WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM desmembramentosImoveis WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM desmembramentosImoveis WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idDesmembramento, unidade, idImovel, matricula, setor, quadra, lote, campo1, 
                campo2, campo3, campo4, campo5, campo6, campo7, campo8, campo9, campo10, copiarCaracteristicas, situacaoImovel):
        objeto = {
            "idIntegracao": f"desmembramentosImoveis{id}",
            "content": {}                                 
        }
        if idDesmembramento:
            objeto["content"]["idDesmembramento"] = { "id": int(idDesmembramento)}

        if campo8:
            objeto["content"]["campo8"] = f"{campo8}"   

        if campo9:
            objeto["content"]["campo9"] = f"{campo9}"
        
        if campo10:
            objeto["content"]["campo10"] = f"{campo10}"
           
        if copiarCaracteristicas:
            objeto["content"]["copiarCaracteristicas"] = f"{copiarCaracteristicas}"
        
        if situacaoImovel:
            objeto["content"]["situacaoImovel"] = f"{situacaoImovel}"            
        
        if campo1:
            objeto["content"]["campo1"] = f"{campo1}"

        if unidade:
            objeto["content"]["unidade"] = f"{unidade}"           
        
        if matricula:
            objeto["content"]["matricula"] = f"{matricula}" 

        if campo4:
            objeto["content"]["campo4"] = f"{campo4}"  

        if setor:
            objeto["content"]["setor"] = f"{setor}"

        if lote:
            objeto["content"]["lote"] = f"{lote}"   

        if campo3:
            objeto["content"]["campo3"] = f"{campo3}"
        
        if campo2:
            objeto["content"]["campo2"] = f"{campo2}"
           
        if campo5:
            objeto["content"]["campo5"] = f"{campo5}"
        
        if campo7:
            objeto["content"]["campo7"] = f"{campo7}"
        
        if quadra:
            objeto["content"]["quadra"] = f"{quadra}"

        if idImovel != None:
            objeto[0]["content"]["idImovel"] = { "id": int(idImovel) }               

        if campo6 != None:
            objeto[0]["content"]["campo6"] = f"{campo6}"        
            
        envio = api_post("desmembramentosImoveis", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

desmembramentosImoveis = desmembramentosImoveis()