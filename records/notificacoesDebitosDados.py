from samples import *
import json

class notificacoesDebitosDados(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idNotificacoesDebitos, idContribuinte, idEnderecoContribuinte, idTelefoneContribuinte, idImovel, idEconomico, idReceitaDiversa, idContribuicaoMelhoria, 
                  idTransferenciaImovel, idNotaAvulsa, unidadeImovel, nomeCorresponsavel, idEnderecoCorresponsavel, idAtividade, idServico, idCreditoTributario, idReceitas, 
                  formaPagamento,
                  idConfigGeracaoParcelas, idGuia, idLancamento, dataVencimento, parcela, situacaoParcela, situacaoLancamento, lancamentoComplementar, apartamentoReferente, 
                  idBairroReferente, cepReferente, complementoReferente, 
                  idCondominioReferente, campo1, campo2, campo3, campo4, campo5, campo6, campo7, campo8, campo9, campo10, idDistritoReferente, inscricaoIncraReferente, idLocalidadeReferente, 
                  idLogradouroReferente, loteReferente, 
                  idLoteamentoReferente, quadraReferente, valorTributoLancamento, valorCorrecaoLancamento, valorJurosLancamento, valorMultaLancamento, valorTributoReceitaLancamento, 
                  valorCorrecaoReceitaLancamento, valorJurosReceitaLancamento, valorMultaReceitaLancamento, 
                  valorTributoParcela, valorCorrecaoParcela, valorJurosParcela, valorMultaParcela, valorTotalParcela, valorTributoReceitaParcela, valorCorrecaoReceitaParcela, 
                  valorJurosReceitaParcela, valorMultaReceitaParcela, valorTotalReceitaParcela):
        try: 
            sql = """
                INSERT INTO notificacoesDebitosDados (                    
                    idIntegracao,                   
                    id_cloud, 
                    idNotificacoesDebitos,
                    idContribuinte,                                               
                    idEnderecoContribuinte, 
                    idTelefoneContribuinte,
                    idImovel,
                    idReceitaDiversa,
                    idContribuicaoMelhoria,
                    idEconomico,
                    idTransferenciaImovel,                    
                    idNotaAvulsa,
                    unidadeImovel,
                    nomeCorresponsavel,
                    idEnderecoCorresponsavel,
                    idAtividade,
                    idServico,
                    idCreditoTributario,
                    idReceitas,
                    formaPagamento,
                    idConfigGeracaoParcelas,
                    idGuia,
                    idLancamento, 
                    dataVencimento,
                    parcela, 
                    situacaoParcela,
                    situacaoLancamento,
                    lancamentoComplementar, 
                    apartamentoReferente, 
                    idBairroReferente,
                    cepReferente,
                    complementoReferente,
                    idCondominioReferente,
                    campo1,
                    campo2,
                    campo3,
                    campo4,
                    campo5, 
                    campo6, 
                    campo7, 
                    campo8, 
                    campo9, 
                    campo10, 
                    idDistritoReferente, 
                    inscricaoIncraReferente, 
                    idLocalidadeReferente, 
                    idLogradouroReferente, 
                    loteReferente, 
                    idLoteamentoReferente, 
                    quadraReferente, 
                    valorTributoLancamento, 
                    valorCorrecaoLancamento, 
                    valorJurosLancamento, 
                    valorMultaLancamento, 
                    valorTributoReceitaLancamento, 
                    valorCorrecaoReceitaLancamento, 
                    valorJurosReceitaLancamento, 
                    valorMultaReceitaLancamento, 
                    valorTributoParcela, 
                    valorCorrecaoParcela, 
                    valorJurosParcela,
                    valorMultaParcela, 
                    valorTotalParcela, 
                    valorTributoReceitaParcela, 
                    valorCorrecaoReceitaParcela, 
                    valorJurosReceitaParcela, 
                    valorMultaReceitaParcela, 
                    valorTotalReceitaParcela
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idNotificacoesDebitos)s,
                    %(idContribuinte)s,
                    %(idEnderecoContribuinte)s,
                    %(idTelefoneContribuinte)s,
                    %(idImovel)s,
                    %(idReceitaDiversa)s,
                    %(idContribuicaoMelhoria)s,
                    %(idEconomico)s,
                    %(idTransferenciaImovel)s,                    
                    %(idNotaAvulsa)s,
                    %(unidadeImovel)s,
                    %(nomeCorresponsavel)s,
                    %(idEnderecoCorresponsavel)s,
                    %(idAtividade)s,
                    %(idServico)s,
                    %(idCreditoTributario)s,
                    %(idConfigGeracaoParcelas)s,
                    %(formaPagamento)s,                    
                    %(idReceitas)s,
                    %(idConfigGeracaoParcelas)s,                    
                    %(idGuia)s,
                    %(idLancamento)s,
                    %(dataVencimento)s,
                    %(parcela)s,
                    %(situacaoParcela)s,
                    %(situacaoLancamento)s,
                    %(lancamentoComplementar)s,
                    %(apartamentoReferente)s,
                    %(idBairroReferente)s,
                    %(cepReferente)s,                    
                    %(complementoReferente)s,
                    %(idCondominioReferente)s,
                    %(campo1)s,
                    %(campo2)s,
                    %(campo3)s,
                    %(campo4)s,
                    %(campo5)s,
                    %(campo6)s,
                    %(campo7)s,
                    %(campo8)s,                    
                    %(campo9)s,
                    %(campo10)s,
                    %(idDistritoReferente)s,
                    %(inscricaoIncraReferente)s,
                    %(idLocalidadeReferente)s,
                    %(idLogradouroReferente)s,
                    %(loteReferente)s,
                    %(idLoteamentoReferente)s,
                    %(quadraReferente)s,                    
                    %(valorTributoLancamento)s,
                    %(valorCorrecaoLancamento)s,
                    %(valorJurosLancamento)s,
                    %(valorMultaLancamento)s,
                    %(valorTributoReceitaLancamento)s,
                    %(valorCorrecaoReceitaLancamento)s,
                    %(valorJurosReceitaLancamento)s,
                    %(valorMultaReceitaLancamento)s,                    
                    %(valorTributoParcela)s,
                    %(valorCorrecaoParcela)s,                    
                    %(valorJurosParcela)s,
                    valorMultaParcela, 
                    valorTotalParcela, 
                    valorTributoReceitaParcela, 
                    valorCorrecaoReceitaParcela, 
                    valorJurosReceitaParcela, 
                    valorMultaReceitaParcela, 
                    valorTotalReceitaParcela
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idNotificacoesDebitos = idNotificacoesDebitos,
                idContribuinte = idContribuinte,
                idEnderecoContribuinte = idEnderecoContribuinte,                               
                idTelefoneContribuinte = idTelefoneContribuinte,
                idImovel = idImovel,
                idReceitaDiversa = idReceitaDiversa,                               
                idContribuicaoMelhoria = idContribuicaoMelhoria,
                idEconomico = idEconomico,
                idTransferenciaImovel = idTransferenciaImovel,                                               
                idNotaAvulsa = idNotaAvulsa,
                unidadeImovel = unidadeImovel,                               
                nomeCorresponsavel = nomeCorresponsavel,
                idEnderecoCorresponsavel = idEnderecoCorresponsavel,
                idAtividade = idAtividade,                               
                idServico = idServico,
                idCreditoTributario = idCreditoTributario,
                idConfigGeracaoParcelas = idConfigGeracaoParcelas,
                formaPagamento = formaPagamento,
                idReceitas = idReceitas,
                idGuia = idGuia,
                idLancamento = idLancamento, 
                dataVencimento = dataVencimento, 
                parcela = parcela, 
                situacaoParcela = situacaoParcela, 
                situacaoLancamento = situacaoLancamento, 
                lancamentoComplementar = lancamentoComplementar, 
                apartamentoReferente = apartamentoReferente, 
                idBairroReferente = idBairroReferente, 
                cepReferente = cepReferente, 
                complementoReferente = complementoReferente, 
                idCondominioReferente = idCondominioReferente, 
                campo1 = campo1, 
                campo2 = campo2,   
                campo3 = campo3, 
                campo4 = campo4, 
                campo5 = campo5, 
                campo6 = campo6, 
                campo7 = campo7, 
                campo8 = campo8, 
                campo9 = campo9, 
                campo10 = campo10, 
                idDistritoReferente = idDistritoReferente, 
                inscricaoIncraReferente = inscricaoIncraReferente, 
                idLocalidadeReferente = idLocalidadeReferente, 
                idLogradouroReferente = idLogradouroReferente, 
                loteReferente = loteReferente, 
                idLoteamentoReferente = idLoteamentoReferente, 
                quadraReferente = quadraReferente, 
                valorTributoLancamento = valorTributoLancamento, 
                valorCorrecaoLancamento =valorCorrecaoLancamento, 
                valorJurosLancamento = valorJurosLancamento, 
                valorMultaLancamento = valorMultaLancamento, 
                valorTributoReceitaLancamento = valorTributoReceitaLancamento, 
                valorCorrecaoReceitaLancamento = valorCorrecaoReceitaLancamento, 
                valorJurosReceitaLancamento = valorJurosReceitaLancamento, 
                valorMultaReceitaLancamento = valorMultaReceitaLancamento, 
                valorTributoParcela = valorTributoParcela, 
                valorCorrecaoParcela = valorCorrecaoParcela, 
                valorJurosParcela = valorJurosParcela,
                valorMultaParcela = valorMultaParcela, 
                valorTotalParcela = valorTotalParcela, 
                valorTributoReceitaParcela = valorTributoReceitaParcela, 
                valorCorrecaoReceitaParcela = valorCorrecaoReceitaParcela, 
                valorJurosReceitaParcela = valorJurosReceitaParcela, 
                valorMultaReceitaParcela = valorMultaReceitaParcela, 
                valorTotalReceitaParcela = valorTotalReceitaParcela
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {notificacoesDebitosDados} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao inserir o anistias {notificacoesDebitosDados}. {contribuintesr}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM notificacoesDebitosDados"
            if not self.query(sql_s):
                send_log_warning(f"notificacoesDebitosDados não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM notificacoesDebitosDados WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de exclusão do atividades econômicas. {contribuintesr}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM notificacoesDebitosDados WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    notificacoesDebitosDados 
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
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de atualização da atividades Economicas. {contribuintesr}")

    def db_search(self, id):
        try:
            sql = f"SELECT * FROM notificacoesDebitosDados WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def db_list(self):
        try:
            sql = "SELECT * FROM notificacoesDebitosDados WHERE id_cloud is null"
            data = self.query(sql)
            if data:
                send_log_info("Consulta de todos os atividades Economicas realizada com sucesso.")
                return data
            return None
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def get_id_cloud(self, id):
        if (id == None):
            return None
        try:
            sql = f"SELECT id_cloud FROM notificacoesDebitosDados WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def send_post(self, id, idNotificacoesDebitos, idContribuinte, idEnderecoContribuinte, idTelefoneContribuinte, idImovel, idEconomico, idReceitaDiversa, idContribuicaoMelhoria, 
                  idTransferenciaImovel, idNotaAvulsa, unidadeImovel, nomeCorresponsavel, idEnderecoCorresponsavel, idAtividade, idServico, idCreditoTributario, idReceitas, formaPagamento,
                  idConfigGeracaoParcelas, idGuia, idLancamento, dataVencimento, parcela, situacaoParcela, situacaoLancamento, lancamentoComplementar, apartamentoReferente, idBairroReferente, cepReferente, complementoReferente, 
                  idCondominioReferente, campo1, campo2, campo3, campo4, campo5, campo6, campo7, campo8, campo9, campo10, idDistritoReferente, inscricaoIncraReferente, idLocalidadeReferente, idLogradouroReferente, loteReferente, 
                  idLoteamentoReferente, quadraReferente, valorTributoLancamento, valorCorrecaoLancamento, valorJurosLancamento, valorMultaLancamento, valorTributoReceitaLancamento, valorCorrecaoReceitaLancamento, valorJurosReceitaLancamento, valorMultaReceitaLancamento, 
                  valorTributoParcela, valorCorrecaoParcela, valorJurosParcela, valorMultaParcela, valorTotalParcela, valorTributoReceitaParcela, valorCorrecaoReceitaParcela, 
                  valorJurosReceitaParcela, valorMultaReceitaParcela, valorTotalReceitaParcela):
        objeto = {
            "idIntegracao": f"Atos{id}",
            "content": {}
        }
        if valorMultaParcela:
            objeto["content"]["valorMultaParcela"] = f"{valorMultaParcela}"
        
        if valorTotalParcela:
            objeto["content"]["valorTotalParcela"] = f"{valorTotalParcela}"
        
        if valorTributoReceitaParcela:
            objeto["content"]["valorTributoReceitaParcela"] = f"{valorTributoReceitaParcela}"
        
        if valorCorrecaoReceitaParcela:
            objeto["content"]["valorCorrecaoReceitaParcela"] = f"{valorCorrecaoReceitaParcela}"
        
        if valorJurosReceitaParcela:
            objeto["content"]["valorJurosReceitaParcela"] = f"{valorJurosReceitaParcela}"
        
        if valorMultaReceitaParcela:
            objeto["content"]["valorMultaReceitaParcela"] = f"{valorMultaReceitaParcela}"
        
        if valorTotalReceitaParcela:
            objeto["content"]["valorTotalReceitaParcela"] = f"{valorTotalReceitaParcela}"

        if idNotificacoesDebitos:
            objeto["content"]["VctoFeriado"] = f"{idNotificacoesDebitos}"
        
        if idEnderecoContribuinte:
            objeto["content"]["idEnderecoContribuinte"] = f"{idEnderecoContribuinte}"
        
        if idContribuinte:
            objeto["content"]["idContribuinte"] = f"{idContribuinte}"
        
        if idTelefoneContribuinte:
            objeto["content"]["idTelefoneContribuinte"] = f"{idTelefoneContribuinte}"
        
        if idServico:
            objeto["content"]["idServico"] = f"{idServico}"
        
        if idCreditoTributario:
            objeto["content"]["idCreditoTributario"] = f"{idCreditoTributario}"
        
        if idImovel:
            objeto["content"]["idImovel"] = f"{idImovel}"
        
        if idReceitaDiversa:
            objeto["content"]["idReceitaDiversa"] = f"{idReceitaDiversa}"
        
        if idReceitas:
            objeto["content"]["idReceitas"] = f"{idReceitas}"       

        if idGuia:
            objeto["content"]["idGuia"] = { "id": int(idGuia) }
        
        if idAtividade:
            objeto["content"]["idAtividade"] = f"{idAtividade}" 

        if formaPagamento:
            objeto["content"]["formaPagamento"] = f"{formaPagamento}"

        if idConfigGeracaoParcelas:
            objeto["content"]["idConfigGeracaoParcelas"] = f"{idConfigGeracaoParcelas}"

        if idEconomico:
            objeto["content"]["idEconomico"] = f"{idEconomico}"     

        if idContribuicaoMelhoria:
            objeto["content"]["idContribuicaoMelhoria"] = f"{idContribuicaoMelhoria}"    

        if idTransferenciaImovel:
            objeto["content"]["idTransferenciaImovel"] = f"{idTransferenciaImovel}"

        if idLoteamentoReferente:
            objeto["content"]["idLoteamentoReferente"] = { "id": int(idLoteamentoReferente) }

        if idNotaAvulsa:
            objeto["content"]["idNotaAvulsa"] = f"{idNotaAvulsa}"

        if unidadeImovel:
            objeto["content"]["unidadeImovel"] = f"{unidadeImovel}"

        if idLancamento:
            objeto["content"]["idLancamento"] = f"{idLancamento}"     

        if dataVencimento:
            objeto["content"]["dataVencimento"] = f"{dataVencimento}"    

        if parcela:
            objeto["content"]["parcela"] = f"{parcela}"

        if situacaoParcela:
            objeto["content"]["situacaoParcela"] = f"{situacaoParcela}"

        if situacaoLancamento:
            objeto["content"]["situacaoLancamento"] = f"{situacaoLancamento}"  

        if lancamentoComplementar:
            objeto["content"]["lancamentoComplementar"] = f"{lancamentoComplementar}"

        if apartamentoReferente:
            objeto["content"]["apartamentoReferente"] = f"{apartamentoReferente}"

        if idBairroReferente:
            objeto["content"]["idBairroReferente"] = f"{idBairroReferente}"

        if cepReferente:
            objeto["content"]["cepReferente"] = f"{cepReferente}"             
        
        if complementoReferente:
            objeto["content"]["complementoReferente"] = f"{complementoReferente}"
        
        if idCondominioReferente:
            objeto["content"]["idCondominioReferente"] = f"{idCondominioReferente}"

        if campo1:
            objeto["content"]["campo1"] = f"{campo1}"    

        if campo2:
            objeto["content"]["campo2"] = f"{campo2}"

        if campo3:
            objeto["content"]["campo3"] = f"{campo3}"

        if campo4:
            objeto["content"]["campo4"] = f"{campo4}"  

        if campo5:
            objeto["content"]["campo5"] = f"{campo5}"

        if campo6:
            objeto["content"]["campo6"] = f"{campo6}"

        if campo7:
            objeto["content"]["campo7"] = f"{campo7}"

        if campo8:
            objeto["content"]["campo8"] = f"{campo8}"             
        
        if campo9:
            objeto["content"]["campo9"] = f"{campo9}"
        
        if campo10:
            objeto["content"]["dataVencimento0"] = f"{campo10}"            
        
        if idDistritoReferente:
            objeto["content"]["idDistritoReferente"] = f"{idDistritoReferente}"
        
        if inscricaoIncraReferente:
            objeto["content"]["inscricaoIncraReferente"] = f"{inscricaoIncraReferente}"
        
        if quadraReferente:
            objeto["content"]["quadraReferente"] = { "id": int(quadraReferente) }
        
        if valorTributoLancamento:
            objeto["content"]["valorTributoLancamento"] = { "id": int(valorTributoLancamento) }
        
        if valorCorrecaoLancamento:
            objeto["content"]["valorCorrecaoLancamento"] = { "id": int(valorCorrecaoLancamento) }

        if valorJurosLancamento:
            objeto["content"]["valorJurosLancamento"] = { "id": int(valorJurosLancamento) }

        if valorTributoReceitaLancamento:
            objeto["content"]["valorTributoReceitaLancamento"] = { "id": int(valorTributoReceitaLancamento) }

        if valorMultaLancamento:
            objeto["content"]["CodCaracteristicas"] = { "id": int(valorMultaLancamento) }            
        
        if idLocalidadeReferente:
            objeto["content"]["idLocalidadeReferente"] = f"{idLocalidadeReferente}",
        
        if idLogradouroReferente:
            objeto["content"]["idLogradouroReferente"] = f"{idLogradouroReferente}"
        
        if loteReferente:
            objeto["content"]["loteReferente"] = f"{loteReferente}" 

        if idEnderecoCorresponsavel != None:
            objeto[0]["calculotributario"]["creditotributario"] = { "id": int(idEnderecoCorresponsavel) }   
        
        if valorCorrecaoReceitaLancamento:
            objeto["content"]["valorCorrecaoReceitaLancamento"] = f"{valorCorrecaoReceitaLancamento}",
        
        if valorJurosReceitaLancamento:
            objeto["content"]["valorJurosReceitaLancamento"] = f"{valorJurosReceitaLancamento}"
        
        if valorMultaReceitaLancamento:
            objeto["content"]["valorMultaReceitaLancamento"] = f"{valorMultaReceitaLancamento}"
        
        if valorTributoParcela:
            objeto["content"]["valorTributoParcela"] = f"{valorTributoParcela}"                       
        
        if valorCorrecaoParcela:
            objeto["content"]["valorCorrecaoParcela"] = f"{valorCorrecaoParcela}"
        
        if valorJurosParcela:
            objeto["content"]["valorJurosParcela"] = f"{valorJurosParcela}"
        
        if nomeCorresponsavel:
            objeto["content"]["nomeCorresponsavel"] = f"{nomeCorresponsavel}"   

        envio = api_post("notificacoesDebitosDados", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

notificacoesDebitosDados = notificacoesDebitosDados()