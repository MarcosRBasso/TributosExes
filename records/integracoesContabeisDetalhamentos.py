from samples import *
import json

class integracoesContabeisDetalhamentos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idGuias, idDivida, idIntegracoesContabeis, idPagamentos, idReceitas, situacao,
                 valorCorrecaoPreFixada, valorDescontoCorrecao, valorCorrecao, valorDescontoJuros, valorDescontoMulta, valorDescontoTributo, valorDiferenca, valorDiferencaCorrecao,
                 valorDiferencaJuros, 
                 valorDiferencaMulta, valorDiferencaTributo, valorImunidade, valorIncentivoFiscal, valorIsencoes, valorJuros, valorJurosFinancimento, valorMulta, valorRemissao, 
                 valorTotalPago, valorTributo, identificacaoIntegracaoOrigem):
        try:
            sql = """
                INSERT INTO integracoesContabeisDetalhamentos (                    
                    idIntegracao,                   
                    id_cloud, 
                    idGuias,
                    idDivida,                                               
                    idIntegracoesContabeis, 
                    idPagamentos,
                    idReceitas,
                    situacao,
                    valorIncentivoFiscal,
                    valorDescontoCorrecao,
                    valorCorrecao,                    
                    valorDescontoJuros,
                    valorDescontoMulta,
                    valorDescontoTributo,
                    valorDiferenca,
                    valorDiferencaCorrecao,
                    valorDiferencaJuros,
                    valorDiferencaMulta,
                    valorDiferencaTributo,
                    valorImunidade,
                    valorCorrecaoPrefixada,
                    valorIsencoes, 
                    valorJuros, 
                    valorJurosFinancimento, 
                    valorMulta, 
                    valorRemissao, 
                    valorTotalPago, 
                    valorTributo, 
                    identificacaoIntegracaoOrigem
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idGuias)s,
                    %(idDivida)s,
                    %(idIntegracoesContabeis)s,
                    %(idPagamentos)s,
                    %(idReceitas)s,
                    %(situacao)s,
                    %(valorCorrecaoPreFixada)s,
                    %(valorDescontoCorrecao)s,
                    %(valorCorrecao)s,                    
                    %(valorDescontoJuros)s,
                    %(valorDescontoMulta)s,
                    %(valorDescontoTributo)s,
                    %(valorDiferenca)s,
                    %(valorDiferencaCorrecao)s,
                    %(valorDiferencaJuros)s,
                    %(valorDiferencaMulta)s,
                    %(valorIncentivoFiscal)s,
                    %(valorImunidade)s,                    
                    %(valorDiferencaTributo)s,
                    %(valorIsencoes)s,
                    %(valorJuros)s,
                    %(valorJurosFinancimento)s,
                    %(valorMulta)s,
                    %(valorRemissao)s,
                    %(valorTotalPago)s,
                    %(valorTributo)s,
                    %(identificacaoIntegracaoOrigem)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idGuias = idGuias,
                idDivida = idDivida,
                idIntegracoesContabeis = idIntegracoesContabeis,                               
                idPagamentos = idPagamentos,
                idReceitas = idReceitas,
                situacao = situacao,                               
                valorCorrecaoPreFixada = valorCorrecaoPreFixada,
                valorDescontoCorrecao = valorDescontoCorrecao,
                valorCorrecao = valorCorrecao,                                               
                valorDescontoJuros = valorDescontoJuros,
                valorDescontoMulta = valorDescontoMulta,                               
                valorDescontoTributo = valorDescontoTributo,
                valorDiferenca = valorDiferenca,
                valorDiferencaCorrecao = valorDiferencaCorrecao,                               
                valorDiferencaJuros = valorDiferencaJuros,
                valorDiferencaMulta = valorDiferencaMulta,
                valorIncentivoFiscal = valorIncentivoFiscal,
                valorImunidade = valorImunidade,
                valorDiferencaTributo = valorDiferencaTributo,
                valorIsencoes = valorIsencoes, 
                valorJuros = valorJuros, 
                valorJurosFinancimento = valorJurosFinancimento, 
                valorMulta = valorMulta, 
                valorRemissao = valorRemissao, 
                valorTotalPago = valorTotalPago, 
                valorTributo = valorTributo, 
                identificacaoIntegracaoOrigem = identificacaoIntegracaoOrigem

            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {integracoesContabeisDetalhamentos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao inserir o anistias {integracoesContabeisDetalhamentos}. {intervaloFimr}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM integracoesContabeisDetalhamentos"
            if not self.query(sql_s):
                send_log_warning(f"integracoesContabeisDetalhamentos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM integracoesContabeisDetalhamentos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao executar a operação de exclusão do atividades econômicas. {intervaloFimr}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM integracoesContabeisDetalhamentos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    integracoesContabeisDetalhamentos 
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
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao executar a operação de atualização da atividades Economicas. {intervaloFimr}")

    def db_search(self, id):
        try:
            sql = f"SELECT * FROM integracoesContabeisDetalhamentos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao executar a operação de busca. {intervaloFimr}")

    def db_list(self):
        try:
            sql = "SELECT * FROM integracoesContabeisDetalhamentos WHERE id_cloud is null"
            data = self.query(sql)
            if data:
                send_log_info("Consulta de todos os atividades Economicas realizada com sucesso.")
                return data
            return None
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao executar a operação de busca. {intervaloFimr}")

    def get_id_cloud(self, id):
        if (id == None):
            return None
        try:
            sql = f"SELECT id_cloud FROM integracoesContabeisDetalhamentos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao executar a operação de busca. {intervaloFimr}")

    def send_post(self, id, idGuias, idDivida, idIntegracoesContabeis, idPagamentos, idReceitas, valorDescontoCorrecao, situacao, valorCorrecaoPreFixada, valorCorrecao, valorDescontoJuros, 
                 valorDescontoMulta, valorDescontoTributo, valorDiferenca, valorDiferencaCorrecao, valorDiferencaJuros, valorDiferencaMulta, valorDiferencaTributo, valorImunidade, 
                 valorIncentivoFiscal, valorIsencoes, valorJuros, valorJurosFinancimento, 
                 valorMulta, valorRemissao, valorTotalPago, valorTributo, identificacaoIntegracaoOrigem):
        objeto = {
                    "idIntegracao": f"Atos{id}",
                    "content": {}
        }

        if valorMulta:
            objeto["content"]["valorMulta"] = f"{valorMulta}"

        if valorTotalPago:
            objeto["content"]["valorTotalPago"] = f"{valorTotalPago}"

        if valorTributo:
            objeto["content"]["valorTributo"] = f"{valorTributo}"

        if identificacaoIntegracaoOrigem:
            objeto["content"]["identificacaoIntegracaoOrigem"] = { "id": int(identificacaoIntegracaoOrigem)}  

        if valorRemissao:
            objeto["content"]["idAgenciaMedida"] = f"{valorRemissao}"

        if idGuias:
            objeto["content"]["idGuias"] = { "id": int(idGuias)}

        if valorJurosFinancimento:
            objeto["content"]["valorJurosFinancimento"] = f"{valorJurosFinancimento}"

        if valorIsencoes:
            objeto["content"]["valorIsencoes"] = f"{valorIsencoes}"

        if valorJuros:
            objeto["content"]["valorJuros"] = f"{valorJuros}"

        if valorDescontoCorrecao:
            objeto["content"]["valorDescontoCorrecao"] = f"{valorDescontoCorrecao}"

        if valorCorrecaoPreFixada:
            objeto["content"]["compartilhadoContribuinteMelhorias"] = f"{valorCorrecaoPreFixada}"

        if valorDescontoJuros:
            objeto["content"]["valorDescontoJuros"] = f"{valorDescontoJuros}"     

        if valorDescontoMulta:
            objeto["content"]["valorDescontoMulta"] = f"{valorDescontoMulta}"

        if valorDescontoTributo:
            objeto["content"]["valorDescontoTributo"] = f"{valorDescontoTributo}"

        if valorIncentivoFiscal:
            objeto["content"]["valorIncentivoFiscal"] = f"{valorIncentivoFiscal}"

        if valorCorrecao:
            objeto["content"]["valorCorrecao"] = f"{valorCorrecao}"             
        
        if idPagamentos:
            objeto["content"]["idPagamentos"] = { "id": int(idPagamentos)}
        
        if valorDiferenca:
            objeto["content"]["valorDiferenca"] = f"{valorDiferenca}"
        
        if idDivida:
            objeto["content"]["idDivida"] = { "id": int(idDivida)}
        
        if idIntegracoesContabeis:
            objeto["content"]["idIntegracoesContabeis"] = { "id": int(idIntegracoesContabeis)}
        
        if valorDiferencaJuros:
            objeto["content"]["CasasDecimais"] = f"{valorDiferencaJuros}"
        
        if valorDiferencaMulta:
            objeto["content"]["MaximoDigitos"] = f"{valorDiferencaMulta}"
        
        if idReceitas:
            objeto["content"]["idReceitass"] = { "id": int(idReceitas)}
        
        if situacao:
            objeto["content"]["CompartilhadoCondominio"] = f"{situacao}"
        
        if valorDiferencaTributo:
            objeto["content"]["valorDiferencaTributo"] = f"{valorDiferencaTributo}"
        
        if valorDiferencaCorrecao:
            objeto["content"]["LivroEletronico"] = f"{valorDiferencaCorrecao}"
        
        if valorImunidade:
            objeto["content"]["valorImunidade"] = f"{valorImunidade}"

        envio = api_post("integracoesContabeisDetalhamentos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

integracoesContabeisDetalhamentos = integracoesContabeisDetalhamentos()