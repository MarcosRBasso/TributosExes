from samples import *
import json

class parcelamentosParcelas(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idParcelamentos, nroParcela, dtVctoOriginal, dtVcto, situacao, vlParcela, vlDesconto, valorDescontoTributo, 
                valorDescontoCorrecao, valorDescontoJuro, valorDescontoMulta, vlReforco, vlCorrPrefixada, vlJuroFinanciamento, vlTotalTaxa, possuiReforco, iParcelamentos, 
                parcelaConversao, tipoParcelamentoConversao):
        try:
            sql = """
                INSERT INTO parcelamentosParcelas (                    
                    idIntegracao,                   
                    id_cloud, 
                    idParcelamentos,
                    nroParcela,                                               
                    dtVctoOriginal, 
                    dtVcto,
                    situacao,
                    vlDesconto,
                    valorDescontoTributo,
                    vlParcela,
                    valorDescontoCorrecao,                    
                    valorDescontoJuro,
                    valorDescontoMulta,
                    vlReforco,
                    vlCorrPrefixada,
                    vlJuroFinanciamento,
                    vlTotalTaxa, 
                    possuiReforco, 
                    iParcelamentos, 
                    parcelaConversao, 
                    tipoParcelamentoConversao         
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idParcelamentos)s,
                    %(nroParcela)s,
                    %(dtVctoOriginal)s,
                    %(dtVcto)s,
                    %(situacao)s,
                    %(vlDesconto)s,
                    %(valorDescontoTributo)s,
                    %(vlParcela)s,
                    %(valorDescontoCorrecao)s,                    
                    %(valorDescontoJuro)s,
                    %(valorDescontoMulta)s,
                    %(vlReforco)s,
                    %(vlCorrPrefixada)s,
                    %(vlJuroFinanciamento)s,
                    %(vlTotalTaxa)s, 
                    %(possuiReforco)s, 
                    %(iParcelamentos)s, 
                    %(parcelaConversao)s, 
                    %(tipoParcelamentoConversao)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idParcelamentos = idParcelamentos,
                nroParcela = nroParcela,
                dtVctoOriginal = dtVctoOriginal,                               
                dtVcto = dtVcto,
                situacao = situacao,
                vlDesconto = vlDesconto,                               
                valorDescontoTributo = valorDescontoTributo,
                vlParcela = vlParcela,
                valorDescontoCorrecao = valorDescontoCorrecao,                                               
                valorDescontoJuro = valorDescontoJuro,
                valorDescontoMulta = valorDescontoMulta,                               
                vlReforco = vlReforco,
                vlCorrPrefixada = vlCorrPrefixada,
                vlJuroFinanciamento = vlJuroFinanciamento,
                vlTotalTaxa = vlTotalTaxa, 
                possuiReforco = possuiReforco, 
                iParcelamentos = iParcelamentos, 
                parcelaConversao = parcelaConversao, 
                tipoParcelamentoConversao = tipoParcelamentoConversao
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {parcelamentosParcelas} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {parcelamentosParcelas}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM parcelamentosParcelas"
            if not self.query(sql_s):
                send_log_warning(f"parcelamentosParcelas não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM parcelamentosParcelas WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM parcelamentosParcelas WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    parcelamentosParcelas 
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
            sql = f"SELECT * FROM parcelamentosParcelas WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM parcelamentosParcelas WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM parcelamentosParcelas WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idParcelamentos, nroParcela, dtVctoOriginal, dtVcto, situacao, vlParcela, vlDesconto, valorDescontoTributo, 
                valorDescontoCorrecao, valorDescontoJuro, valorDescontoMulta, vlReforco, vlCorrPrefixada, vlJuroFinanciamento, 
                vlTotalTaxa, possuiReforco, iParcelamentos, parcelaConversao, tipoParcelamentoConversao):
        objeto = {
            "idIntegracao": f"parcelamentosParcelas{id}",
            "content": {}                                 
        }
        if tipoParcelamentoConversao:
            objeto["content"]["tipoParcelamentoConversao"] = f"{tipoParcelamentoConversao}"   

        if idParcelamentos:
            objeto["content"]["idParcelamentos"] = { "id": int(idParcelamentos)}

        if vlTotalTaxa:
            objeto["content"]["vlTotalTaxa"] = f"{vlTotalTaxa}"   

        if possuiReforco:
            objeto["content"]["possuiReforco"] = f"{possuiReforco}"
        
        if iParcelamentos:
            objeto["content"]["iParcelamentos"] = { "id": int(iParcelamentos)}
           
        if parcelaConversao:
            objeto["content"]["parcelaConversao"] = f"{parcelaConversao}"            
        
        if valorDescontoTributo:
            objeto["content"]["valorDescontoTributo"] = f"{valorDescontoTributo}"

        if nroParcela:
            objeto["content"]["nroParcela"] = f"{nroParcela}"           
        
        if dtVcto:
            objeto["content"]["dtVcto"] = f"{dtVcto}" 

        if valorDescontoMulta:
            objeto["content"]["valorDescontoMulta"] = f"{valorDescontoMulta}"  

        if situacao:
            objeto["content"]["situacao"] = f"{situacao}"

        if vlDesconto:
            objeto["content"]["vlDesconto"] = f"{vlDesconto}"   

        if valorDescontoJuro:
            objeto["content"]["valorDescontoJuro"] = f"{valorDescontoJuro}"
        
        if valorDescontoCorrecao:
            objeto["content"]["valorDescontoCorrecao"] = f"{valorDescontoCorrecao}"
           
        if vlReforco:
            objeto["content"]["vlReforco"] = f"{vlReforco}"
        
        if vlJuroFinanciamento:
            objeto["content"]["vlJuroFinanciamento"] = f"{vlJuroFinanciamento}"
        
        if vlParcela:
            objeto["content"]["vlParcela"] = f"{vlParcela}"

        if dtVctoOriginal != None:
            objeto[0]["content"]["dtVctoOriginal"] = f"{dtVctoOriginal}"               

        if vlCorrPrefixada != None:
            objeto[0]["content"]["vlCorrPrefixada"] = f"{vlCorrPrefixada}"        
            
        envio = api_post("parcelamentosParcelas", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

parcelamentosParcelas = parcelamentosParcelas()