import menu_functions as functions
import os

def linha(tam=155):
    return '*' * tam

def cabecalho():
    print(linha())
    print('ENVIO DE DADOS PARA O SISTEMA TRIBUTOS CLOUD'.center(155))
    print(linha())

def montar_menu():
    cabecalho()
    print('''
[56] Enviar enviar_dados_condominiosInfComplemOp                      [111] enviar_dados_dividasMovtos
[57] Enviar enviar_dados_condominiosInfComplemOp do exercício         [112] enviar_dados_dividasReceitas
[58] Enviar enviar_dados_configEconomicosTabelasAuxiliaresHistorico   [113] enviar_dados_dividasResponsaveis
[59] Enviar enviar_dados_configGeoprocessamento                       [114] enviar_dados_unidadesMedidas        
[60] Enviar enviar_dados_configGeracaoGuias                           [158] Enviar Bairros           
[61] Enviar enviar_dados_configHomologacaoTributos                           
[10] Carregar agenciasBancarias  
[2] enviar dados motivos                                              [62] Enviar enviar_dados_configImobiliarias                                 
[3] Carregar países                                                   [63] Enviar enviar_dados_configInscDividaAtiva                              
[4] Carregar estados                                                  [64] Enviar enviar_dados_configInscrImobiliarias                            
[5] Carregar municípios                                               [65] Enviar enviar_dados_configParcCreditos                      
[11] Enviar unidades de medida                                        [66] Enviar enviar_dados_configNotasAvulsas                                 
[12] Enviar Bairros                                        [67] Enviar enviar_dados_configParcCreditosTaxas                 
[13] Enviar tipos de comprovantes                                     [68] Enviar agrupamentos Campos Adicionais                                  
[14] Enviar deduções de receitas                                      [69] Enviar acréscimos de enviar_dados_configParcelamentos                  
[15] Enviar deduções receitas exercícios                              [70] Enviar enviar_dados_configTaxaExpediente                          
[16] Enviar tipos de logradouros                                      [71] Enviar enviar_dados_configTransfImoMotivos                        
[17] Enviar loteamentos                                               [72] Enviar enviar_dados_configTransfImoReceitas                       
[18] Enviar condomínios                                               [73] Enviar naturezas de enviar_dados_configuracoes                    
[19] Enviar alvaras                                                   [74] Enviar diárias                                                    
[20] Enviar agencias bancarias                                        [75] Enviar enviar_dados_configuracoesArrecadacoes                     
[21] Enviar anistias                                                  [76] Enviar sanção das alterações orçamentárias das receitas           
[22] Enviar tipos de administrações                                   [77] Enviar enviar_dados_configuracoesGeracaoParcelas                                        
[23] Enviar dados arquivos                                            [78] Enviar origens de enviar_dados_configuracoesGeracaoParcelas                             
[24] Enviar enviar_dados_arquivos exercício                           [79] Enviar origens de enviar_dados_construtoras               
[25] Enviar atividades Economicas Inf Complem                         [80] Enviar enviar_dados_construtorasEngArquitetos                                
[26] Enviar atividades Economicas Inf CompOp                          [81] Enviar enviar_dados_contadores      
[27] Enviar atividades Economicas Relacionadas                        [82] Enviar enviar_dados_contadoresCbo    
[28] Enviar atividades Economicas Valores                             [83] Enviar envio ao legislativo a alteração orçamentária da despesa 
[29] Enviar enviar atos                                               [84] Enviar enviar_dados_ContribMelhoriasBairros                   
[30] Enviar atos Fontes Divulgacoes                                   [85] Enviar enviar_dados_contribMelhoriasImoveis                                                  
[31] Enviar ações                                                     [86] Enviar enviar_dados_contribMelhoriasInfComp                                                  
[32] Enviar configurações funcionais                                  [87] enviar_dados_contribMelhoriasMateriaisServicos                                            
[33] Enviar funções                                                   [88] Enviar enviar_dados_contribMelhoriasMovtos                                       
[34] Enviar subfunções                                                [89] Enviar enviar_dados_contribMelhoriasSaldos                          
[35] Enviar localizadores                                             [90] enviar_dados_contribuicoesMelhorias                               
[36] Enviar configurações naturezas despesas                          [91] enviar_dados_contribMelhoriasTaxas                             
[37] Enviar naturezas de despesas                                     [92] enviar_dados_contribMelImovInfComp                             
[38] Enviar configurações de naturezas de despesas                    [93] enviar_dados_contribMovtosDetalhes                             
[39] Enviar naturezas de receitas                                     [94] Enviar saldos iniciais                                         
[40] Enviar responsaveis                                              [95] enviar_dados_conveniosCreditos                                 
[41] Enviar programas                                                 [96] enviar_dados_conveniosMensagens                            
[42] Enviar ordenadores de despesas                                   [97] Enviar enviar_dados_convenios                              
[43] Enviar receitas não previstas                                    [98] enviar_dados_conveniosSimulacoes                           
[44] Enviar enviar_dados_cartorios                                    [99] enviar_dados_creditosTributarios              
[45] Enviar enviar_dados_cbos                                         [100] enviar_dados_creditosTributariosRec          
[46] Enviar enviar_dados_certidoesITBI                                [101] enviar_dados_declaracoes     
[47] Enviar enviar_dados_certidoesNegativas                           [102] enviar_dados_declaracoesServicos       
[48] Enviar agências bancárias                                        [103] enviar_dados_deducaoCreditoSimAm                                     
[49] Enviar agrupamentos                                              [104] enviar_dados_deducaoDividaSimAm                                            
[50] Enviar marcadores                                                [105] enviar_dados_desmembramentos                                    
[51] Enviar contas bancarias da entidade                              [106] enviar_dados_desmembramentosDocumentos                                         [T] Todos
[52] Enviar enviar_dados_compensacoes                                 [107] enviar_dados_desmembramentosImoveis                                            [S] Sair
[53] Enviar enviar_dados_competencias                                 [108] enviar_dados_distritos                                   
[54] Enviar enviar_dados_condominios                                  [109] enviar_dados_dividaDebitoInscrito                          
[55] Enviar enviar_dados_condominiosInfComplem                        [110] enviar_dados_dividas                                                 

    Para executar múltiplas opções, separe-as por vírgula.
    ''')
    
