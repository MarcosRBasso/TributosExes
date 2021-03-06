from samples import *
import json

class configInscrImobiliarias(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idConfigImobiliarias, campo, qtdCaracter, completarCom, descricao, conteudo, conteudoCompletar, posicaoCompletar, posicaoRetirar, 
                  situacao, unidade):
        try:
            sql = """
                INSERT INTO configInscrImobiliarias (                    
                    idIntegracao,                   
                    id_cloud,                     
                    idConfigImobiliarias,                                               
                    campo, 
                    qtdCaracter,
                    completarCom,
                    descricao,
                    conteudo,
                    conteudoCompletar, 
                    posicaoCompletar, 
                    posicaoRetirar, 
                    situacao, 
                    unidade                                 
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,                                        
                    %(idConfigImobiliarias)s,
                    %(campo)s,
                    %(qtdCaracter)s,
                    %(completarCom)s,
                    %(descricao)s,
                    %(conteudo)s,
                    %(conteudoCompletar)s, 
                    %(posicaoCompletar)s, 
                    %(posicaoRetirar)s, 
                    %(situacao)s,
                    %(unidade)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                                               
                idConfigImobiliarias = idConfigImobiliarias,
                campo = campo,                               
                qtdCaracter = qtdCaracter,
                completarCom = completarCom,
                descricao = descricao,                               
                conteudo = conteudo,
                conteudoCompletar = conteudoCompletar, 
                posicaoCompletar = posicaoCompletar, 
                posicaoRetirar = posicaoRetirar, 
                situacao = situacao,
                unidade = unidade               
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {configInscrImobiliarias} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {configInscrImobiliarias}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM configInscrImobiliarias"
            if not self.query(sql_s):
                send_log_warning(f"configInscrImobiliarias n??o encontrado para excluir.")
                return
            sql_d = f"DELETE FROM configInscrImobiliarias WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias exclu??dos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de exclus??o do atividades econ??micas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM configInscrImobiliarias WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} n??o encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    configInscrImobiliarias 
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
            sql = f"SELECT * FROM configInscrImobiliarias WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} n??o encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM configInscrImobiliarias WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM configInscrImobiliarias WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} n??o encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de busca. {error}")

    def send_post(self, id, idConfigImobiliarias, campo, qtdCaracter, completarCom, descricao, conteudo,conteudoCompletar, posicaoCompletar, posicaoRetirar, situacao, unidade):
        objeto = {
            "idIntegracao": f"configInscrImobiliarias{id}",
            "content": {}                                 
        }
        if conteudoCompletar:
            objeto["content"]["conteudoCompletar"] = f"{conteudoCompletar}"
           
        if posicaoCompletar:
            objeto["content"]["posicaoCompletar"] = f"{posicaoCompletar}"
        
        if posicaoRetirar:
            objeto["content"]["posicaoRetirar"] = f"{posicaoRetirar}"
        
        if situacao:
            objeto["content"]["situacao"] = f"{situacao}"

        if unidade:
            objeto["content"]["unidade"] = f"{unidade}"    

        if qtdCaracter:
            objeto["content"]["qtdCaracter"] =  { "id": int(qtdCaracter)}
        
        if completarCom:
            objeto["content"]["completarCom"] =  f"{completarCom}"

        if idConfigImobiliarias:
            objeto["content"]["idConfigImobiliarias"] =  { "id": int(idConfigImobiliarias)}
           
        if campo:
            objeto["content"]["campo"] =  f"{campo}"
        
        if conteudo:
            objeto["content"]["conteudo"] =  f"{conteudo}"
        
        if descricao:
            objeto["content"]["descricao"] =  f"{descricao}"
        envio = api_post("configInscrImobiliarias", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

configInscrImobiliarias = configInscrImobiliarias()