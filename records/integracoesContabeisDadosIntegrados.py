from samples import *
import json

class integracoesContabeisDadosIntegrados(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idLoteIntegracao, identIntegracaoEstornada, idIntegracoesContabeis, agencia, banco, cnpj, dataIntegracao, digitoAgencia, 
                digitoConta, exercicio, formasRecebimento, nomeEntidade, numeroConta, situacaoIntegracao, tipoProcessamentoDivida, valorLote):
        try:
            sql = """
                INSERT INTO integracoesContabeisDadosIntegrados (                    
                    idIntegracao,                   
                    id_cloud, 
                    idLoteIntegracao,
                    identIntegracaoEstornada,                                               
                    idIntegracoesContabeis, 
                    agencia,
                    banco,
                    dataIntegracao,
                    digitoAgencia,
                    cnpj,
                    digitoConta,                    
                    exercicio,
                    formasRecebimento,
                    nomeEntidade,
                    numeroConta,
                    situacaoIntegracao,
                    tipoProcessamentoDivida,
                    valorLote                
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idLoteIntegracao)s,
                    %(identIntegracaoEstornada)s,
                    %(idIntegracoesContabeis)s,
                    %(agencia)s,
                    %(banco)s,
                    %(dataIntegracao)s,
                    %(digitoAgencia)s,
                    %(cnpj)s,
                    %(digitoConta)s,                    
                    %(exercicio)s,
                    %(formasRecebimento)s,
                    %(nomeEntidade)s,
                    %(numeroConta)s,
                    %(situacaoIntegracao)s,
                    %(tipoProcessamentoDivida)s,
                    %(valorLote)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idLoteIntegracao = idLoteIntegracao,
                identIntegracaoEstornada = identIntegracaoEstornada,
                idIntegracoesContabeis = idIntegracoesContabeis,                               
                agencia = agencia,
                banco = banco,
                dataIntegracao = dataIntegracao,                               
                digitoAgencia = digitoAgencia,
                cnpj = cnpj,
                digitoConta = digitoConta,                                               
                exercicio = exercicio,
                formasRecebimento = formasRecebimento,                               
                nomeEntidade = nomeEntidade,
                numeroConta = numeroConta,
                situacaoIntegracao = situacaoIntegracao,                               
                tipoProcessamentoDivida = tipoProcessamentoDivida,
                valorLote = valorLote
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {integracoesContabeisDadosIntegrados} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {integracoesContabeisDadosIntegrados}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM integracoesContabeisDadosIntegrados"
            if not self.query(sql_s):
                send_log_warning(f"integracoesContabeisDadosIntegrados não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM integracoesContabeisDadosIntegrados WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM integracoesContabeisDadosIntegrados WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    integracoesContabeisDadosIntegrados 
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
            sql = f"SELECT * FROM integracoesContabeisDadosIntegrados WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM integracoesContabeisDadosIntegrados WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM integracoesContabeisDadosIntegrados WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idLoteIntegracao, identIntegracaoEstornada, idIntegracoesContabeis, agencia, banco, cnpj, dataIntegracao, digitoAgencia, 
                digitoConta, exercicio, formasRecebimento, nomeEntidade, numeroConta, situacaoIntegracao, tipoProcessamentoDivida, valorLote):
        objeto = {
            "idIntegracao": f"integracoesContabeisDadosIntegrados{id}",
            "content": {}                                 
        }
        if valorLote:
            objeto["content"]["valorLote"] = f"{valorLote}"

        if idLoteIntegracao:
            objeto["content"]["idLoteIntegracao"] = { "id": int(idLoteIntegracao)}
        
        if digitoAgencia:
            objeto["content"]["digitoAgencia"] = f"{digitoAgencia}"

        if identIntegracaoEstornada:
            objeto["content"]["identIntegracaoEstornada"] = { "id": int(identIntegracaoEstornada)}
        
        if agencia:
            objeto["content"]["agencia"] = f"{agencia}" 

        if formasRecebimento:
            objeto["content"]["formasRecebimento"] = f"{formasRecebimento}"  

        if tipoProcessamentoDivida:
            objeto["content"]["tipoProcessamentoDivida"] = f"{tipoProcessamentoDivida}"       
       
        if banco:
            objeto["content"]["banco"] = f"{banco}"

        if dataIntegracao:
            objeto["content"]["dataIntegracao"] = f"{dataIntegracao}"   

        if exercicio:
            objeto["content"]["exercicio"] = f"{exercicio}"
        
        if digitoConta:
            objeto["content"]["digitoConta"] = f"{digitoConta}"
           
        if nomeEntidade:
            objeto["content"]["nomeEntidade"] = f"{nomeEntidade}"
        
        if situacaoIntegracao:
            objeto["content"]["situacaoIntegracao"] = f"{situacaoIntegracao}"

        if cnpj:
            objeto["content"]["cnpj"] = f"{cnpj}"

        if idIntegracoesContabeis != None:
            objeto[0]["content"]["idIntegracoesContabeis"] = { "id": int(idIntegracoesContabeis)}               

        if numeroConta != None:
            objeto[0]["content"]["numeroConta"] = f"{numeroConta}"  
            
        envio = api_post("integracoesContabeisDadosIntegrados", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

integracoesContabeisDadosIntegrados = integracoesContabeisDadosIntegrados()