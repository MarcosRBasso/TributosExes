from samples import *
import json

class pessoasJuridicas(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idPessoas, idNaturezaJuridica, idQualificacao, idResponsavel, nroRegistro, dtRegistro, orgaoRegistro, porteEmpresa, 
                inscricaoEstadual, isentoInscricao, optanteSimples):
        try:
            sql = """
                INSERT INTO pessoasJuridicas (                    
                    idIntegracao,                   
                    id_cloud, 
                    idPessoas,
                    idNaturezaJuridica,                                               
                    idQualificacao, 
                    idResponsavel,
                    nroRegistro,
                    orgaoRegistro,
                    porteEmpresa,
                    dtRegistro,
                    inscricaoEstadual,                    
                    isentoInscricao,
                    optanteSimples     
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idPessoas)s,
                    %(idNaturezaJuridica)s,
                    %(idQualificacao)s,
                    %(idResponsavel)s,
                    %(nroRegistro)s,
                    %(orgaoRegistro)s,
                    %(porteEmpresa)s,
                    %(dtRegistro)s,
                    %(inscricaoEstadual)s,                    
                    %(isentoInscricao)s,
                    %(optanteSimples)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idPessoas = idPessoas,
                idNaturezaJuridica = idNaturezaJuridica,
                idQualificacao = idQualificacao,                               
                idResponsavel = idResponsavel,
                nroRegistro = nroRegistro,
                orgaoRegistro = orgaoRegistro,                               
                porteEmpresa = porteEmpresa,
                dtRegistro = dtRegistro,
                inscricaoEstadual = inscricaoEstadual,                                               
                isentoInscricao = isentoInscricao,
                optanteSimples = optanteSimples
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {pessoasJuridicas} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {pessoasJuridicas}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM pessoasJuridicas"
            if not self.query(sql_s):
                send_log_warning(f"pessoasJuridicas não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM pessoasJuridicas WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM pessoasJuridicas WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    pessoasJuridicas 
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
            sql = f"SELECT * FROM pessoasJuridicas WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM pessoasJuridicas WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM pessoasJuridicas WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idPessoas, idNaturezaJuridica, idQualificacao, idResponsavel, nroRegistro, dtRegistro, orgaoRegistro, porteEmpresa, 
                inscricaoEstadual, isentoInscricao, optanteSimples):
        objeto = {
            "idIntegracao": f"pessoasJuridicas{id}",
            "content": {}                                 
        }
        if idPessoas:
            objeto["content"]["idPessoas"] = { "id": int(idPessoas)}          
        
        if porteEmpresa:
            objeto["content"]["porteEmpresa"] = f"{porteEmpresa}"

        if idNaturezaJuridica:
            objeto["content"]["idNaturezaJuridica"] = { "id": int(idNaturezaJuridica)}           
        
        if idResponsavel:
            objeto["content"]["idResponsavel"] = { "id": int(idResponsavel)} 

        if optanteSimples:
            objeto["content"]["optanteSimples"] = f"{optanteSimples}"  

        if nroRegistro:
            objeto["content"]["nroRegistro"] = f"{nroRegistro}"

        if orgaoRegistro:
            objeto["content"]["orgaoRegistro"] = f"{orgaoRegistro}"   

        if isentoInscricao:
            objeto["content"]["isentoInscricao"] = f"{isentoInscricao}"
        
        if inscricaoEstadual:
            objeto["content"]["inscricaoEstadual"] = f"{inscricaoEstadual}"
        
        if dtRegistro:
            objeto["content"]["dtRegistro"] = f"{dtRegistro}"

        if idQualificacao != None:
            objeto[0]["content"]["idQualificacao"] = { "id": int(idQualificacao) }      
            
        envio = api_post("pessoasJuridicas", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

pessoasJuridicas = pessoasJuridicas()