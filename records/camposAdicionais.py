from samples import *
import json

class camposAdicionais(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, ajudaCampo, anoFinal, anoInicial, cadastro, codCaracteristica, compartilhadoComCondominios,
                 compartilhadoComContribMelhorias, desabilitado, exibirNaHomologacao, faturaPodeAlterar, formato, formatoHora, 
                 itemPai, livroEletronicoPodeAlterar, maxCasasDecimais, maxDigitos, ordem, padrao, producaoPrimariaPodeAlterar,
                 tipo, tipoEnquadramento, tipoUnidade, titulo, idUnidadeMedida, valorPadrao, exibirConsulta, exibirEnvio, exibirParecer):
        try:
            sql = """
                INSERT INTO camposAdicionais (                    
                    idIntegracao,                   
                    id_cloud, 
                    ajudaCampo,
                    anoFinal,                                               
                    anoInicial, 
                    cadastro,
                    codCaracteristica,
                    compartilhadoComCondominios,
                    compartilhadoComContribMelhorias,
                    desabilitado,
                    exibirNaHomologacao,                    
                    faturaPodeAlterar,
                    formato,
                    formatoHora,
                    itemPai,
                    livroEletronicoPodeAlterar,
                    maxCasasDecimais,
                    maxDigitos,
                    ordem,
                    padrao,
                    producaoPrimariaPodeAlterar,
                    tipo, 
                    tipoEnquadramento, 
                    tipoUnidade, 
                    titulo, 
                    idUnidadeMedida, 
                    valorPadrao, 
                    exibirConsulta, 
                    exibirEnvio, 
                    exibirParece                   
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(ajudaCampo)s,
                    %(anoFinal)s,
                    %(anoInicial)s,
                    %(cadastro)s,
                    %(codCaracteristica)s,
                    %(compartilhadoComCondominios)s,
                    %(compartilhadoComContribMelhorias)s,
                    %(desabilitado)s,
                    %(exibirNaHomologacao)s,                    
                    %(faturaPodeAlterar)s,
                    %(formato)s,
                    %(formatoHora)s,
                    %(itemPai)s,
                    %(livroEletronicoPodeAlterar)s,
                    %(maxCasasDecimais)s,
                    %(maxDigitos)s,
                    %(producaoPrimariaPodeAlterar)s,
                    %(padrao)s,                    
                    %(ordem)s,
                    %(tipo)s,
                    %(tipoEnquadramento)s,
                    %(tipoUnidade)s,
                    %(titulo)s,
                    %(idUnidadeMedida)s,
                    %(valorPadrao)s,
                    %(exibirConsulta)s,
                    %(exibirEnvio)s,                    
                    %(exibirParece)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                ajudaCampo = ajudaCampo,
                anoFinal = anoFinal,
                anoInicial = anoInicial,                               
                cadastro = cadastro,
                codCaracteristica = codCaracteristica,
                compartilhadoComCondominios = compartilhadoComCondominios,                               
                compartilhadoComContribMelhorias = compartilhadoComContribMelhorias,
                desabilitado = desabilitado,
                exibirNaHomologacao = exibirNaHomologacao,                                               
                faturaPodeAlterar = faturaPodeAlterar,
                formato = formato,                               
                formatoHora = formatoHora,
                itemPai = itemPai,
                livroEletronicoPodeAlterar = livroEletronicoPodeAlterar,                               
                maxCasasDecimais = maxCasasDecimais,
                maxDigitos = maxDigitos,
                producaoPrimariaPodeAlterar = producaoPrimariaPodeAlterar,
                padrao = padrao,
                ordem = ordem,
                tipo = tipo, 
                tipoEnquadramento = tipoEnquadramento, 
                tipoUnidade = tipoUnidade, 
                titulo = titulo, 
                idUnidadeMedida = idUnidadeMedida, 
                valorPadrao = valorPadrao, 
                exibirConsulta = exibirConsulta, 
                exibirEnvio = exibirEnvio, 
                exibirParecer = exibirParecer
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {camposAdicionais} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as formatoHorar:
            send_log_error(f"formatoHora ao inserir o anistias {camposAdicionais}. {formatoHorar}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM camposAdicionais"
            if not self.query(sql_s):
                send_log_warning(f"camposAdicionais não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM camposAdicionais WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as formatoHorar:
            send_log_error(f"formatoHora ao executar a operação de exclusão do atividades econômicas. {formatoHorar}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM camposAdicionais WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    camposAdicionais 
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
        except Exception as formatoHorar:
            send_log_error(f"formatoHora ao executar a operação de atualização da atividades Economicas. {formatoHorar}")

    def db_search(self, id):
        try:
            sql = f"SELECT * FROM camposAdicionais WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as formatoHorar:
            send_log_error(f"formatoHora ao executar a operação de busca. {formatoHorar}")

    def db_list(self):
        try:
            sql = "SELECT * FROM camposAdicionais WHERE id_cloud is null"
            data = self.query(sql)
            if data:
                send_log_info("Consulta de todos os atividades Economicas realizada com sucesso.")
                return data
            return None
        except Exception as formatoHorar:
            send_log_error(f"formatoHora ao executar a operação de busca. {formatoHorar}")

    def get_id_cloud(self, id):
        if (id == None):
            return None
        try:
            sql = f"SELECT id_cloud FROM camposAdicionais WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as formatoHorar:
            send_log_error(f"formatoHora ao executar a operação de busca. {formatoHorar}")

    def send_post(self, id, ajudaCampo, anoFinal, anoInicial, cadastro, codCaracteristica, desabilitado, compartilhadoComCondominios, 
                  compartilhadoComContribMelhorias, exibirNaHomologacao, faturaPodeAlterar, formato, formatoHora, itemPai, 
                  livroEletronicoPodeAlterar, maxCasasDecimais, maxDigitos, ordem, padrao, producaoPrimariaPodeAlterar, tipo, 
                  tipoEnquadramento, tipoUnidade, titulo, idUnidadeMedida, valorPadrao, exibirConsulta, exibirEnvio, exibirParecer):
        objeto = {
                    "idIntegracao": f"Atos{id}",
                    "content": {}
        }
        if titulo:
            objeto["content"]["titulo"] = f"{titulo}"

        if valorPadrao:
            objeto["content"]["valorPadrao"] = f"{valorPadrao}"

        if exibirConsulta:
            objeto["content"]["exibirConsulta"] = f"{exibirConsulta}"     

        if exibirEnvio:
            objeto["content"]["exibirEnvio"] = f"{exibirEnvio}"    

        if exibirParecer:
            objeto["content"]["exibirParecer"] = f"{exibirParecer}"

        if idUnidadeMedida:
            objeto["content"]["UnidadeMedida"] = { "id": int(idUnidadeMedida) }

        if ajudaCampo:
            objeto["content"]["ajudaCampo"] = f"{ajudaCampo}"

        if tipoUnidade:
            objeto["content"]["tipoUnidade"] = f"{tipoUnidade}"

        if tipo:
            objeto["content"]["tipo"] = f"{tipo}"     

        if tipoEnquadramento:
            objeto["content"]["tipoEnquadramento"] = f"{tipoEnquadramento}"    

        if desabilitado:
            objeto["content"]["desabilitado"] = f"{desabilitado}"

        if compartilhadoComContribMelhorias:
            objeto["content"]["compartilhadoContribuinteMelhorias"] = f"{compartilhadoComContribMelhorias}"

        if faturaPodeAlterar:
            objeto["content"]["faturaPodeAlterar"] = f"{faturaPodeAlterar}"     

        if formato:
            objeto["content"]["formato"] = f"{formato}"

        if formatoHora:
            objeto["content"]["formatoHora"] = f"{formatoHora}"

        if producaoPrimariaPodeAlterar:
            objeto["content"]["producaoPrimariaPodeAlterar"] = f"{producaoPrimariaPodeAlterar}"

        if exibirNaHomologacao:
            objeto["content"]["exibirNaHomologacao"] = f"{exibirNaHomologacao}"             
        
        if anoInicial:
            objeto["content"]["anoInicial"] = f"{anoInicial}"
        
        if itemPai:
            objeto["content"]["ItemPai"] = f"{itemPai}"
        
        if anoFinal:
            objeto["content"]["AnoFinal"] = f"{anoFinal}"
        
        if cadastro:
            objeto["content"]["Cadastro"] = f"{cadastro}"
        
        if maxCasasDecimais:
            objeto["content"]["CasasDecimais"] = { "id": int(maxCasasDecimais) }
        
        if maxDigitos:
            objeto["content"]["MaximoDigitos"] = { "id": int(maxDigitos) }
        
        if codCaracteristica:
            objeto["content"]["CodCaracteristicas"] = { "id": int(codCaracteristica) }
        
        if compartilhadoComCondominios:
            objeto["content"]["CompartilhadoCondominio"] = f"{compartilhadoComCondominios}",
        
        if ordem:
            objeto["content"]["ordem"] = f"{ordem}"
        
        if livroEletronicoPodeAlterar:
            objeto["content"]["LivroEletronico"] = f"{livroEletronicoPodeAlterar}"
        
        if padrao:
            objeto["content"]["padrao"] = f"{padrao}"

        envio = api_post("camposAdicionais", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

camposAdicionais = camposAdicionais()