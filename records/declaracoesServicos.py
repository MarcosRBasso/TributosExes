from samples import *
import json

class declaracoesServicos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idDeclaracao, idListaServico, comentario, itemLista, vlDeducao, vlImposto, vlRetidoDe, vlRetidoPor, 
                vlServico, aliquota):
        try:
            sql = """
                INSERT INTO declaracoesServicos (                    
                    idIntegracao,                   
                    id_cloud, 
                    idDeclaracao,
                    idListaServico,                                               
                    comentario, 
                    itemLista,
                    vlDeducao,
                    vlRetidoDe,
                    vlRetidoPor,
                    vlImposto,
                    vlServico,                    
                    aliquota                   
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idDeclaracao)s,
                    %(idListaServico)s,
                    %(comentario)s,
                    %(itemLista)s,
                    %(vlDeducao)s,
                    %(vlRetidoDe)s,
                    %(vlRetidoPor)s,
                    %(vlImposto)s,
                    %(vlServico)s,                    
                    %(aliquota)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idDeclaracao = idDeclaracao,
                idListaServico = idListaServico,
                comentario = comentario,                               
                itemLista = itemLista,
                vlDeducao = vlDeducao,
                vlRetidoDe = vlRetidoDe,                               
                vlRetidoPor = vlRetidoPor,
                vlImposto = vlImposto,
                vlServico = vlServico,                                               
                aliquota = aliquota
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {declaracoesServicos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {declaracoesServicos}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM declaracoesServicos"
            if not self.query(sql_s):
                send_log_warning(f"declaracoesServicos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM declaracoesServicos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM declaracoesServicos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    declaracoesServicos 
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
            sql = f"SELECT * FROM declaracoesServicos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM declaracoesServicos WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM declaracoesServicos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idDeclaracao, idListaServico, comentario, itemLista, vlDeducao, vlImposto, vlRetidoDe, vlRetidoPor, 
                vlServico, aliquota):
        objeto = {
            "idIntegracao": f"declaracoesServicos{id}",
            "content": {}                                 
        }
        if idDeclaracao:
            objeto["content"]["idDeclaracao"] = { "id": int(idDeclaracao)}
        
        if vlRetidoPor:
            objeto["content"]["vlRetidoPor"] = f"{vlRetidoPor}"

        if idListaServico:
            objeto["content"]["idListaServico"] = { "id": int(idListaServico)}     
       
        if vlDeducao:
            objeto["content"]["vlDeducao"] = f"{vlDeducao}"

        if vlRetidoDe:
            objeto["content"]["vlRetidoDe"] = f"{vlRetidoDe}"   

        if aliquota:
            objeto["content"]["aliquota"] = f"{aliquota}"
        
        if vlServico:
            objeto["content"]["vlServico"] = f"{vlServico}"

        if vlImposto:
            objeto["content"]["vlImposto"] = f"{vlImposto}"

        if comentario != None:
            objeto[0]["content"]["comentario"] = f"{comentario}"              

        
            
        envio = api_post("declaracoesServicos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

declaracoesServicos = declaracoesServicos()