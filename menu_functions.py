from samples import *
from records import *
import json


def carregar_dados_logradourosBairros():
    send_log_info("Iniciando a leitura dos dados do serviço logradourosBairros.")
    temProximoBairro = True
    offsetBairro = 0
    while temProximoBairro:
        consultaBairro = api_get_all(f"logradourosBairros?offset={offsetBairro}&limit=1")
        dadosBairro = json.loads(consultaBairro)
        if dadosBairro:
            for res in dadosBairro["content"]:
                reg = res['content']
                logradourosBairros.db_insert(reg["id"], reg["municipio"]["id"], reg["nome"], None)
                offsetBairro = offsetBairro + 1
                temProximoBairro = dadosBairro["hasNext"]
    else:
        send_log_info("Leitura dos dados do serviço bairro finalizada.")

def carregar_dados_paises():
    send_log_info("Iniciando a leitura dos dados do serviço paises.")
    temProximoPais = True
    offsetPais = 0
    while temProximoPais:
        consultaPais = api_get_all(f"paises?offset={offsetPais}&limit=1")
        dadosPais = json.loads(consultaPais)
        if dadosPais:
            for res in dadosPais["content"]:
                reg = res['content']
                paises.db_insert(reg["id"], reg["codigoBacen"], None,reg["sigla2C"], reg["idTemplate"], reg["sigla3D"], None, reg["sigla3C"])
                offsetPais = offsetPais + 1
                temProximoPais = dadosPais["hasNext"]
    else:
        send_log_info("Leitura dos dados do serviço paises finalizada.")

def carregar_dados_estados():
    send_log_info("Iniciando a leitura dos dados do serviço estados.")
    temProximoEstado = True
    offsetEstado = 0
    while temProximoEstado:
        consultaEstado = api_get_all(f"estados?offset={offsetEstado}&limit=1")
        dadosEstado = json.loads(consultaEstado)
        if dadosEstado:
            for res in dadosEstado["content"]:
                reg = res['content']
                estados.db_insert(reg["id"], reg["paises"]["id"], reg["nome"], None, reg["uf"])
                offsetEstado = offsetEstado + 1
                temProximoEstado = dadosEstado["hasNext"]
    else:
        send_log_info("Leitura dos dados do serviço estados finalizada.")

def carregar_dados_municipios():
    send_log_info("Iniciando a leitura dos dados do serviço municipios.")
    temProximoMunicipio = True
    offsetMunicipio = 0
    while temProximoMunicipio:
        consultaMunicipio = api_get_all(f"municipios?offset={offsetMunicipio}&limit=1")
        dadosMunicipio = json.loads(consultaMunicipio)
        if dadosMunicipio:
            for res in dadosMunicipio["content"]:
                reg = res['content']
                municipios.db_insert(reg["id"], reg["estados"]["id"], reg["nome"], None, None, reg["uf"])
                offsetMunicipio = offsetMunicipio + 1
                temProximoMunicipio = dadosMunicipio["hasNext"]
    else:
        send_log_info("Leitura dos dados do serviço municipios finalizada.")

def enviar_dados_unidades_medida():
    send_log_info("Iniciando o processamento dos dados da tabela unidades-medida.")
    listaUnidadesMedida = unidadesMedidas.db_list()
    if listaUnidadesMedida:
        for res in listaUnidadesMedida:
            unidadesMedidas.send_post(res[0], res[3], res[4])
    else:
        send_log_info("Não foram encontrados registros na tabela unidades-medida para enviar.")
    send_log_info("Processamento dos dados da tabela unidades-medida finalizado.")

def enviar_dados_logradourosBairros():
    send_log_info("Iniciando o processamento dos dados da tabela logradourosBairros.")
    listalogradourosBairros = logradourosBairros.db_list()
    if listalogradourosBairros:
        for res in listalogradourosBairros:
            logradourosBairros.send_post(res[0], res[3], res[4])
    else:
        send_log_info("Não foram encontrados registros na tabela logradourosBairros para enviar.")
    send_log_info("Processamento dos dados da tabela logradourosBairros finalizado.")

#def enviar_dados_Bairros():
 #   send_log_info("Iniciando o processamento dos dados da tabela Bairros.")
  #  listaBairros = Bairros.db_list()
   # if listaBairros:
    #    for res in listaBairros:
     #       Bairros.send_post(res[0], res[1], res[2], res[3])
    #else:
    #    send_log_info("Não foram encontrados registros na tabela Bairros para enviar.")
    #send_log_info("Processamento dos dados da tabela Bairros finalizado.")    

def enviar_dados_advogados():
    send_log_info("Iniciando o processamento dos dados da tabela advogados.")
    listaadvogados = advogados.db_list()
    if listaadvogados:
        for res in listaadvogados:
            advogados.send_post(res[0], res[3], res[4])
    else:
        send_log_info("Não foram encontrados registros na tabela advogados para enviar.")
    send_log_info("Processamento dos dados da tabela advogados finalizado.")

def enviar_dados_advogadosCbo():
    send_log_info("Iniciando o processamento dos dados da tabela advogadosCbo.")
    listaadvogadosCbo = advogadosCbo.db_list()
    if listaadvogadosCbo:
        for res in listaadvogadosCbo:
            advogadosCbo.send_post(res[0], res[3], res[4])
    else:
        send_log_info("Não foram encontrados registros na tabela advogadosCbo para enviar.")
    send_log_info("Processamento dos dados da tabela advogadosCbo finalizado.")

def enviar_dados_advogadosResponsaveis():
    send_log_info("Iniciando o processamento dos dados da tabela advogadosResponsaveis.")
    listaadvogadosResponsaveis = advogadosResponsaveis.db_list()
    if listaadvogadosResponsaveis:
        for res in listaadvogadosResponsaveis:
            id_deducao_receita = advogadosCbo.get_id_cloud(res[3])
            advogadosResponsaveis.send_post(res[0], id_deducao_receita, res[4])
    else:
        send_log_info("Não foram encontrados registros na tabela advogadosResponsaveis para enviar.")
    send_log_info("Processamento dos dados da tabela advogadosResponsaveis finalizado.")

def enviar_dados_tipos_logradouros():
    send_log_info("Iniciando o processamento dos dados da tabela tipos_logradouros.")
    listaTiposLogradouros = tiposLogradouros.db_list()
    if listaTiposLogradouros:
        for res in listaTiposLogradouros:
            tiposLogradouros.send_post(res[0], res[3], res[4])
    else:
        send_log_info("Não foram encontrados registros na tabela tipos_logradouros para enviar.")
    send_log_info("Processamento dos dados da tabela tipos_logradouros finalizado.")

def enviar_dados_loteamentos():
    send_log_info("Iniciando o processamento dos dados da tabela loteamentos.")
    listaLoteamentos = loteamentos.db_list()
    if listaLoteamentos:
        for res in listaLoteamentos:
            id_bairro = logradourosBairros.get_id_cloud(res[3])
            id_distritos = distritos.get_id_cloud(res[4])
            id_municipio = municipios.get_id_cloud(res[5])
            loteamentos.send_post(res[0], id_bairro, id_distritos, id_municipio, res[6])
    else:
        send_log_info("Não foram encontrados registros na tabela loteamentos para enviar.")
    send_log_info("Processamento dos dados da tabela loteamentos finalizado.")

def enviar_dados_agrupamentos():
    send_log_info("Iniciando o processamento dos dados da tabela agrupamentos.")
    listaagrupamentos = agrupamentos.db_list()
    if listaagrupamentos:
        for res in listaagrupamentos:
            agrupamentos.send_post(res[0], res[1], res[2], res[3])
    else:
        send_log_info("Não foram encontrados registros na tabela agrupamentos para enviar.")
    send_log_info("Processamento dos dados da tabela agrupamentos finalizado.")

def enviar_dados_unidadesMedidas():
    send_log_info("Iniciando o processamento dos dados da tabela unidadesMedidas.")
    listaunidadesMedidas = unidadesMedidas.db_list()
    if listaunidadesMedidas:
        for res in listaunidadesMedidas:
            unidadesMedidas.send_post(res[0], res[1], res[2], res[3], res[4], res[5])
    else:
        send_log_info("Não foram encontrados registros na tabela agrupamentos para enviar.")
    send_log_info("Processamento dos dados da tabela agrupamentos finalizado.")

