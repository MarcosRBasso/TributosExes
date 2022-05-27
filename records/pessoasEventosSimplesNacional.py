from samples import *
import json

class pessoasEventosSimplesNacional(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idPessoaJuridica, optante, dataInicio, dataFinal, dataEfeito, processo, responsavel, dataOcorrencia, 
                descricao, comentario):
        try:
            sql = """
                INSERT INTO pessoasEventosSimplesNacional (                    
                    idIntegracao,                   
                    id_cloud, 
                    idPessoaJuridica,
                    optante,                                               
                    dataInicio, 
                    dataFinal,
                    dataEfeito,
                    responsavel,
                    dataOcorrencia,
                    processo,
                    descricao,                    
                    comentario       
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idPessoaJuridica)s,
                    %(optante)s,
                    %(dataInicio)s,
                    %(dataFinal)s,
                    %(dataEfeito)s,
                    %(responsavel)s,
                    %(dataOcorrencia)s,
                    %(processo)s,
                    %(descricao)s,                    
                    %(comentario)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idPessoaJuridica = idPessoaJuridica,
                optante = optante,
                dataInicio = dataInicio,                               
                dataFinal = dataFinal,
                dataEfeito = dataEfeito,
                responsavel = responsavel,                               
                dataOcorrencia = dataOcorrencia,
                processo = processo,
                descricao = descricao,                                               
                comentario = comentario
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {pessoasEventosSimplesNacional} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {pessoasEventosSimplesNacional}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM pessoasEventosSimplesNacional"
            if not self.query(sql_s):
                send_log_warning(f"pessoasEventosSimplesNacional não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM pessoasEventosSimplesNacional WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM pessoasEventosSimplesNacional WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    pessoasEventosSimplesNacional 
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
            sql = f"SELECT * FROM pessoasEventosSimplesNacional WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM pessoasEventosSimplesNacional WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM pessoasEventosSimplesNacional WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idPessoaJuridica, optante, dataInicio, dataFinal, dataEfeito, processo, responsavel, dataOcorrencia, 
                descricao, comentario):
        objeto = {
            "idIntegracao": f"pessoasEventosSimplesNacional{id}",
            "content": {}                                 
        }
        if idPessoaJuridica:
            objeto["content"]["idPessoaJuridica"] = { "id": int(idPessoaJuridica)}          
        
        if dataOcorrencia:
            objeto["content"]["dataOcorrencia"] = f"{dataOcorrencia}"

        if optante:
            objeto["content"]["optante"] = f"{optante}"
        
        if dataFinal:
            objeto["content"]["dataFinal"] = f"{dataFinal}" 

        if dataEfeito:
            objeto["content"]["dataEfeito"] = f"{dataEfeito}"

        if responsavel:
            objeto["content"]["responsavel"] = f"{responsavel}"   

        if comentario:
            objeto["content"]["comentario"] = f"{comentario}"
        
        if descricao:
            objeto["content"]["descricao"] = f"{descricao}"
        
        if processo:
            objeto["content"]["processo"] = f"{processo}"

        if dataInicio != None:
            objeto[0]["content"]["dataInicio"] = f"{dataInicio}"

        envio = api_post("pessoasEventosSimplesNacional", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

pessoasEventosSimplesNacional = pessoasEventosSimplesNacional()