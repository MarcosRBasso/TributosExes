DROP TABLE IF EXISTS agrupamentos;
CREATE TABLE agrupamentos
(
	id SERIAL NOT NULL,
	cadastro character varying,
	descricao character varying,
	desativado character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS agrupamentosCamposAdicionais;
CREATE TABLE agrupamentosCamposAdicionais
(
    id SERIAL NOT NULL,
    id_origem integer,
    id_cloud integer,
	idAgrupamentos integer,
	idCamposAdicionais integer,
    ordemApresentacao integer,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS agenciasBancarias;
CREATE TABLE agenciasBancarias
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idBairros integer,
	idBancos integer,
	idLogradouros integer,
	idMunicipios integer,
	nome character varying,
	nroAgencia integer,
	numero integer, 
	cep character varying,
    digAgencia character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS alvaras;
CREATE TABLE alvaras
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idContribuinte integer,
	idEconomico integer,
	idEconomicosCnaes integer,
	idEconomicosListaServicos integer,
	idEnderecoContribuinte integer, 
	idModelo integer,
	informacoesComplementares character varying,
	nroDocumento integer,
	ano character varying,
	situacaoAlvara character varying,
	tipoAlvara character varying,
	dtValidade character varying,    
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS anistias;
CREATE TABLE anistias
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idDividas integer,
	idDividasMovtos integer,
	idDividasReceitas integer,
	idHomologManutencao integer,
	dtValidade character varying,
	idScriptManutencao integer,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS atividadesEconomicas;
CREATE TABLE atividadesEconomicas
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	risco character varying,
	riscoMei character varying,
	classificacao character varying,
	idCnaes integer,
	idListaServicos integer,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS atividadesEconomicasInfComplem;
CREATE TABLE atividadesEconomicasInfComplem
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idCamposAdicionais integer,
	idAtividadesEconomicas integer,
	iInformacoesComplementares character varying,
	dhCampo character varying,
	dtBase character varying,
	texto character varying,
	vlCampo integer,
	areaTexto character varying,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS atividadesEconomicasInfCompOp;
CREATE TABLE atividadesEconomicasInfCompOp
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idAtividadesEcoInfComplem integer,
	idCamposAdicionaisFilho integer,	
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS atividadesEconomicasRelacionadas;
CREATE TABLE atividadesEconomicasRelacionadas
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idAtividadesEconomicasCnae integer,
	idAtividadesEconomicasServico integer,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS atividadesEconomicasValores;
CREATE TABLE atividadesEconomicasValores
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idAtividadesEconomicas integer,
	idIndexador integer,
	classificacaoValores character varying,
	dataBase character valor_encargos,	
	valor integer,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS atos;
CREATE TABLE atos
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idNaturezasTextoJurAtos integer,
	idTiposAtos integer,
	id_municipio integer,
	cpfResponsavel character varying,
	dtCriacao character varying,
	dtPublicacao character varying,
	dtResolucao character varying,
	dtVigorar character varying,
	ementa character varying,
	nmResponsavel character varying,
	nroDiarioOficial integer,
	nroOficial integer,
	nroProcesso integer,
	nroResolucao integer,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS atosFontesDivulgacoes;
CREATE TABLE atosFontesDivulgacoes
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idAtos integer,
	idFontesDivulgacoesAtos integer,
	numeroPublicacao integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS naturezasTextoJurAtos;
CREATE TABLE naturezasTextoJurAtos
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,		
	descricao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS baixaAutomatica;
CREATE TABLE baixaAutomatica
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idAgenciaBancaria integer,
	arquivo character varying,
	baixaRetroativa character varying,
	idBanco integer,
	idConvenio integer,
	dataArquivo character varying,
	dataHoraEstorno character varying,
	dataPagamento character varying,
	dataRetroativa character varying,
	dhInicio character varying,
	dhTermino character varying,
	erros character varying,
	string character varying,
	string2 character varying,
	string3 character varying,
	identificacaoSimples character varying,
	inconsistencias character varying,
	idMotivoEstorno integer,
	nomeArquivoReduzido character varying,
	nroArquivo integer,
	scriptId integer,
	situacao character varying,
	tempoExecucao character varying,
	usuarioEstorno character varying, 	 
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS baixaAutomaticaPagamentos;
CREATE TABLE baixaAutomaticaPagamentos
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idBaixaAutomatica integer,
	idCredito integer,
	dataVencto character integer,
	dataCredito character varying,
	dataPagamento character varying,
	idGuiaUnificada integer,
	idLancamento integer,
	inconsistencia character varying,
	inscrita character varying,
	nroBaixa integer,
	nroLinha integer,
	parcela integer,
	idReferente integer,
	tipoLancamento character varying,
	tipoPagamento character varying,
	valorDiferenca integer,
	valorPago integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS baixasAutomaticas;
CREATE TABLE baixasAutomaticas
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	baixaAutomatica character varying,
	baixaRetroativa character varying,
	idConvenio integer,
	dataArquivo character varying,
	dataHoraEstorno character varying,
	dataPagamento character varying,
	dataPagamentoRetroativo character varying,
	dhInicioEstorno character varying,
	dhInicioHomologacao character varying,
	dhTerminoEstorno character varying,
	dhTerminoHomologacao character varying,
	erro character varying,
	idMotivoEstorno integer,
	nomeArquivo character varying,
	nroArquivo integer,
	scriptId integer,
	situacao character varying,
	tempoExecucao character varying,
	usuarioEstorno character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS baixaManual;
CREATE TABLE baixaManual
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	ano character varying,
	codigoBarras integer,
	representacaoNumerica integer,
	idsContribuintes integer,
	idsCreditosTributarios integer, 
	idsConfiguracaoGeracaoParcelas integer,
	dtBaixa character varying,
	nroParcela integer,
	guiaUnificada character varying,
	tipo character varying,
	tipoLancamento character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS baixaManualPagamentos;
CREATE TABLE baixaManualPagamentos
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idConvenio integer,
	idMotivo integer,
	idContribuinte integer,
	idBaixaManual character varying,
	dhTerminoHomologacao character varying,
	formaPagamento character varying,
    dtCredito character varying,
    dtPagamento character varying,
	situacao character varying,
	idMotivoEstorno integer,
	usuarioEstorno character varying,
	dhEstorno character varying,
	dhInicioEstorno character varying,
	dhFimEstorno character varying,
	erro character varying,
	lancamentos character varying,
	idCreditoTributario integer,
	idConfiguracaoGeracaoParcelas integer,
	idMotivoDiferenca integer,
	correcao integer,
	juros integer,
	multa integer,
	idLancamento integer,
	tipoLancamento character varying,
	nroParcela integer,
	ano character varying,
	dataVencimento character varying,
	idGuia integer,
	nroBaixa integer,
	valorOriginal integer,
	valorDevido integer,
	valorPago integer,
	parcelaComplementar character varying,
	codigoBarras character varying,
	representacaoNumerica character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS bancos;
CREATE TABLE bancos
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    cep character varying,
    nome character varying,
	cnpj integer,
	numero integer,
	sigla character varying,
	site character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS beneficiosFiscais;
CREATE TABLE beneficiosFiscais
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idAto integer,
	tipoBeneficio character varying,
	fundamentacaoLegal character varying,
	dtValidadeInicial character varying,
	dtValidadeFinal character varying,
	descricao character varying,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS calculosTributarios;
CREATE TABLE calculosTributarios
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	acaoVctoFeriado character varying,
	ano character varying,
	atividades character varying,
	bairros character varying,
	calculoRetroativo character varying,
	complementar character varying,
	condominios character varying,
	consideraEconomicosSuspensos character varying,
	contadores character varying,
	contribuicoesMelhorias character varying,
	contribuicoesMelhoriasImoveis character varying,
	contribuintes character varying,
	idCreditosTributarios integer,
	dataVcto character varying,
	dhInicio character varying,
	dhTermino character varying,
	economicos character varying,
	formaPagamento character varying,
	homologadoPor character varying,
	idCalculoAnterior integer,
	imoveis character varying,
	campo1Final character varying,
	campo2Final character varying,
	campo3Final character varying,
	campo4Final character varying,
	campo5Final character varying,
	campo6Final character varying,
	campo7Final character varying,
	campo8Final character varying,
	campo9Final character varying,
	campo10Final character varying,
	campo1 character varying,
	campo2 character varying,
	campo3 character varying,
	campo4 character varying,
	campo5 character varying,
	campo6 character varying,
	campo7 character varying,
	campo8 character varying,
	campo9 character varying,
	campo10 character varying,
	intervalo character varying,
	itensListaServico character varying,
	logradouros character varying,
	loteamentos character varying,
	notaAvulsa character varying,
	parcelaInicial integer, 
	parcelasCompetencias character varying,
	qtInconsistentes integer,
	qtLanctosGerados integer,
	qtdAnalisada integer,
	qtdDiasMeses integer,
	qtdParcelas integer,
	receitasDiversas character varying,
	receitasDiversasLanctos character varying,
	serieNotaAvulsa integer,
	simulado character varying,
	tipoCalculo character varying,
	tipoImovel character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS errosCalculo;
CREATE TABLE errosCalculo
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idCalculosTributarios integer,
	idEconomicos integer,
	idImoveis integer,
	idMelhorias integer,
	mensagem character varying,
	idReceitasDiversasLanctos integer,
	idNotasAvulsas integer,
	statusErro character varying,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS calculosTributariosAvancado;
CREATE TABLE calculosTributariosAvancado
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idCalculo integer,
	idCampoAdicional integer,
	texto character varying,
	vlCampo integer,
	dhCampo character varying,
	operadorComparacao character varying,
	operadorAcao character varying
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS parcelasCalculo;
CREATE TABLE parcelasCalculo
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idCalculosTributarios integer,
	dataVcto character varying,
	parcela integer,
	percDesconto integer, 
	unica character varying,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS parcelasGeradas;
CREATE TABLE parcelasGeradas
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idCompetencias integer,
	idConfiguracoesGeracaoParcelas integer,
	ordemImpressao integer,
	parcela integer,
	descricao character varying,
	dataVctoOriginal character varying,
    dataVcto character varying,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS parcelasGeradasReceitas;
CREATE TABLE parcelasGeradasReceitas
(
	id SERIAL NOT NULL,
	idCredTribRec integer,
	idConfigParcConf integer,
    percDesconto character varying,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS calculosTributariosAvancadoOpc;
CREATE TABLE calculosTributariosAvancadoOpc
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idOpcao integer,
    idCalculosTributariosAvancado integer,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS camposAdicionais;
CREATE TABLE camposAdicionais
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	id_ppa integer,
    ajudaCampo character varying,
    anoFinal integer,
    anoInicial integer,
	cadastro character varying,
	codCaracteristica integer,
	compartilhadoComCondominios character varying,
	compartilhadoComContribMelhorias character varying,
	desabilitado character varying,
	exibirNaHomologacao character varying,
	faturaPodeAlterar character varying,
	formato character varying,
	formatoHora character varying,
	itemPai integer,
	livroEletronicoPodeAlterar character varying,
	maxCasasDecimais integer,
	maxDigitos integer,
	ordem integer,
	padrao character varying,
	producaoPrimariaPodeAlterar character varying,
	tipo character varying,
	tipoEnquadramento character varying,
	tipoUnidade character varying,
	titulo character varying,
	idUnidadeMedida integer,
	valorPadrao character varying,
	exibirConsulta character varying,
	exibirEnvio character varying,
	exibirParecer character varying,	 
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS certidoesITBI;
CREATE TABLE certidoesITBI
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	descricao character varying,
	idBairroEndereco integer,
    idCondominioEndereco integer, 
	idComprador integer,
    idVendedor integer,
    idCorresponsavel integer,
    idCreditosTributarios integer,
    idDistritoEndereco integer,
    idDividas integer,
    idModelo integer,
    idImoveis integer,
    idImoveisInfComplem integer,
    idLogradouroEndereco integer,
    idLoteamentoEndereco integer,
    idMunicipios integer,
	idReceitas integer,
    idTransfImoveisItens integer,
    idTransfImoveisItensCompra integer,
    idTransfImoveisItensProcessos integer,
    idTransfImoveisItensVenda integer,
	idTransferenciaImoveis integer,
    dtVencimento character varying,
    apartamentoEndereco character varying,
    blocoEndereco character varying,
    cepEndereco integer,
    lote character varying,
    numeroEndereco integer,
    numeroTelefone integer,
    quadra character varying,
    nroDocumento integer,
    valorCorrecao integer,
    valorJuro integer,
    valorLancado integer,
    valorMulta integer,
    valorTotal integer,
    vlDeclarado integer,
    principalEndereco character varying,
    situacaoDivida character varying,
    situacaoLancamento character varying,
    situacaoParcela character varying,
    tipoCertidaoITBI character varying,
    situacaoCertidaoITBI character varying,
    formaPagamento character varying,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS certidoesNegativas;
CREATE TABLE certidoesNegativas
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idContribuinte integer,
    idEconomico integer,
    idEconomicoCnae integer,
    idEconomicoListaServico integer,
    idEnderecoContribuinte integer,
    idModelo integer,
    idImovel integer,
    dataValidade character varying,
    chaveEmissao integer,
    comprovacao character varying,
    finalidade character varying,
    nomeRequerente character varying,
    ressalva character varying,
    informacoesComplementares character varying,
    nroDocumento integer,
    ano integer,
    qtdDeclaracoesAbertoVencidas integer,
    qtdDeclaracoesNaoIniciadasVencidas integer,
    qtdLanctoInscritosSuspensos integer,
    qtdLanctoNaoInscritosAtivos integer,
    qtdLanctoNaoInscritosSuspensos integer,
    qtdLanctoNaoInscritosVencer integer,
    qtdLanctoNaoInscritosVencidos integer,
    qtdLanctoParceladosVencer integer,
    qtdLanctoParceladosVencidos integer,
    situacaoCertidaoNegativa character varying,
    situacaoContribuinte character varying,
    situacaoEconomico character varying, 
    situacaoImovel character varying,
    tipoCertidaoNegativa character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS compensacoes;
CREATE TABLE compensacoes
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idSaldo integer,
    idReceita integer,
    idGuia integer,
	idDivida integer,
	idParcelamentosParcela integer,
	idPagamentosDetalhados integer,
	vlSaldo integer,
	vlTributo integer,
	vlJuro integer,
	vlCorrecao integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS competencias;
CREATE TABLE competencias
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    descricao character varying,
	dataUltimoUso character varying,
	dtFinal character varying,
	dtInicial character varying,
	dtVcto character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS configContribMelhorias;
CREATE TABLE configContribMelhorias
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idCreditoCalculoMelhoria integer,
	idCreditosTributariosRec integer,
	formatoCalculoMelhoria character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS configGeoprocessamento;
CREATE TABLE configGeoprocessamento
(
	id SERIAL NOT NULL,
	deferimentoAutomatico character varying,
	inserirDependencias character varying,
	tipoInteracao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS configGeracaoGuias;
CREATE TABLE configGeracaoGuias
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idCreditosTributarios integer,
	idReceitas integer,
	idTaxas integer,
	idConvenios integer,
	sistemas character varying,
	tipoCadastro character varying,
	tiposGuias character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS configHomologacaoTributos;
CREATE TABLE configHomologacaoTributos
(
	id SERIAL NOT NULL,	
	configConveniosCalculos character varying,
	criacaoDocumentos character varying,
	dadosConvertidos character varying,
	homologado character varying,
	modelosGuias character varying,
	permissaoAcesso character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS configImobiliarias;
CREATE TABLE configImobiliarias
(
	id SERIAL NOT NULL,
	descricaoUnidade character varying,
	id_cloud integer,
    controleSecoes character varying,
	inscricaoDuplicada character varying,
	inscricaoIncraDuplicada  character varying,
	usarCampoUnidade character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS configInscrImobiliarias;
CREATE TABLE configInscrImobiliarias
(
	id SERIAL NOT NULL,
	campo integer,
	idConfigImobiliarias integer,
    completarCom character varying,
	qtdCaracter integer,
	descricao character varying,
	conteudo character varying,
	conteudoCompletar character varying,
	posicaoCompletar character varying,
	posicaoRetirar character varying,
	situacao character varying,
	unidade character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS configInscDividaAtiva;
CREATE TABLE configInscDividaAtiva
(
	id SERIAL NOT NULL,
	numLivro integer,
	id_origem integer,
	id_cloud integer,
    qtdeFolhasLivro integer,
	qtdePosicoesFolha integer,
	anoLivro integer,
	numInscricao integer,
	formatoLivro character varying,
	criterioFormaPagto character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS configNotasAvulsas;
CREATE TABLE configNotasAvulsas
(
	id SERIAL NOT NULL,
	nroDiasAposEmissao integer,
	nroPrimeiraNota integer,
	percCofins integer,
	percCsll integer,
	percPisPasep integer,
	serie integer,
	impressaoAposPagamento character varying,
	permiteAlterarValores character varying,
	tipoDias character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS configParcelamentos;
CREATE TABLE configParcelamentos
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idAto integer,
    idScriptDesconto integer,
    idScriptJurosFinanciamento integer,
    descricao character varying,
    dtValidadeFinal character varying,
    dtValidadeInicial character varying,
    dtVencimentoFinal character varying,
    dtVencimentoInicial character varying,
    qtdDiasPrimeiroVcto integer,
    qtdDiasVencidos integer,
    qtdMaxParcelas integer,
    qtdParcelasAlternadas integer,
    qtdParcelasConsecutivas integer,
    vlMinimoFisica integer,
    vlMinimoJuridica integer,
    percEntrada integer,
    percRenda integer,
    aplicacaoAcrescimos character varying,
    cancelamentoLote character varying,
    formulaAntecipacao character varying,
    intervaloVctoParcelas character varying,
    cancelarPorDias character varying,
    cobrarJuros character varying,
    definirVlMaxRenda character varying,
    editarDataParcela character varying,
    exigirEntrada character varying,
    removerTaxasManual character varying,
    reparcelarParcelamento character varying,
    revogarParcelaDesconto character varying,
    inserirTaxasManual character varying,
    manterAnistiaDivida character varying,
    parcelamentoGerado character varying,
    permitirIncentivosFiscais character varying,
    permitirManutencaoLancamento character varying,
    permitirParcelaSemCpf character varying,
    tipoLancamento character varying,
    tiposDividas character varying,
    aplicarValorMinimo character varying,
    vencimentoLancamento character varying,
	PRIMARY KEY (id)
);
    
	
DROP TABLE IF EXISTS configParcCreditos;
CREATE TABLE configParcCreditos
(
	id SERIAL NOT NULL,
	idConfigParcelamentos integer,
	idCredito integer,
	parceladoConjunto character varying,	
	PRIMARY KEY (id)
);
    
DROP TABLE IF EXISTS configParcCreditosTaxas;
CREATE TABLE configParcCreditosTaxas 
(
	id SERIAL NOT NULL,
	idConfigParcelamentos integer,
	idTaxa integer,
	PRIMARY KEY (id)
);
    
DROP TABLE IF EXISTS configJuntaComercial;
CREATE TABLE configJuntaComercial
(
	id SERIAL NOT NULL,
	id_responsavel integer,
	funcionalidadesJuntaComercial character varying,
	tipoInteracaoEnviar character varying,
	tipoInteracaoReceber character varying,
	PRIMARY KEY (id)
);
    
DROP TABLE IF EXISTS configJuntaComerTabela;
CREATE TABLE configJuntaComerTabela
(
	id SERIAL NOT NULL,
	idConfigJuntaComercial integer,
	idTabelaAuxiliar character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS configTaxaExpediente;
CREATE TABLE configTaxaExpediente
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idReceitas integer,
	idReceitasDebito integer,
	idReceitasDivida integer,
	idReceitasParcelamento integer,
	idReceitasUnico integer,
	vlUnico integer,
	vlDebito integer,
	vlDivida integer,
	vlParcelamento integer,
	vlTaxa integer,
	definirTaxaPorCredito character varying,
	acumularTaxas character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS configTaxaExpedCredts;
CREATE TABLE configTaxaExpedCredts
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idConfigTaxaExpediente integer,
    idCreditosTributarios integer,
	idCreditosTributariosRec integer,
	vlTaxa integer,
	PRIMARY KEY (id)
);
    
DROP TABLE IF EXISTS configTransfImoveis;
CREATE TABLE configTransfImoveis
(
	id SERIAL NOT NULL,
	idCreditosTributariosRecRural integer,
    idCreditosTributariosRecUrbano integer,
    idCreditosTributariosRural integer,
    idCreditosTributariosUrbano integer,
    numeroDias integer,
    percAliqAvistaRur integer,
    percAliqAvistaUrb integer,
    percAliqBenfeitoriaRur integer,
    percAliqBenfeitoriaUrb integer,
    percAliqFinanciadaRur integer,
    percAliqFinanciadaUrb integer,
    percAliqOutrosRur integer,
    percAliqOutrosUrb integer,
    formaTransf character varying,
    transfIsentoAutomatico character varying,
    incluirImoRurAutomatico character varying,
    benfeitoriaValorDeclarado character varying,
    alterarDescricaoOutros character varying,
    alterarValorDeclarado character varying,
    dataCadastro character varying,
    dataTransferencia character varying,
    situacao character varying,
    formaCobranca character varying,
    imovel character varying,
    endereco character varying,
    inscImobiliaIncra character varying,
    areaTotalTerreno character varying,
    areaTotalConstruida character varying,
    valorVenalTerritorial character varying,
    valorVenalConstruido character varying,
    valorVenal character varying,
    valorVenalBenfeitorias character varying,
    motivo character varying,
    tipoVenda character varying,
    cartorio character varying,
    unidadeFutura character varying,
    financiado character varying,
    outros character varying,
    benfeitorias character varying,
    nomeVendedor character varying,
    terrenoVendido character varying,
    construidoVendido character varying,
    percVenda character varying,
    nomeComprador character varying,
    terrenoComprado character varying,
    numImoveisIncluido character varying,
    construidoComprado character varying ,
    percCompra character varying,
    numImoveisIncluido character varying,
    reiniciarSequencial character varying,
    valorTotalItbi character varying,
    tipoDias character varying,
    descricaoOutros character varying,
	PRIMARY KEY (id)
);
	
DROP TABLE IF EXISTS configTransfImoMotivos;
CREATE TABLE configTransfImoMotivos
(
	id SERIAL NOT NULL,
	idConfigTransfImoveis integer,
	percAliqAvista integer,
	percAliqBenfeitoria integer,
	percAliqFinanciada integer,
	percAliqOutros integer,
	nomenclaturaCompra character varying,
	nomenclaturaVenda character varying,
	idMotivos integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS configTransfImoReceitas;
CREATE TABLE configTransfImoReceitas
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idConfigTransfImoveis integer,
	idCreditosTributariosRec integer,
    vlTaxa integer,
	tipoImovel character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS configEconomicosTabelasAuxiliaresHistorico;
CREATE TABLE configEconomicosTabelasAuxiliaresHistorico
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	usuario character varying,
    character varying,
    tabelaDesativada character varying,
    idTabelasAuxiliares character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS configuracoes;
CREATE TABLE configuracoes
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	ano integer,
	nroDocumento integer,
	natureza character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS configuracoesArrecadacoes;
CREATE TABLE configuracoesArrecadacoes
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idCreditosTributarios integer,
    ordem integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS configuracoesGeracaoParcelas;
CREATE TABLE configuracoesGeracaoParcelas
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idConfigParcelasConfig integer,
	idConfiguracoesParcelas integer,
	idLeiAtoDesconto integer,
	idLeiAtoFormaPagto integer,
	qtdDiasMeses integer,
	qtdParcelas integer, 
	descricao character varying,
	dataVcto character varying,
	acaoVctoFeriado character varying,
	intervalo character varying,
	tipoConfiguracao character varying,
	tipoDescricao character varying	
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS configuracoesGeracaoParcelasReceitas;
CREATE TABLE configuracoesGeracaoParcelasReceitas
(
	id SERIAL NOT NULL,
	idConfiguracoesGeracaoParcelas integer,
	idCreditosTributariosRec integer,
	percDesconto integer,
	divideVlrIntegral character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS configuracoesParcelas;
CREATE TABLE configuracoesParcelas
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idCreditosTributarios integer,
	ano integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS contribuicoesMelhorias;
CREATE TABLE contribuicoesMelhorias
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idAgrupamento integer,
    anoEdital integer,
    anoProposta integer,
    edital integer,
	descMelhoria character varying,
    dtEmissaoEdital character varying,
    dtInicio character varying,
    dtProposta character varying,
    dtTermino character varying,
	extensaoLogradouro character integer,
	idContribuicoes integer,
	intervaloFim integer,
	intervaloIni integer,
	larguraLogradouro integer,
	idLogradouro integer,
	memorialDescritivo character varying,
	percJurosFim integer,
	percJurosIni integer,
	percParticipFim integer,
	percParticipIni integer,
	proposta integer,
	qtdImoveis integer,
	qtdParcFim integer,
	qtdParcIni integer,
	situacao character varying,
	tipoIntervaloFim character varying,
	tipoIntervaloIni character varying,
	unidade integer,
	vlMelhoria integer,
	vlMinAmortFim integer,
	vlMinAmortIni integer,
	vlParticipacao integer,
	vlUnidade integer,
	lancamentoGerado character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS contribMelhoriasBairros;
CREATE TABLE contribMelhoriasBairros
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idContribuicaoMelhorias integer,
	idBairro integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS contribMelhoriasImoveis;
CREATE TABLE contribMelhoriasImoveis
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idContribuicaoMelhorias integer,
    dtAdesao integer,
    idImoveis integer,
	intervalo integer,
	percValorizacao integer,
	qtdParcelas integer,
	tipoIntervalo character varying,
    usaSaldoDevedor character varying,
	vlPrevio integer,
	vlValorizacao integer,
	vlVenal integer,
	custoMelhoriaImovel integer,
    situacaoImovelMelhoria character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS contribMelhoriasTaxas;
CREATE TABLE contribMelhoriasTaxas
(
	id SERIAL NOT NULL,
	idContribuicaoMelhorias integer,
	idTaxa integer,
	valorTaxa integer,
	PRIMARY KEY (id)
);
	
DROP TABLE IF EXISTS contribMelhoriasMateriaisServicos;
CREATE TABLE contribMelhoriasMateriaisServicos
(
	id SERIAL NOT NULL,
	idContribuicoesMelhorias integer,
	idMateriaisServicos integer,
	quantidade integer,
	idUnidadesMedidas integer,
	valorUnitario integer,
	valorTotal integer,
	PRIMARY KEY (id)
);
	
DROP TABLE IF EXISTS contribMelhoriasSaldos;
CREATE TABLE contribMelhoriasSaldos
(
	id SERIAL NOT NULL,
	idContribMelhoriaImovel integer,
	idContribuicaoMelhoria integer,
	idCreditoTributario integer,
	idCreditoTributarioRec integer,
	idImoveis integer,
	valorDeclarado integer,
	valorLancado integer,
	valorPago integer,
	PRIMARY KEY (id)
);
	
DROP TABLE IF EXISTS contribMelhoriasMovtos;
CREATE TABLE contribMelhoriasMovtos
(
	id SERIAL NOT NULL,
	idContribuicoesMelhorias integer,
	observacao character varying,
	tipoMovimentacao character varying,
	PRIMARY KEY (id)
);
    
DROP TABLE IF EXISTS contribMelhoriasInfComp;
CREATE TABLE contribMelhoriasInfComp
(
	id SERIAL NOT NULL,
	areaTexto integer,
	idCamposAdicionais integer,
	idContribuicoesMelhorias integer,
	dhCampo character varying,
	texto character varying,
	vlCampo integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS contribMelImovInfComp;
CREATE TABLE contribMelImovInfComp
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idCamposAdicionais integer,
	idContribMelhoriasImoveis integer,
	vlCampo integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS contribMovtosDetalhes;
CREATE TABLE contribMovtosDetalhes
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    descricao character varying,
    tipoArquivo character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS contrMelhoriasInfCompOp;
CREATE TABLE contrMelhoriasInfCompOp
(
	id SERIAL NOT NULL,
	idCamposAdicionais integer,
	idContribMelhoriasInfComp integer,
	PRIMARY KEY (id)
);
    
DROP TABLE IF EXISTS configuracoesContribuicoesMelhorias;
CREATE TABLE configuracoesContribuicoesMelhorias
(
	id SERIAL NOT NULL,
	idCreditoCalculoMelhoria integer,
	idCreditosTributariosRec integer,
	formatoCalculoMelhoria character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS advogados;
CREATE TABLE advogados
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	complementoOab character varying,
    idPessoa integer,
	idSeccionalOab integer
	nroOab integer,
	tipo character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS advogadosCbo;
CREATE TABLE advogadosCbo
(
	id SERIAL NOT NULL,	
	idAdvogados integer,	
	idCbo integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS advogadosResponsaveis;
CREATE TABLE advogadosResponsaveis
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idAdvogados integer,
    idAdvogadosResponsaveis integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS cartorios;
CREATE TABLE cartorios
(
	id SERIAL NOT NULL,
	idPessoa integer,
	identificadorProtesto integer,
	situacao character varying,
	tipoCartorio character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS construtoras;
CREATE TABLE construtoras
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idPessoa integer,
    nroRegistro integer,    
	dtRegistro character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS construtorasEngArquitetos;
CREATE TABLE construtorasEngArquitetos
(
	id SERIAL NOT NULL,
	idConstrutoras integer,
	idEngenheirosArquitetos integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS contadores;
CREATE TABLE contadores
(
	id SERIAL NOT NULL,
	idPessoa integer,
	nroCrc integer,
	PRIMARY KEY (id)
);
	
DROP TABLE IF EXISTS contadoresCbo;
CREATE TABLE contadoresCbo
(
	id SERIAL NOT NULL,
	idCbo integer,
	idContadores integer,
	PRIMARY KEY (id)
);
    
DROP TABLE IF EXISTS contadoresResponsaveis;
CREATE TABLE contadoresResponsaveis
(
	id SERIAL NOT NULL,
	idContadoresResponsaveis integer,
	idContadores integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS engenheirosArquitetos;
CREATE TABLE engenheirosArquitetos
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idPessoa integer,
    nroRegistro integer,
    dtRegistro integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS engenheirosArquitetosCbo;
CREATE TABLE engenheirosArquitetosCbo
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idCbo integer,
    idEngenheiroArquiteto integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS imobiliarias;
CREATE TABLE imobiliarias
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idPessoa integer,
	nroCreci integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS convenios;
CREATE TABLE convenios
(
	id SERIAL NOT NULL,
	idAgenciasBancarias integer,
	idBancos integer,
	carteira integer,
	cedente integer,
	contaBancaria integer,
	descCarteira character varying,
	descricao character varying,
	disponivelUso character varying,
	dvCedente character varying,
	dvContaBancaria character varying,
	nroConvenio integer,
	utilizarParcelamento character varying,
	tipoValidadeNroBaixa character varying,
	valorValidadeNroBaixa integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS conveniosCreditos;
CREATE TABLE conveniosCreditos
(
	id SERIAL NOT NULL,
	idConvenios integer,
    idCreditosTributarios integer,
	PRIMARY KEY (id)
);
    
DROP TABLE IF EXISTS conveniosMensagens;
CREATE TABLE conveniosMensagens
(
	id SERIAL NOT NULL,
	descricao character varying,
	idCreditosTributarios integer,
	idConvenios integer,
    idMensagens integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS conveniosSimulacoes;
CREATE TABLE conveniosSimulacoes
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idConvenio integer,
	idSimulacao integer,
	valor integer,
	nroBaixa integer,
	nossoNumero integer,
	codigoBarras integer,
	linhaDigitavel integer,
	dtVencimento character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS creditosTributarios;
CREATE TABLE creditosTributarios
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    iReceitas integer,
	idIndexadores integer,
	abreviatura character varying,
	descricao character varying,
	calculaImoveisRurais character varying,
	emUso character varying,
	flyProtocolo character varying,
	tipoCadastro character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS creditosTributariosRec;
CREATE TABLE creditosTributariosRec
(
	id SERIAL NOT NULL,
	iReceitas integer,
	idReceitas integer,
	idCreditosTributarios integer,
	situacao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS declaracoes;
CREATE TABLE declaracoes
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idCompetencia integer,
    idCreditosTributariosRec integer,
	idCreditoTributario integer,
    idEconomico integer,
    idGuia integer,
    idRetificada integer,
    daf integer,
    idTaxaExpediente integer,
    das integer,
	dtDeclaracao character varying,
	exercicio integer,
	vlBaseCalculo double precision,
    vlImposto double precision,
    vlServico double precision,
	vlTaxa double precision,
	tipo character varying,
    situacao character varying,
	calcular character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS declaracoesServicos;
CREATE TABLE declaracoesServicos
(
	id SERIAL NOT NULL,
	idDeclaracao integer,
	idListaServico integer,
	comentario character varying,
	itemLista character varying,
	vlDeducao double precision,
	vlImposto double precision,
	vlRetidoDe double precision,
	vlRetidoPor double precision,
	vlServico double precision, 
	aliquota double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS desmembramentos;
CREATE TABLE desmembramentos
(
	id SERIAL NOT NULL,
	idCampoIncrementar integer,
	idEngenheiroArquiteto integer,
	idImovel integer,
	descricao character varying,
	codigoARTRRT character varying,
	dataAprovacao character varying,
	dataCancelamento character varying,
	dataDesmembramento character varying,
	nrProcessoAprovacao integer,
	nrProcessoCancelamento integer,
	observacao character varying,
	metragemMinimaLotes double precision,
	qtdadeLotesGerar integer,
	situacaoProjeto character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS desmembramentosDocumentos;
CREATE TABLE desmembramentosDocumentos
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idDesmembramento integer,
	nomeArquivo character varying,
	tipoArquivo character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS desmembramentosImoveis;
CREATE TABLE desmembramentosImoveis
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idDesmembramento integer,
	idImovel integer,
	unidade integer,
	quadra character varying,
	matricula character varying,
	setor character varying,
	lote character varying,
	campo1 character varying,
	campo2 character varying,
	campo3 character varying,
	campo4 character varying,
	campo5 character varying,
	campo6 character varying,
	campo7 character varying,
	campo8 character varying,
	campo9 character varying,
	campo10 character varying,
	copiarCaracteristicas character varying,
	situacaoImovel character varying, 
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS dividas;
CREATE TABLE dividas
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idPessoa integer,
    idReceitaDiversaLancto integer,
    idEconomico integer,
    idContribMelhoriaImovel integer,
    idCreditoTributario integer,
    idSimulacao integer,
    idGuia integer,
    idImovel integer,
    dataVencimento character varying,
    dataInscricao character varying,
    dataLancamento character varying,
    livro integer,
    folha integer,
    inscricao integer,
    posicao integer,
    processoInscricao character varying,
    situacaoDivida character varying,
    valorInscrito double precision, 
    valorCorrecao double precision,
    valorJuro double precision,
    valorMulta double precision,
    guiaComplementar character varying,
    parcela integer,
    anoLivro integer,
    ano integer,
    idMotivoEstorno integer,
    dataEstorno character varying,
    processoEstorno character varying,
    usuarioEstorno character varying,
    idContribuicaoMelhoria integer,
    das character varying,
    daf character varying,
    codDeclaracaoSimples character varying,
    valorSaldo double precision,
    simplesNacional character varying,
    idNotaAvulsa integer,
    idIndexador integer,
    idReceitasDiversas integer,
    idTransferenciaImoveis integer,
    idObras integer,
    idDivida integer,
    penhora character varying,
    possuiCdaEmitida character varying,
    anoCda integer, 
    nroCda integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS dividasMovtos;
CREATE TABLE dividasMovtos
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idAtoManutencao integer,
    comentario character varying,
    dhEstorno character varying,
    dhManutencao character varying,
    dhMovimentacao character varying,
    idDividas integer,
    dtEstornoInscricao character varying,
    dataInscricao character varying,
    dtValidadeAnistia character varying,
    especificacoesManutencao character varying,
    formasPagamentoPrestacaoDiversa character varying,
    idHomologManutencao integer,
    idMotivoEstornoInscricao integer,
    idMotivoManutencao integer,
    nroParcelamento integer,
    nroParcelas integer,
    nroProcesso integer,
    nroProcessoManutencao integer,
    obsHomologManutencao character varying,
    observacaoManutencao character varying,
    percAnistiaCorrecao double precision,
    percAnistiaJuro double precision,
    percAnistiaMulta double precision,
    percAnistiaSaldo double precision,
    idScriptManutencao integer,
    situacaoAnterior character varying,
    situacaoAtual character varying,
    acoesDocumentos character varying,
    tiposDocumentosDividas character varying,
    tiposManutencoesDividas character varying,
    tiposMovimentacoesDivida character varying,
    nroDocumento integer,
    vlAnistiaCorrecao double precision,
    vlAnistiaJuro double precision,
    vlAnistiaMulta double precision,
    vlAnistiaSaldo double precision,
    vlCorrecao double precision,
    vlInscrito double precision,
    vlJuros double precision,
    valorMulta double precision,
    vlPago double precision,
    vlPrestacaoDiversa double precision,
    vlRemissaoSaldo double precision,
    vlSaldo double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS dividasReceitas;
CREATE TABLE dividasReceitas
(
	id SERIAL NOT NULL,
	idDivida integer,
	idCreditosTributariosRec integer,
	valorInscrito double precision,
	valorCorrecao double precision,
	valorJuro double precision,
	valorMulta double precision,
	valorSaldo double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS dividasResponsaveis;
CREATE TABLE dividasResponsaveis
(
	id SERIAL NOT NULL,
	idDivida integer,
	idResponsavel integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS dividasStatus;
CREATE TABLE dividasStatus
(
	id SERIAL NOT NULL,
	idDividas integer,
	nroDocumento integer,
	cancelado character varying,
	dhStatus character varying,
	statusDivida character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS dividaDebitoInscrito;
CREATE TABLE dividaDebitoInscrito
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idDivida integer,
    idDebito integer,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS cancelamentoDocumentos;
CREATE TABLE cancelamentoDocumentos
(
	id SERIAL NOT NULL,
	qtdDocumentos integer,
	numero integer,
	motivo character varying,
	observacoes character varying,
	responsavel character varying,
	protocoloExecucao character varying,
	dhCriacao character varying,
	tipoManutencao character varying,
	documentos character varying,
	string character varying,
	string2 character varying,
	string3 character varying, 
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS economicos;
CREATE TABLE economicos
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idAgrupamento integer,
    idBairro integer,
    idBanco integer,
    idCondominio integer,
    idContador integer,
    idDistrito integer,
    idEconomico integer,
    idHorarioFuncionamento integer,
    idImovel integer,
    idLogradouro integer,
    idLoteamento integer,
    idMunicipios integer,
    idPessoa integer,
    idPessoasEnderecos integer,
    idTipoEntidadeEspecial integer,
    dataValidadeAlvara character varying,
    apartamento character varying,
    bloco character varying,
    cep character varying,
    complemento character varying,
    descricaoEndereco character varying,
    numero character varying,
    iEconomicos integer,
    economicoPrincipal character varying,
    regimeCobrancaIss character varying,
    situacaoEconomico character varying,
    tipoContribuinte character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS economicosAnexos;
CREATE TABLE economicosAnexos
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idEconomico integer,	
    descricao character varying,
	nomeArquivo character varying,
	idEconomicosMovimentacoes integer,    
    tipoArquivo character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS economicosBeneficiosFiscais;
CREATE TABLE economicosBeneficiosFiscais
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idEconomicos integer,
    idCalculo integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS economicosCnaes;
CREATE TABLE economicosCnaes
(
	id SERIAL NOT NULL,
	idEconomico integer,
	idCnae integer,
	descricao character varying,
	nroDocumento integer,
	principal character varying,
	situacao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS economicosCnaesInfComplem;
CREATE TABLE economicosCnaesInfComplem
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idAgrupamentos integer,
	idCamposAdicionais integer,
	idCamposAdicionaisFilho integer,
    areaTexto character varying,
	dhCampo character varying,
	dtBase character varying,
	idEconomicosCnae integer,
    vlCampo double precision,
    texto character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS economicosCnaesInfComplemOp;
CREATE TABLE economicosCnaesInfComplemOp
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idCamposAdicionaisFilho integer,
	idOpcao integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS economicosCnaesMovtos;
CREATE TABLE economicosCnaesMovtos
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idEconomicosCnae integer,
	observacao character varying,
    dtFinal character varying,	
    dtInicio character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS economicosCnaesValores;
CREATE TABLE economicosCnaesValores
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idEconomicosCnae integer,
	percIssqn double precision,
	valorIssFixo double precision,
	dtIssFixo character varying,
    dtAlvara character varying,
    valorAlvara double precision,
    dtAliquotaIss character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS economicosDocumentos;
CREATE TABLE economicosDocumentos
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idEconomico integer,
    idTipoDocumento integer,
	responsavel character varying,
	dtDocumento character varying
    situacaoDocumento character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS economicosInfComplem;
CREATE TABLE economicosInfComplem
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idAgrupamentos integer,
    idCamposAdicionais integer,
	dhCampo character varying,
	dtBase character varying,
	idEconomico integer,
    idCamposAdicionaisFilho integer,
    texto character varying,
    areaTexto character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS economicosInfComplemOp;
CREATE TABLE economicosInfComplemOp
(
	id SERIAL NOT NULL,
	idEconomicosInformacoesComplementares integer,
	idCamposAdicionaisFilho integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS economicosListaServicos;
CREATE TABLE economicosListaServicos
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idEconomico integer,
	idServico integer,
    principal character varying,
	situacao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS economicosListaServicosMovtos;
CREATE TABLE economicosListaServicosMovtos
(
	id SERIAL NOT NULL,
	idEconomicosListaServico integer,
	dtFinal character varying,
	dtInicio character varying,
	observacao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS economicosListaServicosValores;
CREATE TABLE economicosListaServicosValores
(
	id SERIAL NOT NULL,
	idEconomicosListaServico integer,
    dtAlvara character varying,
	dtAliquotaIss character varying,
	dtIssFixo character varying,
	percIssqn double precision,
	valorIssFixo double precision,
	valorAlvara double precision,
	PRIMARY KEY (id)
);
        
DROP TABLE IF EXISTS economicosMovimentacoes;
CREATE TABLE economicosMovimentacoes
(
	id SERIAL NOT NULL,
	audCriadoPor character varying,
	audDhCriacao character varying,
	audAlteradoPor character varying,
	audDhAlteracao character varying,
	dataValidadeAlvara character varying,
	idEconomico integer,
	descricao character varying,
	dhMovimentacao character varying,
	dtSituacao character varying,
	nroDocumento integer,
	nroProcesso integer,
    tipoMovimentacao character varying,
	situacaoEconomico character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS economicosTabaux;
CREATE TABLE economicosTabaux
(
	id SERIAL NOT NULL,
	idEconomicos integer,
    iTabelaAuxiliar integer,
	idTabelaAuxiliar character varying,
	dtBase character varying,
	campo1 character varying,
	campo2 character varying,
	campo3 character varying,
	campo4 character varying,
	campo5 character varying,
	campo6 character varying,
	campo7 character varying,
	campo8 character varying,
	campo9 character varying,
	campo10 character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS bairros;
CREATE TABLE bairros
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idMunicipio integer,
    codigo integer,
    zonaRural character varying,
    nome character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS condominios;
CREATE TABLE condominios
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idLogradouro integer,
	codigo integer,
    idBairro integer,
	tipoCondominio character varying,
	nome character varying,
	numero integer,
	cep character varying,
	latitude character varying,
	longitude character varying,
	idPessoa integer,
	anoConstrucao integer,
	utilizacao character varying,
	nroPavimentos integer,
	nroBlocos integer,
	nroApartamentos integer,
	nroGaragens integer,
	nroElevadores integer,
	nroSalas integer,
	areaComum integer,
	areaEdificada double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS condominiosInfComplem;
CREATE TABLE condominiosInfComplem
(
	id SERIAL NOT NULL,
	ano integer,
	idCamposAdicionais integer,
	idCamposAdicionaisFilho integer,
	areaTexto character varying,
	idCondominio integer,
	texto character varying,
	vlCampo double precision,
	dhCampo character varying,
	PRIMARY KEY (id)
);
    
DROP TABLE IF EXISTS condominiosInfComplemOp;
CREATE TABLE condominiosInfComplemOp
(
	id SERIAL NOT NULL,
	idCondominiosInfComplem integer,
	idCamposAdicionaisFilho integer,
	PRIMARY KEY (id)
);
		
DROP TABLE IF EXISTS distritos;
CREATE TABLE distritos
(
	id SERIAL NOT NULL,
	idMunicipio integer,
	codigo integer,
	nome character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS estados;
CREATE TABLE estados
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idPaises integer,
	nome character varying,
	uf character varying,
	codigoIBGE integer,
	idTemplate integer,
	versionTemplate character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS faces;
CREATE TABLE faces
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    abreviatura integer,
	descricao character varying,
	padrao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS localidades;
CREATE TABLE localidades
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	descricao integer,
	idDistrito integer,
	idMunicipio  integer.
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS localidadesInfComplem;
CREATE TABLE localidadesInfComplem
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	ano integer,
	idCamposAdicionais integer,
	idLocalidades integer,
	dhCampo character varying,
	texto character varying,
	vlCampo double precision,
	areaTexto character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS localidadesInfComplemOp;
CREATE TABLE localidadesInfComplemOp
(
	id SERIAL NOT NULL,
	idLocalidadesInfComplem integer,
	idCamposAdicionaisFilho integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS logradouros;
CREATE TABLE logradouros
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idLogradouro integer,
	idTipoLogradouro integer,
	idMunicipio integer,
	cep integer,
	epigrafe character varying,
	extensao integer,
	lei character varying,
	zonaFiscal character varying,
    nome character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS logradourosBairros;
CREATE TABLE logradourosBairros
(
	id SERIAL NOT NULL,
	idLogradouros integer,
	idBairro integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS logradourosCep;
CREATE TABLE logradourosCep
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idLogradouros integer,
	cep character varying,
	numeroInicial integer,
	numeroFinal integer,
	idFace integer,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS loteamentos;
CREATE TABLE loteamentos
(
	id SERIAL NOT NULL,
	areaComum integer,
	areaRemanescente integer,
	areaTotal double precision,
	codigo integer,
	dtAprovacao character varying,
	dtCriacao character varying,
	dtLiberacao character varying,
	idBairros integer,
	idDistritos integer,
	idMunicipios integer,
	nome character varying,
	nroCaucionados integer,
	nroLotes integer,
	nroQuadras integer,
	observacao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS municipios;
CREATE TABLE municipios
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    codigoIBGE integer,
    codigoTribunalJustica integer,
	idEstado integer,
    codigoSIAFI character varying,
	uf character varying,
	nome character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS paises;
CREATE TABLE paises
(
	id SERIAL NOT NULL,
	versionTemplate character varying,
	codigoBacen character varying,
	idTemplate integer,
	sigla2C character varying,
	sigla3C character varying,
	sigla3D character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS secoes;
CREATE TABLE secoes
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idLogradouro integer,
    idFace integer,
    secao integer,
    iPlantas integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS secoesInfComplem;
CREATE TABLE secoesInfComplem
(
	id SERIAL NOT NULL,
	ano integer,
	areaTexto character varying,
	idCamposAdicionaisFilho integer,
	idCamposAdicionais integer,
	dhCampo character varying,
	idSecao integer.
	texto character varying,
	vlCampo double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS secoesInfComplemOp;
CREATE TABLE secoesInfComplemOp
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idCamposAdicionaisFilho integer,
	idSecoesInfComplem integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS feriados;
CREATE TABLE feriados
(
	id SERIAL NOT NULL,	
	dataFeriado character varying,
	descricao character varying, 
	abrangencia character varying,
	tipoFeriado character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS fontesDivulgacoesAtos;
CREATE TABLE fontesDivulgacoesAtos
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    meioComunicacao character varying,
    descricao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS guias;
CREATE TABLE guias
(
	id SERIAL NOT NULL,
	idLancamentos ,
	idConfiguracoesGeracaoParcelas integer,
	idIndexadores integer,
	dataVcto character varying,
	nroParcela integer,
	situacao character varying,
	valorLancado double precision,
	valorDesconto double precision,
	unica character varying,
	lancamentoEnglobado character varying,
	complementar character varying,
	idCompetencias integer,
	idPessoaAtual integer,
	valorPago double precision,
	idPessoas integer,
	numeroBaixa integer,
	das character varying,
	daf character varying,
	idPagamentos integer,
	valorCorrecaoPrefixada double precision,
	valorJuroFinanciamento double precision,
	parcelamentoDaf character varying,
	nroOperacao integer,
	dataOperacao character varying,
	dhLancamento character varying,
	dhCancelamento character varying,
	usuarioCancelamento character varying,
	vlTotalTaxa double varying,
	dataCredito character varying,
	dataMovimentacao character varying,
	geradaPorDiferencaPagamento character varying,
	origem character varying,
	situacaoAnterior character varying,
	nroProcesso integer,
	codigoBarras integer,
	representacaoNumerica integer,
	iGuias integer,
	idImovel integer,
	idEconomico integer,
	idReceitaDiversa integer,
	idReceitaDiversaLanctos integer,
	idTransfImoveis integer,
	idNotaAvulsa integer,
	idContribuicaoMelhorias integer,
	idContribuicaoMelhoriasImoveis integer,
	idCreditoTributario integer,
	idObras integer,
	ano integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS guiasEmitidas;
CREATE TABLE guiasEmitidas
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    protocoloEmissao character varying,
    idDebito integer,
    idDivida integer,
	idParcela integer,
	dataVcto character varying,
	valorOriginal double precision,
	valorDevido double precision,
	valorDesconto double precision,
	valorBeneficio double precision,
	valorCorrecao double precision,
	valorRemidoCorrecao double precision,
	valorJuro double precision,
	valorRemidoJuro double precision,
	valorMulta double precision,
	valorRemidoMulta double precision,
	valorDescontoCorrecao double precision,
	valorDescontoJuros double precision,
	valorDescontoMulta double precision,
	valorJuroFinanciamento double precision,
	valorJuroFinanciamento double precision,
	valorDocumento double precision,
	numeroBaixa integer,
	codigoBarras integer,
	nossoNumero integer,
	represNumerica integer,
	dataValidade character varying,
	idConvenio integer,
	idBanco integer,
	idAgencia integer,
	nroConvenio integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS guiasEmitidasReceitas;
CREATE TABLE guiasEmitidasReceitas
(
	id SERIAL NOT NULL,
	idReceita integer,
    idGuiaEmitida integer,
	classificacaoReceita character varying,
	valorOriginal double precision,
	valorDevido double precision,
	valorDesconto double precision,
	valorBeneficio double precision,
	valorCorrecao double precision,
	valorRemidoCorrecao double precision,
	valorJuro double precision,
	valorRemidoJuro double precision,
	valorMulta double precision,
	valorRemidoMulta double precision,
	valorDescontoCorrecao double precision,
	valorDescontoJuros double precision,
	valorDescontoMulta double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS guiasNumerosBaixas;
CREATE TABLE guiasNumerosBaixas
(
	id SERIAL NOT NULL,
	systemId integer,
    utilizado integer,
	vlGuia double precision,
	nroConvenio integer,
	nroBanco integer,
	idGuia integer,
	dtValidade character varying,
	dtVencimento character varying,
	cedente character varying,
	integrado boolean,
	dhGeracao character varying,
	dhIntegracao character varying,
	idGuiaEmitida integer,
	idGuiaUnificada integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS guiasReceitas;
CREATE TABLE guiasReceitas
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idGuias integer,
	idReceitasCreditos integer,
    valorLancado double precision,
	valorDesconto double precision,
	valorBeneficio double precision,
	valorPago double precision,
	percBeneficioCorrecao integer,
	percBeneficioJuros integer,
	percBeneficioMulta integer,
	percBeneficioReceita integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS guiasReceitasManutencoes;
CREATE TABLE guiasReceitasManutencoes
(
	id SERIAL NOT NULL,
	idGuiasReceitas integer,
	idManutencaoRevogacao integer,
    idManutencoesCalculos integer,
	percCorrecao integer,
	percIncentivo integer,
	percIsencao integer,
	percJuros integer,
	percMulta integer,
	percRemissao integer,
	valorIncentivo double precision,
	valorIsencao double precision,
	valorRemissao double precision,
	tipoSolicitacao character varying,
	PRIMARY KEY (id)
);
	
DROP TABLE IF EXISTS guiasTaxas;
CREATE TABLE guiasTaxas
(
	id SERIAL NOT NULL,
	idGuias integer,
	idConfigTaxasExpediente integer,
	idTaxasExpCreditos integer,
	valorTaxa double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS guiasUnificadas;
CREATE TABLE guiasUnificadas
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    base64 character varying,
	idConvenio integer,
	idEconomico integer,
	idImobiliaria integer,
	idImovel integer,
	idPessoa integer,
	idObras integer,
	idScriptGuiaUnificada integer,
	idReceitaTaxaExpediente integer,
	nroBaixa integer,
	codigoBarras integer,
	protocoloExecucao integer,
	representacaoNumerica integer,
	dtVencimento character varying,
	possuiDebitos boolean,
	possuiDividas boolean,
	possuiParcelamento boolean,
	vlAnistiaCorrecao double precision,
	vlAnistiaJuros double precision,
	vlAnistiaMulta double precision,
	vlAnistiaTributo double precision,
	vlBeneficios double precision,
	vlCorrecaoPreFixada double precision,
	vlDescontoCorrecaoGuia double precision,
	vlDescontoDebito double precision,
	vlDescontoJurosGuia double precision,
	vlDescontoMultaGuia double precision,
	vlDescontoParcelamento double precision,
	vlDescontoTributoGuia double precision,
	vlGuia double precision,
	vlJurosFinanciamento double precision,
	vlRemissaoTributo double precision,
	vlSelecionado double precision,
	vlTaxaExpediente double precision,
	vlTaxasParcelamento double precision,
	vlTotalCorrecao double precision,
	vlTotalDescontos double precision,
	vlTotalDescontosGuia double precision,
	vlTotalJuros double precision,
	vlTotalMulta double precision,
	vlTributo double precision,
	criterioFormaPagamento character varying,
	formaPagamento character varying,
	situacao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS guiasUnificadasComp;
CREATE TABLE guiasUnificadasComp
(
	id SERIAL NOT NULL,
	idCreditoTributario integer,
    idDebito integer,
    idDivida integer,
    idGuiaUnificada integer,
    idReferente integer,
    idParcelamento integer,
    idParcelamentoParcela integer,
    ano integer,
    vlAnistiaCorrecao double precision,
    vlAnistiaJuros double precision,
    vlAnistiaMulta double precision,
    vlAnistiaTributo double precision,
    vlBeneficios double precision,
    vlBeneficioCorrecao double precision,
    vlBeneficioJuro double precision,
    vlBeneficioMulta double precision,
    vlCorrecao double precision,
    vlCorrecaoPreFixada double precision,
    vlDescontoCorrecaoGuia double precision,
    vlDescontoDebito double precision,
    vlDescontoJurosGuia double precision,
    vlDescontoMultaGuia double precision,
    vlDescontoParcelamento double precision,
    vlDescontoTributoGuia double precision,
    vlJuros double precision,
    vlJurosFinanciamento double precision,
    vlRemissaoTributo double precision,
    vlMulta double precision,
    vlTributo double precision,
    vlTaxasParcelamento double precision,
    tipoLancamento character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS habitese;
CREATE TABLE habitese
(
	id SERIAL NOT NULL,
	idObra integer,
	idModelo integer,
	nroDocumento integer,
	tipo character varying,
	dtEmissao character varying,
	restricao character varying,
	restricaoObservacao character varying,
	ano integer,
	metragem double precision,
	situacaoHabitese character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS horariosDias;
CREATE TABLE horariosDias
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idHorariosFuncionamento integer,
	horaIntrajornadaEntrada character varying,
    horaIntrajornadaSaida character varying,
    horaSaida character varying,
    diaSemana character varying,
    horaEntrada character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS horariosFuncionamento;
CREATE TABLE horariosFuncionamento
(
	id SERIAL NOT NULL,
	descricao character varying,
	PRIMARY KEY (id)
);	

DROP TABLE IF EXISTS historicoAlteracaoImovel;
CREATE TABLE historicoAlteracaoImovel
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	dhAlteracao character varying,
    usuario character varying,
	entityId integer,
	alteracoes character varying,
    campo character varying,
    descricao character varying,
    anterior character varying,
    atual character varying,
    anteriorFormatado character varying,
	atualFormatado character varying,
	tipo character varying,
	itens character varying,
	codigo integer,
	descricaoItem character varying,
	idEntity integer,	
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS imoveis;
CREATE TABLE imoveis
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    campo1 character varying,
	campo2 character varying,
	campo3 character varying,
	campo4 character varying,
	campo5 character varying,
	campo6 character varying,
	campo7 character varying,
	campo8 character varying,
	campo9 character varying,
	campo10 character varying,
	idAgrupamento integer,
	apartamento integer,
	idBairro integer,
	bloco character varying,
	cep character varying, 
	complemento character varying,
	idCondominio integer,
	idCorresponsavel integer,
	denominacao character varying,
	idDistrito integer,
	enderecoCorrespondencia character varying,
	idFace integer,
	iImoveis integer,
	idImovel integer,
	idImobiliaria integer,
	inscricaoAnterior integer,
	inscricaoIncra character varying,
	latitude character varying,
	idLocalidade integer,
	idLogradouro integer,
	longitude character varying,
	lote character varying,
	idLoteamento integer,
	matricula integer,
	nroImovel integer,
	idPessoa integer,
	idPessoasEnderecos integer,
	quadra character varying,
	idSecoes integer,
	setor character varying,
	situacao character varying,
	tipoImovel character varying,
	unidade character varying,
	garagem character varying,
	sala character varying,
	loja character varying,
	dtConstrucao character varying,
);

DROP TABLE IF EXISTS imoveisBeneficiosFiscais;
CREATE TABLE imoveisBeneficiosFiscais
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idCalculo integer,
	idImovel integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS imoveisDebitoConta;
CREATE TABLE imoveisDebitoConta
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idImoveis integer,
    idPessoa integer,
    idPessoasContasBancos integer,
	dataExclusao character varying,
    dataOpcao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS imoveisEnglobados;
CREATE TABLE imoveisEnglobados
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idImovelEnglobado integer,
	idImovel integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS imoveisImagens;
CREATE TABLE imoveisImagens
(
	id SERIAL NOT NULL,
	idImoveis integer,
	tipoImagem character varying,
	tipoArquivo character varying,
	descricao character varying,
	nomeArquivo character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS imoveisInfComplem;
CREATE TABLE imoveisInfComplem
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idImoveis integer,
    idAgrupamentos integer,
    idCamposAdicionais integer,
    idCamposAdicionaisFilho integer,
	ano integer,
	areaTexto character varying,
    dhCampo character varying,
	texto character varying,
	vlCampo double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS imoveisInfComplemOp;
CREATE TABLE imoveisInfComplemOp
(
	id SERIAL NOT NULL,
	idImoveisInfComplem integer,
	idCamposAdicionaisFilho integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS imoveisMovDetalhes;
CREATE TABLE imoveisMovDetalhes
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idImoveisMovimentacoes integer,
	detalhe character varying,
    tipoArquivo character varying,
	nomeArquivo character varying,
	tipoAnexo character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS imoveisMovimentacoes;
CREATE TABLE imoveisMovimentacoes
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idImoveis integer,
    idTransferenciaImoveis integer,
	idAlteracaoCadastral character varying,
	descricao character varying,
	situacao character varying,
	tipoMovimentacao character varying,
	nroProcesso integer,
    audCriadoPor character varying,
    audDhCriacao character varying,
	audAlteradoPor character varying,
	audDhAlteracao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS imoveisOrigem;
CREATE TABLE imoveisOrigem
(
	id SERIAL NOT NULL,
	idImovelOrigem integer,
	idImovel integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS imoveisResponsaveis;
CREATE TABLE imoveisResponsaveis
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idPessoa integer,
	idImovel integer,
    percentual double varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS imoveisTestadas;
CREATE TABLE imoveisTestadas
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idImovel integer,
    idBairro integer,
    idFace integer,
    idLogradouro integer,
	idSecao integer,
	anoBase integer,
	anoDesativacao integer,
	extensao integer,
	numero integer,
    testadaPrincipal character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS indexadores;
CREATE TABLE indexadores
(
	id SERIAL NOT NULL,
	nome character varying,
	sigla character varying,
	tipo character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS indexadoresValores;
CREATE TABLE indexadoresValores
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idIndexadores integer,    
    data character varying,
    valor double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS integracoesContabeis;
CREATE TABLE integracoesContabeis
(
	id SERIAL NOT NULL,
	idConvenios integer,
	tipoIntegracao character varying,
	tipoLancamentoIntegrados character varying,
	dataCreditoFinal character varying,
	dataCreditoInicial character varying,
	dataEstornoFinal character varying,
	dataEstornoInicial character varying,
	dataMovimentacaoFinal character varying,
	dataMovimentacaoInicial character varying,
	dataPagamentoFinal character varying,
	dataPagamentoInicial character varying,	
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS integracoesContabeisCreditos;
CREATE TABLE integracoesContabeisCreditos
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idCreditosTributarios integer,
    idIntegracoesContabeis integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS integracoesContabeisDadosIntegrados;
CREATE TABLE integracoesContabeisDadosIntegrados
(
	id SERIAL NOT NULL,
	idLoteIntegracao integer,
	identIntegracaoEstornada integer,
	idIntegracoesContabeis integer,
	exercicio integer,
    agencia character varying,
	banco character varying,
	cnpj character varying,
	dataIntegracao character varying,
	digitoAgencia character varying,
	digitoConta character varying,
	formasRecebimento character varying,
	nomeEntidade character varying,
	numeroConta integer,
	situacaoIntegracao character varying,
	tipoProcessamentoDivida character varying,
	valorLote double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS integracoesContabeisDadosIntegradosReceitas;
CREATE TABLE integracoesContabeisDadosIntegradosReceitas
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    anoVcto integer,
	idIntegracoesContabeisDadosIntegrados integer,
    valor integer,
    descricao character varying,
    lancado character varying,
	classificacaoValorIntegrar character varying,
	anoDivida character varying,
	anoVcto character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS integracoesContabeisDadosIntegradosReceitasDeducoes;
CREATE TABLE integracoesContabeisDadosIntegradosReceitasDeducoes
(
	id SERIAL NOT NULL,
	idIntegracoesContabeisDadosIntegradosReceitas integer,	
	tipoDevolucao character varying,
	valor double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS integracoesContabeisDetalhamentos;
CREATE TABLE integracoesContabeisDetalhamentos
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
   	idDividas integer,
    idGuias integer,
    idIntegracoesContabeis integer,
    idPagamentos integer,
    idReceitas integer,
    situacao character varying,
    valorCorrecao double precision, 
    valorCorrecaoPreFixada double precision,
    valorDescontoCorrecao double precision,
    valorDescontoJuros double precision,
    valorDescontoMulta double precision,
    valorDescontoTributo double precision,
    valorDiferenca double precision,
    valorDiferencaCorrecao double precision,
    valorDiferencaJuros double precision,
    valorDiferencaMulta double precision,
    valorDiferencaTributo double precision,
    valorImunidade double precision,
    valorIncentivoFiscal double precision,
    valorIsencoes double precision,
    valorJuros doubple precision,
    valorJurosFinancimento double precision,
    valorMulta double precision,
    valorRemissao double precision,
    valorTotalPago double precision,
    valorTributo double precision,
    identificacaoIntegracaoOrigem integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS integracoesContabeisHistoricos;
CREATE TABLE integracoesContabeisHistoricos
(
	id SERIAL NOT NULL,
	idIntegracoesContabeis integer,
	comentario character varying,
    situacaoIntegracao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS integracoesContabeisReceitas;
CREATE TABLE integracoesContabeisReceitas
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    ano integer,
    comentario character varying,
    idCreditosTributarios integer,
    idIntegracoesContabeis integer,
    idReceitas integer,
    situacao character varying,
    valorCorrecao double precision,
    valorCorrecaoPreFixada double precision,
    valorDescontoCorrecao double precision,
    valorDescontoJuros double precision,
    valorDescontoMulta double precision,
    valorDescontoTributo double precision,
    valorDiferenca double precision,
    valorDiferencaCorrecao double precision,
    valorDiferencaJuros double precision,
    valorDiferencaMulta double precision,
    valorDiferencaTributo double precision,
    valorImunidade double precision,
    valorIncentivoFiscal double precision,
    valorIsencoes double precision,
    valorJuros double precision,
    valorJurosFinancimento double precision,
    valorMulta double precision,
    valorRemissao double precision,
    valorTotalPago double precision,
    valorTributo double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS irrf;
CREATE TABLE irrf
(
	id SERIAL NOT NULL,
	descricao character varying,
	dataInicioVigencia character varying,
    valorDeducao double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS irrfAliquotas;
CREATE TABLE irrfAliquotas
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idIrrf integer,	
    baseInicial character varying,
	baseFinal character varying,
    valorDeducao double precision,
	valorBaseFinal double precision,
	valorBaseInicial double precision,
    aliquota double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS lancamentos;
CREATE TABLE lancamentos
(
	id SERIAL NOT NULL,
	idPessoa integer,
	idImoveis integer,
	idCreditosTributarios integer,
	ano integer,
	idCalculos integer,
	complementar character varying,
	lancamentoEnglobado character varying,
	idReceitasDiversasLanctos integer,
	idEconomicos integer,
	idTransferenciaImoveis integer,
	idReceitasDiversas integer,
	situacao character varying,
	idPessoaAtual integer,
	idContribuicaoMelhorias integer,
	idContribMelhoriasImoveis integer,
	idNotasAvulsas integer,
	idLancamentoPrincipal integer,
	idObras integer,
	dhLancamento character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS lancamentosReceitas;
CREATE TABLE lancamentosReceitas
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idLancamentos integer,
    idReceitasCreditos integer,
	vlLancado double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS limitesArrecadacao;
CREATE TABLE limitesArrecadacao
(
	id SERIAL NOT NULL,
	tipoBaixa character varying,
	formaPagto character varying,
	inscritos character varying,
	naoInscritos character varying,
	valorMaximoDiferenca double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS limitesArrecadacaoCreditos;
CREATE TABLE limitesArrecadacaoCreditos
(
	id SERIAL NOT NULL,
	idCreditosTributarios integer,
	idLimitesArrecadacao integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS livrosDividas;
CREATE TABLE livrosDividas
(
	id SERIAL NOT NULL,
	livro integer,
	anoLivro integer,
	posicao integer,
	folha integer,
	inscricao integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS manutencoesCalculos;
CREATE TABLE manutencoesCalculos
(
	id SERIAL NOT NULL,
	abrangencia character varying,
    anoVigencia integer,
    idBeneficioFiscal integer,
    classificacaoRevisaoCalculo character varying,
    dtRequerimento character varying,
    dtIniVigencia character varying,
    dtFimVigencia character varying,
    idManutencoesCalculos integer,
    justificativa character varying,
    idMotivos integer,
    nroProcesso integer,
    observacao character varying,
    processandoReferentes character varying,
    idRequerente integer,
    situacao character varying,
    tipoRequerimento character varying,
    tipoSolicitacao character varying,
    tipoVigencia character varying,
    tipoSelecaoCreditos character varying,
    percLancadoReq double precision,
    percLancado double precision,
    percCorrecao double precision,
    percCorrecaoReq double precision,
    percJuros double precision,
    percJurosReq double precision,
    percMulta double precision,
    percMultaReq double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS manutCalcCreditos;
CREATE TABLE manutCalcCreditos
(
	id SERIAL NOT NULL,
	idCreditoTributario integer,
	idManutencaoCalculo integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS manutCalcCreditosRec;
CREATE TABLE manutCalcCreditosRec
(
	id SERIAL NOT NULL,
    idCreditosTributariosRec integer,
    idManutencoesCalculos integer,
    idManutCalcReferentes integer,
    idMotivo integer,
    selecionada character varying,
    deferida character varying,
    classificacaoRevisaoCalculo character varying,
    valorLancado double precision,
    valorCorrecao double precision,
    valorJuros double precision,
    valorMulta double precision,
    valorBeneficioLancado double precision,
    valorBeneficioCorrecao double precision,
    valorBeneficioJuros double precision,
    valorBeneficioMulta double precision,
    valorBeneficioLancadoReq double precision,
    valorBeneficioCorrecaoReq double precision,
    valorBeneficioJurosReq double precision,
    valorBeneficioMultaReq double precision,
    percLancadoReq double precision,
    percLancado double precision,
    percCorrecao double precision,
    percCorrecaoReq double precision,
    percJuros double precision,
    percJurosReq double precision,
    percMulta double precision,
    percMultaReq double precision,
    percReqAlterado double precision,
    percAlterado double precision,
    anosVigencia integer,
	PRIMARY KEY (id)
);
        
DROP TABLE IF EXISTS manutCalcDocumentos;
CREATE TABLE manutCalcDocumentos
(
	id SERIAL NOT NULL,
	idManutencoesCalculos integer,
	nomeArquivo character varying,
	tipoArquivo character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS manutCalcGuiasGeradas;
CREATE TABLE manutCalcGuiasGeradas
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idGuias integer,
    idManutencaoCalculo integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS manutCalcMovtos;
CREATE TABLE manutCalcMovtos
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idManutencoesCalculos integer,
    audCriadoPor character varying,
	audDhCriacao character varying,
	audAlteradoPor character varying,
	audDhAlteracao character varying,
	descricao character varying,
	tiposMovimentacoes character varying,
	tipoManutencao character varying,
	situacao character varying,
	situacaoAnterior character varying,
	dhMovimentacao character varying,
	usuarioMovimentacao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS manutCalcReferentes;
CREATE TABLE manutCalcReferentes
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idManutencoesCalculos integer,
	idLancamentos integer,
	idImoveis integer,
	idPessoas integer,
	idContribuicoes integer,
	idReceitasDiversasLanctos integer,
	idReceitasDiversas integer,
	idEconomicos integer,
	idTransferenciaImoveis integer,
	idNotasAvulsas integer,
	idObras integer,
	descricao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS manutencaoDivida;
CREATE TABLE manutencaoDivida
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idAto integer,
    idMotivo integer,
	vlPrestacaoDiversa double precision,
	nroProcesso character varying,
	formasPagamentoPrestacaoDiversa character varying,
	especificacoes character varying,
	observacoes character varying,
	obsHomologManutencao character varying,
	situacao character varying,
	tiposManutencoesDividas character varying,
	qtdDividas integer,
	dtValidade character varying,
	dhManutencao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS manutencaoDividaSelecionada;
CREATE TABLE manutencaoDividaSelecionada
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idDivida integer,
    idManutencaoDivida character varying,
    idContribuinte integer,
    idCredito integer,
    idPagamento integer,
	anoCredito integer,
	valorPrestacaoDiversa double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS materiaisServicos;
CREATE TABLE materiaisServicos
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idUnidadesMedidas integer,
	descricao character varying,
	classificacao character varying,
	formaCalculo character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS motivos;
CREATE TABLE motivos
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	descricao character varying,
    dadtipoMotivoos character varying,
    idAtos integer,
	erroFalha character varying,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS notasAvulsas;
CREATE TABLE notasAvulsas
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idEconomicoPrestador integer,
    idEconomicoTomador integer,
    idPrestador integer,
    idRequerente integer,
    idTomador integer,
    idMotivo integer,
    apartamentoTomador character varying,
    bairroTomador character varying,
    blocoTomador character varying, 
    cepTomador character varying,
    complementoTomador character varying,
    condominioTomador character varying,
    cpfCnpjPrestador character varying,  
    cpfCnpjTomador character varying, 
    descricaoEnderecoTomador character varying,
    distritoTomador character varying,
    enderecoObsTomador character varying,
    inscricaoMunicipalPrestador character varying,
    inscricaoMunicipalTomador character varying,
    logradouroTomador character varying,
    loteamentoTomador character varying,
    municipioTomador character varying,
    nomePrestador character varying,
    nomeRequerente character varying,
    nomeTomador character varying,
    numeroTomador character varying,
    serie character varying,
    modelo integer,
    numeroEmpenho integer,
    numeroNota integer,
    dataEmissao character varying,
    dataEmpenho character varying,
    outrasDeducoes integer,
    qtdDependentes integer,
    totalDeducoes integer,
    totalNotaFiscal integer,
    baseCalcIrrf double precision,
    valorCofins double precision,
    valorCsll double precision,
    valorInss double precision,
    valorInssRecolher double precision,
    valorInssRecolhido double precision,
    valorIrrf double precision,
    valorIssqn double precision,
    valorLiquido double precision,
    valorPisPasep double precision,
    valorSestSenat double precision,
    valorTotalReducao double precision,
    valorTotalServicos double precision,
    vlPorDependente double precision,
    vlPorPensaoAlimenticia double precision,
    vlTotalDependentes double precision,
    lancamentoGerado character varying,
    situacaoNota character varying,	
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS notasAvulsasMovtos;
CREATE TABLE notasAvulsasMovtos
(
	id SERIAL NOT NULL,
	idNotasAvulsas integer,
	descricao character varying,
	situacao character varying,
	situacaoAnterior character varying,
	dhMovimentacao character varying,
	usuarioMovimentacao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS notasAvulsasServicos;
CREATE TABLE notasAvulsasServicos
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idListaServicos integer,
    idNotasAvulsas integer,
	aliquotaIbpt double precision,
	aliquotaServico double precision,
	quantidade double precision,
	valorUnitario double precision,
	valorReducao double precision,
	valorServico double precision,
    descricaoServico character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS notificacoesDebitos;
CREATE TABLE notificacoesDebitos
(
	id SERIAL NOT NULL,
    modelo integer,
    protocoloExecucao character varying,
    nroDocumento integer,
    dataEmissao character varying,
    cancelada character varying,
    idContribuinte integer,
    ano integer,
    dataInscricao character varying,
    idGuia integer,
    idCreditoTributario integer,
    idConfigGeracaoParcelas integer,
    parcela integer,
    dataVencimento character varying,
    situacaoParcela character varying,
    lancamentoComplementar character varying,
    valorDebito double precision,
    idReferente integer,
    tipoReferente character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS notificacoesDebitosDados;
CREATE TABLE notificacoesDebitosDados
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
 	idNotificacoesDebitos integer,
    idContribuinte integer,
    idEnderecoContribuinte integer,
    idTelefoneContribuinte integer,
    idImovel integer,
    idEconomico integer,
    idReceitaDiversa integer,
    idContribuicaoMelhoria integer,
    idTransferenciaImovel integer,
    idNotaAvulsa integer,
    campo1 character varying,
    campo2 character varying,
    campo3 character varying,
    campo4 character varying,
    campo5 character varying,
    campo6 character varying,
    campo7 character varying,
    campo8 character varying,
    campo9 character varying,
    campo10 character varying,
    unidadeImovel integer,
    nomeCorresponsavel character varying,
    idEnderecoCorresponsavel integer
    idAtividade integer,
    idServico integer,
    idCreditoTributario integer,
    idReceitas integer,
    idConfigGeracaoParcelas integer,
    idGuia integer,
    idLancamento integer,
    dataVencimento character varying,
    parcela integer,
    situacaoParcela character varying,
    situacaoLancamento character varying,
    lancamentoComplementar character varying,
    apartamentoReferente character varying,
    idBairroReferente integer,
    cepReferente character varying,
    complementoReferente character varying,
    idCondominioReferente integer,
    idDistritoReferente integer,
    inscricaoIncraReferente integer,
    idLocalidadeReferente integer,
    idLogradouroReferente integer,
    loteReferente integer,
    idLoteamentoReferente integer,
    quadraReferente character varying,
    valorTributoLancamento double precision,
    valorCorrecaoLancamento double precision,
    valorJurosLancamento double precision,
    valorMultaLancamento double precision,
    valorTributoReceitaLancamento double precision,
    valorCorrecaoReceitaLancamento double precision,
    valorJurosReceitaLancamento double precision,
    valorMultaReceitaLancamento double precision,
    valorTributoParcela double precision,
    valorCorrecaoParcela double precision,
    valorJurosParcela double precision,
    valorMultaParcela double precision,
    valorTotalParcela double precision,
    valorTributoReceitaParcela double precision,
    valorCorrecaoReceitaParcela double precision,
    valorJurosReceitaParcela double precision,
    valorMultaReceitaParcela double precision,
    valorTotalReceitaParcela double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS notificacoesDividas;
CREATE TABLE notificacoesDividas
(
	id SERIAL NOT NULL,
	modelo integer,
	nroDocumento integer,
	protocoloExecucao character varying,
	dataEmissao character varying,
	cancelada character varying,
	idContribuinte integer,
	ano integer,
	idDivida integer,
	idCreditoTributario integer,
	parcela integer,
	numeroInscricao integer,
	dataInscricao character varying,
	dataVencimento character varying,
	situacaoDivida character varying,
	valorDivida double precision,
	tipoReferente character varying,
	idReferente integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS notificacoesDividasDados;
CREATE TABLE notificacoesDividasDados
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idNotificacoesDividas integer,
    idContribuinte integer,
    idEnderecoContribuinte integer,
    idTelefoneContribuinte integer,
    idImovel integer,
    idEconomico integer,
    idReceitaDiversa integer,
    idContribuicaoMelhoria integer,
    idTransferenciaImovel integer,
    idNotaAvulsa integer,
    campo1 character varying,
    campo2 character varying,
    campo3 character varying,
    campo4 character varying,
    campo5 character varying,
    campo6 character varying,
    campo7 character varying,
    campo8 character varying,
    campo9 character varying,
    campo10 character varying,
    unidadeImovel integer,
    nomeCorresponsavel character varying,
    idEnderecoCorresponsavel integer,
    idAtividade integer,
    idServico integer,
    idCreditoTributario integer,
    idReceitas integer,
    apartamentoReferente character varying,
    idBairroReferente integer,
    cepReferente character varying,
    complementoReferente character varying,
    idCondominioReferente integer,
    idDistritoReferente integer,
    inscricaoIncraReferente integer,
    idLocalidadeReferente integer,
    idLogradouroReferente integer,
    loteReferente character varying,
    idLoteamentoReferente integer,
    quadraReferente character varying,
    idDivida integer,
    numeroInscricao integer,
    ano integer,
    dataInscricao character varying,
    dataVencimento character varying,
    numero integer,
    anoLivro integer,
    folha integer,
    posicao integer,
    parcela integer,
    valorTributoInscritoMoedaOriginal double precision,
    valorTributoInscritoMoedaCorrente double precision,
    valorSaldoMoedaOriginal double precision,
    valorSaldoMoedaCorrente double precision,
    valorCorrecaoAtual double precision,
    valorJurosAtual double precision,
    valorMultaAtual double precision,
    valorSaldoTotalMoedaCorrente double precision,
    valorTributoReceitaInscritoMoedaOriginal double precision,
    valorTributoReceitaInscritoMoedaCorrente double precision,
    valorSaldoReceitaMoedaOriginal double precision,
    valorSaldoReceitaMoedaCorrente double precision,
    valorCorrecaoReceitaAtual double precision,
    valorJurosReceitaAtual double precision,
    valorMultaReceitaAtual double precision,
    valorSaldoTotalReceitaMoedaCorrente double precision,
    situacaoDivida character varying,
    mesesCobrancaAcrescimos integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS obras;
CREATE TABLE obras
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idAgrupamentos integer,
	idImoveis integer,
    idSolicitantes integer,
    codigo integer,
    dataEntrada character varying,
	descricao character varying,
	nroProcesso integer,
	observacao character varying,
	situacao character varying,
	solicitanteProprietario character varying,
    medida double precision,
    unidadeMedida character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS obrasConstrutoras;
CREATE TABLE obrasConstrutoras
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idConstrutoras integer,
	idObras integer,    
    dtValidade character varying,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS obrasResponsaveisTecnicos;
CREATE TABLE obrasResponsaveisTecnicos
(
	id SERIAL NOT NULL,
	idEngenheirosArquitetos integer,
	idObras integer,
    nroDocumento double precision,
	observacao character varying,
	responsabilidade character varying,
	tipoDocumento character varying,
	PRIMARY KEY (id)
);
	
DROP TABLE IF EXISTS obrasResponsaveisTecnicosAtividades;
CREATE TABLE obrasResponsaveisTecnicosAtividades
(
	id SERIAL NOT NULL,
	idObrasResponsaveisTecnicos integer,
	idCbos integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS obrasImoveisRurais;
CREATE TABLE obrasImoveisRurais
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    apartamento integer,
    idBairro integer,
	bloco character varying,
	cep character varying,
	complemento character varying,
	idCondominio integer,
	denominacao character varying,
    idDistrito integer,
	idFace integer,
    latitude character varying,
	idLocalidade integer,
	idLogradouro integer,
	longitude character varying,
	lote integer,
	idLoteamento integer,
	matricula character varying,
	quadra character varying,
	idSecao integer,
	setor integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS obrasImoveisInfComp;
CREATE TABLE obrasImoveisInfComp
(
	id SERIAL NOT NULL,
	idObras integer,
	idImoveis integer,
	idCamposAdicionais integer,
	idCamposAdicionaisFilho integer,
	ano integer,
    vlCampo double precision,
	areaTexto character varying,
	dhCampo character varying,
	PRIMARY KEY (id)
);
    
DROP TABLE IF EXISTS obrasImoveisInfCompOp;
CREATE TABLE obrasImoveisInfCompOp
(
	id SERIAL NOT NULL,
	idObrasImoveisInfComp integer,
	idCamposAdicionaisFilho integer,
	PRIMARY KEY (id)
);
        
DROP TABLE IF EXISTS obrasInfComp;
CREATE TABLE obrasInfComp
(
	id SERIAL NOT NULL,
	idObras integer,
	idAgrupamentos integer,
	idCamposAdicionais integer,
	idCamposAdicionaisFilho integer,
	ano integer,
	vlCampo double precision,
	texto character varying,
	areaTexto character varying,
	dhCampo character varying,
	PRIMARY KEY (id)
);
	
DROP TABLE IF EXISTS obrasInfCompOp;
CREATE TABLE obrasInfCompOp
(
	id SERIAL NOT NULL,
	idObrasInfComp integer,
	idCamposAdicionaisFilho integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS obrasAnexos;
CREATE TABLE obrasAnexos
(
	id SERIAL NOT NULL,
	idObra integer,
	descricao character varying,
    nomeArquivo character varying,
	tipoArquivo character varying,
	s3Key character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS obrasImagens;
CREATE TABLE obrasImagens
(
	id SERIAL NOT NULL,
	idObra integer,
	descricao character varying,
	nomeArquivo character varying,
	tipoArquivo character varying,
	s3Key character varying,
	s3KeyThumbnail character varying,
	principal boolean,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS obrasMovimentacoes;
CREATE TABLE obrasMovimentacoes
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idObra integer,
	dhMovimentacao character varying,
    observacao character varying,
	usuarioMovimentacao character varying,
	usuariosDestino character varying,
	name character varying,
	tipoMovimentacao character varying,
	status character varying,
	statusRotulo character varying,
	statusIcone character varying,
	statusCor character varying,
	estornado character varying,
	statusEstornado character varying,
	statusEstornadoRotulo character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS obrasResponsavelExecucao;
CREATE TABLE obrasResponsavelExecucao
(
	id SERIAL NOT NULL,
	idObra integer,
	idContribuinte integer,
	idContribuinteSecundario integer,
	idConstrutora integer,
	dtValidade character varying,
	obraResponsavelExecucaoLiderConsorcios character varying,
	idContribuinte integer,
	tipoResponsavel character varying,
	PRIMARY KEY (id)	
);

DROP TABLE IF EXISTS obrasResponsavelExecucaoLiderConsorcio;
CREATE TABLE obrasResponsavelExecucaoLiderConsorcio
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idObraResponsavelExecucao integer,
    idContribuinte integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS pagamentos;
CREATE TABLE pagamentos
(
	id SERIAL NOT NULL,
	idGuiasUnificadas integer,
    idPessoas integer,
    idBaixaManual character varying,
    idBaixaAutomatica integer,
    idConvenio integer,
    idGuia integer,
    idDivida integer,
    idParcelamentoParcela integer,
    idMotivoEstorno integer,
    numeroBaixa integer,
    dtPagamento character varying,
    dhEstorno character varying,
    dtCredito character varying,
    dtPagamentoRetroativo character varying,
    tipoBaixa character varying,
    tipoPagamento character varying,
    vlPago double precision,
    vlCorrecao double precision,
    vlJuro double precision,
    vlMulta double precision,
    vlJuroFinanciamento double precision,
    vlCorrecaoPreFixada double precision,
    vlDiferenca double precision,
    vlDescontoTributo double precision,
    vlDescontoCorrecao double precision,
    vlDescontoJuro double precision,
    vlDescontoMulta double precision,
    vlTributoDevido double precision,
    vlCorrecaoDevido double precision,
    vlJuroDevido double precision,
    vlMultaDevido double precision,
    vlJuroFinanciamentoDevido double precision,
    vlCorrecaoPreFixadaDevido double precision,
    vlTributoPago double precision,
    usuarioEstorno character varying,
    quitadoPorLimiteArrecadacao boolean,
    saldoGerado boolean,
    saldoUtilizado boolean,
    situacaoSaldoAnterior character varying,
    situacaoSaldoAtual character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS pagamentosDetalhados;
CREATE TABLE pagamentosDetalhados
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idPagamento integer,
    tipoReceitaPagamento character varying,
    idGuia integer,
    idDivida integer,
    idParcelamentoParcela integer,
    idReceita integer,
    valorAnistiadoCorrecao double precision,
    valorPagoIndexador double precision,
    valorAnistiadoJuros double precision,
    valorAnistiadoLancado double precision,
    valorAnistiadoMulta double precision,
    valorDescontoConcedidoCorrecao double precision,
    valorDescontoConcedidoJuros double precision,
    valorDescontoConcedidoLancado double precision,
    valorDescontoConcedidoMulta double precision,
    valorDescontoCorrecao double precision,
    valorDescontoJuros double precision,
    valorDescontoLancado double precision,
    valorDescontoMulta double precision,
    valorDevidoCorrecao double precision,
    valorDevidoJuros double precision,
    valorDevidoLancado double precision,
    valorDevidoMulta double precision,
    valorDiferencaCorrecao double precision,
    valorDiferencaJuros double precision,
    valorDiferencaMulta double precision,
    valorDiferencaTributo double precision,
    valorPagoCorrecao double precision,
    valorPagoCorrecaoParcelada double precision,
    valorPagoJuros double precision,
    valorPagoJurosParcelado double precision,
    valorPagoLancado double precision,
    valorPagoMulta double precision,
    valorPagoMultaParcelada double precision,
    valorRemidoCorrecao double precision,
    valorRemidoJuros double precision,
    valorRemidoLancado double precision,
    valorRemidoMulta double precision,
    valorDevidoJuroParcelado double precision,
    valorDevidoMultaParcelado double precision,
    valorDevidoCorrecaoParcelado double precision,
    outrosDescCorrecao double precision,
    outrosDescJuros double precision,
    outrosDescMulta double precision,
    outrosDescLancado double precision,
    complementar character varying,
    ano character varying,
    idImovel integer,
    idEconomico integer,
    idReceitaDiversa integer,
    idReceitaDiversaLanctos integer,
    idTransfImoveis integer,
    idNotaAvulsa integer,
    idContribuicaoMelhorias integer,
    idContribuicaoMelhoriasImoveis integer,
    idCreditoTributario integer,
    idPessoas integer,
    idObras integer,
    dataVcto character varying,
    dataVctoOriginalv character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS pagamentosInconsistencias;
CREATE TABLE pagamentosInconsistencias
(
	id SERIAL NOT NULL,
	idPagamento integer,
	mensagem character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS pagamentosReceitas;
CREATE TABLE pagamentosReceitas
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idCreditosTributariosRec integer,
	idPagamento integer,
	vlTributoDevido double precision,
	vlCorrecaoDevido double precision,
	vlJuroDevido double precision,
	vlMultaDevido double precision,
	vlTributoPago double precision,
	vlCorrecao double precision,
	vlJuro double precision,
	vlMulta double precision,
	vlDescontoTributo double precision,
	vlDescontoCorrecao double precision,
	vlDescontoJuro double precision,
	vlDescontoMulta double precision,
	vlBeneficios double precision,
	vlDiferenca double precision,
	vlPago double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS parcelamentos;
CREATE TABLE parcelamentos
(
	id SERIAL NOT NULL,
	idPessoas integer,
	idConfigParcelamentos integer,
	nroParcelamento integer,
	situacao character varying,
	vlRendaFamiliar double precision,
	dhParcelamento character varying,
	tipoEntrada character varying,
	vlEntrada double precision,
	percEntrada double precision,
	dtVencimento character varying,
	intervaloVencimento character varying,
	intervalo integer,
	qtdParcela integer,
	qtdParcelaOriginal integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS parcelamentosCancelados;
CREATE TABLE parcelamentosCancelados
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idParcelamentos integer,
    idMotivos integer,
	comentario character varying,
    dhCancelamento character varying,    
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS parcelamentosComposicoes;
CREATE TABLE parcelamentosComposicoes
(
	id SERIAL NOT NULL,
	idParcelamentos integer,
	idParcelamentosAnt integer,
	idGuias integer,
	idDividas integer,
	idReceitas integer,
	valorReceita double precision,
	valorCorrecao double precision.
	valorJuro double precision,
	valorMulta double precision,
	valorDescontoReceita double precision,
	valorDescontoCorrecao double precision,
	valorDescontoJuro double precision,
	valorDescontoMulta double precision,
	valorRemissaoReceita double precision,
	valorAnistiaReceita double precision,
	valorAnistiaCorrecao double precision,
	valorAnistiaJuro double precision,
	valorAnistiaMulta double precision,		
	valor character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS parcelamentosCompOrigem;
CREATE TABLE parcelamentosCompOrigem
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idParcelamentos integer,
    idParcelamentosAnt integer,
    idGuias integer,
	idDividas integer,
	idReceitas integer,
	valorReceita double precision,
	valorCorrecao double precision,
	valorJuro double precision,
	valorMulta double precision,
	valorDescontoReceita double precision,
	valorDescontoCorrecao double precision,
	valorDescontoJuro double precision,
	valorDescontoMulta double precision,
	valorRemissaoReceita double precision,
	valorAnistiaReceita double precision,
	valorAnistiaCorrecao double precision,
	valorAnistiaJuro double precision,
	valorAnistiaMulta double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS parcelamentosOrdens;
CREATE TABLE parcelamentosOrdens
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idParcelamentos integer,
    idGuias integer,
    idDividas integer,
	vlParcelado double precision,
	vlPago double precision,
	vlSaldo double precision,
	ordem integer,	
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS parcelamentosOrdensRec;
CREATE TABLE parcelamentosOrdensRec
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idParcelamentos integer,
    idGuias integer,
    idDividas integer,
    idReceitas integer,
    vlTributo double precision,
    vlCorrecao double precision,
    vlJuro double precision,
    vlMulta double precision,
    vlDescontoTributo double precision,
    vlDescontoCorrecao double precision,
    vlDescontoJuro double precision,
    vlDescontoMulta double precision,
    vlPagoTributo double precision,
    vlPagoCorrecao double precision,
    vlPagoJuro double precision,
    vlPagoMulta double precision,
    vlPagoDescontoTributo double precision,
    vlPagoDescontoCorrecao double precision,
    vlPagoDescontoJuro double precision,
    vlPagoDescontoMulta double precision,
    vlSaldoTributo double precision,
    vlSaldoCorrecao double precision,
    vlSaldoJuro double precision,
    vlSaldoMulta double precision,
    vlSaldoDescontoTributo double precision,
    vlSaldoDescontoCorrecao double precision,
    vlSaldoDescontoJuro double precision,
    vlSaldoDescontoMulta double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS parcelamentosParcelas;
CREATE TABLE parcelamentosParcelas
(
	id SERIAL NOT NULL,
	idParcelamentos integer,
    nroParcela integer,
    dtVctoOriginal character varying,
    dtVcto character varying,
    situacao character varying,
    vlParcela double precision,
    vlDesconto double precision,
    valorDescontoTributo double precision,
    valorDescontoCorrecao double precision,
    valorDescontoJuro double precision,
    valorDescontoMulta double precision,
    vlReforco double precision,
    vlCorrPrefixada integer,
    vlJuroFinanciamento double precision,
    vlTotalTaxa double precision,
    possuiReforco character varying,
    iParcelamentos integer,
    parcelaConversao integer,
    tipoParcelamentoConversao character varying,    
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS parcelamentosParcTaxas;
CREATE TABLE parcelamentosParcTaxas
(
	id SERIAL NOT NULL,
	idParcelas integer,
	idCreditosTributarios integer,
	taxaAutomatica character varying,
	vlTaxa double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS parcelamentosReferentes;
CREATE TABLE parcelamentosReferentes
(
	id SERIAL NOT NULL,
	idParcelamentos integer,
	idReferente integer,
	tipoCadastro character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS parcelamentosCreditos;
CREATE TABLE parcelamentosCreditos
(
	id SERIAL NOT NULL,
	idCreditosTributarios integer,
	idParcelamentos integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS pessoas;
CREATE TABLE pessoas
(
	id SERIAL NOT NULL,
	cpfCnpj character varying,
	idPessoas integer,
	idEnderecoPrincipal integer,
	inscricaoMunicipal character varying,
	nome character varying,
	nomeFantasia character varying,
	site character varying,
	situacao character varying,
	situacao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS pessoasAnexos;
CREATE TABLE pessoasAnexos
(
	id SERIAL NOT NULL,
	idPessoas integer,
	descricao character varying,
	tipoArquivo character varying,
	nomeArquivo character varying,
	idPessoasMovimentacoes integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS pessoasContasBancos;
CREATE TABLE pessoasContasBancos
(
	id SERIAL NOT NULL,
	dtAbertura character varying,
	dtEncerramento character varying,
	dvConta integer,
	idAgenciasBancarias integer,
	idBancos integer,
	idPessoas integer,
	nroConta integer,
	ordem integer,
	principal character varying,
	status character varying,
	tipoConta character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS pessoasEmails;
CREATE TABLE pessoasEmails
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    descricao character varying,
	email character varying,
    idPessoas integer,
    ordem integer,
    principal character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS pessoasEnderecos;
CREATE TABLE pessoasEnderecos
(
	id SERIAL NOT NULL,
	idPessoa integer,
	idCondominio integer,
	idLogradouro integer,
	idLoteamento integer,
	idBairro integer,
	idDistrito integer,
	idMunicipio integer,
	idEstado integer,	
	principal character varying,
	ordem integer,
	cep integer,
	apartamento integer,
	descricao character varying,
	cep character varying,
	numero integer,
	complemento character varying,
	bloco character varying,
	observacao character varying,
	latitude character varying,
	longitude character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS pessoasEstrangeiras;
CREATE TABLE pessoasEstrangeiras
(
	id SERIAL NOT NULL,
	idPessoas integer,
	dtChegada character varying,
	dtExpedicao character varying,
	dtValidade character varying,
	nroIdentidade integer,
	orgaoEmissor character varying,
	tipoVisto character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS pessoasEventosSimplesNacional;
CREATE TABLE pessoasEventosSimplesNacional
(
	id SERIAL NOT NULL,
	idPessoaJuridica integer,
	optante character varying,
	dataInicio character varying,
	dataFinal character varying,
	dataEfeito character varying,
	processo character varying,
	responsavel character varying,
	dataOcorrencia character varying,
	descricao character varying,
	comentario character varying,
	PRIMARY KEY (id)
);
        
DROP TABLE IF EXISTS pessoasFisicas;
CREATE TABLE pessoasFisicas
(
	id SERIAL NOT NULL,
	dtNascimento character varying,
	dtObito character varying,
	estadoCivil character varying,
	idMunicipio integer,
	idPais integer,
	idPessoas integer,
	naturalizado character varying,
	sexo character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS pessoasFisicasDocumentos;
CREATE TABLE pessoasFisicasDocumentos
(
	id SERIAL NOT NULL,
	idPessoas integer,
	idEstadoRg integer,
	idEstadoRic integer,
	dtEmissaoRg character varying,
	dtEmissaoRic character varying,
	dtEmissaoPisPasep character varying,
	nroRg character varying,
	nroRic character varying,
	pisPasep character varying,
	orgaoEmissorRg character varying,
	orgaoEmissorRic character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS pessoasFisicasFiliacoes;
CREATE TABLE pessoasFisicasFiliacoes
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idPessoa integer,
    idPessoasFiliacao integer,
    naturezaFiliacao character varying,
	tipoFiliacao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS pessoasImagens;
CREATE TABLE pessoasImagens
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idPessoas integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS pessoasInfComplem;
CREATE TABLE pessoasInfComplem
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	ano integer,
    idCampoAdicional integer,
    idCampoAdicionalFilho integer,
	idAgrupamento integer,
	iInformacoesComplementares integer,
	idPessoa integer,
	dhCampo character varying,
	texto character varying,
	vlCampo double precision,
    areaTexto character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS pessoasInfComplemOp;
CREATE TABLE pessoasInfComplemOp
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idCampoAdicionalFilho integer,
	idPessoaInfComplem integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS pessoasJuridicas;
CREATE TABLE pessoasJuridicas
(
	id SERIAL NOT NULL,
	idPessoas integer,
	dtRegistro character varying,
	idNaturezaJuridica integer,
	orgaoRegistro character varying,
	porteEmpresa character varying,
	idQualificacao integer,
	idResponsavel integer,
	inscricaoEstadual character varying,
	isentoInscricao character varying,
	nroRegistro character varying,
	optanteSimples character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS pessoasJuridicasSocios;
CREATE TABLE pessoasJuridicasSocios
(
	id SERIAL NOT NULL,
	dtDesligamento character varying,
	dtInclusao character varying,	
	idPessoa integer,
	idQualificacoesResponsaveis integer,
	idQualificacoesSocios integer,
	idResponsavelLegal integer,
	idSocio integer,
	percSociedade double precision,
	PRIMARY KEY (id)
);
        
DROP TABLE IF EXISTS pessoasMovimentacoes;
CREATE TABLE pessoasMovimentacoes
(
	id SERIAL NOT NULL,
	audCriadoPor character varying,
	audDhCriacao character varying,
	audAlteradoPor character varying,
	audDhAlteracao character varying,
	idPessoa integer,
	tipoMovimentacao character varying,
	situacao character varying,
	descricao character varying,
	nroProcesso integer,
	dhMovimentacao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS pessoasMovtosMEI;
CREATE TABLE pessoasMovtosMEI
(
	id SERIAL NOT NULL,
	idPessoa integer,
	idMotivos integer,
	optante character varying,
	dtInicio character varying,
	dtEfeito character varying,
	comentario character varying,
	orgao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS pessoasMovtosSimplesNacional;
CREATE TABLE pessoasMovtosSimplesNacional
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idPessoaJuridica integer,
	optante character varying,
    dtInicio character varying,
    idMotivos integer,
    comentario character varying,
    orgao character varying,
    dtEfeito character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS pessoasTelefones;
CREATE TABLE pessoasTelefones
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	idPessoa integer,
    descricao character varying,
	tipo character varying,
	principal character varying,
	ordem integer,
	numero integer,
	observacao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS plantasValores;
CREATE TABLE plantasValores
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idBairros integer,
    idDistritos integer,
    idFaces integer,
	idIndexadores integer,
	idLogradouros integer,
	idSecoes integer,
	idAtos integer,
	ano integer,
    vlMetroQuadrado double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS qualificacoes;
CREATE TABLE qualificacoes
(
	id SERIAL NOT NULL,	
	descricao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS qualificacoesResponsaveis;
CREATE TABLE qualificacoesResponsaveis
(
	id SERIAL NOT NULL,
	idQualificacao integer,
	idNaturezaJuridica integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS qualificacoesSocios;
CREATE TABLE qualificacoesSocios
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idQualificacao integer,
	idNaturezaJuridica integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS receitas;
CREATE TABLE receitas
(
	id SERIAL NOT NULL,
	idAtoExecucaoFiscal integer,
	idAtoInscrito integer,
    idAtoNaoInscrito integer,
	descricao character varying,
	abreviatura character varying,
	codigoTCE integer,
	classificacao character varying,
	tipoVinculoAtoInscrito character varying,
	tipoVinculoAtoNaoInscrito character varying,
	inscDividaAtiva boolean,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS receitasAtosHist;
CREATE TABLE receitasAtosHist
(
	id SERIAL NOT NULL,
	idReceita integer,
	idAto integer,
    tipoAtoReceita character varying,
	tipoVinculo character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS receitasDiversas;
CREATE TABLE receitasDiversas
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idCreditoTributario integer,
    idEconomico integer,
	idImovel integer,
    idPessoa integer,
	idTipoServico integer,
	nroProcesso character varying,
    comentarioServico character varying,
    dtReceitaDiversa character varying,
    descricaoServico character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS receitasDiversasInfComp;
CREATE TABLE receitasDiversasInfComp
(
	id SERIAL NOT NULL,
	idCamposAdicionais integer,
	idReceitaDiversa integer,
	areaTexto character varying,
	texto character varying,
	dhCampo character varying,
	vlCampo double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS receitasDiversasInfCompOp;
CREATE TABLE receitasDiversasInfCompOp
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idReceitasDiversasInformacoesComplementares integer,
	idCamposAdicionais integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS receitasDiversasLanctos;
CREATE TABLE receitasDiversasLanctos
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idReceitaDiversa integer,
	qtdDiasMeses integer,
    qtdParcelas integer,
	dtCriacao character varying,
	dtVcto character varying,
	observacao character varying,
    totalLancado integer,
    intervaloVenctos character varying,
    situacao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS receitasDiversasLanctosRec;
CREATE TABLE receitasDiversasLanctosRec
(
	id SERIAL NOT NULL,
	idReceita integer,
	idReceitasDiversasLanctos integer,
	valorLancado double precision,
	PRIMARY KEY (id)
);
	
DROP TABLE IF EXISTS receitasDiversasMovtos;
CREATE TABLE receitasDiversasMovtos
(
	id SERIAL NOT NULL,
	idReceitaDiversa integer,
	descricao character varying,
	tipoMovimentacao character varying,
	dhMovimentacao character varying,
	usuarioMovimentacao character varying,
	valor double precision,
	PRIMARY KEY (id)
);
	
DROP TABLE IF EXISTS referentesCnaes;
CREATE TABLE referentesCnaes
(
	id SERIAL NOT NULL,
	idAtividade integer,
	idManutCalcReferentes integer,
	PRIMARY KEY (id)
);
		
DROP TABLE IF EXISTS referentesListaServicos;
CREATE TABLE referentesListaServicos
(
	id SERIAL NOT NULL,
	idServico integer,
	idManutCalcReferentes integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS registrosTabaux;
CREATE TABLE registrosTabaux
(
	id SERIAL NOT NULL,
	iTabelaAuxiliar integer,
	idTabelaAuxiliar integer,
    campo1 character varying,
	campo2 character varying,
	campo3 character varying,
	campo4 character varying,
	campo5 character varying,
	campo6 character varying,
	campo7 character varying,
	campo8 character varying,
	campo9 character varying,
	campo10 character varying,
	PRIMARY KEY (id)
);
	
DROP TABLE IF EXISTS relacaoTiposServicoCreditosTributarios;
CREATE TABLE relacaoTiposServicoCreditosTributarios
(
	id SERIAL NOT NULL,
	idAgrupamentos integer,
	idCreditoTributario integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS remembramentos;
CREATE TABLE remembramentos
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idAgrupamentos integer,
    idEngenheirosArquitetos integer,
    idPessoas integer,
    codArtRrt integer,
    nroProcesso integer,
	nroProcessoCancelamento integer,
    observacao character varying,
    dhAprovacao character varying,
    dhCancelamento character varying,
    situacao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS remembramentosDocumentos;
CREATE TABLE remembramentosDocumentos
(
	id SERIAL NOT NULL,
	idRemembramentos integer,
	tipoArquivo character varying,
	nomeArquivo character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS remembramentosImoveis;
CREATE TABLE remembramentosImoveis
(
	id SERIAL NOT NULL,
	idAgrupamentos integer,
	idImoveis integer,
	idRemembramentos integer,
	unidade integer,
	unidadeAnt integer,
	matricula integer,
	matriculaAnt integer,
	setor character varying,
	setorAnt character varying,
	quadra character varying,
	quadraAnt character varying,
	lote character varying,
	loteAnt character varying,
	principal character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS remembramentosImoveisInfComplem;
CREATE TABLE remembramentosImoveisInfComplem
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    ano integer,
    idCamposAdicionais integer,
    idCamposAdicionaisFilho integer,
    idRemembramentosImoveis integer,
    idAgrupamentos integer,
    idImoveis integer,
	idRemembramentos integer,
    dhCampo character varying,
	texto character varying,
	vlCampo double precision,
	areaTexto character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS remembramentosImoveisInfComplemOp;
CREATE TABLE remembramentosImoveisInfComplemOp
(
	id SERIAL NOT NULL,
	idRemembramentosImoveisInfComplem integer,
	idCamposAdicionaisFilho integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS remembramentosInfComplem;
CREATE TABLE remembramentosInfComplem
(
	id SERIAL NOT NULL,
	idCamposAdicionais integer,
	idCamposAdicionaisFilho integer,
	areaTexto character varying,
	idRemembramentos integer,
	idAgrupamentos integer,
	dhCampo character varying,
	texto character varying,
	vlCampo double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS remembramentosInfComplemOp;
CREATE TABLE remembramentosInfComplemOp
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idRemembramentosInfComplem integer,
    idCamposAdicionaisFilho integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS remissoes;
CREATE TABLE remissoes
(
	id SERIAL NOT NULL,
	idDividas integer,
	idDividasMovtos integer,
	idDividasReceitas integer,
	idHomologManutencao integer,
	percRemissao double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS restituicoes;
CREATE TABLE restituicoes
(
	id SERIAL NOT NULL,
	idSaldo integer,
	idReceita integer,
	idPagamentosDetalhados integer,
	vlSaldo double precision,
	vlRestituir double precision,
	vlJuro double precision,
	vlCorrecao double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS saldos;
CREATE TABLE saldos
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idSaldoOrigem integer,
    idSaldo integer,
    idPessoa integer,
    idPagamentos integer,
    idManutencaoPagamento integer,
    comentario character varying,
	nroProcesso integer,
	observacoes character varying,
	dtSaldo character varying,
	dtValidade character varying,
	vlSaldoTotal double precision,
	vlSaldoUtilizado double precision,
	situacao character varying,
	tipoInconsistencia character varying,
	tipoSaldo character varying,
	tipoUtilizacaoSaldo character varying,
	utilizado character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS simulacoes;
CREATE TABLE simulacoes
(
	id SERIAL NOT NULL,
	anoInicial integer,
	anoFinal integer,
	nroDiasVencidos integer,
	nroLivro integer,
	nroFolha integer,
	nroPosicao integer,
	anoLivro integer,
	qtdTotalCreditos integer,
	qtdInconsistentes integer,
	filtroCreditos character varying,
	filtroPessoas character varying,
	filtroImoveis character varying,
	filtroEconomicos character varying,
	filtroReceitasDiversas character varying,
	filtroContribMelhorias character varying,
	filtroNotasAvulsas character varying,
	filtroSerieNotas character varying,
	ordemInscricao character varying,
	dhSimulacao character varying,
	dtVctoInicial character varying,
	dtVctoFinal	character varying,
	dtInscricao character varying,
	vlTotalCreditos double precision,
	situacao character varying,
	tipoIntervalo character varying,
	criterioFormaPagamento character varying,
	novoLivro character varying,
	PRIMARY KEY (id)
);
   
DROP TABLE IF EXISTS tabelasAuxiliares;
CREATE TABLE tabelasAuxiliares
(
	id SERIAL NOT NULL,
	campos integer,
	tipo character varying,
	descricao character varying,
	exibe boolean,
	tamanho character varying,
	exibirNoEconomico boolean,
	principalConfigEconomico boolean,
	descricao character varying,
	idTabelaAuxiliar integer,	
	desativadaConfigEconomico boolean,
	inseridaConfigEconomico boolean,
	PRIMARY KEY (id)
);
    
DROP TABLE IF EXISTS tabelasCalculos;
CREATE TABLE tabelasCalculos
(
	id SERIAL NOT NULL,
	descricao character varying,
	idTabelasCalculos integer,
	ano integer,
	origemCampos character varying,
	situacao character varying,	
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS tabelasCalculosCampos;
CREATE TABLE tabelasCalculosCampos
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idCamposAdicionais integer,
    idTabelasCalculos integer,
    descricao character varying,    
    atributo character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS tabelasConjuntos;
CREATE TABLE tabelasConjuntos
(
	id SERIAL NOT NULL,
	idIndexadores integer,
	idTabelasCalculos integer,
	resultado double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS tabelasConjuntosCampos;
CREATE TABLE tabelasConjuntosCampos
(
	id SERIAL NOT NULL,
	idTabelasCalculosCampos integer,
	idTabelasCalculos integer,
	idTabelasConjuntos integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS tabelasConjuntosValores;
CREATE TABLE tabelasConjuntosValores
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    idTabelasCalculos integer,
    idTabelasConjuntos integer,
    idCamposAdicionais integer,
    idTabelasConjuntosCampos integer,
    id_contrato_rateio integer,
    operadorAcao character varying,
    valor double precision,
    operadorComparacao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS termosParcelamento;
CREATE TABLE termosParcelamento
(
	id SERIAL NOT NULL,
	idContribuinte integer,
    idParcelamento integer,
    idParcelamentoParcela integer,
    nroParcelamento integer,
    idConfigParcelamento integer,
    leiParcelamento integer,
    idCreditoTributario integer,
    idDivida integer,
    idGuia integer,
    idParcelamentoAnterior integer,
    idReceita integer,
    idEnderecoContribuinte integer,
    idTelefoneContribuinte integer,
    nroDocumento integer,
    intervalo integer,
    qtdParcelas integer,
    qtdParcelasOriginal integer,
    nroParcela integer,
    ano integer,
    anoCredito integer,
    nroProcesso integer,
    referente character varying,
    vlRendaFamiliar double precision,
    vlEntrada double precision,
    percEntrada double precision,
    vlCorrecaoPrefixada double precision,
    vlDesconto double precision,
    vlJuroFinanciamento double precision,
    vlParcela double precision,
    vlReforco double precision,
    vlTotalTaxa double precision,
    valorReceita double precision,
    valorDescontoReceita double precision,
    valorCorrecao double precision,
    valorDescontoCorrecao double precision,
    valorJuro double precision,
    valorDescontoJuro double precision,
    valorMultaReceita double precision,
    valorDescontoMulta double precision,
    saldoParcela double precision,
    correcaoParcela double precision,
    juroParcela double precision,
    valorMultaParcela double precision,
    totalAcrescimos double precision,
    situacaoParcelamento character varying,
    tipoEntrada character varying,
    intervaloVencimento character varying,
    possuiReforco character varying,
    situacaoParcela character varying,
    tipoCredito character varying,
    dhParcelamento character varying,
    dtVencimentoParcelamento character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS tiposAtos;
CREATE TABLE tiposAtos
(
	id SERIAL NOT NULL,
	descricao character varying,
	classificacao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS tiposCadastros;
CREATE TABLE tiposCadastros
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    exercicio integer,
    descricao character varying,
    referente character varying,
    utilizado character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS tiposDocumentos;
CREATE TABLE tiposDocumentos
(
	id SERIAL NOT NULL,
	descricao integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS tiposDocumentosDigitais;
CREATE TABLE tiposDocumentosDigitais
(
	id SERIAL NOT NULL,
	descricao character varying,
	codigoTJ integer,
	codigoTJRJ integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS tiposParticipacao;
CREATE TABLE tiposParticipacao
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,    
    codigoTJ integer,
    descricao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS tiposPublicidades;
CREATE TABLE tiposPublicidades
(
	id SERIAL NOT NULL,
	valorBase double precision,
	descricao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS tiposEntidadesEspeciais;
CREATE TABLE tiposEntidadesEspeciais
(
	id SERIAL NOT NULL,
	descricao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS cbos;
CREATE TABLE cbos	
(
	id SERIAL NOT NULL,
	identificador integer,
	descricao character varying,
	nivel character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS cnaes;
CREATE TABLE cnaes
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    nivel integer,
    ordem integer,
    descricao character varying,
    cnae character varying,
    secao character varying,
    grauRisco character varying,
    visivel character varying,
    impeditivoSimples character varying,
    grauRiscoMei character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS listaServicos;
CREATE TABLE listaServicos
(
	id SERIAL NOT NULL,
	descricao character varying,
    itemLista character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS tiposLogradouros;
CREATE TABLE tiposLogradouros
(
	id SERIAL NOT NULL,
	abreviatura character varying,	
    descricao character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS transferenciaImoveis;
CREATE TABLE transferenciaImoveis	
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
    codigo integer,
	idPagador integer,
    dtCadastro character varying,
    dtVencimento character varying,
    dtTransferencia character varying,
	formaTransf character varying,
	lancamentoGerado character varying,
	statusCertidaoITBI character varying,
	situacao character varying,
	tipoCobranca character varying,
	tipoImovel character varying,
    anoTransferencia integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS transfImoveisItens;
CREATE TABLE transfImoveisItens
(
	id SERIAL NOT NULL,
	idArrematante integer,
    idCartorios integer,
    idImoveis integer,
    idLocalidades integer,
    idMotivos integer,
    idPagadores integer,
    idProprietario integer,
    idTransferenciaImoveis integer,
    denominacao character varying,
    dtArrematacao character varying,
    inscricaoIncra character varying,
    obsArrematacao character varying,
    vlAreaConstruidaUnidade double precision,
    vlAreaTotalTerrenoUnidade double precision,
    vlArrematacao double precision,
    vlVenalBenfeitoriasUnidade double precision,
    vlVenalConstruidoUnidade double precision,
    vlVenalTerritorialUnidade double precision,
    vlVenalUnidade double precision,
    percAvista double precision,
    percBenfeitoria double precision,
    percFinanciado double precision,
    percOutros double precision,
    benfeitorias character varying,
    definicaoPagador character varying,
    financiado character varying,
    outros character varying,
    tipoVenda character varying,
    unidadeFutura character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS transfImoveisItensAnexos;
CREATE TABLE transfImoveisItensAnexos
(
	id SERIAL NOT NULL,
	idTransfImoveisItens integer,
	nomeArquivo character varying,
    tipoArquivo character varying,
	comentario character varying,
	PRIMARY KEY (id)
);
	
DROP TABLE IF EXISTS transfImoveisItensCompra;
CREATE TABLE transfImoveisItensCompra
(
	id SERIAL NOT NULL,
	idComprador integer,
	idTransfImoveisItensVenda integer,
	percCompra double precision,
	vlAreaConstruida double precision,
	vlAreaTerreno double precision,
	vlBenfeitorias double precision,
	vlDeclarado double precision,
	vlFinanciado double precision,
	vlItbi double precision,
	vlOutros double precision,
	vlVendaAVista double precision,
	transferido character varying,
	PRIMARY KEY (id)
);
        
DROP TABLE IF EXISTS transfImoveisItensProcessos;
CREATE TABLE transfImoveisItensProcessos
(
	id SERIAL NOT NULL,
	idTransfImoveisItens integer,
	nroProcesso integer,
	comentario character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS transfImoveisItensVenda;
CREATE TABLE transfImoveisItensVenda
(
	id SERIAL NOT NULL,
	idPessoas integer,
	idTransfImoveisItens integer,
    percVenda double precision,
	qtdCompradores integer,
    vlAreaConstruidaUnidade double precision,
	vlAreaTotalTerrenoUnidade double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS unidadesMedidas;
CREATE TABLE unidadesMedidas
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,    
    nome character varying,    
	simbolo character varying,
    nomePlural character varying,
    grandeza character varying,
	fracionaria character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS arquivos;
CREATE TABLE arquivos
(
	id SERIAL NOT NULL,
	cancelado boolean,
	idContribuinte integer,
	idParcelamento integer,
	classificacaoCertidao integer,
	protocoloExecucao character varying,
	dtValidade character varying,
	descricao character varying,
	informacoesComplementares character varying,
	dhCancelamento character varying,
	dhEmissao character varying,
	natureza character varying,
	nome character varying,
	nroDocumento integer,
	referente character varying,
	identificador integer,
	tipoCadastro character varying
	tipo character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS lancamentoCreditoSimAm;
CREATE TABLE lancamentoCreditoSimAm
(
	id SERIAL NOT NULL,	
	chaveUnificada character varying,
	chave character varying,
	tabela character varying,
	cdCadastro integer,
	codigoTceReceita integer,
	nrOperacao integer,
	nrAnoOperacao integer,
	idPessoa integer,
	idTipoNaturezaCredito integer,
	idTipoCredito integer,
	idTipoOperacaoCredito integer,
	dtLancamento character varying,
	nrMesBase integer,
	nrAnoBase integer,
	cdControleLeiAto integer,
	vlLancamento double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS estornoLancamentoCreditoSimAm;
CREATE TABLE estornoLancamentoCreditoSimAm
(
	id SERIAL NOT NULL,
	chaveUnificada character varying,
	chave character varying,
	tabela character varying,
	cdCadastro integer,
	codigoTceReceita integer,
	nrOperacao integer,
	nrAnoOperacao integer,
	idPessoa integer,
	nrCredito integer,
	nrAnoCredito integer,
	dtEstorno character varying,
	cdControleLeiAto integer,
	vlEstorno double precision,
	dsMotivo character varying,
	PRIMARY KEY (id)
);
      
DROP TABLE IF EXISTS atualizacaoMonetariaSimAm;
CREATE TABLE atualizacaoMonetariaSimAm
(
	id SERIAL NOT NULL,
	chaveUnificada character varying,
	chave character varying,
	tabela character varying,
	idPagamento integer,
	idTipoAtualizacaoCredito integer,
	codigoTceReceita integer,
	nrOperacao integer,
	nrAnoOperacao integer,
	idPessoa integer,
	nrCredito integer,
	nrAnoCredito integer,
	dtOperacao character varying,
	cdControleLeiAto integer,
	vlOperacao double precision,
	idTipoAtualizacaoCredito integer,
	PRIMARY KEY (id)
);
    
DROP TABLE IF EXISTS estornoAtualizacaoMonetariaSimAm;
CREATE TABLE estornoAtualizacaoMonetariaSimAm
(
	id SERIAL NOT NULL,
	chaveUnificada character varying,
	chave character varying,
	tabela character varying,
	idPagamento integer,
	idTipoAtualizacaoCredito integer,
	codigoTceReceita integer,
	nrOperacao integer,
	nrAnoOperacao integer,
	idPessoa integer,
	nrAtualizacao integer,
	nrAnoAtualizacao integer,	
	dsMotivo character varying,
	dtOperacao character varying,
	cdControleLeiAto integer,
	vlOperacao double precision,
	idTipoAtualizacaoCredito integer,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS deducaoCreditoSimAm;
CREATE TABLE deducaoCreditoSimAm
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	chaveUnificada character varying,
    chave character varying,
    tabela character varying,
    cdCadastro integer,
    tipoDeducao character varying,
    codigoTce integer,
    nrOperacao integer,
    nrAnoOperacao integer,
    idPessoa integer,
    nrCredito integer,
    nrAnoCredito integer,
    dtOperacao character varying,
    cdControleLeiAto integer,
    vlOperacao double precision,
    tipoDeducao character varying,
    dsMotivo character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS estornoDeducaoCreditoSimAm;
CREATE TABLE estornoDeducaoCreditoSimAm
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	chaveUnificada character varying,
    chave character varying,
    tabela character varying,
    cdCadastro integer,
    tipoDeducao character varying,
    codigoTce integer,
    nrOperacao integer,
    nrAnoOperacao integer,
    idPessoa integer,
    nrDeducao integer,
    nrAnoCredito integer,
    dtOperacao character varying,
    cdControleLeiAto integer,
    vlOperacao double precision,
    dsMotivo character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS inscricaoDividaSimAm;
CREATE TABLE inscricaoDividaSimAm
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	chaveUnificada character varying,
    chave character varying
    tabela character varying,
    cdCadastro integer,
    codigoTceReceita integer,
    nrOperacao integer,
    nrCredito integer,
    nrAnoOperacao integer,
    idPessoa integer,
    idTipoNaturezaCredito character varying,
    idTipoCredito character varying,
    idTipoOperacaoCredito character varying,
    dtInscricao character varying,
    nrAnoBase integer,
    nrAnoInscricao integer,
    nrAnoCredito integer,
    cdControleLeiAto integer,
    vlInscricao double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS estornoInscricaoDividaSimAm;
CREATE TABLE estornoInscricaoDividaSimAm
(
	id SERIAL NOT NULL,
	chaveUnificada character varying,
    chavecharacter varying,
    tabela character varying,
    cdCadastro integer,
    codigoTceReceita integer,
    nrOperacao integer,
    nrAnoOperacao integer,
    idPessoa integer,
    nrDivida integer,
    nrAnoDivida integer,
    cdControleLeiAto integer,
    dtEstorno character varying,
    vlEstorno double precision,
    dsMotivo character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS atualizacaoDividaAtivaSimAm;
CREATE TABLE atualizacaoDividaAtivaSimAm
(
	id SERIAL NOT NULL,
	chaveUnificada character varying,
    chave character varying,
    tabela character varying,
    idPagamento integer,
    codigoTceReceita integer,
    idTipoAtualizacaoCredito integer,
    nrOperacao integer,
    nrAnoOperacao integer,
    nrDivida integer,
    nrAnoDivida integer,
    idPessoa integer,
    idTipoAtualizacaoCredito integer,
    dtAtualizacao character varying,
    cdControleLeiAto integer,
    vlAtualizacao double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS estornoAtualizacaoDividaAtivaSimAm;
CREATE TABLE estornoAtualizacaoDividaAtivaSimAm
(
	id SERIAL NOT NULL,
	chaveUnificada character varying,
    chave character varying,
    tabela character varying,
    idPagamento integer,
    codigoTceReceita integer,
    idTipoAtualizacaoCredito integer,
    nrOperacao integer,
    nrAnoOperacao integer,
    nrAtualizacao integer,
    nrAnoAtualizacao integer,
    idPessoa integer,
    dtEstorno integer,
    cdControleLeiAto integer,
    vlEstorno double precision,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS deducaoDividaSimAm;
CREATE TABLE deducaoDividaSimAm
(
	id SERIAL NOT NULL,
	chaveUnificada character varying,
    chave character varying,
    tabela character varying,
    cdCadastro integer,
    tipoDeducao character varying,
    codigoTce integer,
    nrOperacao integer,
    nrAnoOperacao integer,
    idPessoa integer,
    nrDivida integer,
    nrAnoDivida integer,
    dtOperacao character varying,
    cdControleLeiAto integer,
    vlOperacao double precision,
    tipoDeducao character varying,
    dsMotivo character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS estornoDeducaoDividaSimAm;
CREATE TABLE estornoDeducaoDividaSimAm
(
	id SERIAL NOT NULL,
	id_origem integer,
	id_cloud integer,
	chaveUnificada character varying,
    chavecharacter varying,
    tabela character varying,
    cdCadastro integer,
    tipoDeducao character varying,
    codigoTce integer,
    nrOperacao integer,
    nrAnoOperacao integer,
    idPessoa integer,
    nrDeducao integer,
    nrAnoDeducao integer,
    dtOperacao character varying,
    cdControleLeiAto integer,
    vlOperacao double precision,
    dsMotivo character varying,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS sisobra;
CREATE TABLE sisobra
(
	id SERIAL NOT NULL,
	idObra integer,
    tipoArea character varying,
    tipoAreaComplementar character varying,
    categoria character varying,    
    destinacao character varying,
    tipoObra character varying,
    area double precision,
    areaCoberta double precision,
	areaDescoberta double precision,
	PRIMARY KEY (id)
);