def enviar_dados_condominios():
    send_log_info("Iniciando o processamento dos dados da tabela condominios.")
    listaCondominios = condominios.db_list()
    if listaCondominios:
        for res in listaCondominios:
            id_logradouro = logradouros.get_id_cloud(res[3])
            id_bairro = logradourosBairros.get_id_cloud(res[4])
            id_municipio = municipios.get_id_cloud(res[5])
            condominios.send_post(res[0], id_logradouro, id_bairro, id_municipio, res[6], res[7], res[8], res[9])
    else:
        send_log_info("Não foram encontrados registros na tabela condominios para enviar.")
    send_log_info("Processamento dos dados da tabela condominios finalizado.")

def enviar_dados_agrupamentosCamposAdicionais():
    send_log_info("Iniciando o processamento dos dados da tabela agrupamentosCamposAdicionais.")
    listaagrupamentosCamposAdicionais = agrupamentosCamposAdicionais.db_list()
    if listaagrupamentosCamposAdicionais:
        for res in listaagrupamentosCamposAdicionais:
            agrupamentosCamposAdicionais.send_post(res[0], res[3], res[4], res[5])
    else:
        send_log_info("Não foram encontrados registros na tabela agrupamentosCamposAdicionais para enviar.")
    send_log_info("Processamento dos dados da tabela agrupamentosCamposAdicionais finalizado.")

def enviar_dados_alvaras():
    send_log_info("Iniciando o processamento dos dados da tabela alvaras.")
    listaalvaras = alvaras.db_list()
    if listaalvaras:
        for res in listaalvaras:
            alvaras.send_post(res[0], res[3], res[4])
    else:
        send_log_info("Não foram encontrados registros na tabela alvaras para enviar.")
    send_log_info("Processamento dos dados da tabela alvaras finalizado.")

def enviar_dados_anistias():
    send_log_info("Iniciando o processamento dos dados da tabela anistias.")
    listaanistias = anistias.db_list()
    if listaanistias:
        for res in listaanistias:
            anistias.send_post(res[0], res[3])
    else:
        send_log_info("Não foram encontrados registros na tabela anistias para enviar.")
    send_log_info("Processamento dos dados da tabela anistias finalizado.")

def enviar_dados_arquivos():
    send_log_info("Iniciando o processamento dos dados da tabela arquivos.")
    listaarquivos = arquivos.db_list()
    if listaarquivos:
        for res in listaarquivos:
            arquivos.send_post(res[0], res[4], res[5], res[6])
    else:
        send_log_info("Não foram encontrados registros na tabela arquivos para enviar.")
    send_log_info("Processamento dos dados da tabela arquivos finalizado.")

def enviar_dados_atividadesEconomicas():
    send_log_info("Iniciando o processamento dos dados da tabela atividadesEconomicas.")
    listaatividadesEconomicas = atividadesEconomicas.db_list()
    if listaatividadesEconomicas:
        for res in listaatividadesEconomicas:
            atividadesEconomicas.send_post(res[0], res[3], res[4])
    else:
        send_log_info("Não foram encontrados registros na tabela atividadesEconomicas para enviar.")
    send_log_info("Processamento dos dados da tabela atividadesEconomicas finalizado.")

def enviar_dados_configuracoesArrecadacoes():
    send_log_info("Iniciando o processamento dos dados da tabela configuracoesArrecadacoes.")
    listaconfiguracoesArrecadacoes = configuracoesArrecadacoes.db_list()
    if listaconfiguracoesArrecadacoes:
        for res in listaconfiguracoesArrecadacoes:
            configuracoesArrecadacoes.send_post(res[0], res[4])
    else:
        send_log_info("Não foram encontrados registros na tabela configuracoesArrecadacoes para enviar.")
    send_log_info("Processamento dos dados da tabela configuracoesArrecadacoes finalizado.")

def enviar_dados_atividadesEconomicasInfComplem():
    send_log_info("Iniciando o processamento dos dados da tabela enviar_dados_atividadesEconomicasInfComplem.")
    listaTransacoesFinanceiras = atividadesEconomicasInfComplem.db_list()
    if listaTransacoesFinanceiras:
        for res in listaTransacoesFinanceiras:
            atividadesEconomicasInfComplem.send_post(res[0], res[3], res[4])
    else:
        send_log_info("Não foram encontrados registros na tabela enviar_dados_atividadesEconomicasInfComplem para enviar.")
    send_log_info("Processamento dos dados da tabela enviar_dados_atividadesEconomicasInfComplem finalizado.")

def enviar_dados_atividadesEconomicasInfCompOp():
    send_log_info("Iniciando o processamento dos dados da tabela atividadesEconomicasInfCompOp.")
    listaatividadesEconomicasInfCompOpExercicios = atividadesEconomicasInfCompOp.db_list()
    if listaatividadesEconomicasInfCompOpExercicios:
        for res in listaatividadesEconomicasInfCompOpExercicios:
            atividadesEconomicasInfCompOp.send_post(res[0], res[4])
    else:
        send_log_info("Não foram encontrados registros na tabela atividadesEconomicasInfCompOp para enviar.")
    send_log_info("Processamento dos dados da tabela atividadesEconomicasInfCompOp finalizado.")

def enviar_dados_atividadesEconomicasRelacionadas():
    send_log_info("Iniciando o processamento dos dados da tabela atividadesEconomicasRelacionadas.")
    listaatividadesEconomicasRelacionadas = atividadesEconomicasRelacionadas.db_list()
    if listaatividadesEconomicasRelacionadas:
        for res in listaatividadesEconomicasRelacionadas:
            atividadesEconomicasRelacionadas.send_post(res[0], res[3])
    else:
        send_log_info("Não foram encontrados registros na tabela atividadesEconomicasRelacionadas para enviar.")
    send_log_info("Processamento dos dados da tabela atividadesEconomicasRelacionadas finalizado.")

def enviar_dados_atividadesEconomicasValores():
    send_log_info("Iniciando o processamento dos dados da tabela atividadesEconomicasValores.")
    listaatividadesEconomicasValores = atividadesEconomicasValores.db_list()
    if listaatividadesEconomicasValores:
        for res in listaatividadesEconomicasValores:
            atividadesEconomicasValores.send_post(res[0], res[4])
    else:
        send_log_info("Não foram encontrados registros na tabela atividadesEconomicasValores para enviar.")
    send_log_info("Processamento dos dados da tabela atividadesEconomicasValores finalizado.")

def enviar_dados_atos():
    send_log_info("Iniciando o processamento dos dados da tabela atos.")
    listaatos = atos.db_list()
    if listaatos:
        for res in listaatos:
            lista_niveis = atos.db_list_atos_niveis(res[1])
            atos.send_post(res[0], res[3], lista_niveis)
    else:
        send_log_info("Não foram encontrados registros na tabela atos para enviar.")
    send_log_info("Processamento dos dados da tabela atos finalizado.")

def enviar_dados_atosFontesDivulgacoes():
    send_log_info("Iniciando o processamento dos dados da tabela atosFontesDivulgacoes.")
    listaatosFontesDivulgacoes = atosFontesDivulgacoes.db_list()
    if listaatosFontesDivulgacoes:
        for res in listaatosFontesDivulgacoes:
            atosFontesDivulgacoes.send_post(res[0], res[5], res[6])
    else:
        send_log_info("Não foram encontrados registros na tabela atosFontesDivulgacoes para enviar.")
    send_log_info("Processamento dos dados da tabela atosFontesDivulgacoes finalizado.")

def enviar_dados_atualizacaoDividaAtivaSimAm():
    send_log_info("Iniciando o processamento dos dados da tabela atualizacaoDividaAtivaSimAm.")
    listaatualizacaoDividaAtivaSimAm = atualizacaoDividaAtivaSimAm.db_list()
    if listaatualizacaoDividaAtivaSimAm:
        for res in listaatualizacaoDividaAtivaSimAm:
            atualizacaoDividaAtivaSimAm.send_post(res[0], res[4], res[5], res[6])
    else:
        send_log_info("Não foram encontrados registros na tabela acoes para enviar.")
    send_log_info("Processamento dos dados da tabela acoes finalizado.")

