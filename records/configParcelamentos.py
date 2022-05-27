from samples import *
import json

class configParcelamentos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idAto, idScriptDesconto, idScriptJurosFinanciamento, descricao, dtValidadeFinal, dtValidadeInicial, dtVencimentoFinal, 
                  dtVencimentoInicial, qtdDiasPrimeiroVcto, qtdDiasVencidos, qtdMaxParcelas, qtdParcelasAlternadas, qtdParcelasConsecutivas, vlMinimoFisica, vlMinimoJuridica,
                  percEntrada, percRenda, aplicacaoAcrescimos, cancelamentoLote, formulaAntecipacao, intervaloVctoParcelas, 
                  cancelarPorDias, cobrarJuros, definirVlMaxRenda, editarDataParcela, exigirEntrada, removerTaxasManual, reparcelarParcelamento, revogarParcelaDesconto, 
                  inserirTaxasManual, manterAnistiaDivida, parcelamentoGerado, permitirIncentivosFiscais, 
                  permitirManutencaoLancamento, permitirParcelaSemCpf, tipoLancamento, tiposDividas, aplicarValorMinimo, vencimentoLancamento):
        try:
            sql = """
                INSERT INTO configParcelamentos (                    
                    idIntegracao,                   
                    id_cloud, 
                    idAto,
                    idScriptDesconto,                                               
                    idScriptJurosFinanciamento, 
                    descricao,
                    dtValidadeFinal,
                    dtValidadeInicial,
                    dtVencimentoFinal,
                    dtVencimentoInicial,
                    qtdDiasPrimeiroVcto,                    
                    qtdDiasVencidos,
                    qtdMaxParcelas,
                    qtdParcelasAlternadas,
                    qtdParcelasConsecutivas,
                    vlMinimoFisica,
                    vlMinimoJuridica,
                    percEntrada,
                    percRenda,
                    aplicacaoAcrescimos,
                    cancelamentoLote,
                    formulaAntecipacao, 
                    intervaloVctoParcelas, 
                    cancelarPorDias, 
                    cobrarJuros, 
                    definirVlMaxRenda, 
                    editarDataParcela, 
                    exigirEntrada, 
                    removerTaxasManual, 
                    exibirParece,
                    revogarParcelaDesconto, 
                    inserirTaxasManual, 
                    manterAnistiaDivida, 
                    parcelamentoGerado, 
                    permitirIncentivosFiscais, 
                    permitirManutencaoLancamento, 
                    permitirParcelaSemCpf, 
                    tipoLancamento, 
                    tiposDividas, 
                    aplicarValorMinimo, 
                    vencimentoLancamento              
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idAto)s,
                    %(idScriptDesconto)s,
                    %(idScriptJurosFinanciamento)s,
                    %(descricao)s,
                    %(dtValidadeFinal)s,
                    %(dtValidadeInicial)s,
                    %(dtVencimentoFinal)s,
                    %(dtVencimentoInicial)s,
                    %(qtdDiasPrimeiroVcto)s,                    
                    %(qtdDiasVencidos)s,
                    %(qtdMaxParcelas)s,
                    %(qtdParcelasAlternadas)s,
                    %(qtdParcelasConsecutivas)s,
                    %(vlMinimoFisica)s,
                    %(vlMinimoJuridica)s,
                    %(percEntrada)s,
                    %(cancelamentoLote)s,
                    %(aplicacaoAcrescimos)s,                    
                    %(percRenda)s,
                    %(formulaAntecipacao)s,
                    %(intervaloVctoParcelas)s,
                    %(cancelarPorDias)s,
                    %(cobrarJuros)s,
                    %(definirVlMaxRenda)s,
                    %(editarDataParcela)s,
                    %(exigirEntrada)s,
                    %(removerTaxasManual)s,                    
                    %(exibirParece)s,
                    %(revogarParcelaDesconto)s, 
                    %(inserirTaxasManual)s, 
                    %(manterAnistiaDivida)s, 
                    %(parcelamentoGerado)s, 
                    %(permitirIncentivosFiscais)s, 
                    %(permitirManutencaoLancamento)s, 
                    %(permitirParcelaSemCpf)s, 
                    %(tipoLancamento)s, 
                    %(tiposDividas)s, 
                    %(aplicarValorMinimo)s, 
                    %(vencimentoLancamento)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idAto = idAto,
                idScriptDesconto = idScriptDesconto,
                idScriptJurosFinanciamento = idScriptJurosFinanciamento,                               
                descricao = descricao,
                dtValidadeFinal = dtValidadeFinal,
                dtValidadeInicial = dtValidadeInicial,                               
                dtVencimentoFinal = dtVencimentoFinal,
                dtVencimentoInicial = dtVencimentoInicial,
                qtdDiasPrimeiroVcto = qtdDiasPrimeiroVcto,                                               
                qtdDiasVencidos = qtdDiasVencidos,
                qtdMaxParcelas = qtdMaxParcelas,                               
                qtdParcelasAlternadas = qtdParcelasAlternadas,
                qtdParcelasConsecutivas = qtdParcelasConsecutivas,
                vlMinimoFisica = vlMinimoFisica,                               
                vlMinimoJuridica = vlMinimoJuridica,
                percEntrada = percEntrada,
                cancelamentoLote = cancelamentoLote,
                aplicacaoAcrescimos = aplicacaoAcrescimos,
                percRenda = percRenda,
                formulaAntecipacao = formulaAntecipacao, 
                intervaloVctoParcelas = intervaloVctoParcelas, 
                cancelarPorDias = cancelarPorDias, 
                cobrarJuros = cobrarJuros, 
                definirVlMaxRenda = definirVlMaxRenda, 
                editarDataParcela = editarDataParcela, 
                exigirEntrada = exigirEntrada, 
                removerTaxasManual = removerTaxasManual, 
                reparcelarParcelamento = reparcelarParcelamento,
                revogarParcelaDesconto = revogarParcelaDesconto,                  
                inserirTaxasManual = inserirTaxasManual, 
                manterAnistiaDivida = manterAnistiaDivida,  
                parcelamentoGerado = parcelamentoGerado, 
                permitirIncentivosFiscais = permitirIncentivosFiscais, 
                permitirManutencaoLancamento = permitirManutencaoLancamento, 
                permitirParcelaSemCpf = permitirParcelaSemCpf, 
                tipoLancamento = tipoLancamento, 
                tiposDividas = tiposDividas, 
                aplicarValorMinimo = aplicarValorMinimo, 
                vencimentoLancamento = vencimentoLancamento
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {configParcelamentos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as idLogradouroEnderecor:
            send_log_error(f"idLogradouroEndereco ao inserir o anistias {configParcelamentos}. {idLogradouroEnderecor}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM configParcelamentos"
            if not self.query(sql_s):
                send_log_warning(f"configParcelamentos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM configParcelamentos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as idLogradouroEnderecor:
            send_log_error(f"idLogradouroEndereco ao executar a operação de exclusão do atividades econômicas. {idLogradouroEnderecor}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM configParcelamentos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    configParcelamentos 
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
        except Exception as idLogradouroEnderecor:
            send_log_error(f"idLogradouroEndereco ao executar a operação de atualização da atividades Economicas. {idLogradouroEnderecor}")

    def db_search(self, id):
        try:
            sql = f"SELECT * FROM configParcelamentos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as idLogradouroEnderecor:
            send_log_error(f"idLogradouroEndereco ao executar a operação de busca. {idLogradouroEnderecor}")

    def db_list(self):
        try:
            sql = "SELECT * FROM configParcelamentos WHERE id_cloud is null"
            data = self.query(sql)
            if data:
                send_log_info("Consulta de todos os atividades Economicas realizada com sucesso.")
                return data
            return None
        except Exception as idLogradouroEnderecor:
            send_log_error(f"idLogradouroEndereco ao executar a operação de busca. {idLogradouroEnderecor}")

    def get_id_cloud(self, id):
        if (id == None):
            return None
        try:
            sql = f"SELECT id_cloud FROM configParcelamentos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as idLogradouroEnderecor:
            send_log_error(f"idLogradouroEndereco ao executar a operação de busca. {idLogradouroEnderecor}")

    def send_post(self, id, idAto, idScriptDesconto, idScriptJurosFinanciamento, descricao, dtValidadeFinal, dtVencimentoInicial, dtValidadeInicial, dtVencimentoFinal, qtdDiasPrimeiroVcto, 
                  qtdDiasVencidos, qtdMaxParcelas, qtdParcelasAlternadas, qtdParcelasConsecutivas, vlMinimoFisica, vlMinimoJuridica, percEntrada, percRenda, 
                  aplicacaoAcrescimos, cancelamentoLote, formulaAntecipacao, intervaloVctoParcelas, cancelarPorDias, cobrarJuros, definirVlMaxRenda, editarDataParcela, exigirEntrada, 
                  removerTaxasManual, reparcelarParcelamento, revogarParcelaDesconto, inserirTaxasManual, manterAnistiaDivida, parcelamentoGerado, permitirIncentivosFiscais, 
                  permitirManutencaoLancamento, permitirParcelaSemCpf, tipoLancamento, tiposDividas, aplicarValorMinimo, vencimentoLancamento):
        objeto = {
                    "idIntegracao": f"Atos{id}",
                    "content": {}
        }
        if tipoLancamento:
            objeto["content"]["tipoLancamento"] = f"{tipoLancamento}"

        if tiposDividas:
            objeto["content"]["tiposDividas"] = f"{tiposDividas}"

        if aplicarValorMinimo:
            objeto["content"]["aplicarValorMinimo"] = f"{aplicarValorMinimo}"     

        if vencimentoLancamento:
            objeto["content"]["vencimentoLancamento"] = f"{vencimentoLancamento}"    

        if dtVencimentoFinal:
            objeto["content"]["dtVencimentoFinal"] = f"{dtVencimentoFinal}"

        if intervaloVctoParcelas:
            objeto["content"]["intervaloVctoParcelas"] = f"{intervaloVctoParcelas}"
        
        if permitirParcelaSemCpf:
            objeto["content"]["permitirParcelaSemCpf"] = f"{permitirParcelaSemCpf}"

        if permitirManutencaoLancamento:
            objeto["content"]["permitirManutencaoLancamento"] = f"{permitirManutencaoLancamento}"

        if permitirIncentivosFiscais:
            objeto["content"]["permitirIncentivosFiscais"] = f"{permitirIncentivosFiscais}"

        if parcelamentoGerado:
            objeto["content"]["parcelamentoGerado"] = f"{parcelamentoGerado}"     

        if manterAnistiaDivida:
            objeto["content"]["manterAnistiaDivida"] = f"{manterAnistiaDivida}"    

        if inserirTaxasManual:
            objeto["content"]["inserirTaxasManual"] = f"{inserirTaxasManual}"

        if revogarParcelaDesconto:
            objeto["content"]["revogarParcelaDesconto"] = f"{revogarParcelaDesconto}"

        if cobrarJuros:
            objeto["content"]["cobrarJuros"] = f"{cobrarJuros}"

        if definirVlMaxRenda:
            objeto["content"]["definirVlMaxRenda"] = f"{definirVlMaxRenda}"

        if exigirEntrada:
            objeto["content"]["exigirEntrada"] = f"{exigirEntrada}"     

        if removerTaxasManual:
            objeto["content"]["removerTaxasManual"] = f"{removerTaxasManual}"    

        if reparcelarParcelamento:
            objeto["content"]["reparcelarParcelamento"] = f"{reparcelarParcelamento}"

        if editarDataParcela:
            objeto["content"]["UnidadeMedida"] = f"{editarDataParcela}"

        if idAto:
            objeto["content"]["idAto"] = { "id": int(idAto)}

        if cancelarPorDias:
            objeto["content"]["cancelarPorDias"] = f"{cancelarPorDias}"

        if formulaAntecipacao:
            objeto["content"]["formulaAntecipacao"] = f"{formulaAntecipacao}"

        if dtVencimentoInicial:
            objeto["content"]["dtVencimentoInicial"] = f"{dtVencimentoInicial}"

        if qtdDiasVencidos:
            objeto["content"]["qtdDiasVencidos"] = { "id": int(qtdDiasVencidos)}     

        if qtdMaxParcelas:
            objeto["content"]["qtdMaxParcelas"] = { "id": int(qtdMaxParcelas)}

        if qtdParcelasAlternadas:
            objeto["content"]["qtdParcelasAlternadas"] = { "id": int(qtdParcelasAlternadas)}

        if cancelamentoLote:
            objeto["content"]["cancelamentoLote"] = { "id": int(cancelamentoLote)}

        if qtdDiasPrimeiroVcto:
            objeto["content"]["qtdDiasPrimeiroVcto"] = { "id": int(qtdDiasPrimeiroVcto)}
        
        if idScriptJurosFinanciamento:
            objeto["content"]["idScriptJurosFinanciamento"] = { "id": int(idScriptJurosFinanciamento)}
        
        if qtdParcelasConsecutivas:
            objeto["content"]["qtdParcelasConsecutivas"] = { "id": int(qtdParcelasConsecutivas)}
        
        if idScriptDesconto:
            objeto["content"]["idScriptDesconto"] ={ "id": int(idScriptDesconto)}
        
        if descricao:
            objeto["content"]["descricao"] = f"{descricao}"
        
        if vlMinimoJuridica:
            objeto["content"]["CasasDecimais"] = { "id": int(vlMinimoJuridica) }
        
        if percEntrada:
            objeto["content"]["MaximoDigitos"] = { "id": int(percEntrada) }
        
        if dtValidadeFinal:
            objeto["content"]["dtValidadeFinals"] = f"{dtValidadeFinal}"
        
        if dtValidadeInicial:
            objeto["content"]["CompartilhadoCondominio"] = f"{dtValidadeInicial}"
        
        if percRenda:
            objeto["content"]["percRenda"] = { "id": int(percRenda)}
        
        if vlMinimoFisica:
            objeto["content"]["LivroEletronico"] = f"{vlMinimoFisica}"
        
        if aplicacaoAcrescimos:
            objeto["content"]["aplicacaoAcrescimos"] = { "id": int(aplicacaoAcrescimos)}

        envio = api_post("configParcelamentos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

configParcelamentos = configParcelamentos()