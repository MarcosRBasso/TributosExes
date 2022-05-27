from samples import *
import json

class calculosTributarios(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, acaoVctoFeriado, ano, atividades, bairros, calculoRetroativo, condominios, complementar, consideraEconomicosSuspensos, 
                  contadores, contribuicoesMelhorias, contribuicoesMelhoriasImoveis, contribuintes, idCreditosTributarios, dataVcto, dhInicio, dhTermino, economicos, formaPagamento,
                  homologadoPor, idCalculoAnterior, imoveis, campo1Final, campo2Final, campo3Final, campo4Final, campo5Final, campo6Final, campo7Final, campo8Final, campo9Final, 
                  campo10Final, campo1, campo2, campo3, campo4, campo5, campo6, campo7, campo8, campo9, campo10, intervalo, itensListaServico, logradouros, loteamentos, notaAvulsa, 
                  parcelaInicial, parcelasCompetencias, qtInconsistentes, qtLanctosGerados, qtdAnalisada, qtdDiasMeses, qtdParcelas, receitasDiversas, receitasDiversasLanctos, serieNotaAvulsa, 
                  simulado, tipoCalculo, tipoImovel):
        try: 
            sql = """
                INSERT INTO calculosTributarios (                    
                    idIntegracao,                   
                    id_cloud, 
                    acaoVctoFeriado,
                    ano,                                               
                    atividades, 
                    bairros,
                    calculoRetroativo,
                    complementar,
                    consideraEconomicosSuspensos,
                    condominios,
                    contadores,                    
                    contribuicoesMelhorias,
                    contribuicoesMelhoriasImoveis,
                    contribuintes,
                    idCreditosTributarios,
                    dataVcto,
                    dhInicio,
                    dhTermino,
                    economicos,
                    formaPagamento,
                    homologadoPor,
                    idCalculoAnterior,
                    imoveis, 
                    campo1Final,
                    campo2Final, 
                    campo3Final,
                    campo4Final,
                    campo5Final, 
                    campo6Final, 
                    campo7Final,
                    campo8Final,
                    campo9Final,
                    campo10Final,
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
                    intervalo, 
                    itensListaServico, 
                    logradouros, 
                    loteamentos, 
                    notaAvulsa, 
                    parcelaInicial, 
                    parcelasCompetencias, 
                    qtInconsistentes, 
                    qtLanctosGerados, 
                    qtdAnalisada, 
                    qtdDiasMeses, 
                    qtdParcelas, 
                    receitasDiversas, 
                    receitasDiversasLanctos, 
                    serieNotaAvulsa, 
                    simulado, 
                    tipoCalculo, 
                    tipoImovel
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(acaoVctoFeriado)s,
                    %(ano)s,
                    %(atividades)s,
                    %(bairros)s,
                    %(calculoRetroativo)s,
                    %(complementar)s,
                    %(consideraEconomicosSuspensos)s,
                    %(condominios)s,
                    %(contadores)s,                    
                    %(contribuicoesMelhorias)s,
                    %(contribuicoesMelhoriasImoveis)s,
                    %(contribuintes)s,
                    %(idCreditosTributarios)s,
                    %(dataVcto)s,
                    %(dhInicio)s,
                    %(dhTermino)s,
                    %(homologadoPor)s,
                    %(formaPagamento)s,                    
                    %(economicos)s,
                    %(homologadoPor)s,                    
                    %(idCalculoAnterior)s,
                    %(imoveis)s,
                    %(campo1Final)s,
                    %(campo2Final)s,
                    %(campo3Final)s,
                    %(campo4Final)s,
                    %(campo5Final)s,
                    %(campo6Final)s,
                    %(campo7Final)s,
                    %(campo8Final)s,                    
                    %(campo9Final)s,
                    %(campo10Final)s,
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
                    %(intervalo)s,
                    %(itensListaServico)s,
                    %(logradouros)s,
                    %(loteamentos)s,
                    %(notaAvulsa)s,
                    %(parcelaInicial)s,
                    %(parcelasCompetencias)s,                    
                    %(qtInconsistentes)s,
                    %(qtLanctosGerados)s,
                    %(qtdAnalisada)s,
                    %(qtdDiasMeses)s,
                    %(qtdParcelas)s,
                    %(receitasDiversas)s,
                    %(receitasDiversasLanctos)s,
                    %(serieNotaAvulsa)s,                    
                    %(simulado)s,
                    %(tipoCalculo)s,                    
                    %(tipoImovel)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                acaoVctoFeriado = acaoVctoFeriado,
                ano = ano,
                atividades = atividades,                               
                bairros = bairros,
                calculoRetroativo = calculoRetroativo,
                complementar = complementar,                               
                consideraEconomicosSuspensos = consideraEconomicosSuspensos,
                condominios = condominios,
                contadores = contadores,                                               
                contribuicoesMelhorias = contribuicoesMelhorias,
                contribuicoesMelhoriasImoveis = contribuicoesMelhoriasImoveis,                               
                contribuintes = contribuintes,
                idCreditosTributarios = idCreditosTributarios,
                dataVcto = dataVcto,                               
                dhInicio = dhInicio,
                dhTermino = dhTermino,
                homologadoPor = homologadoPor,
                formaPagamento = formaPagamento,
                economicos = economicos,
                idCalculoAnterior = idCalculoAnterior,
                imoveis = imoveis, 
                campo1Final = campo1Final, 
                campo2Final = campo2Final, 
                campo3Final = campo3Final, 
                campo4Final = campo4Final, 
                campo5Final = campo5Final, 
                campo6Final = campo6Final, 
                campo7Final = campo7Final, 
                campo8Final = campo8Final, 
                campo9Final = campo9Final, 
                campo10Final = campo10Final, 
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
                intervalo = intervalo, 
                itensListaServico = itensListaServico, 
                logradouros = logradouros, 
                loteamentos = loteamentos, 
                notaAvulsa = notaAvulsa, 
                parcelaInicial = parcelaInicial, 
                parcelasCompetencias = parcelasCompetencias, 
                qtInconsistentes = qtInconsistentes, 
                qtLanctosGerados =qtLanctosGerados, 
                qtdAnalisada = qtdAnalisada, 
                qtdDiasMeses = qtdDiasMeses, 
                qtdParcelas = qtdParcelas, 
                receitasDiversas = receitasDiversas, 
                receitasDiversasLanctos = receitasDiversasLanctos, 
                serieNotaAvulsa = serieNotaAvulsa, 
                simulado = simulado, 
                tipoCalculo = tipoCalculo, 
                tipoImovel = tipoImovel
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {calculosTributarios} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao inserir o anistias {calculosTributarios}. {contribuintesr}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM calculosTributarios"
            if not self.query(sql_s):
                send_log_warning(f"calculosTributarios não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM calculosTributarios WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de exclusão do atividades econômicas. {contribuintesr}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM calculosTributarios WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    calculosTributarios 
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
            sql = f"SELECT * FROM calculosTributarios WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def db_list(self):
        try:
            sql = "SELECT * FROM calculosTributarios WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM calculosTributarios WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def send_post(self, id, acaoVctoFeriado, ano, atividades, bairros, calculoRetroativo, condominios, complementar, consideraEconomicosSuspensos, 
                  contadores, contribuicoesMelhorias, contribuicoesMelhoriasImoveis, contribuintes, idCreditosTributarios, dataVcto, dhInicio, dhTermino, economicos, formaPagamento,
                  homologadoPor, idCalculoAnterior, imoveis, campo1Final, campo2Final, campo3Final, campo4Final, campo5Final, campo6Final, campo7Final, campo8Final, campo9Final, 
                  campo10Final, campo1, campo2, campo3, campo4, campo5, campo6, campo7, campo8, campo9, campo10, intervalo, itensListaServico, logradouros, loteamentos, notaAvulsa, 
                  parcelaInicial, parcelasCompetencias, qtInconsistentes, qtLanctosGerados, qtdAnalisada, qtdDiasMeses, qtdParcelas, receitasDiversas, receitasDiversasLanctos, serieNotaAvulsa, 
                  simulado, tipoCalculo, tipoImovel):
        objeto = {
            "idIntegracao": f"Atos{id}",
            "content": {}
        }
        if acaoVctoFeriado:
            objeto["content"]["VctoFeriado"] = f"{acaoVctoFeriado}"
        
        if atividades:
            objeto["content"]["atividades"] = f"{atividades}"
        
        if ano:
            objeto["content"]["ano"] = f"{ano}"
        
        if bairros:
            objeto["content"]["bairros"] = f"{bairros}"
        
        if dhInicio:
            objeto["content"]["dhInicio"] = f"{dhInicio}"
        
        if dhTermino:
            objeto["content"]["dhTermino"] = f"{dhTermino}"
        
        if calculoRetroativo:
            objeto["content"]["calculoRetroativo"] = f"{calculoRetroativo}"
        
        if complementar:
            objeto["content"]["complementar"] = f"{complementar}"
        
        if economicos:
            objeto["content"]["economicos"] = f"{economicos}"       

        if idCalculoAnterior:
            objeto["content"]["idCalculoAnterior"] = { "id": int(idCalculoAnterior) }
        
        if dataVcto:
            objeto["content"]["dataVcto"] = f"{dataVcto}" 

        if formaPagamento:
            objeto["content"]["formaPagamento"] = f"{formaPagamento}"

        if homologadoPor:
            objeto["content"]["homologadoPor"] = f"{homologadoPor}"

        if condominios:
            objeto["content"]["condominios"] = f"{condominios}"     

        if consideraEconomicosSuspensos:
            objeto["content"]["consideraEconomicosSuspensos"] = f"{consideraEconomicosSuspensos}"    

        if contadores:
            objeto["content"]["contadores"] = f"{contadores}"

        if parcelaInicial:
            objeto["content"]["parcelaInicial"] = { "id": int(parcelaInicial) }

        if contribuicoesMelhorias:
            objeto["content"]["contribuicoesMelhorias"] = f"{contribuicoesMelhorias}"

        if contribuicoesMelhoriasImoveis:
            objeto["content"]["contribuicoesMelhoriasImoveis"] = f"{contribuicoesMelhoriasImoveis}"

        if imoveis:
            objeto["content"]["imoveis"] = f"{imoveis}"     

        if campo1Final:
            objeto["content"]["campo1Final"] = f"{campo1Final}"    

        if campo2Final:
            objeto["content"]["campo2Final"] = f"{campo2Final}"

        if campo3Final:
            objeto["content"]["campo3Final"] = f"{campo3Final}"

        if campo4Final:
            objeto["content"]["campo4Final"] = f"{campo4Final}"  

        if campo5Final:
            objeto["content"]["campo5Final"] = f"{campo5Final}"

        if campo6Final:
            objeto["content"]["campo6Final"] = f"{campo6Final}"

        if campo7Final:
            objeto["content"]["campo7Final"] = f"{campo7Final}"

        if campo8Final:
            objeto["content"]["campo8Final"] = f"{campo8Final}"             
        
        if campo9Final:
            objeto["content"]["campo9Final"] = f"{campo9Final}"
        
        if campo10Final:
            objeto["content"]["campo10Final"] = f"{campo10Final}"

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
            objeto["content"]["campo1Final0"] = f"{campo10}"            
        
        if intervalo:
            objeto["content"]["intervalo"] = f"{intervalo}"
        
        if itensListaServico:
            objeto["content"]["itensListaServico"] = f"{itensListaServico}"
        
        if parcelasCompetencias:
            objeto["content"]["parcelasCompetencias"] = { "id": int(parcelasCompetencias) }
        
        if qtInconsistentes:
            objeto["content"]["qtInconsistentes"] = { "id": int(qtInconsistentes) }
        
        if qtLanctosGerados:
            objeto["content"]["qtLanctosGerados"] = { "id": int(qtLanctosGerados) }

        if qtdAnalisada:
            objeto["content"]["qtdAnalisada"] = { "id": int(qtdAnalisada) }

        if qtdParcelas:
            objeto["content"]["qtdParcelas"] = { "id": int(qtdParcelas) }

        if qtdDiasMeses:
            objeto["content"]["CodCaracteristicas"] = { "id": int(qtdDiasMeses) }            
        
        if logradouros:
            objeto["content"]["logradouros"] = f"{logradouros}",
        
        if loteamentos:
            objeto["content"]["loteamentos"] = f"{loteamentos}"
        
        if notaAvulsa:
            objeto["content"]["notaAvulsa"] = f"{notaAvulsa}"
        
        if contribuicoesMelhoriasImoveis:
            objeto["content"]["contribuicoesMelhoriasImoveis"] = f"{contribuicoesMelhoriasImoveis}"       

        if idCreditosTributarios != None:
            objeto[0]["calculotributario"]["creditotributario"] = { "id": int(idCreditosTributarios) }   
        
        if receitasDiversas:
            objeto["content"]["receitasDiversas"] = f"{receitasDiversas}",
        
        if receitasDiversasLanctos:
            objeto["content"]["receitasDiversasLanctos"] = f"{receitasDiversasLanctos}"
        
        if serieNotaAvulsa:
            objeto["content"]["serieNotaAvulsa"] = f"{serieNotaAvulsa}"
        
        if simulado:
            objeto["content"]["simulado"] = f"{simulado}"                       
        
        if tipoCalculo:
            objeto["content"]["tipoCalculo"] = f"{tipoCalculo}"
        
        if tipoImovel:
            objeto["content"]["tipoImovel"] = f"{tipoImovel}"
        
        if contribuintes:
            objeto["content"]["contribuintes"] = f"{contribuintes}"   

        envio = api_post("calculosTributarios", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

calculosTributarios = calculosTributarios()