def enviar_dados_atualizacaoMonetariaSimAm():
    send_log_info("Iniciando o processamento dos dados da tabela catualizacaoMonetariaSimAm.")
    listaatualizacaoMonetariaSimAm = atualizacaoMonetariaSimAm.db_list()
    if listaatualizacaoMonetariaSimAm:
        for res in listaatualizacaoMonetariaSimAm:
            atualizacaoMonetariaSimAm.send_post(res[0], res[3])
    else:
        send_log_info("Não foram encontrados registros na tabela atualizacaoMonetariaSimAm para enviar.")
    send_log_info("Processamento dos dados da tabela atualizacaoMonetariaSimAm finalizado.")

def enviar_dados_baixaAutomatica():
    send_log_info("Iniciando o processamento dos dados da tabela baixaAutomatica.")
    listabaixaAutomatica = baixaAutomatica.db_list()
    if listabaixaAutomatica:
        for res in listabaixaAutomatica:
            baixaAutomatica.send_post(res[0], res[4], res[5])
    else:
        send_log_info("Não foram encontrados registros na tabela funcoes para enviar.")
    send_log_info("Processamento dos dados da tabela funcoes finalizado.")

def enviar_dados_baixaAutomaticaPagamentos():
    send_log_info("Iniciando o processamento dos dados da tabela baixaAutomaticaPagamentos.")
    listabaixaAutomaticaPagamentos = baixaAutomaticaPagamentos.db_list()
    if listabaixaAutomaticaPagamentos:
        for res in listabaixaAutomaticaPagamentos:
            baixaAutomaticaPagamentos.send_post(res[0], res[4], res[5])
    else:
        send_log_info("Não foram encontrados registros na tabela baixaAutomaticaPagamentos para enviar.")
    send_log_info("Processamento dos dados da tabela baixaAutomaticaPagamentos finalizado.")

def enviar_dados_baixaManual():
    send_log_info("Iniciando o processamento dos dados da tabela baixaManual.")
    listabaixaManual = baixaManual.db_list()
    if listabaixaManual:
        for res in listabaixaManual:
            id_ppa = None # TODO ver serviço de origem da informação
            baixaManual.send_post(res[0], id_ppa, res[4])
    else:
        send_log_info("Não foram encontrados registros na tabela baixaManual para enviar.")
    send_log_info("Processamento dos dados da tabela baixaManual finalizado.")

def enviar_dados_baixaManualPagamentos():
    send_log_info("Iniciando o processamento dos dados da tabela baixaManualPagamentos.")
    listaConfiguracoesNaturezasDespesas = baixaManualPagamentos.db_list()
    if listaConfiguracoesNaturezasDespesas:
        for res in listaConfiguracoesNaturezasDespesas:
            baixaManualPagamentos.send_post(res[0], res[3])
    else:
        send_log_info("Não foram encontrados registros na tabela baixaManualPagamentos para enviar.")
    send_log_info("Processamento dos dados da tabela baixaManualPagamentos finalizado.")

def enviar_dados_baixasAutomaticas():
    send_log_info("Iniciando o processamento dos dados da tabela baixasAutomaticas.")
    listaNaturezasDespesas = baixasAutomaticas.db_list()
    if listaNaturezasDespesas:
        for res in listaNaturezasDespesas:
            baixasAutomaticas.send_post(res[0],res[4], res[5], res[6])
    else:
        send_log_info("Não foram encontrados registros na tabela configuracoes_baixasAutomaticas para enviar.")
    send_log_info("Processamento dos dados da tabela baixasAutomaticas finalizado.")

def enviar_dados_beneficiosFiscais():
    send_log_info("Iniciando o processamento dos dados da tabela configuracoes_naturezas_receitas.")
    listabeneficiosFiscais = beneficiosFiscais.db_list()
    if listabeneficiosFiscais:
        for res in listabeneficiosFiscais:
            lista_niveis = beneficiosFiscais.db_list_configuracoes_naturezas_receitas_niveis(res[1])
            beneficiosFiscais.send_post(res[0], res[3], lista_niveis)
    else:
        send_log_info("Não foram encontrados registros na tabela configuracoes_naturezas_receitas para enviar.")
    send_log_info("Processamento dos dados da tabela configuracoes_naturezas_receitas finalizado.")

def enviar_dados_calculosTributarios():
    send_log_info("Iniciando o processamento dos dados da tabela calculosTributarios.")
    listacalculosTributarios = calculosTributarios.db_list()
    if listacalculosTributarios:
        for res in listacalculosTributarios:
            calculosTributarios.send_post(res[0], res[4], res[5], res[6] )
    else:
        send_log_info("Não foram encontrados registros na tabela calculosTributarios para enviar.")
    send_log_info("Processamento dos dados da tabela calculosTributarios finalizado.")

def enviar_dados_calculosTributariosAvancado():
    send_log_info("Iniciando o processamento dos dados da tabela calculosTributariosAvancado.")
    listacalculosTributariosAvancado = calculosTributariosAvancado.db_list()
    if listacalculosTributariosAvancado:
        for res in listacalculosTributariosAvancado:            
            calculosTributariosAvancado.send_post(res[0], res[4], res[5], res[6], res[7], res[8], res[9], res[10])
    else:
        send_log_info("Não foram encontrados registros na tabela calculosTributariosAvancado para enviar.")
    send_log_info("Processamento dos dados da tabela calculosTributariosAvancado finalizado.")

def enviar_dados_calculosTributariosAvancadoOpc():
    send_log_info("Iniciando o processamento dos dados da tabela calculosTributariosAvancadoOpc.")
    listacalculosTributariosAvancadoOpc = calculosTributariosAvancadoOpc.db_list()
    if listacalculosTributariosAvancadoOpc:
        for res in listacalculosTributariosAvancadoOpc:
            calculosTributariosAvancadoOpc.send_post(res[0], res[6], res[7], res[8], res[9], res[10], res[11], res[12], res[13], res[14])
    else:
        send_log_info("Não foram encontrados registros na tabela programas para enviar.")
    send_log_info("Processamento dos dados da tabela programas finalizado.")

def enviar_dados_camposAdicionais():
    send_log_info("Iniciando o processamento dos dados da tabela camposAdicionais.")
    listacamposAdicionais = camposAdicionais.db_list()
    if listacamposAdicionais:
        for res in listacamposAdicionais:
            camposAdicionais.send_post(res[0], res[3], res[4])
    else:
        send_log_info("Não foram encontrados registros na tabela camposAdicionais para enviar.")
    send_log_info("Processamento dos dados da tabela camposAdicionais finalizado.")

def enviar_dados_motivos():
    send_log_info("Iniciando o processamento dos dados da tabela motivos.")
    listamotivos = motivos.db_list()
    if listamotivos:
        for res in listamotivos:
            motivos.send_post(res[0], res[1], res[2]. res[3], res[4])
    else:
        send_log_info("Não foram encontrados registros na tabela motivos para enviar.")
    send_log_info("Processamento dos dados da tabela motivos finalizado.")    

def enviar_dados_cancelamentoDocumentos():
    send_log_info("Iniciando o processamento dos dados da tabela cancelamentoDocumentos.")
    listacancelamentoDocumentos = cancelamentoDocumentos.db_list()
    if listacancelamentoDocumentos:
        for res in listacancelamentoDocumentos:
            cancelamentoDocumentos.send_post(res[0], res[5])
    else:
        send_log_info("Não foram encontrados registros na tabela cancelamentoDocumentos para enviar.")
    send_log_info("Processamento dos dados da tabela cancelamentoDocumentos finalizado.")

