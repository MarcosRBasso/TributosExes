from samples import *
import json

class configNotasAvulsas(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, nroDiasAposEmissao, nroPrimeiraNota, percCofins, percCsll, percPisPasep, serie, impressaoAposPagamento, permiteAlterarValores, tipoDias):
        try:
            sql = """
                INSERT INTO configNotasAvulsas (                    
                    idIntegracao,                   
                    id_cloud,                     
                    nroDiasAposEmissao,                                               
                    nroPrimeiraNota, 
                    percCofins,
                    percCsll,
                    percPisPasep,
                    serie,
                    impressaoAposPagamento, 
                    permiteAlterarValores, 
                    tipoDias                              
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,                                        
                    %(nroDiasAposEmissao)s,
                    %(nroPrimeiraNota)s,
                    %(percCofins)s,
                    %(percCsll)s,
                    %(percPisPasep)s,
                    %(serie)s,
                    %(impressaoAposPagamento)s, 
                    %(permiteAlterarValores)s, 
                    %(tipoDias)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                                               
                nroDiasAposEmissao = nroDiasAposEmissao,
                nroPrimeiraNota = nroPrimeiraNota,                               
                percCofins = percCofins,
                percCsll = percCsll,
                percPisPasep = percPisPasep,                               
                serie = serie,
                impressaoAposPagamento = impressaoAposPagamento, 
                permiteAlterarValores = permiteAlterarValores, 
                tipoDias = tipoDias              
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {configNotasAvulsas} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {configNotasAvulsas}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM configNotasAvulsas"
            if not self.query(sql_s):
                send_log_warning(f"configNotasAvulsas não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM configNotasAvulsas WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM configNotasAvulsas WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    configNotasAvulsas 
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
            sql = f"SELECT * FROM configNotasAvulsas WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM configNotasAvulsas WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM configNotasAvulsas WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, nroDiasAposEmissao, nroPrimeiraNota, percCofins, percCsll, percPisPasep, serie, impressaoAposPagamento, permiteAlterarValores, tipoDias):
        objeto = {
            "idIntegracao": f"configNotasAvulsas{id}",
            "content": {}                                 
        }
        if impressaoAposPagamento:
            objeto["content"]["impressaoAposPagamento"] = f"{impressaoAposPagamento}"
           
        if permiteAlterarValores:
            objeto["content"]["permiteAlterarValores"] = f"{permiteAlterarValores}"
        
        if tipoDias:
            objeto["content"]["tipoDias"] = f"{tipoDias}" 

        if percCofins:
            objeto["content"]["percCofins"] =  { "id": int(percCofins)}
        
        if percCsll:
            objeto["content"]["percCsll"] =  { "id": int(percCsll)}

        if nroDiasAposEmissao:
            objeto["content"]["nroDiasAposEmissao"] =  { "id": int(nroDiasAposEmissao)}
           
        if nroPrimeiraNota:
            objeto["content"]["nroPrimeiraNota"] =  { "id": int(nroPrimeiraNota)}
        
        if serie:
            objeto["content"]["serie"] =  f"{serie}"
        
        if percPisPasep:
            objeto["content"]["percPisPasep"] =  f"{percPisPasep}"
        envio = api_post("configNotasAvulsas", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

configNotasAvulsas = configNotasAvulsas()