from samples import *
import json

class pessoasContasBancos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idPessoas, idAgenciasBancarias, idBancos, nroConta, ordem, dtAbertura, dtEncerramento, dvConta, 
                principal, status, tipoConta):
        try:
            sql = """
                INSERT INTO pessoasContasBancos (                    
                    idIntegracao,                   
                    id_cloud, 
                    idPessoas,
                    idAgenciasBancarias,                                               
                    idBancos, 
                    nroConta,
                    ordem,
                    dtEncerramento,
                    dvConta,
                    dtAbertura,
                    principal,                    
                    status,
                    tipoConta       
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idPessoas)s,
                    %(idAgenciasBancarias)s,
                    %(idBancos)s,
                    %(nroConta)s,
                    %(ordem)s,
                    %(dtEncerramento)s,
                    %(dvConta)s,
                    %(dtAbertura)s,
                    %(principal)s,                    
                    %(status)s,
                    %(tipoConta)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idPessoas = idPessoas,
                idAgenciasBancarias = idAgenciasBancarias,
                idBancos = idBancos,                               
                nroConta = nroConta,
                ordem = ordem,
                dtEncerramento = dtEncerramento,                               
                dvConta = dvConta,
                dtAbertura = dtAbertura,
                principal = principal,                                               
                status = status,
                tipoConta = tipoConta
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {pessoasContasBancos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {pessoasContasBancos}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM pessoasContasBancos"
            if not self.query(sql_s):
                send_log_warning(f"pessoasContasBancos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM pessoasContasBancos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM pessoasContasBancos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    pessoasContasBancos 
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
            sql = f"SELECT * FROM pessoasContasBancos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM pessoasContasBancos WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM pessoasContasBancos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idPessoas, idAgenciasBancarias, idBancos, nroConta, ordem, dtAbertura, dtEncerramento, dvConta, 
                principal, status, tipoConta):
        objeto = {
            "idIntegracao": f"pessoasContasBancos{id}",
            "content": {}                                 
        }
        if idPessoas:
            objeto["content"]["idPessoas"] = { "id": int(idPessoas)}          
        
        if dvConta:
            objeto["content"]["dvConta"] = f"{dvConta}"

        if idAgenciasBancarias:
            objeto["content"]["idAgenciasBancarias"] = { "id": int(idAgenciasBancarias)}           
        
        if nroConta:
            objeto["content"]["nroConta"] = f"{nroConta}" 

        if tipoConta:
            objeto["content"]["tipoConta"] = f"{tipoConta}"  

        if ordem:
            objeto["content"]["ordem"] = f"{ordem}"

        if dtEncerramento:
            objeto["content"]["dtEncerramento"] = f"{dtEncerramento}"   

        if status:
            objeto["content"]["status"] = f"{status}"
        
        if principal:
            objeto["content"]["principal"] = f"{principal}"
        
        if dtAbertura:
            objeto["content"]["dtAbertura"] = f"{dtAbertura}"

        if idBancos != None:
            objeto[0]["content"]["idBancos"] = { "id": int(idBancos) }               
            
        envio = api_post("pessoasContasBancos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

pessoasContasBancos = pessoasContasBancos()