def enviar_dados_cartorios():
    send_log_info("Iniciando o processamento dos dados da tabela cartorios.")
    listacartorios = cartorios.db_list()
    if listacartorios:
        for res in listacartorios:
            cartorios.send_post(res[0], res[10])
    else:
        send_log_info("Não foram encontrados registros na tabela cartorios para enviar.")
    send_log_info("Processamento dos dados da tabela cartorios finalizado.")

def enviar_dados_cbos():
    send_log_info("Iniciando o processamento dos dados da tabela cbos.")
    listacbos = cbos.db_list()
    if listacbos:
        for res in listacbos:
            cbos.send_post(res[0], res[3])
    else:
        send_log_info("Não foram encontrados registros na tabela cbos para enviar.")
    send_log_info("Processamento dos dados da tabela cbos finalizado.")

def enviar_dados_certidoesITBI():
    send_log_info("Iniciando o processamento dos dados da tabela certidoesITBI.")
    listacertidoesITBI = certidoesITBI.db_list()
    if listacertidoesITBI:
        for res in listacertidoesITBI:
            certidoesITBI.send_post(res[0], res[3], res[4], res[5], res[6])
    else:
        send_log_info("Não foram encontrados registros na tabela certidoesITBI para enviar.")
    send_log_info("Processamento dos dados da tabela certidoesITBI finalizado.")

def enviar_dados_certidoesNegativas():
    send_log_info("Iniciando o processamento dos dados da tabela certidoesNegativas.")
    listacertidoesNegativas = certidoesNegativas.db_list()
    if listacertidoesNegativas:
        for res in listacertidoesNegativas:
            certidoesNegativas.send_post(res[0])
    else:
        send_log_info("Não foram encontrados registros na tabela certidoesNegativas para enviar.")
    send_log_info("Processamento dos dados da tabela certidoesNegativas finalizado.")

def carregar_dados_agenciasBancarias():
    send_log_info("Iniciando a leitura dos dados do serviço agenciasBancarias.")
    temProximoBanco = True
    offsetBanco = 0
    while temProximoBanco:
        consultaBanco = api_get_all(f"agenciasBancarias?offset={offsetBanco}&limit=1")
        dadosBanco = json.loads(consultaBanco)
        if dadosBanco:
            for res in dadosBanco["content"]:
                reg = res['content']
                agenciasBancarias.db_insert(
                    reg["id"],
                    reg["sigla"] if "sigla" in reg else None,
                    reg["numero"] if "numero" in reg else None,
                    reg["associadoFebraban"] if "associadoFebraban" in reg else None,
                    reg["nome"]
                )
                offsetBanco = offsetBanco + 1
                temProximoBanco = dadosBanco["hasNext"]
    else:
        send_log_info("Leitura dos dados do serviço agenciasBancarias finalizada.")

def enviar_dados_agencias_bancarias():
    send_log_info("Iniciando o processamento dos dados da tabela agencias_bancarias.")
    listaAgenciasBancarias = agenciasBancarias.db_list()
    if listaAgenciasBancarias:
        for res in listaAgenciasBancarias:
            id_banco = agenciasBancarias.get_id_cloud(res[3])
            id_logradouro = logradouros.get_id_cloud(res[4])
            id_municipio = municipios.get_id_cloud(res[5])
            id_bairro = logradourosBairros.get_id_cloud(res[6])
            agenciasBancarias.send_post(res[0], id_banco, id_logradouro, id_municipio, id_bairro, res[7], res[8], res[9], res[10], res[11])
    else:
        send_log_info("Não foram encontrados registros na tabela agencias_bancarias para enviar.")
    send_log_info("Processamento dos dados da tabela agencias_bancarias finalizado.")

def enviar_dados_contas_bancarias():
    send_log_info("Iniciando o processamento dos dados da tabela classificacoes_contas_bancarias.")
    listaagenciasBancarias = agenciasBancarias.db_list()
    if listaagenciasBancarias:
        for res in listaagenciasBancarias:
            agenciasBancarias.send_post(res[0], res[3])
    else:
        send_log_info("Não foram encontrados registros na tabela classificacoes_contas_bancarias para enviar.")
    send_log_info("Processamento dos dados da tabela classificacoes_contas_bancarias finalizado.")

def enviar_dados_cnaes():
    send_log_info("Iniciando o processamento dos dados da tabela cnaes.")
    listacnaes = cnaes.db_list()
    if listacnaes:
        for res in listacnaes:
            cnaes.send_post(res[0], res[6], res[7], res[8])
    else:
        send_log_info("Não foram encontrados registros na tabela cnaes para enviar.")
    send_log_info("Processamento dos dados da tabela cnaes finalizado.")

def enviar_dados_compensacoes():
    send_log_info("Iniciando o processamento dos dados da tabela compensacoes.")
    listacompensacoes = compensacoes.db_list()
    if listacompensacoes:
        for res in listacompensacoes:
            compensacoes.send_post(res[0], res[3])
    else:
        send_log_info("Não foram encontrados registros na tabela compensacoes para enviar.")
    send_log_info("Processamento dos dados da tabela compensacoes finalizado.")

def enviar_dados_competencias():
    send_log_info("Iniciando o processamento dos dados da tabela competencias.")
    listacompetencias = competencias.db_list()
    if listacompetencias:
        for res in listacompetencias:
            competencias.send_post(res[0], res[5])
    else:
        send_log_info("Não foram encontrados registros na tabela competencias para enviar.")
    send_log_info("Processamento dos dados da tabela competencias finalizado.")

def enviar_dados_condominios():
    send_log_info("Iniciando o processamento dos dados da tabela condominios.")
    listacondominios = condominios.db_list()
    if listacondominios:
        for res in listacondominios:
            condominios.send_post(res[0], res[3], res[4], res[5])
    else:
        send_log_info("Não foram encontrados registros na tabela condominios para enviar.")
    send_log_info("Processamento dos dados da tabela condominios finalizado.")

def enviar_dados_condominiosInfComplem():
    send_log_info("Iniciando o processamento dos dados da tabela condominiosInfComplem.")
    listacondominiosInfComplem = condominiosInfComplem.db_list()
    if listacondominiosInfComplem:
        for res in listacondominiosInfComplem:
            condominiosInfComplem.send_post(res[0], res[5], res[6], res[7])
    else:
        send_log_info("Não foram encontrados registros na tabela condominiosInfComplem para enviar.")
    send_log_info("Processamento dos dados da tabela condominiosInfComplem finalizado.")

def enviar_dados_condominiosInfComplemOp():
    send_log_info("Iniciando o processamento dos dados da tabela condominiosInfComplemOp.")
    listacondominiosInfComplemOp = condominiosInfComplemOp.db_list()
    if listacondominiosInfComplemOp:
        for res in listacondominiosInfComplemOp:
            condominiosInfComplemOp.send_post(res[0], res[6], res[7], res[8], res[9], res[10], res[11], res[12], res[13], res[14], res[15], res[16])
    else:
        send_log_info("Não foram encontrados registros na tabela condominiosInfComplemOp para enviar.")
    send_log_info("Processamento dos dados da tabela condominiosInfComplemOp finalizado.")

def enviar_dados_configContribMelhorias():
    send_log_info("Iniciando o processamento dos dados da tabela configContribMelhorias.")
    listaconfigContribMelhorias = configContribMelhorias.db_list()
    if listaconfigContribMelhorias:
        for res in listaconfigContribMelhorias:
            configContribMelhorias.send_post(res[0], res[3], res[4], res[5])
    else:
        send_log_info("Não foram encontrados registros na tabela configContribMelhorias para enviar.")
    send_log_info("Processamento dos dados da tabela configContribMelhorias finalizado.")

def enviar_dados_configEconomicosTabelasAuxiliaresHistorico():
    send_log_info("Iniciando o processamento dos dados da tabela configEconomicosTabelasAuxiliaresHistorico.")
    listaconfigEconomicosTabelasAuxiliaresHistorico = configEconomicosTabelasAuxiliaresHistorico.db_list()
    if listaconfigEconomicosTabelasAuxiliaresHistorico:
        for res in listaconfigEconomicosTabelasAuxiliaresHistorico:
            configEconomicosTabelasAuxiliaresHistorico.send_post(res[0], res[6], res[7])
    else:
        send_log_info("Não foram encontrados registros na tabela configEconomicosTabelasAuxiliaresHistorico para enviar.")
    send_log_info("Processamento dos dados da tabela configEconomicosTabelasAuxiliaresHistorico finalizado.")

