from samples import *
import json

class remembramentosImoveis(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idAgrupamentos, idImoveis, idRemembramentos, unidade, unidadeAnt, matricula, matriculaAnt, setor, 
                setorAnt, quadra, quadraAnt, lote, loteAnt, principal):
        try:
            sql = """
                INSERT INTO remembramentosImoveis (                    
                    idIntegracao,                   
                    id_cloud, 
                    idAgrupamentos,
                    idImoveis,                                               
                    idRemembramentos, 
                    unidade,
                    unidadeAnt,
                    matriculaAnt,
                    setor,
                    matricula,
                    setorAnt,                    
                    quadra,
                    quadraAnt,
                    lote,
                    loteAnt,
                    principal         
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idAgrupamentos)s,
                    %(idImoveis)s,
                    %(idRemembramentos)s,
                    %(unidade)s,
                    %(unidadeAnt)s,
                    %(matriculaAnt)s,
                    %(setor)s,
                    %(matricula)s,
                    %(setorAnt)s,                    
                    %(quadra)s,
                    %(quadraAnt)s,
                    %(lote)s,
                    %(loteAnt)s,
                    %(principal)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idAgrupamentos = idAgrupamentos,
                idImoveis = idImoveis,
                idRemembramentos = idRemembramentos,                               
                unidade = unidade,
                unidadeAnt = unidadeAnt,
                matriculaAnt = matriculaAnt,                               
                setor = setor,
                matricula = matricula,
                setorAnt = setorAnt,                                               
                quadra = quadra,
                quadraAnt = quadraAnt,                               
                lote = lote,
                loteAnt = loteAnt,
                principal = principal
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {remembramentosImoveis} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {remembramentosImoveis}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM remembramentosImoveis"
            if not self.query(sql_s):
                send_log_warning(f"remembramentosImoveis não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM remembramentosImoveis WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM remembramentosImoveis WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    remembramentosImoveis 
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
            sql = f"SELECT * FROM remembramentosImoveis WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM remembramentosImoveis WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM remembramentosImoveis WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idAgrupamentos, idImoveis, idRemembramentos, unidade, unidadeAnt, matricula, matriculaAnt, setor, 
                setorAnt, quadra, quadraAnt, lote, loteAnt, principal):
        objeto = {
            "idIntegracao": f"remembramentosImoveis{id}",
            "content": {}                                 
        }
        if idAgrupamentos:
            objeto["content"]["idAgrupamentos"] = { "id": int(idAgrupamentos)}          
        
        if setor:
            objeto["content"]["setor"] = f"{setor}"

        if idImoveis:
            objeto["content"]["idImoveis"] = { "id": int(idImoveis)}           
        
        if unidade:
            objeto["content"]["unidade"] = f"{unidade}" 

        if quadraAnt:
            objeto["content"]["quadraAnt"] = f"{quadraAnt}"  

        if unidadeAnt:
            objeto["content"]["unidadeAnt"] = f"{unidadeAnt}"

        if matriculaAnt:
            objeto["content"]["matriculaAnt"] = f"{matriculaAnt}"   

        if quadra:
            objeto["content"]["quadra"] = f"{quadra}"
        
        if setorAnt:
            objeto["content"]["setorAnt"] = f"{setorAnt}"
           
        if lote:
            objeto["content"]["lote"] = f"{lote}"
        
        if principal:
            objeto["content"]["principal"] = f"{principal}"
        
        if matricula:
            objeto["content"]["matricula"] = f"{matricula}"

        if idRemembramentos != None:
            objeto[0]["content"]["idRemembramentos"] = { "id": int(idRemembramentos) }               

        if loteAnt != None:
            objeto[0]["content"]["loteAnt"] = f"{loteAnt}"        
            
        envio = api_post("remembramentosImoveis", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

remembramentosImoveis = remembramentosImoveis()