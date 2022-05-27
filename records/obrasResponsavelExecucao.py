from samples import *
import json

class obrasResponsavelExecucao(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idObra, idContribuinte, idContribuinteSecundario, idConstrutora, tipoResponsavel, dtValidade, obraResponsavelExecucaoLiderConsorcios):
        try:
            sql = """
                INSERT INTO obrasResponsavelExecucao (                    
                    idIntegracao,                   
                    id_cloud, 
                    idObra,
                    idContribuinte,                                               
                    idContribuinteSecundario, 
                    idConstrutora,
                    tipoResponsavel,
                    obraResponsavelExecucaoLiderConsorcios,
                    dtValidade                
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idObra)s,
                    %(idContribuinte)s,
                    %(idContribuinteSecundario)s,
                    %(idConstrutora)s,
                    %(tipoResponsavel)s,
                    %(obraResponsavelExecucaoLiderConsorcios)s,
                    %(dtValidade)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idObra = idObra,
                idContribuinte = idContribuinte,
                idContribuinteSecundario = idContribuinteSecundario,                               
                idConstrutora = idConstrutora,
                tipoResponsavel = tipoResponsavel,
                obraResponsavelExecucaoLiderConsorcios = obraResponsavelExecucaoLiderConsorcios,
                dtValidade = dtValidade
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {obrasResponsavelExecucao} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {obrasResponsavelExecucao}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM obrasResponsavelExecucao"
            if not self.query(sql_s):
                send_log_warning(f"obrasResponsavelExecucao não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM obrasResponsavelExecucao WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM obrasResponsavelExecucao WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    obrasResponsavelExecucao 
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
            sql = f"SELECT * FROM obrasResponsavelExecucao WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM obrasResponsavelExecucao WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM obrasResponsavelExecucao WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idObra, idContribuinte, idContribuinteSecundario, idConstrutora, tipoResponsavel, dtValidade, obraResponsavelExecucaoLiderConsorcios):
        objeto = {
            "idIntegracao": f"obrasResponsavelExecucao{id}",
            "content": {}                                 
        }
        if idObra:
            objeto["content"]["idObra"] = { "id": int(idObra)}

        if idContribuinte:
            objeto["content"]["idContribuinte"] = { "id": int(idContribuinte)}        
       
        if idConstrutora:
            objeto["content"]["idConstrutora"] = { "id": int(idConstrutora)}       
       
        if tipoResponsavel:
            objeto["content"]["tipoResponsavel"] = f"{tipoResponsavel}"

        if obraResponsavelExecucaoLiderConsorcios:
            objeto["content"]["obraResponsavelExecucaoLiderConsorcios"] = f"{obraResponsavelExecucaoLiderConsorcios}"  
        
        if dtValidade:
            objeto["content"]["dtValidade"] = f"{dtValidade}"              

        if idContribuinteSecundario != None:
            objeto[0]["content"]["idContribuinteSecundario"] = { "id": int(idContribuinteSecundario)}    
            
        envio = api_post("obrasResponsavelExecucao", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

obrasResponsavelExecucao = obrasResponsavelExecucao()