def enviar_dados_configGeoprocessamento():
    send_log_info("Iniciando o processamento dos dados da tabela configGeoprocessamento.")
    listaconfigGeoprocessamento = configGeoprocessamento.db_list()
    if listaconfigGeoprocessamento:
        for res in listaconfigGeoprocessamento:
            configGeoprocessamento.send_post(res[0], res[4])
    else:
        send_log_info("Não foram encontrados registros na tabela configGeoprocessamento para enviar.")
    send_log_info("Processamento dos dados da tabela configGeoprocessamento finalizado.")

def enviar_dados_configGeracaoGuias():
    send_log_info("Iniciando o processamento dos dados da tabela configGeracaoGuias.")
    listaconfigGeracaoGuias = configGeracaoGuias.db_list()
    if listaconfigGeracaoGuias:
        for res in listaconfigGeracaoGuias:
            configGeracaoGuias.send_post(res[0], res[3], res[4])
    else:
        send_log_info("Não foram encontrados registros na tabela configGeracaoGuias para enviar.")
    send_log_info("Processamento dos dados da tabela  finalizado.")

def enviar_dados_configHomologacaoTributos():
    send_log_info("Iniciando o processamento dos dados da tabela configHomologacaoTributos.")
    listaconfigHomologacaoTributos = configHomologacaoTributos.db_list()
    if listaconfigHomologacaoTributos:
        for res in listaconfigHomologacaoTributos:
            configHomologacaoTributos.send_post(res[0], res[4])
    else:
        send_log_info("Não foram encontrados registros na tabela configHomologacaoTributos para enviar.")
    send_log_info("Processamento dos dados da tabela configHomologacaoTributos finalizado.")

def enviar_dados_configImobiliarias():
    send_log_info("Iniciando o processamento dos dados da tabela configImobiliarias.")
    listaconfigImobiliarias = configImobiliarias.db_list()
    if listaconfigImobiliarias:
        for res in listaconfigImobiliarias:
            configImobiliarias.send_post(res[0], res[3])
    else:
        send_log_info("Não foram encontrados registros na tabela configImobiliarias para enviar.")
    send_log_info("Processamento dos dados da tabela configImobiliarias finalizado.")

def enviar_dados_configInscDividaAtiva():
    send_log_info("Iniciando o processamento dos dados da tabela configInscDividaAtiva.")
    listaconfigInscDividaAtiva = configInscDividaAtiva.db_list()
    if listaconfigInscDividaAtiva:
        for res in listaconfigInscDividaAtiva:
            configInscDividaAtiva.send_post(res[0], res[3], res[4])
    else:
        send_log_info("Não foram encontrados registros na tabela configInscDividaAtiva para enviar.")
    send_log_info("Processamento dos dados da tabela configInscDividaAtiva finalizado.")

def enviar_dados_configInscrImobiliarias():
    send_log_info("Iniciando o processamento dos dados da tabela configInscrImobiliarias.")
    listaconfigInscrImobiliarias = configInscrImobiliarias.db_list()
    if listaconfigInscrImobiliarias:
        for res in listaconfigInscrImobiliarias:
            configInscrImobiliarias.send_post(res[0], res[3], res[4])
    else:
        send_log_info("Não foram encontrados registros na tabela configInscrImobiliarias para enviar.")
    send_log_info("Processamento dos dados da tabela configInscrImobiliarias finalizado.")

def enviar_dados_configParcCreditos():
    send_log_info("Iniciando o processamento dos dados da tabela configParcCreditos.")
    listaconfigParcCreditos = configParcCreditos.db_list()
    if listaconfigParcCreditos:
        for res in listaconfigParcCreditos:
            configParcCreditos.send_post(res[0], res[5], res[6], res[7], res[8], res[9], res[10], res[11])
    else:
        send_log_info("Não foram encontrados registros na tabela configParcCreditos para enviar.")
    send_log_info("Processamento dos dados da tabela configParcCreditos finalizado.")

def enviar_dados_configNotasAvulsas():
    send_log_info("Iniciando o processamento dos dados da tabela configNotasAvulsas.")
    listaconfigNotasAvulsas = configNotasAvulsas.db_list()
    if listaconfigNotasAvulsas:
        for res in listaconfigNotasAvulsas:
            configNotasAvulsas.send_post(res[0], res[6], res[7], res[8], res[9], res[10], res[11])
    else:
        send_log_info("Não foram encontrados registros na tabela configNotasAvulsas para enviar.")
    send_log_info("Processamento dos dados da tabela configNotasAvulsas finalizado.")

def enviar_dados_configParcCreditosTaxas():
    send_log_info("Iniciando o processamento dos dados da tabela configParcCreditosTaxas.")
    listaconfigParcCreditosTaxas = configParcCreditosTaxas.db_list()
    if listaconfigParcCreditosTaxas:
        for res in listaconfigParcCreditosTaxas:
            configParcCreditosTaxas.send_post(res[0], res[4], res[5], res[6], res[7])
    else:
        send_log_info("Não foram encontrados registros na tabela configParcCreditosTaxas para enviar.")
    send_log_info("Processamento dos dados da tabela configParcCreditosTaxas finalizado.")

def enviar_dados_configParcelamentos():
    send_log_info("Iniciando o processamento dos dados da tabela configParcelamentos.")
    listaconfigParcelamentos = configParcelamentos.db_list()
    if listaconfigParcelamentos:
        for res in listaconfigParcelamentos:
            configParcelamentos.send_post(res[0], res[4], res[5], res[6], res[7])
    else:
        send_log_info("Não foram encontrados registros na tabela configParcelamentos para enviar.")
    send_log_info("Processamento dos dados da tabela configParcelamentos finalizado.")

def enviar_dados_configTaxaExpedCredts():
    send_log_info("Iniciando o processamento dos dados da tabela configTaxaExpedCredt.")
    listaconfigTaxaExpedCredts = configTaxaExpedCredts.db_list()
    if listaconfigTaxaExpedCredts:
        for res in listaconfigTaxaExpedCredts:
            configTaxaExpedCredts.send_post(res[0], res[7], res[8], res[9], res[10], res[11])
    else:
        send_log_info("Não foram encontrados registros na tabela configTaxaExpedCredt para enviar.")
    send_log_info("Processamento dos dados da tabela configTaxaExpedCredt finalizado.")

def enviar_dados_configTaxaExpediente():
    send_log_info("Iniciando o processamento dos dados da tabela configTaxaExpediente.")
    listaconfigTaxaExpediente = configTaxaExpediente.db_list()
    if listaconfigTaxaExpediente:
        for res in listaconfigTaxaExpediente:
            configTaxaExpediente.send_post(res[0], res[4], res[5], res[6], res[7])
    else:
        send_log_info("Não foram encontrados registros na tabela configTaxaExpediente para enviar.")
    send_log_info("Processamento dos dados da tabela configTaxaExpediente finalizado.")

def enviar_dados_configTransfImoMotivos():
    send_log_info("Iniciando o processamento dos dados da tabela configTransfImoMotivos.")
    listaconfigTransfImoMotivos = configTransfImoMotivos.db_list()
    if listaconfigTransfImoMotivos:
        for res in listaconfigTransfImoMotivos:
            configTransfImoMotivos.send_post(res[0], res[4], res[5], res[6], res[7])
    else:
        send_log_info("Não foram encontrados registros na tabela configTransfImoMotivos para enviar.")
    send_log_info("Processamento dos dados da tabela configTransfImoMotivos finalizado.")

def enviar_dados_configTransfImoReceitas():
    send_log_info("Iniciando o processamento dos dados da tabela configTransfImoReceitas.")
    listaconfigTransfImoReceitas = configTransfImoReceitas.db_list()
    if listaconfigTransfImoReceitas:
        for res in listaconfigTransfImoReceitas:
            id_divida = dividas.get_id_cloud(res[3])
            configTransfImoReceitas.send_post(res[0], id_divida, res[4], res[5], res[6], res[7], res[8], res[9], res[10])
    else:
        send_log_info("Não foram encontrados registros na tabela configTransfImoReceitas para enviar.")
    send_log_info("Processamento dos dados da tabela configTransfImoReceitas finalizado.")

