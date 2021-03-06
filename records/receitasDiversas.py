from samples import *
import json

class receitasDiversas(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idPessoa, idTipoServico, idImovel, idEconomico, idCreditoTributario, comentarioServico, descricaoServico, nroProcesso, 
                dtReceitaDiversa):
        try:
            sql = """
                INSERT INTO receitasDiversas (                    
                    idIntegracao,                   
                    id_cloud, 
                    idPessoa,
                    idTipoServico,                                               
                    idImovel, 
                    idEconomico,
                    idCreditoTributario,
                    descricaoServico,
                    nroProcesso,
                    comentarioServico,
                    dtReceitaDiversa       
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idPessoa)s,
                    %(idTipoServico)s,
                    %(idImovel)s,
                    %(idEconomico)s,
                    %(idCreditoTributario)s,
                    %(descricaoServico)s,
                    %(nroProcesso)s,
                    %(comentarioServico)s,
                    %(dtReceitaDiversa)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idPessoa = idPessoa,
                idTipoServico = idTipoServico,
                idImovel = idImovel,                               
                idEconomico = idEconomico,
                idCreditoTributario = idCreditoTributario,
                descricaoServico = descricaoServico,                               
                nroProcesso = nroProcesso,
                comentarioServico = comentarioServico,
                dtReceitaDiversa = dtReceitaDiversa
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {receitasDiversas} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {receitasDiversas}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM receitasDiversas"
            if not self.query(sql_s):
                send_log_warning(f"receitasDiversas n??o encontrado para excluir.")
                return
            sql_d = f"DELETE FROM receitasDiversas WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias exclu??dos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de exclus??o do atividades econ??micas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM receitasDiversas WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} n??o encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    receitasDiversas 
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
            sql = f"SELECT * FROM receitasDiversas WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} n??o encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM receitasDiversas WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM receitasDiversas WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} n??o encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de busca. {error}")

    def send_post(self, id, idPessoa, idTipoServico, idImovel, idEconomico, idCreditoTributario, comentarioServico, descricaoServico, nroProcesso, 
                dtReceitaDiversa):
        objeto = {
            "idIntegracao": f"receitasDiversas{id}",
            "content": {}                                 
        }
        if idPessoa:
            objeto["content"]["idPessoa"] = { "id": int(idPessoa)}          
        
        if nroProcesso:
            objeto["content"]["nroProcesso"] = f"{nroProcesso}"

        if idTipoServico:
            objeto["content"]["idTipoServico"] = { "id": int(idTipoServico)}           
        
        if idEconomico:
            objeto["content"]["idEconomico"] = { "id": int(idEconomico)}   

        if idCreditoTributario:
            objeto["content"]["idCreditoTributario"] = { "id": int(idCreditoTributario)}

        if descricaoServico:
            objeto["content"]["descricaoServico"] = f"{descricaoServico}" 
        
        if dtReceitaDiversa:
            objeto["content"]["dtReceitaDiversa"] = f"{dtReceitaDiversa}"
        
        if comentarioServico:
            objeto["content"]["comentarioServico"] = f"{comentarioServico}"

        if idImovel != None:
            objeto[0]["content"]["idImovel"] = { "id": int(idImovel) }          
            
        envio = api_post("receitasDiversas", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

receitasDiversas = receitasDiversas()