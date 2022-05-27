from samples import *
import json

class guiasEmitidas(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idDebito, idDivida, idParcela, dataVcto, valorOriginal, valorDevido,
                 valorDesconto, valorBeneficio, valorCorrecao, valorRemidoCorrecao, valorJuro, valorRemidoJuro, valorMulta, valorRemidoMulta, valorDescontoCorrecao, valorDescontoJuros,
                  valorDescontoMulta,
                 valorJuroFinanciamento, valorCorrecaoPrefixada, valorDocumento, numeroBaixa, 
                 codigoBarras, nossoNumero, represNumerica, dataValidade, idConvenio, 
                 idBanco, idAgencia, nroConvenio):
        try:
            sql = """
                INSERT INTO guiasEmitidas (                    
                    idIntegracao,                   
                    id_cloud, 
                    idDebito,
                    idDivida,                                               
                    idParcela, 
                    dataVcto,
                    valorOriginal,
                    valorDevido,
                    valorDesconto,
                    valorBeneficio,
                    valorCorrecao,                    
                    valorRemidoCorrecao,
                    valorJuro,
                    valorRemidoJuro,
                    valorMulta,
                    valorRemidoMulta,
                    valorDescontoCorrecao,
                    valorDescontoJuros,
                    valorDescontoMulta,
                    valorJuroFinanciamento,
                    valorCorrecaoPrefixada,
                    valorDocumento, 
                    numeroBaixa, 
                    codigoBarras, 
                    nossoNumero, 
                    represNumerica, 
                    dataValidade, 
                    idConvenio, 
                    idBanco, 
                    exibirParece,
                    nroConvenio                  
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idDebito)s,
                    %(idDivida)s,
                    %(idParcela)s,
                    %(dataVcto)s,
                    %(valorOriginal)s,
                    %(valorDevido)s,
                    %(valorDesconto)s,
                    %(valorBeneficio)s,
                    %(valorCorrecao)s,                    
                    %(valorRemidoCorrecao)s,
                    %(valorJuro)s,
                    %(valorRemidoJuro)s,
                    %(valorMulta)s,
                    %(valorRemidoMulta)s,
                    %(valorDescontoCorrecao)s,
                    %(valorDescontoJuros)s,
                    %(valorCorrecaoPrefixada)s,
                    %(valorJuroFinanciamento)s,                    
                    %(valorDescontoMulta)s,
                    %(valorDocumento)s,
                    %(numeroBaixa)s,
                    %(codigoBarras)s,
                    %(nossoNumero)s,
                    %(represNumerica)s,
                    %(dataValidade)s,
                    %(idConvenio)s,
                    %(idBanco)s,                    
                    %(exibirParece)s,
                    %(nroConvenio)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idDebito = idDebito,
                idDivida = idDivida,
                idParcela = idParcela,                               
                dataVcto = dataVcto,
                valorOriginal = valorOriginal,
                valorDevido = valorDevido,                               
                valorDesconto = valorDesconto,
                valorBeneficio = valorBeneficio,
                valorCorrecao = valorCorrecao,                                               
                valorRemidoCorrecao = valorRemidoCorrecao,
                valorJuro = valorJuro,                               
                valorRemidoJuro = valorRemidoJuro,
                valorMulta = valorMulta,
                valorRemidoMulta = valorRemidoMulta,                               
                valorDescontoCorrecao = valorDescontoCorrecao,
                valorDescontoJuros = valorDescontoJuros,
                valorCorrecaoPrefixada = valorCorrecaoPrefixada,
                valorJuroFinanciamento = valorJuroFinanciamento,
                valorDescontoMulta = valorDescontoMulta,
                valorDocumento = valorDocumento, 
                numeroBaixa = numeroBaixa, 
                codigoBarras = codigoBarras, 
                nossoNumero = nossoNumero, 
                represNumerica = represNumerica, 
                dataValidade = dataValidade, 
                idConvenio = idConvenio, 
                idBanco = idBanco, 
                idAgencia = idAgencia,
                nroConvenio = nroConvenio

            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {guiasEmitidas} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao inserir o anistias {guiasEmitidas}. {intervaloFimr}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM guiasEmitidas"
            if not self.query(sql_s):
                send_log_warning(f"guiasEmitidas não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM guiasEmitidas WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao executar a operação de exclusão do atividades econômicas. {intervaloFimr}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM guiasEmitidas WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    guiasEmitidas 
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
            sql = f"SELECT * FROM guiasEmitidas WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao executar a operação de busca. {intervaloFimr}")

    def db_list(self):
        try:
            sql = "SELECT * FROM guiasEmitidas WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM guiasEmitidas WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao executar a operação de busca. {intervaloFimr}")

    def send_post(self, id, idDebito, idDivida, idParcela, dataVcto, valorOriginal, valorBeneficio, valorDevido, valorDesconto, valorCorrecao, valorRemidoCorrecao, 
                 valorJuro, valorRemidoJuro, valorMulta, valorRemidoMulta, valorDescontoCorrecao, valorDescontoJuros, valorDescontoMulta, valorJuroFinanciamento, 
                 valorCorrecaoPrefixada, valorDocumento, numeroBaixa, codigoBarras, 
                 nossoNumero, represNumerica, dataValidade, idConvenio, idBanco, 
                 idAgencia, nroConvenio):
        objeto = {
                    "idIntegracao": f"Atos{id}",
                    "content": {}
        }

        if nroConvenio:
            objeto["content"]["nroConvenio"] = f"{nroConvenio}"

        if nossoNumero:
            objeto["content"]["nossoNumero"] = { "id": int(nossoNumero)}

        if dataValidade:
            objeto["content"]["dataValidade"] = f"{dataValidade}"

        if idConvenio:
            objeto["content"]["idConvenio"] = { "id": int(idConvenio)}

        if idBanco:
            objeto["content"]["idBanco"] = { "id": int(idBanco)}    

        if idAgencia:
            objeto["content"]["idAgencia"] = { "id": int(idAgencia)}

        if represNumerica:
            objeto["content"]["idAgenciaMedida"] = { "id": int(represNumerica) }

        if idDebito:
            objeto["content"]["idDebito"] = { "id": int(idDebito)}

        if codigoBarras:
            objeto["content"]["codigoBarras"] = { "id": int(codigoBarras)}

        if valorDocumento:
            objeto["content"]["valorDocumento"] = f"{valorDocumento}"

        if numeroBaixa:
            objeto["content"]["numeroBaixa"] = f"{numeroBaixa}"

        if valorBeneficio:
            objeto["content"]["valorBeneficio"] = f"{valorBeneficio}"

        if valorDesconto:
            objeto["content"]["compartilhadoContribuinteMelhorias"] = f"{valorDesconto}"

        if valorRemidoCorrecao:
            objeto["content"]["valorRemidoCorrecao"] = f"{valorRemidoCorrecao}"     

        if valorJuro:
            objeto["content"]["valorJuro"] = f"{valorJuro}"

        if valorRemidoJuro:
            objeto["content"]["valorRemidoJuro"] = f"{valorRemidoJuro}"

        if valorCorrecaoPrefixada:
            objeto["content"]["valorCorrecaoPrefixada"] = f"{valorCorrecaoPrefixada}"

        if valorCorrecao:
            objeto["content"]["valorCorrecao"] = f"{valorCorrecao}"             
        
        if dataVcto:
            objeto["content"]["dataVcto"] = f"{dataVcto}"
        
        if valorMulta:
            objeto["content"]["valorMulta"] = f"{valorMulta}"
        
        if idDivida:
            objeto["content"]["idDivida"] = { "id": int(idDivida)}
        
        if idParcela:
            objeto["content"]["idParcela"] = { "id": int(idParcela)}
        
        if valorDescontoCorrecao:
            objeto["content"]["CasasDecimais"] = f"{valorDescontoCorrecao}"
        
        if valorDescontoJuros:
            objeto["content"]["MaximoDigitos"] = f"{valorDescontoJuros}"
        
        if valorOriginal:
            objeto["content"]["valorOriginals"] = f"{valorOriginal}"
        
        if valorDevido:
            objeto["content"]["CompartilhadoCondominio"] = f"{valorDevido}"
        
        if valorDescontoMulta:
            objeto["content"]["valorDescontoMulta"] = f"{valorDescontoMulta}"
        
        if valorRemidoMulta:
            objeto["content"]["LivroEletronico"] = f"{valorRemidoMulta}"
        
        if valorJuroFinanciamento:
            objeto["content"]["valorJuroFinanciamento"] = f"{valorJuroFinanciamento}"

        envio = api_post("guiasEmitidas", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

guiasEmitidas = guiasEmitidas()