def enviar_dados_configTransfImoveis():
    send_log_info("Iniciando o processamento dos dados da tabela configTransfImoveis.")
    listaconfigTransfImoveis = configTransfImoveis.db_list()
    if listaconfigTransfImoveis:
        for res in listaconfigTransfImoveis:
            configTransfImoveis.send_post(res[0], res[4], res[5], res[6], res[7])
    else:
        send_log_info("Não foram encontrados registros na tabela configTransfImoveis para enviar.")
    send_log_info("Processamento dos dados da tabela configTransfImoveis finalizado.")

def enviar_dados_configuracoes():
    send_log_info("Iniciando o processamento dos dados da tabela configuracoes.")
    listaconfiguracoes = configuracoes.db_list()
    if listaconfiguracoes:
        for res in listaconfiguracoes:
            configuracoes.send_post(res[0], res[5], res[6])
    else:
        send_log_info("Não foram encontrados registros na tabela configuracoes para enviar.")
        send_log_info("Processamento dos dados da tabela configuracoes finalizado.")

def enviar_dados_configuracoesArrecadacoes():
    send_log_info("Iniciando o processamento dos dados da tabela configuracoesArrecadacoes.")
    listaconfiguracoesArrecadacoes = configuracoesArrecadacoes.db_list()
    if listaconfiguracoesArrecadacoes:
        for res in listaconfiguracoesArrecadacoes:
            configuracoesArrecadacoes.send_post(res[0], res[5], res[6], res[7], res[8])
    else:
        send_log_info("Não foram encontrados registros na tabela configuracoesArrecadacoes para enviar.")
    send_log_info("Processamento dos dados da tabela configuracoesArrecadacoes finalizado.")

def enviar_dados_contribMelhoriasTaxas():
    send_log_info("Iniciando o processamento dos dados da tabela contribMelhoriasTaxas.")
    listacontribMelhoriasTaxas = contribMelhoriasTaxas.db_list()
    if listacontribMelhoriasTaxas:
        for res in listacontribMelhoriasTaxas:
            contribMelhoriasTaxas.send_post(res[0], res[4], res[5])
    else:
        send_log_info("Não foram encontrados registros na tabela contribMelhoriasTaxas para enviar.")
    send_log_info("Processamento dos dados da tabela contribMelhoriasTaxas finalizado.")

def enviar_dados_configuracoesGeracaoParcelas():
    send_log_info("Iniciando o processamento dos dados da tabela configuracoesGeracaoParcelas.")
    listaconfiguracoesGeracaoParcelas = configuracoesGeracaoParcelas.db_list()
    if listaconfiguracoesGeracaoParcelas:
        for res in listaconfiguracoesGeracaoParcelas:
            configuracoesGeracaoParcelas.send_post(res[0], res[5], res[6])
    else:
        send_log_info("Não foram encontrados registros na tabela configuracoesGeracaoParcelas para enviar.")
    send_log_info("Processamento dos dados da tabela configuracoesGeracaoParcelas finalizado.")

def enviar_dados_configuracoesGeracaoParcelasReceitas():
    send_log_info("Iniciando o processamento dos dados da tabela configuracoesGeracaoParcelasReceitas.")
    listaconfiguracoesGeracaoParcelasReceitas = configuracoesGeracaoParcelasReceitas.db_list()
    if listaconfiguracoesGeracaoParcelasReceitas:
        for res in listaconfiguracoesGeracaoParcelasReceitas:
            configuracoesGeracaoParcelasReceitas.send_post(res[0], res[4], res[5], res[6], res[7])
    else:
        send_log_info("Não foram encontrados registros na tabela configuracoesGeracaoParcelasReceitas para enviar.")
    send_log_info("Processamento dos dados da tabela configuracoesGeracaoParcelasReceitas finalizado.")

def enviar_dados_configuracoesParcelas():
    send_log_info("Iniciando o processamento dos dados da tabela configuracoesParcelas.")
    listaconfiguracoesParcelas = configuracoesParcelas.db_list()
    if listaconfiguracoesParcelas:
        for res in listaconfiguracoesParcelas:
            configuracoesParcelas.send_post(res[0], res[3], res[4])
    else:
        send_log_info("Não foram encontrados registros na tabela configuracoesParcelas para enviar.")
    send_log_info("Processamento dos dados da tabela configuracoesParcelas finalizado.")

def enviar_dados_construtoras():
    send_log_info("Iniciando o processamento dos dados da tabela construtoras.")
    listaconstrutoras = construtoras.db_list()
    if listaconstrutoras:
        for res in listaconstrutoras:
            construtoras.send_post(res[0], res[4])
    else:
        send_log_info("Não foram encontrados registros na tabela construtoras para enviar.")
    send_log_info("Processamento dos dados da tabela construtoras finalizado.")

def enviar_dados_construtorasEngArquitetos():
    send_log_info("Iniciando o processamento dos dados da tabela construtorasEngArquitetos.")
    listaconstrutorasEngArquitetos = construtorasEngArquitetos.db_list()
    if listaconstrutorasEngArquitetos:
        for res in listaconstrutorasEngArquitetos:
            construtorasEngArquitetos.send_post(res[0], res[3], res[4], res[5])
    else:
        send_log_info("Não foram encontrados registros na tabela construtorasEngArquitetos para enviar.")
    send_log_info("Processamento dos dados da tabela construtorasEngArquitetos finalizado.")

def enviar_dados_contadores():
    send_log_info("Iniciando o processamento dos dados da tabela contadores.")
    listacontadores = contadores.db_list()
    if listacontadores:
        for res in listacontadores:
            contadores.send_post(res[0], res[3])
    else:
        send_log_info("Não foram encontrados registros na tabela contadores para enviar.")
    send_log_info("Processamento dos dados da tabela contadores finalizado.")

def enviar_dados_contadoresCbo():
    send_log_info("Iniciando o processamento dos dados da tabela contadoresCbo.")
    listacontadoresCbo = contadoresCbo.db_list()
    if listacontadoresCbo:
        for res in listacontadoresCbo:
            contadoresCbo.send_post(res[0], res[3], res[4])
    else:
        send_log_info("Não foram encontrados registros na tabela contadoresCbo para enviar.")
    send_log_info("Processamento dos dados da tabela contadoresCbo finalizado.")

def enviar_dados_contadoresResponsaveis():
    send_log_info("Iniciando o processamento dos dados da tabela contadoresResponsaveis.")
    listacontadoresResponsaveis = contadoresResponsaveis.db_list()
    if listacontadoresResponsaveis:
        for res in listacontadoresResponsaveis:
            contadoresResponsaveis.send_post(res[0], res[3], res[4])
    else:
        send_log_info("Não foram encontrados registros na tabela contadoresResponsaveis para enviar.")
    send_log_info("Processamento dos dados da tabela contadoresResponsaveis finalizado.")

def enviar_dados_ContribMelhoriasBairros():
    send_log_info("Iniciando o processamento dos dados da tabela ContribMelhoriasBairros.")
    listaContribMelhoriasBairros = ContribMelhoriasBairros.db_list()
    if listaContribMelhoriasBairros:
        for res in listaContribMelhoriasBairros:
            ContribMelhoriasBairros.send_post(res[0], res[5], res[6])
    else:
        send_log_info("Não foram encontrados registros na tabela ContribMelhoriasBairros para enviar.")
    send_log_info("Processamento dos dados da tabela ContribMelhoriasBairros finalizado.")

def enviar_dados_contribMelhoriasImoveis():
    send_log_info("Iniciando o processamento dos dados da tabela contribMelhoriasImoveis.")
    listacontribMelhoriasImoveis = contribMelhoriasImoveis.db_list()
    if listacontribMelhoriasImoveis:
        for res in listacontribMelhoriasImoveis:
            contribMelhoriasImoveis.send_post(res[0], res[7], res[8], res[9], res[10], res[11])
    else:
        send_log_info("Não foram encontrados registros na tabela contribMelhoriasImoveis para enviar.")
    send_log_info("Processamento dos dados da tabela contribMelhoriasImoveis finalizado.")

