from samples import *
import json

class pessoasFisicasDocumentos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idPessoas, idEstadoRg, idEstadoRic, dtEmissaoRg, dtEmissaoRic, dtEmissaoPisPasep, nroRg, nroRic, 
                pisPasep, orgaoEmissorRg, orgaoEmissorRic):
        try:
            sql = """
                INSERT INTO pessoasFisicasDocumentos (                    
                    idIntegracao,                   
                    id_cloud, 
                    idPessoas,
                    idEstadoRg,                                               
                    idEstadoRic, 
                    dtEmissaoRg,
                    dtEmissaoRic,
                    nroRg,
                    nroRic,
                    dtEmissaoPisPasep,
                    pisPasep,                    
                    orgaoEmissorRg,
                    orgaoEmissorRic         
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idPessoas)s,
                    %(idEstadoRg)s,
                    %(idEstadoRic)s,
                    %(dtEmissaoRg)s,
                    %(dtEmissaoRic)s,
                    %(nroRg)s,
                    %(nroRic)s,
                    %(dtEmissaoPisPasep)s,
                    %(pisPasep)s,                    
                    %(orgaoEmissorRg)s,
                    %(orgaoEmissorRic)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idPessoas = idPessoas,
                idEstadoRg = idEstadoRg,
                idEstadoRic = idEstadoRic,                               
                dtEmissaoRg = dtEmissaoRg,
                dtEmissaoRic = dtEmissaoRic,
                nroRg = nroRg,                               
                nroRic = nroRic,
                dtEmissaoPisPasep = dtEmissaoPisPasep,
                pisPasep = pisPasep,                                               
                orgaoEmissorRg = orgaoEmissorRg,
                orgaoEmissorRic = orgaoEmissorRic
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {pessoasFisicasDocumentos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {pessoasFisicasDocumentos}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM pessoasFisicasDocumentos"
            if not self.query(sql_s):
                send_log_warning(f"pessoasFisicasDocumentos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM pessoasFisicasDocumentos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM pessoasFisicasDocumentos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    pessoasFisicasDocumentos 
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
            sql = f"SELECT * FROM pessoasFisicasDocumentos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM pessoasFisicasDocumentos WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM pessoasFisicasDocumentos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idPessoas, idEstadoRg, idEstadoRic, dtEmissaoRg, dtEmissaoRic, dtEmissaoPisPasep, nroRg, nroRic, 
                pisPasep, orgaoEmissorRg, orgaoEmissorRic):
        objeto = {
            "idIntegracao": f"pessoasFisicasDocumentos{id}",
            "content": {}                                 
        }
        if idPessoas:
            objeto["content"]["idPessoas"] = { "id": int(idPessoas)}          
        
        if nroRic:
            objeto["content"]["nroRic"] = f"{nroRic}"

        if idEstadoRg:
            objeto["content"]["idEstadoRg"] = { "id": int(idEstadoRg)}           
        
        if dtEmissaoRg:
            objeto["content"]["dtEmissaoRg"] = f"{dtEmissaoRg}" 

        if orgaoEmissorRic:
            objeto["content"]["orgaoEmissorRic"] = f"{orgaoEmissorRic}"  

        if dtEmissaoRic:
            objeto["content"]["dtEmissaoRic"] = f"{dtEmissaoRic}"

        if nroRg:
            objeto["content"]["nroRg"] = f"{nroRg}"   

        if orgaoEmissorRg:
            objeto["content"]["orgaoEmissorRg"] = f"{orgaoEmissorRg}"
        
        if pisPasep:
            objeto["content"]["pisPasep"] = f"{pisPasep}"
        
        if dtEmissaoPisPasep:
            objeto["content"]["dtEmissaoPisPasep"] = f"{dtEmissaoPisPasep}"

        if idEstadoRic != None:
            objeto[0]["content"]["idEstadoRic"] = { "id": int(idEstadoRic) }            
            
        envio = api_post("pessoasFisicasDocumentos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

pessoasFisicasDocumentos = pessoasFisicasDocumentos()