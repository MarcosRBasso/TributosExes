from tkinter import *
import menu_functions as functions

class MinhaGUI:
    def __init__(self):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
        # Cria janela principal
        self.janela_principal = Tk()   

        self.var_carregar_dados_paises = IntVar()
        self.cb_carregar_dados_paises = Checkbutton(self.janela_principal, text='Carregar países', variable=self.var_carregar_dados_paises).place(x=20, y=20)

        self.var_carregar_dados_estados = IntVar()
        self.cb_carregar_dados_estados = Checkbutton(self.janela_principal, text='Carregar estados', variable=self.var_carregar_dados_estados).place(x=20, y=40)

        self.var_carregar_dados_municipios = IntVar()
        self.cb_carregar_dados_municipios = Checkbutton(self.janela_principal, text='Carregar municípios', variable=self.var_carregar_dados_municipios).place(x=20, y=60)     

        self.var_enviar_dados_agrupamentosCamposAdicionais = IntVar()
        self.cb_enviar_dados_agrupamentosCamposAdicionais = Checkbutton(self.janela_principal, text='Enviar agrupamentos Campos Adicionais', variable=self.var_enviar_dados_agrupamentosCamposAdicionais).place(x=20, y=80)

        self.var_enviar_dados_logradourosBairros = IntVar()
        self.cb_enviar_dados_logradourosBairros = Checkbutton(self.janela_principal, text='Enviar Bairros', variable=self.var_enviar_dados_logradourosBairros).place(x=20, y=100)

        self.var_enviar_dados_advogados = IntVar()
        self.cb_enviar_dados_advogados = Checkbutton(self.janela_principal, text='Enviar advogados', variable=self.var_enviar_dados_advogados).place(x=20, y=120)

        self.var_enviar_dados_advogadosCbo = IntVar()
        self.cb_enviar_dados_advogadosCbo = Checkbutton(self.janela_principal, text='Enviar advogados Cbo', variable=self.var_enviar_dados_advogadosCbo).place(x=20, y=140)

        self.var_enviar_dados_advogadosResponsaveis = IntVar()
        self.cb_enviar_dados_advogadosResponsaveis = Checkbutton(self.janela_principal, text='Enviar advogados Responsaveis', variable=self.var_enviar_dados_advogadosResponsaveis).place(x=20, y=160)

        self.var_tipos_logradouros = IntVar()
        self.cb_tipos_logradouros = Checkbutton(self.janela_principal, text='Enviar tipos de logradouros', variable=self.var_tipos_logradouros).place(x=20, y=180)

        self.var_enviar_dados_loteamentos = IntVar()
        self.cb_enviar_dados_loteamentos = Checkbutton(self.janela_principal, text='Enviar enviar dados loteamentos', variable=self.var_enviar_dados_loteamentos).place(x=20, y=200)

        self.var_enviar_dados_condominios = IntVar()
        self.cb_enviar_dados_condominios = Checkbutton(self.janela_principal, text='Enviar condomínios', variable=self.var_enviar_dados_condominios).place(x=20, y=220)

        self.var_enviar_dados_agrupamentos = IntVar()
        self.cb_enviar_dados_agrupamentos = Checkbutton(self.janela_principal, text='Enviar agrupamentos', variable=self.var_enviar_dados_agrupamentos).place(x=20, y=240)

        self.var_enviar_dados_alvaras = IntVar()
        self.cb_enviar_dados_alvaras = Checkbutton(self.janela_principal, text='Enviar alvaras', variable=self.var_enviar_dados_alvaras).place(x=20, y=260)

        self.var_enviar_dados_anistias = IntVar()
        self.cb_enviar_dados_anistias = Checkbutton(self.janela_principal, text='Enviar anistias', variable=self.var_enviar_dados_anistias).place(x=20, y=280)

        self.var_enviar_dados_arquivos = IntVar()
        self.cb_enviar_dados_arquivos = Checkbutton(self.janela_principal, text='Enviar arquivos', variable=self.var_enviar_dados_arquivos).place(x=20, y=300)

        self.var_enviar_dados_atividadesEconomicas = IntVar()
        self.cb_enviar_dados_atividadesEconomicas = Checkbutton(self.janela_principal, text='Enviar atividades Economicas', variable=self.var_enviar_dados_atividadesEconomicas).place(x=20, y=320)

        self.var_enviar_dados_configuracoesArrecadacoes = IntVar()
        self.cb_enviar_dados_configuracoesArrecadacoes = Checkbutton(self.janela_principal, text='Enviar configurações Arrecadacoes', variable=self.var_enviar_dados_configuracoesArrecadacoes).place(x=20, y=340)

        self.var_enviar_dados_atividadesEconomicasInfComplem = IntVar()
        self.cb_enviar_dados_atividadesEconomicasInfComplem = Checkbutton(self.janela_principal, text='Enviar atividades Economicas Informações Complementares', variable=self.var_enviar_dados_atividadesEconomicasInfComplem).place(x=20, y=360)

        self.var_enviar_dados_atividadesEconomicasInfCompOp = IntVar()
        self.cb_enviar_dados_atividadesEconomicasInfCompOp = Checkbutton(self.janela_principal, text='Enviar atividades Economicas Informações Complementar Op', variable=self.var_enviar_dados_atividadesEconomicasInfCompOp).place(x=20, y=380)

        self.var_enviar_dados_atividadesEconomicasRelacionadas = IntVar()
        self.cb_enviar_dados_atividadesEconomicasRelacionadas = Checkbutton(self.janela_principal, text='Enviar atividades Economicas Relacionadas', variable=self.var_enviar_dados_atividadesEconomicasRelacionadas).place(x=20, y=400)

        self.var_enviar_dados_atividadesEconomicasValores = IntVar()
        self.cb_enviar_dados_atividadesEconomicasValores = Checkbutton(self.janela_principal, text='Enviar atividades Economicas Valores', variable=self.var_enviar_dados_atividadesEconomicasValores).place(x=20, y=420)

        self.var_enviar_dados_atos = IntVar()
        self.cb_enviar_dados_atos = Checkbutton(self.janela_principal, text='Enviar atos', variable=self.var_enviar_dados_atos).place(x=20, y=440)

        self.var_enviar_dados_atosFontesDivulgacoes = IntVar()
        self.cb_enviar_dados_atosFontesDivulgacoes = Checkbutton(self.janela_principal, text='Enviar atos Fontes Divulgacoes', variable=self.var_enviar_dados_atosFontesDivulgacoes).place(x=20, y=460)

        self.var_acoes = IntVar()
        self.cb_acoes = Checkbutton(self.janela_principal, text='Enviar ações', variable=self.var_acoes).place(x=20, y=480)

        self.var_enviar_dados_atualizacaoDividaAtivaSimAm = IntVar()
        self.cb_enviar_dados_atualizacaoDividaAtivaSimAm = Checkbutton(self.janela_principal, text='Enviar atualizacao Divida Ativa SimAm', variable=self.var_enviar_dados_atualizacaoDividaAtivaSimAm).place(x=20, y=500)

        self.var_enviar_dados_atualizacaoMonetariaSimAm = IntVar()
        self.cb_enviar_dados_atualizacaoMonetariaSimAm = Checkbutton(self.janela_principal, text='Enviar atualizacao Monetaria SimAm', variable=self.var_enviar_dados_atualizacaoMonetariaSimAm).place(x=20, y=520)

        self.var_enviar_dados_baixaAutomatica = IntVar()
        self.cb_enviar_dados_baixaAutomatica = Checkbutton(self.janela_principal, text='Enviar baixa Automatica', variable=self.var_enviar_dados_baixaAutomatica).place(x=20, y=540)

        self.var_enviar_dados_baixaAutomaticaPagamentos = IntVar()
        self.cb_enviar_dados_baixaAutomaticaPagamentos = Checkbutton(self.janela_principal, text='Enviar baixa Automatica Pagamentos', variable=self.var_enviar_dados_baixaAutomaticaPagamentos).place(x=20, y=560)

        self.var_enviar_dados_baixaManual = IntVar()
        self.cb_enviar_dados_baixaManual = Checkbutton(self.janela_principal, text='Enviar baixa manual', variable=self.var_enviar_dados_baixaManual).place(x=20, y=580)

        self.var_enviar_dados_baixaManualPagamentos = IntVar()
        self.cb_enviar_dados_baixaManualPagamentos = Checkbutton(self.janela_principal, text='Enviar baixa manual pagamentos', variable=self.var_enviar_dados_baixaManualPagamentos).place(x=20, y=600)

        self.var_enviar_dados_baixasAutomaticas = IntVar()
        self.cb_enviar_dados_baixasAutomaticas = Checkbutton(self.janela_principal, text='Enviar baixas Automaticas', variable=self.var_enviar_dados_baixasAutomaticas).place(x=20, y=620)

        self.var_enviar_dados_beneficiosFiscais = IntVar()
        self.cb_enviar_dados_beneficiosFiscais = Checkbutton(self.janela_principal, text='Enviar beneficios Fiscais', variable=self.var_enviar_dados_beneficiosFiscais).place(x=20, y=640)

        self.var_enviar_dados_calculosTributarios = IntVar()
        self.cb_enviar_dados_calculosTributarios = Checkbutton(self.janela_principal, text='Enviar calculos Tributarios', variable=self.var_enviar_dados_calculosTributarios).place(x=20, y=660)

        self.var_enviar_dados_calculosTributariosAvancado = IntVar()
        self.cb_enviar_dados_calculosTributariosAvancado = Checkbutton(self.janela_principal, text='Enviar calculos Tributarios Avancado', variable=self.var_enviar_dados_calculosTributariosAvancado).place(x=20, y=680)

        self.var_enviar_dados_calculosTributariosAvancadoOpc = IntVar()
        self.cb_enviar_dados_calculosTributariosAvancadoOpc = Checkbutton(self.janela_principal, text='Enviar calculos Tributarios Avancado Opc', variable=self.var_enviar_dados_calculosTributariosAvancadoOpc).place(x=20, y=700)

        self.var_enviar_dados_camposAdicionais = IntVar()
        self.cb_enviar_dados_camposAdicionais = Checkbutton(self.janela_principal, text='Enviar campos adicionais', variable=self.var_enviar_dados_camposAdicionais).place(x=540, y=160)

        self.var_enviar_dados_cancelamentoDocumentos = IntVar()
        self.cb_enviar_dados_cancelamentoDocumentos = Checkbutton(self.janela_principal, text='Enviar cancelamentos adicionais', variable=self.var_enviar_dados_cancelamentoDocumentos).place(x=540, y=180)

        self.var_enviar_dados_cartorios = IntVar()
        self.cb_enviar_dados_cartorios = Checkbutton(self.janela_principal, text='Enviar dados cartórios', variable=self.var_enviar_dados_cartorios).place(x=540, y=200)

        self.var_enviar_dados_cbos = IntVar()
        self.cb_enviar_dados_cbos = Checkbutton(self.janela_principal, text='Enviar cbos', variable=self.var_enviar_dados_cbos).place(x=540, y=220)

        self.var_enviar_dados_certidoesITBI = IntVar()
        self.cb_enviar_dados_certidoesITBI = Checkbutton(self.janela_principal, text='Enviar certidoes ITBI', variable=self.var_enviar_dados_certidoesITBI).place(x=540, y=240)

        self.var_enviar_dados_certidoesNegativas = IntVar()
        self.cb_enviar_dados_certidoesNegativas = Checkbutton(self.janela_principal, text='Enviar certidões negativas', variable=self.var_enviar_dados_certidoesNegativas).place(x=540, y=260)

        self.var_carregar_dados_agenciasBancarias = IntVar()
        self.cb_carregar_dados_agenciasBancarias = Checkbutton(self.janela_principal, text='carregar agencias bancárias', variable=self.var_carregar_dados_agenciasBancarias).place(x=540, y=280)

        self.var_enviar_dados_agencias_bancarias = IntVar()
        self.cb_enviar_dados_agencias_bancarias = Checkbutton(self.janela_principal, text='Enviar agencias bancarias', variable=self.var_enviar_dados_agencias_bancarias).place(x=540, y=300)

        self.var_enviar_dados_contas_bancarias = IntVar()
        self.cb_enviar_dados_contas_bancarias = Checkbutton(self.janela_principal, text='Enviar contas bancarias', variable=self.var_enviar_dados_contas_bancarias).place(x=540, y=320)

        self.var_enviar_dados_cnaes = IntVar()
        self.cb_enviar_dados_cnaes = Checkbutton(self.janela_principal, text='Enviar cnaes', variable=self.var_enviar_dados_cnaes).place(x=540, y=340)

        self.var_enviar_dados_compensacoes = IntVar()
        self.cb_enviar_dados_compensacoes = Checkbutton(self.janela_principal, text='Enviar ccompensações', variable=self.var_enviar_dados_compensacoes).place(x=540, y=360)

        self.var_enviar_dados_competencias = IntVar()
        self.cb_enviar_dados_competencias = Checkbutton(self.janela_principal, text='Enviar enviar_dados_competencias', variable=self.var_enviar_dados_competencias).place(x=540, y=380)

        self.var_enviar_dados_condominiosInfComplem = IntVar()
        self.cb_enviar_dados_condominiosInfComplem = Checkbutton(self.janela_principal, text='Enviar condominios Inf Complemtares', variable=self.var_enviar_dados_condominiosInfComplem).place(x=275, y=20)

        self.var_enviar_dados_condominiosInfComplemOp = IntVar()
        self.cb_enviar_dados_condominiosInfComplemOp = Checkbutton(self.janela_principal, text='Enviar condominios Inf Complementares Op', variable=self.var_enviar_dados_condominiosInfComplemOp).place(x=275, y=40)

        self.var_enviar_dados_configContribMelhorias = IntVar()
        self.cb_enviar_dados_configContribMelhorias = Checkbutton(self.janela_principal, text='Enviar config Contribuição Melhorias', variable=self.var_enviar_dados_configContribMelhorias).place(x=275, y=60)

        self.var_enviar_dados_configEconomicosTabelasAuxiliaresHistorico = IntVar()
        self.cb_enviar_dados_configEconomicosTabelasAuxiliaresHistorico = Checkbutton(self.janela_principal, text='Enviar config Economicos Tabelas Auxiliares Historico', variable=self.var_enviar_dados_configEconomicosTabelasAuxiliaresHistorico).place(x=275, y=80)

        self.var_enviar_dados_configGeoprocessamento = IntVar()
        self.cb_enviar_dados_configGeoprocessamento = Checkbutton(self.janela_principal, text='Enviar config Geoprocessamento', variable=self.var_enviar_dados_configGeoprocessamento).place(x=275, y=100)

        self.var_enviar_dados_configGeracaoGuias = IntVar()
        self.cb_enviar_dados_configGeracaoGuias = Checkbutton(self.janela_principal, text='Enviar config GeracaoGuias', variable=self.var_enviar_dados_configGeracaoGuias).place(x=275, y=120)

        self.var_enviar_dados_configHomologacaoTributos = IntVar()
        self.cb_enviar_dados_configHomologacaoTributos = Checkbutton(self.janela_principal, text='Enviar config Homologação Tributos', variable=self.var_enviar_dados_configHomologacaoTributos).place(x=275, y=140)

        self.var_enviar_dados_configImobiliarias = IntVar()
        self.cb_enviar_dados_configImobiliarias = Checkbutton(self.janela_principal, text='Enviar config Imobiliarias', variable=self.var_enviar_dados_configImobiliarias).place(x=275, y=160)

        self.var_enviar_dados_configImobiliarias = IntVar()
        self.cb_enviar_dados_configImobiliarias = Checkbutton(self.janela_principal, text='Enviar config Imobiliarias', variable=self.var_enviar_dados_configImobiliarias).place(x=275, y=180)

        self.var_enviar_dados_configInscrImobiliarias = IntVar()
        self.cb_enviar_dados_configInscrImobiliarias = Checkbutton(self.janela_principal, text='Enviar config Inscrição Imobiliarias', variable=self.var_enviar_dados_configInscrImobiliarias).place(x=275, y=200)

        self.var_enviar_dados_configParcCreditos = IntVar()
        self.cb_enviar_dados_configParcCreditos = Checkbutton(self.janela_principal, text='Enviar config Parc Creditos', variable=self.var_enviar_dados_configParcCreditos).place(x=275, y=220)

        self.var_enviar_dados_configNotasAvulsas = IntVar()
        self.cb_enviar_dados_configNotasAvulsas = Checkbutton(self.janela_principal, text='Enviar config Notas Avulsas', variable=self.var_enviar_dados_configNotasAvulsas).place(x=275, y=240)

        self.var_enviar_dados_configParcCreditosTaxas = IntVar()
        self.cb_enviar_dados_configParcCreditosTaxas = Checkbutton(self.janela_principal, text='Enviar config Parc Creditos Taxas', variable=self.var_enviar_dados_configParcCreditosTaxas).place(x=275, y=260)

        self.var_enviar_dados_configParcelamentos = IntVar()
        self.cb_enviar_dados_configParcelamentos = Checkbutton(self.janela_principal, text='Enviar config Parcelamentos', variable=self.var_enviar_dados_configParcelamentos).place(x=275, y=280)

        self.var_enviar_dados_configTaxaExpedCredts = IntVar()
        self.cb_enviar_dados_configTaxaExpedCredts = Checkbutton(self.janela_principal, text='Enviar config Taxa Exped Creditos', variable=self.var_enviar_dados_configTaxaExpedCredts).place(x=275, y=300)

        self.var_enviar_dados_configTaxaExpediente = IntVar()
        self.cb_enviar_dados_configTaxaExpediente = Checkbutton(self.janela_principal, text='Enviar config Taxa Expediente', variable=self.var_enviar_dados_configTaxaExpediente).place(x=275, y=320)

        self.var_enviar_dados_configTransfImoMotivos = IntVar()
        self.cb_enviar_dados_configTransfImoMotivos = Checkbutton(self.janela_principal, text='Enviar config Transferencia Imoveis Motivos', variable=self.var_enviar_dados_configTransfImoMotivos).place(x=275, y=340)

        self.var_enviar_dados_configTransfImoReceitas = IntVar()
        self.cb_enviar_dados_configTransfImoReceitas = Checkbutton(self.janela_principal, text='Enviar config Transf Imoveis Receitas', variable=self.var_enviar_dados_configTransfImoReceitas).place(x=275, y=360)

        self.var_enviar_dados_configTransfImoveis = IntVar()
        self.cb_enviar_dados_configTransfImoveis = Checkbutton(self.janela_principal, text='Enviar config Transf Imoveis', variable=self.var_enviar_dados_configTransfImoveis).place(x=275, y=380)

        self.var_enviar_dados_configuracoes = IntVar()
        self.cb_enviar_dados_configuracoes = Checkbutton(self.janela_principal, text='Enviar configuracoes', variable=self.var_enviar_dados_configuracoes).place(x=275, y=400)

        self.var_enviar_dados_configuracoesArrecadacoes = IntVar()
        self.cb_enviar_dados_configuracoesArrecadacoes = Checkbutton(self.janela_principal, text='Enviar configurações Arrecadacoes', variable=self.var_enviar_dados_configuracoesArrecadacoes).place(x=275, y=420)

        self.var_enviar_dados_contribMelhoriasTaxas = IntVar()
        self.cb_enviar_dados_contribMelhoriasTaxas = Checkbutton(self.janela_principal, text='Enviar contrib Melhorias Taxas', variable=self.var_enviar_dados_contribMelhoriasTaxas).place(x=275, y=440)

        self.var_enviar_dados_configuracoesGeracaoParcelas = IntVar()
        self.cb_enviar_dados_configuracoesGeracaoParcelas = Checkbutton(self.janela_principal, text='Enviar configuracoes Geracao Parcelas', variable=self.var_enviar_dados_configuracoesGeracaoParcelas).place(x=275, y=460)

        self.var_enviar_dados_configuracoesGeracaoParcelasReceitas = IntVar()
        self.cb_enviar_dados_configuracoesGeracaoParcelasReceitas = Checkbutton(self.janela_principal, text='Enviar configuracoes Geracao Parcelas Receitas', variable=self.var_enviar_dados_configuracoesGeracaoParcelasReceitas).place(x=275, y=480)

        self.var_enviar_dados_configuracoesParcelas = IntVar()
        self.cb_enviar_dados_configuracoesParcelas = Checkbutton(self.janela_principal, text='Enviar configuracoes Parcelas', variable=self.var_enviar_dados_configuracoesParcelas).place(x=275, y=500)

        self.var_enviar_dados_construtoras = IntVar()
        self.cb_enviar_dados_construtoras = Checkbutton(self.janela_principal, text='Enviar construtoras', variable=self.var_enviar_dados_construtoras).place(x=275, y=520)

        self.var_enviar_dados_construtorasEngArquitetos = IntVar()
        self.cb_enviar_dados_construtorasEngArquitetos = Checkbutton(self.janela_principal, text='Enviar construtoras Eng. Arquitetos', variable=self.var_enviar_dados_construtorasEngArquitetos).place(x=275, y=540)

        self.var_enviar_dados_contadores = IntVar()
        self.cb_enviar_dados_contadores = Checkbutton(self.janela_principal, text='Enviar contadores.', variable=self.var_enviar_dados_contadores).place(x=275, y=560)

        self.var_enviar_dados_contadoresCbo = IntVar()
        self.cb_enviar_dados_contadoresCbo = Checkbutton(self.janela_principal, text='Enviar contadoresCbo', variable=self.var_enviar_dados_contadoresCbo).place(x=275, y=580)

        self.var_enviar_dados_contadoresResponsaveis = IntVar()
        self.cb_enviar_dados_contadoresResponsaveis = Checkbutton(self.janela_principal, text='Enviar enviar_dados_contadoresResponsaveis', variable=self.var_enviar_dados_contadoresResponsaveis).place(x=275, y=600)

        self.var_enviar_dados_ContribMelhoriasBairros = IntVar()
        self.cb_enviar_dados_ContribMelhoriasBairros = Checkbutton(self.janela_principal, text='Enviar configuracoes Parcelas', variable=self.var_enviar_dados_ContribMelhoriasBairros).place(x=275, y=620)

        self.var_enviar_dados_contribMelhoriasImoveis = IntVar()
        self.cb_enviar_dados_contribMelhoriasImoveis = Checkbutton(self.janela_principal, text='Enviar contrib Melhorias Imoveis', variable=self.var_enviar_dados_contribMelhoriasImoveis).place(x=275, y=640)

        self.var_enviar_dados_contribMelhoriasInfComp = IntVar()
        self.cb_enviar_dados_contribMelhoriasInfComp = Checkbutton(self.janela_principal, text='Enviar contrib Melhorias Inf Comp', variable=self.var_enviar_dados_contribMelhoriasInfComp).place(x=275, y=660)

        self.var_enviar_dados_contribMelhoriasMateriaisServicos = IntVar()
        self.cb_enviar_dados_contribMelhoriasMateriaisServicos = Checkbutton(self.janela_principal, text='Enviar contrib Melhorias Materiais Servicos', variable=self.var_enviar_dados_contribMelhoriasMateriaisServicos).place(x=275, y=680)

        self.var_enviar_dados_contribMelhoriasMovtos = IntVar()
        self.cb_enviar_dados_contribMelhoriasMovtos = Checkbutton(self.janela_principal, text='Enviar contrib Melhorias Movtos', variable=self.var_enviar_dados_contribMelhoriasMovtos).place(x=275, y=700)

        self.var_enviar_dados_contribMelhoriasSaldos = IntVar()
        self.cb_enviar_dados_contribMelhoriasSaldos = Checkbutton(self.janela_principal, text='Enviar contrib Melhorias Saldos', variable=self.var_enviar_dados_contribMelhoriasSaldos).place(x=275, y=720)

        self.var_enviar_dados_contribMelhoriasTaxas = IntVar()
        self.cb_enviar_dados_contribMelhoriasTaxas = Checkbutton(self.janela_principal, text='Enviar contrib Melhorias Taxas', variable=self.var_enviar_dados_contribMelhoriasTaxas).place(x=275, y=740)

        self.var_enviar_dados_contribMelImovInfComp = IntVar()
        self.cb_enviar_dados_contribMelImovInfComp = Checkbutton(self.janela_principal, text='Enviar enviar dados contrib MelImovInfComp', variable=self.var_enviar_dados_contribMelImovInfComp).place(x=275, y=760)

        self.var_enviar_dados_contribMovtosDetalhes = IntVar()
        self.cb_enviar_dados_contribMovtosDetalhes = Checkbutton(self.janela_principal, text='Enviar contrib Movtos Detalhes', variable=self.var_enviar_dados_contribMovtosDetalhes).place(x=275, y=780)

        self.var_enviar_dados_contribuicoesMelhorias = IntVar()
        self.cb_enviar_dados_contribuicoesMelhorias = Checkbutton(self.janela_principal, text='Enviar contribuicoes Melhorias', variable=self.var_enviar_dados_contribuicoesMelhorias).place(x=275, y=800)

        self.var_enviar_dados_conveniosMensagens = IntVar()
        self.cb_enviar_dados_conveniosMensagens = Checkbutton(self.janela_principal, text='Enviar convenios Mensagens', variable=self.var_enviar_dados_conveniosMensagens).place(x=275, y=820)

        self.var_enviar_dados_contrMelhoriasInfCompOp = IntVar()
        self.cb_enviar_dados_contrMelhoriasInfCompOp = Checkbutton(self.janela_principal, text='Enviar contr Melhorias Inf CompOp', variable=self.var_enviar_dados_contrMelhoriasInfCompOp).place(x=275, y=840)

        self.var_enviar_dados_contrMelhoriasInfCompOp_exercicios = IntVar()
        self.cb_enviar_dados_contrMelhoriasInfCompOp_exercicios = Checkbutton(self.janela_principal, text='Enviar lançamentos aberturas do exercício', variable=self.var_enviar_dados_contrMelhoriasInfCompOp_exercicios).place(x=540, y=140)

        self.var_enviar_dados_convenios = IntVar()
        self.cb_enviar_dados_convenios = Checkbutton(self.janela_principal, text='Enviar convenios', variable=self.var_enviar_dados_convenios).place(x=540, y=120)

        self.var_enviar_dados_conveniosSimulacoes = IntVar()
        self.cb_enviar_dados_conveniosSimulacoes = Checkbutton(self.janela_principal, text='Enviar convenios Simulacoes', variable=self.var_enviar_dados_conveniosSimulacoes).place(x=540, y=100)

        self.var_enviar_dados_creditosTributarios = IntVar()
        self.cb_enviar_dados_creditosTributarios = Checkbutton(self.janela_principal, text='Enviar creditos Tributarios', variable=self.var_enviar_dados_creditosTributarios).place(x=540, y=220)

        self.var_contas_correntes_enviar_dados_creditosTributarios_itens = IntVar()
        self.cb_contas_correntes_enviar_dados_creditosTributarios_itens = Checkbutton(self.janela_principal, text='Enviar contas correntes lançamentos encerramentos itens', variable=self.var_contas_correntes_enviar_dados_creditosTributarios_itens).place(x=540, y=400)

        self.var_enviar_dados_creditosTributariosRec = IntVar()
        self.cb_enviar_dados_creditosTributariosRec = Checkbutton(self.janela_principal, text='Enviar creditos Tributarios Rec', variable=self.var_enviar_dados_creditosTributariosRec).place(x=275, y=960)

        self.var_enviar_dados_declaracoes = IntVar()
        self.cb_enviar_dados_declaracoes = Checkbutton(self.janela_principal, text='Enviar declaracoes', variable=self.var_enviar_dados_declaracoes).place(x=275, y=980)

        self.var_enviar_dados_declaracoesServicos = IntVar()
        self.cb_enviar_dados_declaracoesServicos = Checkbutton(self.janela_principal, text='enviar declaracoes Servicos', variable=self.var_enviar_dados_declaracoesServicos).place(x=275, y=1000)

        self.var_enviar_dados_deducaoCreditoSimAm = IntVar()
        self.cb_enviar_dados_deducaoCreditoSimAm = Checkbutton(self.janela_principal, text='Enviar deducao Credito SimAm', variable=self.var_enviar_dados_deducaoCreditoSimAm).place(x=275, y=1020)

        self.var_aenviar_dados_deducaoDividaSimAm = IntVar()
        self.cb_aenviar_dados_deducaoDividaSimAm = Checkbutton(self.janela_principal, text='Enviar deducao Divida SimAm', variable=self.var_aenviar_dados_deducaoDividaSimAm).place(x=275, y=1040)

        self.var_enviar_dados_desmembramentos = IntVar()
        self.cb_enviar_dados_desmembramentos = Checkbutton(self.janela_principal, text='Enviar desmembramentos', variable=self.var_enviar_dados_desmembramentos).place(x=275, y=1060)

        self.var_enviar_dados_desmembramentosDocumentos = IntVar()
        self.cb_enviar_dados_desmembramentosDocumentos = Checkbutton(self.janela_principal, text='Enviar desmembramentos Documentos', variable=self.var_enviar_dados_desmembramentosDocumentos).place(x=275, y=1080)

        self.varenviar_dados_desmembramentosImoveis = IntVar()
        self.cbenviar_dados_desmembramentosImoveis = Checkbutton(self.janela_principal, text='Enviar desmembramentos Imoveis', variable=self.varenviar_dados_desmembramentosImoveis).place(x=275, y=1100)

        self.var_enviar_dados_distritos = IntVar()
        self.cb_enviar_dados_distritos = Checkbutton(self.janela_principal, text='Enviar parâmetros orcamentários', variable=self.var_enviar_dados_distritos).place(x=540, y=20)

        self.var_enviar_dados_dividaDebitoInscrito = IntVar()
        self.cb_enviar_dados_dividaDebitoInscrito = Checkbutton(self.janela_principal, text='Enviar divida Debito Inscrito', variable=self.var_enviar_dados_dividaDebitoInscrito).place(x=540, y=40)

        self.var_enviar_dados_dividas = IntVar()
        self.cb_enviar_dados_dividas = Checkbutton(self.janela_principal, text='Enviar dividas', variable=self.var_enviar_dados_dividas).place(x=540, y=60)

        self.var_enviar_dados_dividasMovtos = IntVar()
        self.cb_enviar_dados_dividasMovtos = Checkbutton(self.janela_principal, text='Enviar dividas Movtos', variable=self.var_enviar_dados_dividasMovtos).place(x=540, y=80)

        self.var_enviar_dados_dividasReceitas = IntVar()
        self.cb_enviar_dados_dividasReceitas = Checkbutton(self.janela_principal, text='Enviar dividas Receitas', variable=self.var_enviar_dados_dividasReceitas).place(x=540, y=100)

        self.var_enviar_dados_dividasResponsaveis = IntVar()
        self.cb_enviar_dados_dividasResponsaveis = Checkbutton(self.janela_principal, text='Enviar dividas Responsaveis', variable=self.var_enviar_dados_dividasResponsaveis).place(x=540, y=120)

        self.var_enviar_dados_unidadesMedidas = IntVar()
        self.cb_enviar_dados_unidadesMedidas = Checkbutton(self.janela_principal, text='Enviar dados unidades Medidas', variable=self.var_enviar_dados_unidadesMedidas).place(x=540, y=140)				

        self.var_enviar_dados_motivos = IntVar()
        self.cb_enviar_dados_motivos = Checkbutton(self.janela_principal, text='Enviar dados motivos', variable=self.var_enviar_dados_motivos).place(x=540, y=420)				        

                        
        # Criando os botões
        self.botao = Button(self.janela_principal, text='Executar', command=self.executar).place(x=600, y=540, height=40, width=150)
        self.botao_sair = Button(self.janela_principal, text='Sair', command=self.janela_principal.quit).place(x=800, y=540, height=40, width=150)
        
        # Define o título da janela
        self.janela_principal.title("Envio de dados para o sistema Contabilidade Cloud")

        # Define o tamanho da janela
        self.janela_principal.geometry('1360x920')
        self.janela_principal.resizable(False, False)
        #self.janela_principal.state('zoomed')

        # Rodando
        mainloop()
    
    def executar(self):
        if self.var_carregar_dados_paises.get() == 1:
            functions.carregar_dados_paises()
        if self.var_carregar_dados_estados.get() == 1:
            functions.carregar_dados_estados()
        if self.var_carregar_dados_municipios.get() == 1:
            functions.carregar_dados_municipios()
        if self.var_enviar_dados_logradourosBairros.get() == 1:
            functions.enviar_dados_logradourosBairros()
        if self.var_enviar_dados_advogados.get() == 1:
            functions.enviar_dados_advogados()
        if self.var_enviar_dados_advogadosCbo.get() == 1:
            functions.enviar_dados_advogadosCbo()
        if self.var_enviar_dados_advogadosResponsaveis.get() == 1:
            functions.enviar_dados_advogadosResponsaveis()
        if self.var_tipos_logradouros.get() == 1:
            functions.enviar_dados_tipos_logradouros()
        if self.var_enviar_dados_loteamentos.get() == 1:
            functions.enviar_dados_loteamentos()
        if self.var_enviar_dados_condominios.get() == 1:
            functions.enviar_dados_condominios()                
        if self.var_enviar_dados_agrupamentos() == 1:
            functions.enviar_dados_agrupamentos()       
        if self.var_enviar_dados_agrupamentosCamposAdicionais() == 1:
            functions.enviar_dados_agrupamentosCamposAdicionais()   
        if self.var_enviar_dados_alvaras.get() == 1:
            functions.enviar_dados_alvaras()
        if self.var_enviar_dados_anistias.get() == 1:
            functions.enviar_dados_anistias()
        if self.var_enviar_dados_arquivos.get() == 1:
            functions.enviar_dados_arquivos()
        if self.var_enviar_dados_atividadesEconomicas.get() == 1:
            functions.enviar_dados_atividadesEconomicas()
        if self.var_enviar_dados_configuracoesArrecadacoes.get() == 1:
            functions.enviar_dados_configuracoesArrecadacoes()
        if self.var_enviar_dados_atividadesEconomicasInfComplem.get() == 1:
            functions.enviar_dados_atividadesEconomicasInfComplem()
        if self.var_enviar_dados_atividadesEconomicasInfCompOp.get() == 1:
            functions.enviar_dados_atividadesEconomicasInfCompOp()
        if self.var_enviar_dados_atividadesEconomicasRelacionadas.get() == 1:
            functions.enviar_dados_atividadesEconomicasRelacionadas()
        if self.var_enviar_dados_atividadesEconomicasValores.get() == 1:
            functions.enviar_dados_atividadesEconomicasValores()
        if self.var_enviar_dados_atos.get() == 1:
            functions.enviar_dados_atos()
        if self.var_enviar_dados_atosFontesDivulgacoes.get() == 1:
            functions.enviar_dados_atosFontesDivulgacoes()
        if self.var_enviar_dados_atualizacaoDividaAtivaSimAm.get() == 1:
            functions.enviar_dados_atualizacaoDividaAtivaSimAm()
        if self.var_enviar_dados_atualizacaoMonetariaSimAm.get() == 1:
            functions.enviar_dados_atualizacaoMonetariaSimAm()
        if self.var_enviar_dados_baixaAutomatica.get() == 1:
            functions.enviar_dados_baixaAutomatica()
        if self.var_enviar_dados_baixaAutomaticaPagamentos.get() == 1:
            functions.enviar_dados_baixaAutomaticaPagamentos()
        if self.var_enviar_dados_baixaManual.get() == 1:
            functions.enviar_dados_baixaManual()
        if self.var_enviar_dados_baixaManualPagamentos.get() == 1:
            functions.enviar_dados_baixaManualPagamentos()
        if self.var_enviar_dados_baixasAutomaticas.get() == 1:
            functions.enviar_dados_baixasAutomaticas()
        if self.var_enviar_dados_beneficiosFiscais.get() == 1:
            functions.enviar_dados_beneficiosFiscais()
        if self.var_enviar_dados_calculosTributarios.get() == 1:
            functions.enviar_dados_calculosTributarios()
        if self.var_enviar_dados_calculosTributariosAvancado.get() == 1:
            functions.enviar_dados_calculosTributariosAvancado()
        if self.var_enviar_dados_calculosTributariosAvancadoOpc.get() == 1:
            functions.enviar_dados_calculosTributariosAvancadoOpc()
        if self.var_enviar_dados_camposAdicionais.get() == 1:
            functions.enviar_dados_camposAdicionais()
        if self.var_enviar_dados_cancelamentoDocumentos.get() == 1:
            functions.enviar_dados_cancelamentoDocumentos()
        if self.var_enviar_dados_cartorios.get() == 1:
            functions.enviar_dados_cartorios()
        if self.var_enviar_dados_cbos.get() == 1:
            functions.enviar_dados_cbos()
        if self.var_enviar_dados_certidoesITBI.get() == 1:
            functions.enviar_dados_certidoesITBI()
        if self.var_enviar_dados_certidoesNegativas.get() == 1:
            functions.enviar_dados_certidoesNegativas()
        if self.var_carregar_dados_agenciasBancarias.get() == 1:
            functions.carregar_dados_agenciasBancarias()
        if self.var_enviar_dados_agencias_bancarias.get() == 1:
            functions.enviar_dados_agencias_bancarias()
        if self.var_enviar_dados_contas_bancarias.get() == 1:
            functions.enviar_dados_contas_bancarias()
        if self.var_enviar_dados_cnaes.get() == 1:
            functions.enviar_dados_cnaes()
        if self.var_enviar_dados_compensacoes.get() == 1:
            functions.enviar_dados_compensacoes()
        if self.var_enviar_dados_competencias.get() == 1:
            functions.enviar_dados_competencias()
        if self.var_enviar_dados_condominios.get() == 1:
            functions.enviar_dados_condominios()
        if self.var_enviar_dados_condominiosInfComplem.get() == 1:
            functions.enviar_dados_condominiosInfComplem()
        if self.var_enviar_dados_condominiosInfComplemOp.get() == 1:
            functions.enviar_dados_condominiosInfComplemOp()
        if self.var_enviar_dados_configContribMelhorias.get() == 1:
            functions.enviar_dados_configContribMelhorias()
        if self.var_enviar_dados_configEconomicosTabelasAuxiliaresHistorico.get() == 1:
            functions.enviar_dados_configEconomicosTabelasAuxiliaresHistorico()
        if self.var_enviar_dados_configGeoprocessamento.get() == 1:
            functions.enviar_dados_configGeoprocessamento()
        if self.var_enviar_dados_configGeracaoGuias.get() == 1:
            functions.enviar_dados_configGeracaoGuias()
        if self.var_enviar_dados_configHomologacaoTributos.get() == 1:
            functions.enviar_dados_configHomologacaoTributos()
        if self.var_enviar_dados_configImobiliarias.get() == 1:
            functions.enviar_dados_configImobiliarias()
        if self.var_enviar_dados_configImobiliarias.get() == 1:
            functions.enviar_dados_configImobiliarias()
        if self.var_enviar_dados_configInscrImobiliarias.get() == 1:
            functions.enviar_dados_configInscrImobiliarias()
        if self.var_enviar_dados_configParcCreditos.get() == 1:
            functions.enviar_dados_configParcCreditos()
        if self.var_enviar_dados_configNotasAvulsas.get() == 1:
            functions.enviar_dados_configNotasAvulsas()
        if self.var_enviar_dados_configParcCreditosTaxas.get() == 1:
            functions.enviar_dados_configParcCreditosTaxas()
        if self.var_enviar_dados_configParcelamentos.get() == 1:
            functions.enviar_dados_configParcelamentos()
        if self.var_enviar_dados_configTaxaExpedCredts.get() == 1:
            functions.enviar_dados_configTaxaExpedCredts()
        if self.var_enviar_dados_configTaxaExpediente.get() == 1:
            functions.enviar_dados_configTaxaExpediente()
        if self.var_enviar_dados_configTransfImoMotivos.get() == 1:
            functions.enviar_dados_configTransfImoMotivos()
        if self.var_enviar_dados_configTransfImoReceitas.get() == 1:
            functions.enviar_dados_configTransfImoReceitas()
        if self.var_enviar_dados_configTransfImoveis.get() == 1:
            functions.enviar_dados_configTransfImoveis()
        if self.var_enviar_dados_configuracoes.get() == 1:
            functions.enviar_dados_configuracoes()
        if self.var_enviar_dados_configuracoesArrecadacoes.get() == 1:
            functions.enviar_dados_configuracoesArrecadacoes()
        if self.var_enviar_dados_contribMelhoriasTaxas.get() == 1:
            functions.enviar_dados_contribMelhoriasTaxas()
        if self.var_enviar_dados_configuracoesGeracaoParcelasReceitas.get() == 1:
            functions.enviar_dados_configuracoesGeracaoParcelasReceitas()
        if self.var_enviar_dados_configuracoesParcelas.get() == 1:
            functions.enviar_dados_configuracoesParcelas()
        if self.var_enviar_dados_construtoras.get() == 1:
            functions.enviar_dados_construtoras()
        if self.var_enviar_dados_construtorasEngArquitetos.get() == 1:
            functions.enviar_dados_construtorasEngArquitetos()
        if self.var_enviar_dados_contadores.get() == 1:
            functions.enviar_dados_contadores()
        if self.var_enviar_dados_contadoresCbo.get() == 1:
            functions.enviar_dados_contadoresCbo()
        if self.var_enviar_dados_contadoresResponsaveis.get() == 1:
            functions.enviar_dados_contadoresResponsaveis()
        if self.var_enviar_dados_ContribMelhoriasBairros.get() == 1:
            functions.enviar_dados_ContribMelhoriasBairros()
        if self.var_enviar_dados_contribMelhoriasImoveis.get() == 1:
            functions.enviar_dados_contribMelhoriasImoveis()
        if self.var_enviar_dados_contribMelhoriasInfComp.get() == 1:
            functions.enviar_dados_contribMelhoriasInfComp()
        if self.var_enviar_dados_contribMelhoriasMateriaisServicos.get() == 1:
            functions.enviar_dados_contribMelhoriasMateriaisServicos()
        if self.var_enviar_dados_contribMelhoriasMovtos.get() == 1:
            functions.enviar_dados_contribMelhoriasMovtos()
        if self.var_enviar_dados_contribMelhoriasSaldos.get() == 1:
            functions.enviar_dados_contribMelhoriasSaldos()
        if self.var_enviar_dados_contribMelhoriasTaxas.get() == 1:
            functions.enviar_dados_contribMelhoriasTaxas()
        if self.var_enviar_dados_contribMelImovInfComp.get() == 1:
            functions.enviar_dados_contribMelImovInfComp()
        if self.var_enviar_dados_contribMovtosDetalhes.get() == 1:
            functions.enviar_dados_contribMovtosDetalhes()
        if self.var_enviar_dados_contribuicoesMelhorias.get() == 1:
            functions.enviar_dados_contribuicoesMelhorias()
        if self.var_enviar_dados_conveniosMensagens.get() == 1:
            functions.enviar_dados_conveniosMensagens()
        if self.var_enviar_dados_contrMelhoriasInfCompOp.get() == 1:
            functions.enviar_dados_contrMelhoriasInfCompOp()
        if self.var_enviar_dados_convenios.get() == 1:
            functions.enviar_dados_convenios()
        if self.var_enviar_dados_conveniosSimulacoes.get() == 1:
            functions.enviar_dados_conveniosSimulacoes()
        if self.var_enviar_dados_creditosTributarios.get() == 1:
            functions.enviar_dados_creditosTributarios()        
        if self.var_enviar_dados_creditosTributariosRec.get() == 1:
            functions.enviar_dados_creditosTributariosRec()
        if self.var_enviar_dados_declaracoes.get() == 1:
            functions.enviar_dados_declaracoes()
        if self.var_enviar_dados_declaracoesServicos.get() == 1:
            functions.enviar_dados_declaracoesServicos()
        if self.var_enviar_dados_deducaoCreditoSimAm.get() == 1:
            functions.enviar_dados_deducaoCreditoSimAm()
        if self.var_aenviar_dados_deducaoDividaSimAm.get() == 1:
            functions.enviar_dados_deducaoDividaSimAm()
        if self.var_enviar_dados_desmembramentos.get() == 1:
            functions.enviar_dados_desmembramentos()
        if self.var_enviar_dados_desmembramentosDocumentos.get() == 1:
            functions.enviar_dados_desmembramentosDocumentos()
        if self.varenviar_dados_desmembramentosImoveis.get() == 1:
            functions.enviar_dados_desmembramentosImoveis()
        if self.var_enviar_dados_distritos.get() == 1:
            functions.enviar_dados_distritos()
        if self.var_enviar_dados_dividaDebitoInscrito.get() == 1:
            functions.enviar_dados_dividaDebitoInscrito()
        if self.var_enviar_dados_dividas.get() == 1:
            functions.enviar_dados_dividas()
        if self.var_enviar_dados_dividasMovtos.get() == 1:
            functions.enviar_dados_dividasMovtos()
        if self.var_enviar_dados_dividasReceitas.get() == 1:
            functions.enviar_dados_dividasReceitas()
        if self.var_enviar_dados_dividasResponsaveis.get() == 1:
            functions.enviar_dados_dividasResponsaveis()     
        if self.var_enviar_dados_unidadesMedidas.get() == 1:    
            functions.enviar_dados_unidadesMedidas() 
        if self.var_enviar_dados_motivos.get() == 1:
            functions.enviar_dados_motivos()    

if __name__ == "__main__":
    
    gui = MinhaGUI()