def enviar_dados_contribMelhoriasInfComp():
    send_log_info("Iniciando o processamento dos dados da tabela contribMelhoriasInfComp.")
    listacontribMelhoriasInfComp = contribMelhoriasInfComp.db_list()
    if listacontribMelhoriasInfComp:
        for res in listacontribMelhoriasInfComp:
            contribMelhoriasInfComp.send_post(res[0], res[4], res[5], res[6], res[7], res[8])
    else:
        send_log_info("Não foram encontrados registros na tabela contribMelhoriasInfComp para enviar.")
    send_log_info("Processamento dos dados da tabela contribMelhoriasInfComp finalizado.")

def enviar_dados_contribMelhoriasMateriaisServicos():
    send_log_info("Iniciando o processamento dos dados da tabela contribMelhoriasMateriaisServicos.")
    listacontribMelhoriasMateriaisServicos = contribMelhoriasMateriaisServicos.db_list()
    if listacontribMelhoriasMateriaisServicos:
        for res in listacontribMelhoriasMateriaisServicos:
            contribMelhoriasMateriaisServicos.send_post(res[0], res[3], res[4], res[5], res[6])
    else:
        send_log_info("Não foram encontrados registros na tabela contribMelhoriasMateriaisServicos para enviar.")
    send_log_info("Processamento dos dados da tabela contribMelhoriasMateriaisServicos finalizado.")

def enviar_dados_contribMelhoriasMovtos():
    send_log_info("Iniciando o processamento dos dados da tabela contribMelhoriasMovtos.")
    listacontribMelhoriasMovtos = contribMelhoriasMovtos.db_list()
    if listacontribMelhoriasMovtos:
        for res in listacontribMelhoriasMovtos:
            contribMelhoriasMovtos.send_post(res[0], res[6], res[7], res[8], res[9])
    else:
        send_log_info("Não foram encontrados registros na tabela contribMelhoriasMovtos para enviar.")
    send_log_info("Processamento dos dados da tabela contribMelhoriasMovtos finalizado.")

def enviar_dados_contribMelhoriasSaldos():
    send_log_info("Iniciando o processamento dos dados da tabela contribMelhoriasSaldos.")
    listacontribMelhoriasSaldos = contribMelhoriasSaldos.db_list()
    if listacontribMelhoriasSaldos:
        for res in listacontribMelhoriasSaldos:
            contribMelhoriasSaldos.send_post(res[0], res[4], res[5], res[6], res[7])
    else:
        send_log_info("Não foram encontrados registros na tabela contribMelhoriasSaldos para enviar.")
    send_log_info("Processamento dos dados da tabela contribMelhoriasSaldos finalizado.")

def enviar_dados_contribMelhoriasTaxas():
    send_log_info("Iniciando o processamento dos dados da tabela contribMelhoriasTaxas.")
    listacontribMelhoriasTaxas = contribMelhoriasTaxas.db_list()
    if listacontribMelhoriasTaxas:
        for res in listacontribMelhoriasTaxas:
            contribMelhoriasTaxas.send_post(res[0], res[4], res[5], res[6], res[7], res[8], res[9], res[10], res[11])
    else:
        send_log_info("Não foram encontrados registros na tabela contribMelhoriasTaxas para enviar.")
    send_log_info("Processamento dos dados da tabela contribMelhoriasTaxas finalizado.")

def enviar_dados_contribMelImovInfComp():
    send_log_info("Iniciando o processamento dos dados da tabela contribMelImovInfComp.")
    listacontribMelImovInfComp = contribMelImovInfComp.db_list()
    if listacontribMelImovInfComp:
        for res in listacontribMelImovInfComp:
            contribMelImovInfComp.send_post(res[0], res[4], res[5], res[6], res[7], res[8])
    else:
        send_log_info("Não foram encontrados registros na tabela contribMelImovInfComp para enviar.")
    send_log_info("Processamento dos dados da tabela contribMelImovInfComp finalizado.")

def enviar_dados_contribMovtosDetalhes():
    send_log_info("Iniciando o processamento dos dados da tabela contribMovtosDetalhes.")
    listacontribMovtosDetalhes = contribMovtosDetalhes.db_list()
    if listacontribMovtosDetalhes:
        for res in listacontribMovtosDetalhes:
            contribMovtosDetalhes.send_post(res[0], res[4], res[5], res[6], res[7], res[8], res[9])
    else:
        send_log_info("Não foram encontrados registros na tabela contribMovtosDetalhes para enviar.")
    send_log_info("Processamento dos dados da tabela contribMovtosDetalhes finalizado.")

def enviar_dados_contribuicoesMelhorias():
    send_log_info("Iniciando o processamento dos dados da tabela contribuicoesMelhorias.")
    listacontribuicoesMelhorias = contribuicoesMelhorias.db_list()
    if listacontribuicoesMelhorias:
        for res in listacontribuicoesMelhorias:
            contribuicoesMelhorias.send_post(res[0], res[4], res[5], res[6])
    else:
        send_log_info("Não foram encontrados registros na tabela contribuicoesMelhorias para enviar.")
    send_log_info("Processamento dos dados da tabela contribuicoesMelhorias finalizado.")

def enviar_dados_contrMelhoriasInfCompOp():
    send_log_info("Iniciando o processamento dos dados da tabela contrMelhoriasInfCompOp.")
    listacontrMelhoriasInfCompOp = contrMelhoriasInfCompOp.db_list()
    if listacontrMelhoriasInfCompOp:
        for res in listacontrMelhoriasInfCompOp:
            contrMelhoriasInfCompOp.send_post(res[0], res[4], res[5])
    else:
        send_log_info("Não foram encontrados registros na tabela contrMelhoriasInfCompOp para enviar.")
    send_log_info("Processamento dos dados da tabela contrMelhoriasInfCompOp finalizado.")

def enviar_dados_convenios():
    send_log_info("Iniciando o processamento dos dados da tabela convenios.")
    listaconvenios = convenios.db_list()
    if listaconvenios:
        for res in listaconvenios:
            convenios.send_post(res[0], res[6], res[7], res[8], res[9])
    else:
        send_log_info("Não foram encontrados registros na tabela convenios para enviar.")
    send_log_info("Processamento dos dados da tabela convenios finalizado.")

def enviar_dados_conveniosCreditos():
    send_log_info("Iniciando o processamento dos dados da tabela conveniosCreditos.")
    listaconveniosCreditos = conveniosCreditos.db_list()
    if listaconveniosCreditos:
        for res in listaconveniosCreditos:
            conveniosCreditos.send_post(res[0], res[4], res[5], res[6], res[7])
    else:
        send_log_info("Não foram encontrados registros na tabela conveniosCreditos para enviar.")
    send_log_info("Processamento dos dados da tabela conveniosCreditos finalizado.")

def enviar_dados_conveniosMensagens():
    send_log_info("Iniciando o processamento dos dados da tabela conveniosMensagens.")
    listaconveniosMensagens = conveniosMensagens.db_list()
    if listaconveniosMensagens:
        for res in listaconveniosMensagens:
            conveniosMensagens.send_post(res[0], res[5], res[6], res[7])
    else:
        send_log_info("Não foram encontrados registros na tabela conveniosMensagens para enviar.")
    send_log_info("Processamento dos dados da tabela conveniosMensagens finalizado.")

def enviar_dados_conveniosSimulacoes():
    send_log_info("Iniciando o processamento dos dados da tabela conveniosSimulacoes.")
    listaconveniosSimulacoes = conveniosSimulacoes.db_list()
    if listaconveniosSimulacoes:
        for res in listaconveniosSimulacoes:
            conveniosSimulacoes.send_post(res[0], res[4], res[5])
    else:
        send_log_info("Não foram encontrados registros na tabela conveniosSimulacoes para enviar.")
    send_log_info("Processamento dos dados da tabela conveniosSimulacoes finalizado.")

