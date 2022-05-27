from samples import *
import json

class compensacoes(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idSaldo, idReceita, idGuia, idDivida, idParcelamentosParcela, idPagamentosDetalhados, vlSaldo, vlTributo, vlJuro, vlCorrecao):
        try:
            sql = """
                INSERT INTO compensacoes (                    
                    idIntegracao,                   
                    id_cloud,                     
                    idSaldo,                                               
                    idReceita, 
                    idGuia,
                    idDivida,
                    idParcelamentosParcela,
                    idPagamentosDetalhados,
                    vlSaldo, 
                    vlTributo, 
                    vlJuro, 
                    vlCorrecao                                 
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,                                        
                    %(idSaldo)s,
                    %(idReceita)s,
                    %(idGuia)s,
                    %(idDivida)s,
                    %(idParcelamentosParcela)s,
                    %(idPagamentosDetalhados)s,
                    %(vlSaldo)s, 
                    %(vlTributo)s, 
                    %(vlJuro)s, 
                    %(vlCorrecao)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                                               
                idSaldo = idSaldo,
                idReceita = idReceita,                               
                idGuia = idGuia,
                idDivida = idDivida,
                idParcelamentosParcela = idParcelamentosParcela,                               
                idPagamentosDetalhados = idPagamentosDetalhados,
                vlSaldo = vlSaldo, 
                vlTributo = vlTributo, 
                vlJuro = vlJuro, 
                vlCorrecao = vlCorrecao               
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {compensacoes} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {compensacoes}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM compensacoes"
            if not self.query(sql_s):
                send_log_warning(f"compensacoes não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM compensacoes WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM compensacoes WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    compensacoes 
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
            sql = f"SELECT * FROM compensacoes WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM compensacoes WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM compensacoes WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idSaldo, idReceita, idGuia, idDivida, idParcelamentosParcela, idPagamentosDetalhados,vlSaldo, vlTributo, vlJuro, vlCorrecao):
        objeto = {
            "idIntegracao": f"compensacoes{id}",
            "content": {}                                 
        }
        if vlSaldo:
            objeto["content"]["vlSaldo"] = f"{vlSaldo}"
           
        if vlTributo:
            objeto["content"]["vlTributo"] = f"{vlTributo}"
        
        if vlJuro:
            objeto["content"]["vlJuro"] = f"{vlJuro}"
        
        if vlCorrecao:
            objeto["content"]["vlCorrecao"] = f"{vlCorrecao}"

        if idGuia:
            objeto["content"]["idGuia"] =  { "id": int(idGuia)}
        
        if idDivida:
            objeto["content"]["idDivida"] =  { "id": int(idDivida)}

        if idSaldo:
            objeto["content"]["idSaldo"] =  { "id": int(idSaldo)}
           
        if idReceita:
            objeto["content"]["idReceita"] =  { "id": int(idReceita)}
        
        if idPagamentosDetalhados:
            objeto["content"]["idPagamentosDetalhados"] =  { "id": int(idPagamentosDetalhados)}
        
        if idParcelamentosParcela:
            objeto["content"]["idParcelamentosParcela"] =  { "id": int(idParcelamentosParcela)}
        envio = api_post("compensacoes", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

compensacoes = compensacoes()