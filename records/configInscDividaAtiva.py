from samples import *
import json

class configInscDividaAtiva(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, numLivro, qtdeFolhasLivro, qtdePosicoesFolha, anoLivro, numInscricao, formatoLivro, criterioFormaPagto):
        try:
            sql = """
                INSERT INTO configInscDividaAtiva (                    
                    idIntegracao,                   
                    id_cloud,                     
                    numLivro,                                               
                    qtdeFolhasLivro, 
                    qtdePosicoesFolha,
                    anoLivro,
                    numInscricao,
                    formatoLivro,
                    criterioFormaPagto                               
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,                                        
                    %(numLivro)s,
                    %(qtdeFolhasLivro)s,
                    %(qtdePosicoesFolha)s,
                    %(anoLivro)s,
                    %(numInscricao)s,
                    %(formatoLivro)s,
                    %(criterioFormaPagto)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                                               
                numLivro = numLivro,
                qtdeFolhasLivro = qtdeFolhasLivro,                               
                qtdePosicoesFolha = qtdePosicoesFolha,
                anoLivro = anoLivro,
                numInscricao = numInscricao,                               
                formatoLivro = formatoLivro,
                criterioFormaPagto = criterioFormaPagto            
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {configInscDividaAtiva} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {configInscDividaAtiva}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM configInscDividaAtiva"
            if not self.query(sql_s):
                send_log_warning(f"configInscDividaAtiva não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM configInscDividaAtiva WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM configInscDividaAtiva WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    configInscDividaAtiva 
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
            sql = f"SELECT * FROM configInscDividaAtiva WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM configInscDividaAtiva WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM configInscDividaAtiva WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, numLivro, qtdeFolhasLivro, qtdePosicoesFolha, anoLivro, numInscricao, formatoLivro, criterioFormaPagto):
        objeto = {
            "idIntegracao": f"configInscDividaAtiva{id}",
            "content": {}                                 
        }
        if criterioFormaPagto:
            objeto["content"]["criterioFormaPagto"] = f"{criterioFormaPagto}"

        if qtdePosicoesFolha:
            objeto["content"]["qtdePosicoesFolha"] =  { "id": int(qtdePosicoesFolha)}
        
        if anoLivro:
            objeto["content"]["anoLivro"] =  { "id": int(anoLivro)}

        if numLivro:
            objeto["content"]["numLivro"] =  { "id": int(numLivro)}
           
        if qtdeFolhasLivro:
            objeto["content"]["qtdeFolhasLivro"] =  { "id": int(qtdeFolhasLivro)}
        
        if formatoLivro:
            objeto["content"]["formatoLivro"] =  f"{formatoLivro}"
        
        if numInscricao:
            objeto["content"]["numInscricao"] =  { "id": int(numInscricao)}
        envio = api_post("configInscDividaAtiva", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

configInscDividaAtiva = configInscDividaAtiva()