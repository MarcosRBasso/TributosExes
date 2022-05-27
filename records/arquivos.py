from samples import *
import json

class arquivos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idContribuinte, idParcelamento, nroDocumento, cancelado, classificacaoCertidao, protocoloExecucao, dtValidade, descricao, 
                informacoesComplementares, dhCancelamento, dhEmissao, natureza, nome, referente, tipo):
        try:
            sql = """
                INSERT INTO arquivos (                    
                    idIntegracao,                   
                    id_cloud, 
                    idContribuinte,
                    idParcelamento,                                               
                    nroDocumento, 
                    cancelado,
                    classificacaoCertidao,
                    dtValidade,
                    descricao,
                    protocoloExecucao,
                    informacoesComplementares,                    
                    dhCancelamento,
                    dhEmissao,
                    natureza,
                    nome,
                    referente,
                    tipo         
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idContribuinte)s,
                    %(idParcelamento)s,
                    %(nroDocumento)s,
                    %(cancelado)s,
                    %(classificacaoCertidao)s,
                    %(dtValidade)s,
                    %(descricao)s,
                    %(protocoloExecucao)s,
                    %(informacoesComplementares)s,                    
                    %(dhCancelamento)s,
                    %(dhEmissao)s,
                    %(natureza)s,
                    %(nome)s,
                    %(referente)s,
                    %(tipo)s 
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idContribuinte = idContribuinte,
                idParcelamento = idParcelamento,
                nroDocumento = nroDocumento,                               
                cancelado = cancelado,
                classificacaoCertidao = classificacaoCertidao,
                dtValidade = dtValidade,                               
                descricao = descricao,
                protocoloExecucao = protocoloExecucao,
                informacoesComplementares = informacoesComplementares,                                               
                dhCancelamento = dhCancelamento,
                dhEmissao = dhEmissao,                               
                natureza = natureza,
                nome = nome,
                referente = referente,
                tipo = tipo
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {arquivos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {arquivos}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM arquivos"
            if not self.query(sql_s):
                send_log_warning(f"arquivos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM arquivos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM arquivos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    arquivos 
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
            sql = f"SELECT * FROM arquivos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM arquivos WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM arquivos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idContribuinte, idParcelamento, nroDocumento, cancelado, classificacaoCertidao, protocoloExecucao, dtValidade, descricao, 
                informacoesComplementares, dhCancelamento, dhEmissao, natureza, nome, referente, tipo):
        objeto = {
            "idIntegracao": f"arquivos{id}",
            "content": {}                                 
        }
        if tipo:
            objeto["content"]["tipo"] = f"{tipo}"

        if idContribuinte:
            objeto["content"]["idContribuinte"] = { "id": int(idContribuinte)}          
        
        if descricao:
            objeto["content"]["descricao"] = f"{descricao}"

        if idParcelamento:
            objeto["content"]["idParcelamento"] = { "id": int(idParcelamento)}           
        
        if cancelado:
            objeto["content"]["cancelado"] = f"{cancelado}" 

        if dhEmissao:
            objeto["content"]["dhEmissao"] = f"{dhEmissao}"  

        if classificacaoCertidao:
            objeto["content"]["classificacaoCertidao"] = f"{classificacaoCertidao}"

        if dtValidade:
            objeto["content"]["dtValidade"] = f"{dtValidade}"   

        if dhCancelamento:
            objeto["content"]["dhCancelamento"] = f"{dhCancelamento}"
        
        if informacoesComplementares:
            objeto["content"]["informacoesComplementares"] = f"{informacoesComplementares}"
           
        if natureza:
            objeto["content"]["natureza"] = f"{natureza}"
        
        if referente:
            objeto["content"]["referente"] = f"{referente}"
        
        if protocoloExecucao:
            objeto["content"]["protocoloExecucao"] = f"{protocoloExecucao}"

        if nroDocumento != None:
            objeto[0]["content"]["nroDocumento"] = { "id": int(nroDocumento) }               

        if nome != None:
            objeto[0]["content"]["nome"] = f"{nome}"        
            
        envio = api_post("arquivos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

arquivos = arquivos()