def chama_funcao_menu(escolha):

    if  (escolha == '3'):
        functions.carregar_dados_paises() # [3] Carregar países
    elif(escolha == '2'):
        functions.enviar_dados_motivos() #[2] enviar dados motivos   
    elif (escolha == '4'):
        functions.carregar_dados_estados() # [4] Carregar estados
    elif (escolha == '5'):
        functions.carregar_dados_municipios() # [5] Carregar municípios
    elif (escolha == '11'):
        functions.enviar_dados_unidades_medida() # [11] Enviar unidades de medida
    elif (escolha == '12'):
        functions.enviar_dados_Bairros() # [12] Enviar logradourosBairros
    elif (escolha == '13'):
        functions.enviar_dados_advogados() # [13] Enviar tipos de comprovantes
    elif (escolha == '14'):
        functions.enviar_dados_advogadosCbo() # [14] Enviar deduções de receitas
    elif (escolha == '15'):
        functions.enviar_dados_advogadosResponsaveis() # [15] Enviar deduções receitas exercícios
    elif (escolha == '16'):
        functions.enviar_dados_tipos_logradouros() # [16] Enviar tipos de logradouros
    elif (escolha == '17'):
        functions.enviar_dados_loteamentos() # [17] Enviar loteamentos
    elif (escolha == '18'):
        functions.enviar_dados_condominios() # [18] Enviar condomínios
    elif (escolha == '19'):
        functions.enviar_dados_alvaras() # [19] Enviar tipos de dívidas
    elif (escolha == '20'):
        functions.enviar_dados_agencias_bancarias() # [20] Enviar agencias bancarias
    elif (escolha == '21'):
        functions.enviar_dados_anistias() # [21] Enviar dados anistias
    #elif (escolha == '22'):
        #functions.enviar_dados_tipos_administracoes() # [22] Enviar tipos de administrações
    elif (escolha == '23'):
        functions.enviar_dados_arquivos() # [23] Enviar dados arquivos
    elif (escolha == '24'):
        functions.enviar_dados_atividadesEconomicas() # [24] Enviar atividades Economicas
    elif (escolha == '25'):
        functions.enviar_dados_atividadesEconomicasInfComplem() # [25] Enviar atividades Economicas Inf Complem
    elif (escolha == '26'):
        functions.enviar_dados_atividadesEconomicasInfCompOp() # [26] Enviar atividades Economicas Inf CompOp
    elif (escolha == '27'):
        functions.enviar_dados_atividadesEconomicasRelacionadas() # [27] Enviar atividadesEconomicasRelacionadas
    elif (escolha == '28'):
        functions.enviar_dados_atividadesEconomicasValores() # [28] Enviar atividades Economicas Valores
    elif (escolha == '29'):
        functions.enviar_dados_atos() # [29] Enviar atos
    elif (escolha == '30'):
        functions.enviar_dados_atosFontesDivulgacoes() # [30] Enviar atos Fontes Divulgacoes
    elif (escolha == '31'):
        functions.enviar_dados_atualizacaoDividaAtivaSimAm() # [31] Enviar ações
    elif (escolha == '32'):
        functions.enviar_dados_atualizacaoMonetariaSimAm() # [32] Enviar configurações funcionais
    elif (escolha == '33'):
        functions.enviar_dados_baixaAutomaticaPagamentos() # [33] Enviar baixa Automatica Pagamentos
    elif (escolha == '34'):
        functions.enviar_dados_baixaAutomatica() # [34] Enviar baixa Automatica
    elif (escolha == '35'):
        functions.enviar_dados_baixaManual() # [35] Enviar baixa Manual
    elif (escolha == '36'):
        functions.enviar_dados_calculosTributariosAvancado() # [36] Enviar calculos Tributarios Avancado
    elif (escolha == '37'):
        functions.enviar_dados_baixaManualPagamentos() # [37] Enviar baixa Manual Pagamentos
    elif (escolha == '38'):
        functions.enviar_dados_baixasAutomaticas() # [38] Enviar configurações de naturezas de despesas
    elif (escolha == '39'):
        functions.enviar_dados_calculosTributariosAvancadoOpc() # [39] Enviar calculos Tributarios Avancado Opc
    elif (escolha == '40'):
        functions.enviar_dados_beneficiosFiscais() # [40] Enviar beneficiosFiscais
    elif (escolha == '41'):
        functions.enviar_dados_calculosTributarios() # [41] Enviar calculosTributarios
    elif (escolha == '42'):
        functions.enviar_dados_camposAdicionais() # [42] Enviar campos Adicionais
    elif (escolha == '43'):
        functions.enviar_dados_cancelamentoDocumentos() # [43] Enviar cancelamento Documentos
    elif (escolha == '44'):
        functions.enviar_dados_cartorios() # [44] Enviar cartorios
    elif (escolha == '45'):
        functions.enviar_dados_cbos() # [45] Enviar cbos
    elif (escolha == '46'):
        functions.enviar_dados_certidoesITBI() # [46] Enviar certidoesITBI
    elif (escolha == '47'):
        functions.enviar_dados_certidoesNegativas() # [47] Enviar certidoesNegativas
    elif (escolha == '48'):
        functions.enviar_dados_agencias_bancarias() # [48] Enviar agências bancárias
    elif (escolha == '49'):
        functions.enviar_dados_agrupamentos() # [49] Enviar agrupamentos   
    elif (escolha == '51'):
        functions.enviar_dados_cnaes() # [51] Enviar cnaes
    elif (escolha == '52'):
        functions.enviar_dados_compensacoes() # [52] Enviar compensacoes
    elif (escolha == '53'):
        functions.enviar_dados_competencias() # [53] Enviar competencias
    elif (escolha == '54'):
        functions.enviar_dados_condominios() # [54] Enviar condominios
    elif (escolha == '55'):
        functions.enviar_dados_condominiosInfComplem() # [55] Enviar condominios Inf Complem
    elif (escolha == '56'):
        functions.enviar_dados_condominiosInfComplemOp() # [56] Enviar condominios Inf ComplemOp
    elif (escolha == '57'):
        functions.enviar_dados_configContribMelhorias() # [57] Enviar enviar_dados_configContribMelhorias do exercício
    elif (escolha == '58'):
        functions.enviar_dados_configEconomicosTabelasAuxiliaresHistorico() # [58] Enviar enviar_dados_configEconomicosTabelasAuxiliaresHistorico
    elif (escolha == '59'):
        functions.enviar_dados_configGeoprocessamento() # [59] Enviar config Geoprocessamento
    elif (escolha == '60'):
        functions.enviar_dados_configGeracaoGuias() # [60] Enviar config GeracaoGuias
    elif (escolha == '61'):
        functions.enviar_dados_configHomologacaoTributos() # [61] Enviar config Homologacao Tributos
    elif (escolha == '62'):
        functions.enviar_dados_configImobiliarias() # [62] Enviar config Imobiliarias
    elif (escolha == '63'):
        functions.enviar_dados_configInscDividaAtiva() # [63] Enviar config Insc Divida Ativa
    elif (escolha == '64'):
        functions.enviar_dados_configInscrImobiliarias() # [64] Enviar config Inscr Imobiliarias
    elif (escolha == '65'):
        functions.enviar_dados_configParcCreditos() # [65] Enviar configParcCreditos
    elif (escolha == '66'):
        functions.enviar_dados_configNotasAvulsas() # [66] Enviar config Notas Avulsas
    elif (escolha == '67'):
        functions.enviar_dados_configParcCreditosTaxas() # [67] Enviar config Parc Creditos Taxas
    elif (escolha == '68'):
        functions.enviar_dados_configParcelamentos() # [68] Enviar configParcelamentos
    elif (escolha == '69'):
        functions.enviar_dados_configTaxaExpedCredts() # [69] Enviar configTaxaExpedCredts
    elif (escolha == '70'):
        functions.enviar_dados_configTaxaExpediente() # [70] Enviar config Taxa Expediente
    elif (escolha == '71'):
        functions.enviar_dados_configTransfImoMotivos() # [71] Enviar config Transf ImoMotivos
    elif (escolha == '72'):
        functions.enviar_dados_configTransfImoReceitas() # [72] Enviar config Transf Imo Receitas
    elif (escolha == '73'):
        functions.enviar_dados_configTransfImoveis() # [73] Enviar config Transf Imoveis
    elif (escolha == '74'):
        functions.enviar_dados_configuracoes() # [74] Enviar enviar_dados_configuracoes
    elif (escolha == '75'):
        functions.enviar_dados_configuracoesArrecadacoes() # [75] Enviar configuracoesArrecadacoes
    elif (escolha == '76'):
        functions.enviar_dados_contribMelhoriasTaxas() # [76] Enviar contrib Melhorias Taxas
    elif (escolha == '77'):
        functions.enviar_dados_configuracoesGeracaoParcelas() # [77] Enviar configuracoes Geracao Parcelas
    elif (escolha == '78'):
        functions.enviar_dados_configuracoesGeracaoParcelasReceitas() # [78] Enviar origens de configuracoes Geracao Parcelas Receitas
    elif (escolha == '79'):
        functions.enviar_dados_construtoras() # [79] Enviar origens de enviar_dados_construtoras
    elif (escolha == '80'):
        functions.enviar_dados_construtorasEngArquitetos() # [80] Enviar construtoras Eng Arquitetos
    elif (escolha == '81'):
        functions.enviar_dados_contadores() # [81] Enviar enviar_dados_contadores
    elif (escolha == '82'):
        functions.enviar_dados_contadoresCbo() # [82] Enviar contadoresCbo
    elif (escolha == '83'):
        functions.enviar_dados_contadoresResponsaveis() # [83] Enviar envio ao legislativo a alteração orçamentária da despesa.
    elif (escolha == '84'):
        functions.enviar_dados_ContribMelhoriasBairros() # [84] Enviar enviar_dados_ContribMelhoriasBairros
    elif (escolha == '85'):
        functions.enviar_dados_contribMelhoriasImoveis() # [85] Enviar contribMelhoriasImoveis
    elif (escolha == '86'):
        functions.enviar_dados_contribMelhoriasInfComp() # [86] Enviar contrib Melhorias Inf Comp
    elif (escolha == '87'):
        functions.enviar_dados_contribMelhoriasMateriaisServicos() # [87] enviar contrib Melhorias Materiais Servicos
    elif (escolha == '88'):
        functions.enviar_dados_contribMelhoriasMovtos() # [88] Enviar enviar_dados_contribMelhoriasMovtos
    elif (escolha == '89'):
        functions.enviar_dados_contribMelhoriasSaldos() # [89] Enviar contribMelhoriasSaldos
    elif (escolha == '90'):
        functions.enviar_dados_contribuicoesMelhorias() # [90] enviar_dados_contribuicoesMelhorias
    elif (escolha == '91'):
        functions.enviar_dados_contribMelhoriasTaxas() # [91] enviar_dados_contribMelhoriasTaxas
    elif (escolha == '92'):
        functions.enviar_dados_contribMelImovInfComp() # [92] enviar_dados_contribMelImovInfComp
    elif (escolha == '93'):
        functions.enviar_dados_contribMovtosDetalhes() # [93] enviar_dados_contribMovtosDetalhes
    elif (escolha == '94'):
        functions.enviar_dados_contrMelhoriasInfCompOp() # [94] Enviar saldos iniciais
    elif (escolha == '95'):
        functions.enviar_dados_conveniosCreditos() # [95] enviar_dados_conveniosCreditos
    elif (escolha == '96'):
        functions.enviar_dados_conveniosMensagens() # [96] enviar_dados_conveniosMensagens
    elif (escolha == '97'):
        functions.enviar_dados_convenios() # [97] Enviar enviar_dados_convenios
    elif (escolha == '98'):
        functions.enviar_dados_conveniosSimulacoes() # [98] enviar_dados_conveniosSimulacoes
    elif (escolha == '99'):
        functions.enviar_dados_creditosTributarios() # [99] enviar_dados_creditosTributarios
    elif (escolha == '100'):
        functions.enviar_dados_creditosTributariosRec() # [100] enviar_dados_creditosTributariosRec
    elif (escolha == '101'):
        functions.enviar_dados_declaracoes() # [101] enviar_dados_declaracoes
    elif (escolha == '102'):
        functions.enviar_dados_declaracoesServicos() # [102] enviar_dados_declaracoesServicos
    elif (escolha == '103'):
        functions.enviar_dados_deducaoCreditoSimAm() # [103] enviar_dados_deducaoCreditoSimAm
    elif (escolha == '104'):
        functions.enviar_dados_deducaoDividaSimAm() # [104] enviar_dados_deducaoDividaSimAm
    elif (escolha == '105'):
        functions.enviar_dados_desmembramentos() # [105] enviar desmembramentos
    elif (escolha == '106'):
        functions.enviar_dados_desmembramentosDocumentos() # [106] enviar_dados_desmembramentosDocumentos
    elif (escolha == '107'):
        functions.enviar_dados_desmembramentosImoveis() # [107] enviar_dados_desmembramentosImoveis
    elif (escolha == '108'):
        functions.enviar_dados_distritos() # [108] enviar_dados_distritos
    elif (escolha == '109'):
        functions.enviar_dados_dividaDebitoInscrito() # [109] enviar_dados_dividaDebitoInscrito
    elif (escolha == '110'):
        functions.enviar_dados_dividas() # [110] enviar_dados_dividas
    elif (escolha == '111'):
        functions.enviar_dados_dividasMovtos() # [111] enviar_dados_dividasMovtos
    elif (escolha == '112'):
        functions.enviar_dados_dividasReceitas() # [112] enviar_dados_dividasReceitas
    elif (escolha == '113'):
        functions.enviar_dados_dividasResponsaveis() # [113] enviar_dados_dividasResponsaveis        
    elif (escolha == '114'):     
        functions.enviar_dados_unidadesMedidas() # [157] enviar dados unidades Medidas  
    elif (escolha == '157'):     
        functions.enviar_dados_agrupamentosCamposAdicionais() # [157] Consultar  agrupamentos Campos Adicionais  
    elif (escolha == '84'):
        functions.enviar_dados_Bairros() # [158] Enviar Bairros    
    elif (escolha.upper() == 'T'):
        functions.carregar_dados_paises() # [3] Carregar países
        functions.carregar_dados_estados() # [4] Carregar estados
        functions.carregar_dados_municipios() # [5] Carregar municípios
        functions.enviar_dados_unidades_medida() # [11] Enviar unidades de medida
        functions.enviar_dados_Bairros() # [12] Enviar logradourosBairros
        functions.enviar_dados_advogados() # [13] Enviar tipos de comprovantes
        functions.enviar_dados_advogadosCbo() # [14] Enviar deduções de receitas
        functions.enviar_dados_advogadosResponsaveis() # [15] Enviar deduções receitas exercícios
        functions.enviar_dados_tipos_logradouros() # [16] Enviar tipos de logradouros
        functions.enviar_dados_loteamentos() # [17] Enviar loteamentos
        functions.enviar_dados_condominios() # [18] Enviar condomínios
        functions.enviar_dados_alvaras() # [19] Enviar dados alvaras        
        functions.enviar_dados_anistias() # [21] Enviar tipos de responsáveis
        functions.enviar_dados_arquivos() # [23] Enviar enviar_dados_arquivos
        functions.enviar_dados_atividadesEconomicas() # [24] Enviar atividades Economicas
        functions.enviar_dados_atividadesEconomicasInfComplem() # [25] Enviar atividades Economicas Inf Complem
        functions.enviar_dados_atividadesEconomicasInfCompOp() # [26] Enviar transações financeiras exercício
        functions.enviar_dados_atividadesEconomicasRelacionadas() # [27] Enviar tipos de enviar_dados_contribMelhoriasImoveis
        functions.enviar_dados_atividadesEconomicasValores() # [28] Enviar tipos de enviar_dados_contribMelhoriasImoveis exercício
        functions.enviar_dados_atos() # [29] Enviar atos
        functions.enviar_dados_atosFontesDivulgacoes() # [30] Enviar atos Fontes Divulgacoes
        functions.enviar_dados_atualizacaoDividaAtivaSimAm() # [31] Enviar atualizacao Divida Ativa SimAm
        functions.enviar_dados_atualizacaoMonetariaSimAm() # [32] Enviar configurações funcionais
        functions.enviar_dados_baixaAutomaticaPagamentos() # [33] Enviar funções
        functions.enviar_dados_baixaAutomatica() # [34] Enviar subfunções
        functions.enviar_dados_baixaManual() # [35] Enviar localizadores
        functions.enviar_dados_calculosTributariosAvancado() # [36] Enviar configurações naturezas despesas
        functions.enviar_dados_baixaManualPagamentos() # [37] Enviar naturezas de despesas
        functions.enviar_dados_baixasAutomaticas() # [38] Enviar configurações de naturezas de despesas
        functions.enviar_dados_calculosTributariosAvancadoOpc() # [39] Enviar naturezas de receitas
        functions.enviar_dados_beneficiosFiscais() # [40] Enviar responsaveis
        functions.enviar_dados_calculosTributarios() # [41] Enviar programas
        functions.enviar_dados_camposAdicionais() # [42] Enviar ordenadores de despesas
        functions.enviar_dados_cancelamentoDocumentos() # [43] Enviar receitas não previstas
        functions.enviar_dados_cartorios() # [44] Enviar enviar_dados_cartorios
        functions.enviar_dados_cbos() # [45] Enviar enviar_dados_cbos
        functions.enviar_dados_certidoesITBI() # [46] Enviar enviar_dados_certidoesITBI
        functions.enviar_dados_certidoesNegativas() # [47] Enviar enviar_dados_certidoesNegativas
        functions.enviar_dados_agencias_bancarias() # [48] Enviar agências bancárias
        functions.enviar_dados_agrupamentos() # [59] agrupamentos
        functions.enviar_dados_cnaes() # [51] Enviar contas bancarias da entidade
        functions.enviar_dados_compensacoes() # [52] Enviar enviar_dados_compensacoes
        functions.enviar_dados_competencias() # [53] Enviar enviar_dados_competencias
        functions.enviar_dados_condominios() # [54] Enviar enviar_dados_condominios
        functions.enviar_dados_condominiosInfComplem() # [55] Enviar enviar_dados_condominiosInfComplem
        functions.enviar_dados_configContribMelhorias() # [56] Enviar enviar_dados_condominiosInfComplemOp
        functions.enviar_dados_configContribMelhorias() # [57] Enviar enviar_dados_condominiosInfComplemOp do exercício
        functions.enviar_dados_configEconomicosTabelasAuxiliaresHistorico() # [58] Enviar enviar_dados_configEconomicosTabelasAuxiliaresHistorico
        functions.enviar_dados_configGeoprocessamento() # [59] Enviar enviar_dados_configGeoprocessamento
        functions.enviar_dados_configGeracaoGuias() # [60] Enviar enviar_dados_configGeracaoGuias
        functions.enviar_dados_configHomologacaoTributos() # [61] Enviar enviar_dados_configHomologacaoTributos
        functions.enviar_dados_configImobiliarias() # [62] Enviar enviar_dados_configImobiliarias
        functions.enviar_dados_configInscDividaAtiva() # [63] Enviar enviar_dados_configInscDividaAtiva
        functions.enviar_dados_configInscrImobiliarias() # [64] Enviar enviar_dados_configInscrImobiliarias
        functions.enviar_dados_configParcCreditos() # [65] Enviar enviar_dados_configParcCreditos
        functions.enviar_dados_configNotasAvulsas() # [66] Enviar enviar_dados_configNotasAvulsas
        functions.enviar_dados_configParcCreditosTaxas() # [67] Enviar enviar_dados_configParcCreditosTaxas
        functions.enviar_dados_configParcelamentos() # [68] Enviar enviar_dados_configParcelamentos
        functions.enviar_dados_configTaxaExpedCredts() # [69] Enviar agrupamentos Campos Adicionais
        functions.enviar_dados_configTaxaExpediente() # [70] Enviar enviar_dados_configTaxaExpediente
        functions.enviar_dados_configTransfImoMotivos() # [71] Enviar enviar_dados_configTransfImoMotivos
        functions.enviar_dados_configTransfImoReceitas() # [72] Enviar enviar_dados_configTransfImoReceitas
        functions.enviar_dados_configTransfImoveis() # [73] Enviar naturezas de diárias
        functions.enviar_dados_configuracoes() # [74] Enviar enviar_dados_configuracoes
        functions.enviar_dados_configuracoesArrecadacoes() # [75] Enviar enviar_dados_configuracoesArrecadacoes
        functions.enviar_dados_contribMelhoriasTaxas() # [76] Enviar contrib Melhorias Taxas
        #functions.enviar_dados_pagamentos() # [151] Enviar pagamentos
        functions.enviar_dados_agrupamentosCamposAdicionais() # [157] Consultar status dos consultar agrupamentos
        functions.enviar_dados_configuracoesGeracaoParcelasReceitas() # [78] Enviar origens de enviar_dados_configuracoesGeracaoParcelas
        functions.enviar_dados_construtoras() # [79] Enviar origens de enviar_dados_construtoras
        functions.enviar_dados_construtorasEngArquitetos() # [80] Enviar enviar_dados_construtorasEngArquitetos
        functions.enviar_dados_contadores() # [81] Enviar enviar_dados_contadores
        functions.enviar_dados_contadoresCbo() # [82] Enviar enviar_dados_contadoresCbo
        functions.enviar_dados_contadoresResponsaveis() # [83] Enviar envio ao legislativo a alteração orçamentária da despesa.
        functions.enviar_dados_ContribMelhoriasBairros() # [84] Enviar enviar_dados_ContribMelhoriasBairros
        functions.enviar_dados_contribMelhoriasImoveis() # [85] Enviar enviar_dados_contribMelhoriasImoveis
        functions.enviar_dados_contribMelhoriasInfComp() # [86] Enviar enviar_dados_contribMelhoriasInfComp
        functions.enviar_dados_contribMelhoriasMateriaisServicos() # [87] enviar_dados_contribMelhoriasMateriaisServicos
        functions.enviar_dados_contribMelhoriasMovtos() # [88] Enviar enviar_dados_contribMelhoriasMovtos
        functions.enviar_dados_contribMelhoriasSaldos() # [89] Enviar enviar_dados_contribMelhoriasSaldos
        functions.enviar_dados_contribuicoesMelhorias() # [90] enviar_dados_contribuicoesMelhorias
        functions.enviar_dados_contribMelhoriasTaxas() # [91] enviar_dados_contribMelhoriasTaxas
        functions.enviar_dados_contribMelImovInfComp() # [92] enviar_dados_contribMelImovInfComp
        functions.enviar_dados_contribMovtosDetalhes() # [93] enviar_dados_contribMovtosDetalhes
        functions.enviar_dados_contrMelhoriasInfCompOp() # [94] Enviar saldos iniciais
        functions.enviar_dados_conveniosCreditos() # [95] enviar_dados_conveniosCreditos
        functions.enviar_dados_conveniosMensagens() # [96] enviar_dados_conveniosMensagens
        functions.enviar_dados_convenios() # [97] Enviar enviar_dados_convenios
        functions.enviar_dados_conveniosSimulacoes() # [98] enviar_dados_conveniosSimulacoes
        functions.enviar_dados_creditosTributarios() # [99] enviar_dados_creditosTributarios
        functions.enviar_dados_creditosTributariosRec() # [100] enviar_dados_creditosTributariosRec
        functions.enviar_dados_declaracoes() # [101] enviar_dados_declaracoes
        functions.enviar_dados_declaracoesServicos() # [102] enviar_dados_declaracoesServicos
        functions.enviar_dados_deducaoCreditoSimAm() # [103] enviar_dados_deducaoCreditoSimAm
        functions.enviar_dados_deducaoDividaSimAm() # [104] enviar_dados_deducaoDividaSimAm
        functions.enviar_dados_desmembramentos() # [105] enviar_dados_desmembramentos
        functions.enviar_dados_desmembramentosDocumentos() # [106] enviar_dados_desmembramentosDocumentos
        functions.enviar_dados_desmembramentosImoveis() # [107] enviar_dados_desmembramentosImoveis
        functions.enviar_dados_distritos() # [108] enviar_dados_distritos
        functions.enviar_dados_dividaDebitoInscrito() # [109] enviar_dados_dividaDebitoInscrito
        functions.enviar_dados_dividas() # [110] enviar_dados_dividas
        functions.enviar_dados_dividasMovtos() # [111] enviar_dados_dividasMovtos
        functions.enviar_dados_dividasReceitas() # [112] enviar_dados_dividasReceitas
        functions.enviar_dados_dividasResponsaveis() # [113] enviar_dados_dividasResponsaveis
        functions.enviar_dados_unidadesMedidas() # [157] enviar dados unidades Medidas 
        functions.enviar_dados_motivos()#[2] enviar dados motivos
        functions.enviar_dados_Bairros() # [158] Enviar Bairros    
    else:
        print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    
    montar_menu()
    escolha = 0

    while (escolha != "S"):

        escolha = input("Digite a opção para executar (M para exibir novamente o menu): ")
        listaOpcoes = escolha.split(",")

        for opcao in listaOpcoes:

            if (opcao == "S" or opcao == "s"):
                print("Saindo...")
                quit()

            elif (opcao == "M" or opcao == "m"):
                os.system('cls')
                montar_menu()
            else:
                chama_funcao_menu(opcao)