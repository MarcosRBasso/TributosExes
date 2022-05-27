from samples import *
import json

class certidoesNegativas(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idContribuinte, idEconomico, idEconomicoCnae, idEconomicoListaServico, idEnderecoContribuinte, idModelo,
                 idImovel, dataValidade, chaveEmissao, comprovacao, finalidade, nomeRequerente, ressalva, informacoesComplementares, nroDocumento, ano, qtdDeclaracoesAbertoVencidas,
                 qtdDeclaracoesNaoIniciadasVencidas, qtdLanctoInscritosSuspensos, qtdLanctoNaoInscritosAtivos, qtdLanctoNaoInscritosAtivosEnquadramento, 
                 qtdLanctoNaoInscritosAtivosUnidade, qtdLanctoNaoInscritosSuspensos, qtdLanctoNaoInscritosVencer, qtdLanctoNaoInscritosVencidos, qtdLanctoParceladosVencer, 
                 qtdLanctoParceladosVencidos, situacaoCertidaoNegativa, situacaoContribuinte, situacaoEconomico, situacaoImovel, tipoCertidaoNegativa):
        try:
            sql = """
                INSERT INTO certidoesNegativas (                    
                    idIntegracao,                   
                    id_cloud, 
                    idContribuinte,
                    idEconomico,                                               
                    idEconomicoCnae, 
                    idEconomicoListaServico,
                    idEnderecoContribuinte,
                    idModelo,
                    idImovel,
                    dataValidade,
                    chaveEmissao,                    
                    comprovacao,
                    finalidade,
                    nomeRequerente,
                    ressalva,
                    informacoesComplementares,
                    nroDocumento,
                    ano,
                    qtdDeclaracoesAbertoVencidas,
                    qtdDeclaracoesNaoIniciadasVencidas,
                    qtdLanctoInscritosSuspensos,
                    qtdLanctoNaoInscritosAtivos, 
                    qtdLanctoNaoInscritosAtivosEnquadramento, 
                    qtdLanctoNaoInscritosAtivosUnidade, 
                    qtdLanctoNaoInscritosSuspensos, 
                    qtdLanctoNaoInscritosVencer, 
                    qtdLanctoNaoInscritosVencidos, 
                    qtdLanctoParceladosVencer, 
                    qtdLanctoParceladosVencidos, 
                    exibirParece,
                    situacaoContribuinte, 
                    situacaoEconomico, 
                    situacaoImovel, 
                    tipoCertidaoNegativa                   
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idContribuinte)s,
                    %(idEconomico)s,
                    %(idEconomicoCnae)s,
                    %(idEconomicoListaServico)s,
                    %(idEnderecoContribuinte)s,
                    %(idModelo)s,
                    %(idImovel)s,
                    %(dataValidade)s,
                    %(chaveEmissao)s,                    
                    %(comprovacao)s,
                    %(finalidade)s,
                    %(nomeRequerente)s,
                    %(ressalva)s,
                    %(informacoesComplementares)s,
                    %(nroDocumento)s,
                    %(ano)s,
                    %(qtdLanctoInscritosSuspensos)s,
                    %(qtdDeclaracoesNaoIniciadasVencidas)s,                    
                    %(qtdDeclaracoesAbertoVencidas)s,
                    %(qtdLanctoNaoInscritosAtivos)s,
                    %(qtdLanctoNaoInscritosAtivosEnquadramento)s,
                    %(qtdLanctoNaoInscritosAtivosUnidade)s,
                    %(qtdLanctoNaoInscritosSuspensos)s,
                    %(qtdLanctoNaoInscritosVencer)s,
                    %(qtdLanctoNaoInscritosVencidos)s,
                    %(qtdLanctoParceladosVencer)s,
                    %(qtdLanctoParceladosVencidos)s,                    
                    %(exibirParece)s,
                    %(situacaoContribuinte)s, 
                    %(situacaoEconomico)s, 
                    %(situacaoImovel)s, 
                    %(tipoCertidaoNegativa)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idContribuinte = idContribuinte,
                idEconomico = idEconomico,
                idEconomicoCnae = idEconomicoCnae,                               
                idEconomicoListaServico = idEconomicoListaServico,
                idEnderecoContribuinte = idEnderecoContribuinte,
                idModelo = idModelo,                               
                idImovel = idImovel,
                dataValidade = dataValidade,
                chaveEmissao = chaveEmissao,                                               
                comprovacao = comprovacao,
                finalidade = finalidade,                               
                nomeRequerente = nomeRequerente,
                ressalva = ressalva,
                informacoesComplementares = informacoesComplementares,                               
                nroDocumento = nroDocumento,
                ano = ano,
                qtdLanctoInscritosSuspensos = qtdLanctoInscritosSuspensos,
                qtdDeclaracoesNaoIniciadasVencidas = qtdDeclaracoesNaoIniciadasVencidas,
                qtdDeclaracoesAbertoVencidas = qtdDeclaracoesAbertoVencidas,
                qtdLanctoNaoInscritosAtivos = qtdLanctoNaoInscritosAtivos, 
                qtdLanctoNaoInscritosAtivosEnquadramento = qtdLanctoNaoInscritosAtivosEnquadramento, 
                qtdLanctoNaoInscritosAtivosUnidade = qtdLanctoNaoInscritosAtivosUnidade, 
                qtdLanctoNaoInscritosSuspensos = qtdLanctoNaoInscritosSuspensos, 
                qtdLanctoNaoInscritosVencer = qtdLanctoNaoInscritosVencer, 
                qtdLanctoNaoInscritosVencidos = qtdLanctoNaoInscritosVencidos, 
                qtdLanctoParceladosVencer = qtdLanctoParceladosVencer, 
                qtdLanctoParceladosVencidos = qtdLanctoParceladosVencidos, 
                situacaoCertidaoNegativa = situacaoCertidaoNegativa,
                situacaoContribuinte = situacaoContribuinte, 
                situacaoEconomico = situacaoEconomico, 
                situacaoImovel = situacaoImovel, 
                tipoCertidaoNegativa = tipoCertidaoNegativa

            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {certidoesNegativas} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as nomeRequerenter:
            send_log_error(f"nomeRequerente ao inserir o anistias {certidoesNegativas}. {nomeRequerenter}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM certidoesNegativas"
            if not self.query(sql_s):
                send_log_warning(f"certidoesNegativas não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM certidoesNegativas WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as nomeRequerenter:
            send_log_error(f"nomeRequerente ao executar a operação de exclusão do atividades econômicas. {nomeRequerenter}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM certidoesNegativas WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    certidoesNegativas 
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
        except Exception as nomeRequerenter:
            send_log_error(f"nomeRequerente ao executar a operação de atualização da atividades Economicas. {nomeRequerenter}")

    def db_search(self, id):
        try:
            sql = f"SELECT * FROM certidoesNegativas WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as nomeRequerenter:
            send_log_error(f"nomeRequerente ao executar a operação de busca. {nomeRequerenter}")

    def db_list(self):
        try:
            sql = "SELECT * FROM certidoesNegativas WHERE id_cloud is null"
            data = self.query(sql)
            if data:
                send_log_info("Consulta de todos os atividades Economicas realizada com sucesso.")
                return data
            return None
        except Exception as nomeRequerenter:
            send_log_error(f"nomeRequerente ao executar a operação de busca. {nomeRequerenter}")

    def get_id_cloud(self, id):
        if (id == None):
            return None
        try:
            sql = f"SELECT id_cloud FROM certidoesNegativas WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as nomeRequerenter:
            send_log_error(f"nomeRequerente ao executar a operação de busca. {nomeRequerenter}")

    def send_post(self, id, idContribuinte, idEconomico, idEconomicoCnae, idEconomicoListaServico, idEnderecoContribuinte, dataValidade, idModelo, idImovel, chaveEmissao, comprovacao, 
                 finalidade, nomeRequerente, ressalva, informacoesComplementares, nroDocumento, ano, qtdDeclaracoesAbertoVencidas, qtdDeclaracoesNaoIniciadasVencidas, 
                 qtdLanctoInscritosSuspensos, qtdLanctoNaoInscritosAtivos, qtdLanctoNaoInscritosAtivosEnquadramento, qtdLanctoNaoInscritosAtivosUnidade, 
                 qtdLanctoNaoInscritosSuspensos, qtdLanctoNaoInscritosVencer, qtdLanctoNaoInscritosVencidos, qtdLanctoParceladosVencer, qtdLanctoParceladosVencidos, 
                 situacaoCertidaoNegativa, situacaoContribuinte, situacaoEconomico, situacaoImovel, tipoCertidaoNegativa):
        objeto = {
                    "idIntegracao": f"Atos{id}",
                    "content": {}
        }
        if situacaoContribuinte:
            objeto["content"]["situacaoContribuinte"] = f"{situacaoContribuinte}"

        if situacaoEconomico:
            objeto["content"]["situacaoEconomico"] = f"{situacaoEconomico}"

        if situacaoImovel:
            objeto["content"]["situacaoImovel"] = f"{situacaoImovel}"     

        if tipoCertidaoNegativa:
            objeto["content"]["tipoCertidaoNegativa"] = f"{tipoCertidaoNegativa}"  

        if qtdLanctoNaoInscritosSuspensos:
            objeto["content"]["qtdLanctoNaoInscritosSuspensos"] = { "id": int(qtdLanctoNaoInscritosSuspensos)}

        if qtdLanctoNaoInscritosVencidos:
            objeto["content"]["qtdLanctoNaoInscritosVencidos"] = { "id": int(qtdLanctoNaoInscritosVencidos)}

        if qtdLanctoParceladosVencer:
            objeto["content"]["qtdLanctoParceladosVencer"] = { "id": int(qtdLanctoParceladosVencer)}

        if qtdLanctoParceladosVencidos:
            objeto["content"]["qtdLanctoParceladosVencidos"] = { "id": int(qtdLanctoParceladosVencidos)}    

        if situacaoCertidaoNegativa:
            objeto["content"]["situacaoCertidaoNegativa"] = f"{situacaoCertidaoNegativa}"

        if qtdLanctoNaoInscritosVencer:
            objeto["content"]["UnidadeMedida"] = { "id": int(qtdLanctoNaoInscritosVencer) }

        if idContribuinte:
            objeto["content"]["idContribuinte"] = { "id": int(idContribuinte)}

        if qtdLanctoNaoInscritosAtivosUnidade:
            objeto["content"]["qtdLanctoNaoInscritosAtivosUnidade"] = { "id": int(qtdLanctoNaoInscritosAtivosUnidade)}

        if qtdLanctoNaoInscritosAtivos:
            objeto["content"]["qtdLanctoNaoInscritosAtivos"] = { "id": int(qtdLanctoNaoInscritosAtivos)}

        if qtdLanctoNaoInscritosAtivosEnquadramento:
            objeto["content"]["qtdLanctoNaoInscritosAtivosEnquadramento"] = { "id": int(qtdLanctoNaoInscritosAtivosEnquadramento)}

        if dataValidade:
            objeto["content"]["dataValidade"] = f"{dataValidade}"

        if idImovel:
            objeto["content"]["compartilhadoContribuinteMelhorias"] = { "id": int(idImovel)}

        if comprovacao:
            objeto["content"]["comprovacao"] = f"{comprovacao}"     

        if finalidade:
            objeto["content"]["finalidade"] = f"{finalidade}"

        if nomeRequerente:
            objeto["content"]["nomeRequerente"] = f"{nomeRequerente}"

        if qtdLanctoInscritosSuspensos:
            objeto["content"]["qtdLanctoInscritosSuspensos"] = { "id": int(qtdLanctoInscritosSuspensos)}

        if chaveEmissao:
            objeto["content"]["chaveEmissao"] = f"{chaveEmissao}"             
        
        if idEconomicoListaServico:
            objeto["content"]["idEconomicoListaServico"] = { "id": int(idEconomicoListaServico)}
        
        if ressalva:
            objeto["content"]["ressalva"] = f"{ressalva}"
        
        if idEconomico:
            objeto["content"]["idEconomico"] = { "id": int(idEconomico)}
        
        if idEconomicoCnae:
            objeto["content"]["idEconomicoCnae"] = { "id": int(idEconomicoCnae)}
        
        if nroDocumento:
            objeto["content"]["CasasDecimais"] = { "id": int(nroDocumento) }
        
        if ano:
            objeto["content"]["MaximoDigitos"] = { "id": int(ano) }
        
        if idEnderecoContribuinte:
            objeto["content"]["idEnderecoContribuintes"] = { "id": int(idEnderecoContribuinte) }
        
        if idModelo:
            objeto["content"]["CompartilhadoCondominio"] = { "id": int(idModelo)}
        
        if qtdDeclaracoesAbertoVencidas:
            objeto["content"]["qtdDeclaracoesAbertoVencidas"] = { "id": int(qtdDeclaracoesAbertoVencidas)}
        
        if informacoesComplementares:
            objeto["content"]["LivroEletronico"] = f"{informacoesComplementares}"
        
        if qtdDeclaracoesNaoIniciadasVencidas:
            objeto["content"]["qtdDeclaracoesNaoIniciadasVencidas"] = { "id": int(qtdDeclaracoesNaoIniciadasVencidas)}

        envio = api_post("certidoesNegativas", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

certidoesNegativas = certidoesNegativas()