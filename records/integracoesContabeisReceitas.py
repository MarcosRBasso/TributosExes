from samples import *
import json

class integracoesContabeisReceitas(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idCreditosTributarios, idIntegracoesContabeis, idReceitas, ano, comentario, situacao,
                 valorCorrecaoPreFixada, valorDescontoCorrecao, valorCorrecao, valorDescontoJuros, valorDescontoMulta, valorDescontoTributo, valorDiferenca, valorDiferencaCorrecao, 
                 valorDiferencaMulta, 
                 valorCorrecaoPreFixadaJuros, valorDiferencaTributo, valorImunidade, valorIncentivoFiscal, valorIsencoes, valorJuros, 
                 valorJurosFinancimento, valorMulta, valorRemissao, valorTotalPago, valorTributo):
        try:
            sql = """
                INSERT INTO integracoesContabeisReceitas (                    
                    idIntegracao,                   
                    id_cloud, 
                    idCreditosTributarios,
                    idIntegracoesContabeis,                                               
                    idReceitas, 
                    ano,
                    comentario,
                    situacao,
                    valorCorrecaoPreFixada,
                    valorDescontoCorrecao,
                    valorCorrecao,                    
                    valorDescontoJuros,
                    valorDescontoMulta,
                    valorDescontoTributo,
                    valorDiferenca,
                    valorDiferencaCorrecao,
                    valorDiferencaMulta,
                    valorCorrecaoPreFixadaJuros,
                    valorDiferencaTributo,
                    valorImunidade,
                    valorIncentivoFiscal,
                    valorIsencoes, 
                    valorJuros, 
                    valorJurosFinancimento, 
                    valorMulta, 
                    valorRemissao, 
                    valorTotalPago, 
                    valorTributo                 
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idCreditosTributarios)s,
                    %(idIntegracoesContabeis)s,
                    %(idReceitas)s,
                    %(ano)s,
                    %(comentario)s,
                    %(situacao)s,
                    %(valorCorrecaoPreFixada)s,
                    %(valorDescontoCorrecao)s,
                    %(valorCorrecao)s,                    
                    %(valorDescontoJuros)s,
                    %(valorDescontoMulta)s,
                    %(valorDescontoTributo)s,
                    %(valorDiferenca)s,
                    %(valorDiferencaCorrecao)s,
                    %(valorDiferencaMulta)s,
                    %(valorCorrecaoPreFixadaJuros)s,
                    %(valorIncentivoFiscal)s,
                    %(valorImunidade)s,                    
                    %(valorDiferencaTributo)s,
                    %(valorIsencoes)s,
                    %(valorJuros)s,
                    %(valorJurosFinancimento)s,
                    %(valorMulta)s,
                    %(valorRemissao)s,
                    %(valorTotalPago)s,
                    %(valorTributo)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idCreditosTributarios = idCreditosTributarios,
                idIntegracoesContabeis = idIntegracoesContabeis,
                idReceitas = idReceitas,                               
                ano = ano,
                comentario = comentario,
                situacao = situacao,                               
                valorCorrecaoPreFixada = valorCorrecaoPreFixada,
                valorDescontoCorrecao = valorDescontoCorrecao,
                valorCorrecao = valorCorrecao,                                               
                valorDescontoJuros = valorDescontoJuros,
                valorDescontoMulta = valorDescontoMulta,                               
                valorDescontoTributo = valorDescontoTributo,
                valorDiferenca = valorDiferenca,
                valorDiferencaCorrecao = valorDiferencaCorrecao,                               
                valorDiferencaMulta = valorDiferencaMulta,
                valorCorrecaoPreFixadaJuros = valorCorrecaoPreFixadaJuros,
                valorIncentivoFiscal = valorIncentivoFiscal,
                valorImunidade = valorImunidade,
                valorDiferencaTributo = valorDiferencaTributo,
                valorIsencoes = valorIsencoes, 
                valorJuros = valorJuros, 
                valorJurosFinancimento = valorJurosFinancimento, 
                valorMulta = valorMulta, 
                valorRemissao = valorRemissao, 
                valorTotalPago = valorTotalPago, 
                valorTributo = valorTributo

            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {integracoesContabeisReceitas} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao inserir o anistias {integracoesContabeisReceitas}. {intervaloFimr}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM integracoesContabeisReceitas"
            if not self.query(sql_s):
                send_log_warning(f"integracoesContabeisReceitas não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM integracoesContabeisReceitas WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao executar a operação de exclusão do atividades econômicas. {intervaloFimr}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM integracoesContabeisReceitas WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    integracoesContabeisReceitas 
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
            sql = f"SELECT * FROM integracoesContabeisReceitas WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao executar a operação de busca. {intervaloFimr}")

    def db_list(self):
        try:
            sql = "SELECT * FROM integracoesContabeisReceitas WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM integracoesContabeisReceitas WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao executar a operação de busca. {intervaloFimr}")

    def send_post(self, id, idCreditosTributarios, idIntegracoesContabeis, idReceitas, ano, comentario, valorDescontoCorrecao, situacao, valorCorrecaoPreFixada, valorCorrecao, valorDescontoJuros, 
                 valorDescontoMulta, valorDescontoTributo, valorDiferenca, valorDiferencaCorrecao, valorDiferencaMulta, valorCorrecaoPreFixadaJuros, valorDiferencaTributo, valorImunidade, 
                 valorIncentivoFiscal, valorIsencoes, valorJuros, valorJurosFinancimento, 
                 valorMulta, valorRemissao, valorTotalPago, valorTributo):
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

        if valorRemissao:
            objeto["content"]["idAgenciaMedida"] = f"{valorRemissao}"

        if idCreditosTributarios:
            objeto["content"]["idCreditosTributarios"] = { "id": int(idCreditosTributarios)}

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
        
        if ano:
            objeto["content"]["ano"] = f"{ano}"
        
        if valorDiferenca:
            objeto["content"]["valorDiferenca"] = f"{valorDiferenca}"
        
        if idIntegracoesContabeis:
            objeto["content"]["idIntegracoesContabeis"] = { "id": int(idIntegracoesContabeis)}
        
        if idReceitas:
            objeto["content"]["idReceitas"] = { "id": int(idReceitas)}
        
        if valorDiferencaMulta:
            objeto["content"]["CasasDecimais"] = f"{valorDiferencaMulta}"
        
        if valorCorrecaoPreFixadaJuros:
            objeto["content"]["MaximoDigitos"] = f"{valorCorrecaoPreFixadaJuros}"
        
        if comentario:
            objeto["content"]["comentarios"] = f"{comentario}"
        
        if situacao:
            objeto["content"]["CompartilhadoCondominio"] = f"{situacao}"
        
        if valorDiferencaTributo:
            objeto["content"]["valorDiferencaTributo"] = f"{valorDiferencaTributo}"
        
        if valorDiferencaCorrecao:
            objeto["content"]["LivroEletronico"] = f"{valorDiferencaCorrecao}"
        
        if valorImunidade:
            objeto["content"]["valorImunidade"] = f"{valorImunidade}"

        envio = api_post("integracoesContabeisReceitas", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

integracoesContabeisReceitas = integracoesContabeisReceitas()