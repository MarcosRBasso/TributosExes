from samples import *
import json

class cancelamentoDocumentos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, motivo, observacoes, qtdDocumentos, responsavel, protocoloExecucao, dhCriacao, tipoManutencao, documentos):
        try:
            sql = """
                INSERT INTO cancelamentoDocumentos (                    
                    idIntegracao,                   
                    id_cloud, 
                    motivo,
                    observacoes,                                               
                    qtdDocumentos, 
                    responsavel,
                    protocoloExecucao,
                    tipoManutencao,
                    documentos                 
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(motivo)s,
                    %(observacoes)s,
                    %(qtdDocumentos)s,
                    %(responsavel)s,
                    %(protocoloExecucao)s,
                    %(tipoManutencao)s,
                    %(documentos)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                motivo = motivo,
                observacoes = observacoes,
                qtdDocumentos = qtdDocumentos,                               
                responsavel = responsavel,
                protocoloExecucao = protocoloExecucao,
                tipoManutencao = tipoManutencao,                               
                documentos = documentos,
                dhCriacao = dhCriacao
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {cancelamentoDocumentos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {cancelamentoDocumentos}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM cancelamentoDocumentos"
            if not self.query(sql_s):
                send_log_warning(f"cancelamentoDocumentos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM cancelamentoDocumentos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM cancelamentoDocumentos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    cancelamentoDocumentos 
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
            sql = f"SELECT * FROM cancelamentoDocumentos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM cancelamentoDocumentos WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM cancelamentoDocumentos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, motivo, observacoes, qtdDocumentos, responsavel, protocoloExecucao, dhCriacao, tipoManutencao, documentos):
        objeto = {
            "idIntegracao": f"cancelamentoDocumentos{id}",
            "content": {}                                 
        }
        if motivo:
            objeto["content"]["motivo"] = f"{motivo}"
        
        if documentos:
            objeto["content"]["documentos"] = f"{documentos}"

        if observacoes:
            objeto["content"]["observacoes"] = f"{observacoes}"        
       
        if responsavel:
            objeto["content"]["responsavel"] = f"{responsavel}"       
       
        if protocoloExecucao:
            objeto["content"]["protocoloExecucao"] = f"{protocoloExecucao}"

        if tipoManutencao:
            objeto["content"]["tipoManutencao"] = f"{tipoManutencao}"  
        
        if dhCriacao:
            objeto["content"]["dhCriacao"] = f"{dhCriacao}"              

        if qtdDocumentos != None:
            objeto[0]["content"]["qtdDocumentos"] = { "id": int(qtdDocumentos)}    
            
        envio = api_post("cancelamentoDocumentos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

cancelamentoDocumentos = cancelamentoDocumentos()