def enviar_dados_creditosTributarios():
    send_log_info("Iniciando o processamento dos dados da tabela creditosTributarios.")
    listacreditosTributarios = creditosTributarios.db_list()
    if listacreditosTributarios:
        for res in listacreditosTributarios:
            creditosTributarios.send_post(res[0], res[5], res[6], res[7],)
    else:
        send_log_info("Não foram encontrados registros na tabela creditosTributarios para enviar.")
    send_log_info("Processamento dos dados da tabela creditosTributarios finalizado.")

def enviar_dados_creditosTributariosRec():
    send_log_info("Iniciando o processamento dos dados da tabela creditosTributariosRec.")
    listacreditosTributariosRec = creditosTributariosRec.db_list()
    if listacreditosTributariosRec:
        for res in listacreditosTributariosRec:
            creditosTributariosRec.send_post(res[0], res[4], res[5])
    else:
        send_log_info("Não foram encontrados registros na tabela creditosTributariosRec para enviar.")
    send_log_info("Processamento dos dados da tabela creditosTributariosRec finalizado.")

def enviar_dados_declaracoes():
    send_log_info("Iniciando o processamento dos dados da tabela declaracoes.")
    listadeclaracoes = declaracoes.db_list()
    if listadeclaracoes:
        for res in listadeclaracoes:
            declaracoes.send_post(res[0], res[5], res[6], res[7])
    else:
        send_log_info("Não foram encontrados registros na tabela declaracoes para enviar.")
    send_log_info("Processamento dos dados da tabela declaracoes finalizado.")

def enviar_dados_declaracoesServicos():
    send_log_info("Iniciando o processamento dos dados da tabela declaracoesServicos.")
    listadeclaracoesServicos = declaracoesServicos.db_list()
    if listadeclaracoesServicos:
        for res in listadeclaracoesServicos:
            declaracoesServicos.send_post(res[0], res[5], res[6], res[7])
    else:
        send_log_info("Não foram encontrados registros na tabela declaracoesServicos para enviar.")
    send_log_info("Processamento dos dados da tabela declaracoesServicos finalizado.")

def enviar_dados_deducaoCreditoSimAm():
    send_log_info("Iniciando o processamento dos dados da tabela deducaoCreditoSimAm.")
    listadeducaoCreditoSimAm = deducaoCreditoSimAm.db_list()
    if listadeducaoCreditoSimAm:
        for res in listadeducaoCreditoSimAm:
            deducaoCreditoSimAm.send_post(res[0], res[5], res[6], res[7])
    else:
        send_log_info("Não foram encontrados registros na tabela deducaoCreditoSimAm para enviar.")
    send_log_info("Processamento dos dados da tabela deducaoCreditoSimAm finalizado.")

def enviar_dados_deducaoDividaSimAm():
    send_log_info("Iniciando o processamento dos dados da tabela deducaoDividaSimAm.")
    listadeducaoDividaSimAm = deducaoDividaSimAm.db_list()
    if listadeducaoDividaSimAm:
        for res in listadeducaoDividaSimAm:
            deducaoDividaSimAm.send_post(res[0], res[4], res[5], res[6], res[7])
    else:
        send_log_info("Não foram encontrados registros na tabela deducaoDividaSimAm para enviar.")
    send_log_info("Processamento dos dados da tabela deducaoDividaSimAm finalizado.")

def enviar_dados_desmembramentos():
    send_log_info("Iniciando o processamento dos dados da tabela desmembramentos.")
    listadesmembramentos = desmembramentos.db_list()
    if listadesmembramentos:
        for res in listadesmembramentos:
            desmembramentos.send_post(res[0], res[5], res[6], res[7])
    else:
        send_log_info("Não foram encontrados registros na tabela desmembramentos para enviar.")
    send_log_info("Processamento dos dados da tabela desmembramentos finalizado.")

def enviar_dados_desmembramentosDocumentos():
    send_log_info("Iniciando o processamento dos dados da tabela desmembramentosDocumentos.")
    listadesmembramentosDocumentos = desmembramentosDocumentos.db_list()
    if listadesmembramentosDocumentos:
        for res in listadesmembramentosDocumentos:
            desmembramentosDocumentos.send_post(res[0], res[4], res[5], res[6], res[7])
    else:
        send_log_info("Não foram encontrados registros na tabela desmembramentosDocumentos para enviar.")
    send_log_info("Processamento dos dados da tabela desmembramentosDocumentos finalizado.")

def enviar_dados_desmembramentosImoveis():
    send_log_info("Iniciando o processamento dos dados da tabela desmembramentosImoveis.")
    listadesmembramentosImoveis = desmembramentosImoveis.db_list()
    if listadesmembramentosImoveis:
        for res in listadesmembramentosImoveis:
            desmembramentosImoveis.send_post(res[0], res[4], res[5], res[6], res[7], res[8])
    else:
        send_log_info("Não foram encontrados registros na tabela desmembramentosImoveis para enviar.")
    send_log_info("Processamento dos dados da tabela desmembramentosImoveis finalizado.")

def enviar_dados_distritos():
    send_log_info("Iniciando o processamento dos dados da tabela distritos.")
    listadistritos = distritos.db_list()
    if listadistritos:
        for res in listadistritos:
            distritos.send_post(res[0], res[5], res[6], res[7], res[8])
    else:
        send_log_info("Não foram encontrados registros na tabela distritos para enviar.")
    send_log_info("Processamento dos dados da tabela distritos finalizado.")

def enviar_dados_dividaDebitoInscrito():
    send_log_info("Iniciando o processamento dos dados da tabela dividaDebitoInscrito.")
    listadividaDebitoInscrito = dividaDebitoInscrito.db_list()
    if listadividaDebitoInscrito:
        for res in listadividaDebitoInscrito:
            dividaDebitoInscrito.send_post(res[0], res[5], res[6], res[7], res[8])
    else:
        send_log_info("Não foram encontrados registros na tabela dividaDebitoInscrito para enviar.")
    send_log_info("Processamento dos dados da tabela dividaDebitoInscrito finalizado.")

def enviar_dados_dividas():
    send_log_info("Iniciando o processamento dos dados da tabela dividas.")
    listadividas = dividas.db_list()
    if listadividas:
        for res in listadividas:
            dividas.send_post(res[0], res[3], res[4], res[5])
    else:
        send_log_info("Não foram encontrados registros na tabela dividas para enviar.")
    send_log_info("Processamento dos dados da tabela dividas finalizado.")

def enviar_dados_dividasMovtos():
    send_log_info("Iniciando o processamento dos dados da tabela dividasMovtos.")
    listadividasMovtos = dividasMovtos.db_list()
    if listadividasMovtos:
        for res in listadividasMovtos:
            dividasMovtos.send_post(res[0], res[8], res[9])
    else:
        send_log_info("Não foram encontrados registros na tabela dividasMovtos para enviar.")
    send_log_info("Processamento dos dados da tabela dividasMovtos finalizado.")

def enviar_dados_dividasReceitas():
    send_log_info("Iniciando o processamento dos dados da tabela dividasReceitas.")
    listadividasReceitas = dividasReceitas.db_list()
    if listadividasReceitas:
        for res in listadividasReceitas:
            dividasReceitas.send_post(res[0], res[3], res[4], res[5], res[6], res[7])
    else:
        send_log_info("Não foram encontrados registros na tabela dividasReceitas para enviar.")
    send_log_info("Processamento dos dados da tabela dividasReceitas finalizado.")

def enviar_dados_dividasResponsaveis():
    send_log_info("Iniciando o processamento dos dados da tabela dividasResponsaveis.")
    listadividasResponsaveis = dividasResponsaveis.db_list()
    if listadividasResponsaveis:
        for res in listadividasResponsaveis:
            dividasResponsaveis.send_post(res[0], res[4])
    else:
        send_log_info("Não foram encontrados registros na tabela dividasResponsaveis para enviar.")
    send_log_info("Processamento dos dados da tabela dividasResponsaveis finalizado.")

