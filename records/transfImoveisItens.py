from samples import *
import json

class transfImoveisItens(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idArrematante, idCartorios, idImoveis, idLocalidades, idMotivos, idPagadores, idProprietario, denominacao, 
                  dtArrematacao, inscricaoIncra, obsArrematacao, vlAreaConstruidaUnidade, vlAreaTotalTerrenoUnidade, vlArrematacao, vlVenalBenfeitoriasUnidade, 
                  vlVenalConstruidoUnidade, vlVenalTerritorialUnidade, vlVenalUnidade,
                  percAvista, percBenfeitoria, percFinanciado, percOutros, benfeitorias, definicaoPagador, financiado, outros, tipoVenda, unidadeFutura):
        try: 
            sql = """
                INSERT INTO transfImoveisItens (                    
                    idIntegracao,                   
                    id_cloud, 
                    idArrematante,
                    idCartorios,                                               
                    idImoveis, 
                    idLocalidades,
                    idMotivos,
                    idProprietario,
                    denominacao,
                    idPagadores,
                    dtArrematacao,                    
                    inscricaoIncra,
                    obsArrematacao,
                    vlAreaConstruidaUnidade,
                    vlAreaTotalTerrenoUnidade,
                    vlArrematacao,
                    vlVenalBenfeitoriasUnidade,
                    vlVenalConstruidoUnidade,
                    vlVenalTerritorialUnidade,
                    vlVenalUnidade,
                    percAvista,
                    percBenfeitoria,
                    percFinanciado, 
                    percOutros,
                    benfeitorias, 
                    definicaoPagador,
                    financiado,
                    outros, 
                    tipoVenda, 
                    unidadeFutura
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idArrematante)s,
                    %(idCartorios)s,
                    %(idImoveis)s,
                    %(idLocalidades)s,
                    %(idMotivos)s,
                    %(idProprietario)s,
                    %(denominacao)s,
                    %(idPagadores)s,
                    %(dtArrematacao)s,                    
                    %(inscricaoIncra)s,
                    %(obsArrematacao)s,
                    %(vlAreaConstruidaUnidade)s,
                    %(vlAreaTotalTerrenoUnidade)s,
                    %(vlArrematacao)s,
                    %(vlVenalBenfeitoriasUnidade)s,
                    %(vlVenalConstruidoUnidade)s,
                    %(percAvista)s,
                    %(vlVenalUnidade)s,                    
                    %(vlVenalTerritorialUnidade)s,
                    %(percAvista)s,                    
                    %(percBenfeitoria)s,
                    %(percFinanciado)s,
                    %(percOutros)s,
                    %(benfeitorias)s,
                    %(definicaoPagador)s,
                    %(financiado)s,
                    %(outros)s,
                    %(tipoVenda)s,
                    %(unidadeFutura)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idArrematante = idArrematante,
                idCartorios = idCartorios,
                idImoveis = idImoveis,                               
                idLocalidades = idLocalidades,
                idMotivos = idMotivos,
                idProprietario = idProprietario,                               
                denominacao = denominacao,
                idPagadores = idPagadores,
                dtArrematacao = dtArrematacao,                                               
                inscricaoIncra = inscricaoIncra,
                obsArrematacao = obsArrematacao,                               
                vlAreaConstruidaUnidade = vlAreaConstruidaUnidade,
                vlAreaTotalTerrenoUnidade = vlAreaTotalTerrenoUnidade,
                vlArrematacao = vlArrematacao,                               
                vlVenalBenfeitoriasUnidade = vlVenalBenfeitoriasUnidade,
                vlVenalConstruidoUnidade = vlVenalConstruidoUnidade,
                percAvista = percAvista,
                vlVenalUnidade = vlVenalUnidade,
                vlVenalTerritorialUnidade = vlVenalTerritorialUnidade,
                percBenfeitoria = percBenfeitoria,
                percFinanciado = percFinanciado, 
                percOutros = percOutros, 
                benfeitorias = benfeitorias, 
                definicaoPagador = definicaoPagador, 
                financiado = financiado, 
                outros = outros, 
                tipoVenda = tipoVenda, 
                unidadeFutura = unidadeFutura
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {transfImoveisItens} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao inserir o anistias {transfImoveisItens}. {contribuintesr}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM transfImoveisItens"
            if not self.query(sql_s):
                send_log_warning(f"transfImoveisItens não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM transfImoveisItens WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de exclusão do atividades econômicas. {contribuintesr}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM transfImoveisItens WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    transfImoveisItens 
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
            sql = f"SELECT * FROM transfImoveisItens WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def db_list(self):
        try:
            sql = "SELECT * FROM transfImoveisItens WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM transfImoveisItens WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def send_post(self, id, idArrematante, idCartorios, idImoveis, idLocalidades, idMotivos, idPagadores, idProprietario, denominacao, 
                  dtArrematacao, inscricaoIncra, obsArrematacao, vlAreaConstruidaUnidade, vlAreaTotalTerrenoUnidade, vlArrematacao, vlVenalBenfeitoriasUnidade, vlVenalConstruidoUnidade, vlVenalTerritorialUnidade, vlVenalUnidade,
                  percAvista, percBenfeitoria, percFinanciado, percOutros, benfeitorias, definicaoPagador, financiado, outros, tipoVenda, unidadeFutura):
        objeto = {
            "idIntegracao": f"Atos{id}",
            "content": {}
        }
        if idArrematante:
            objeto["content"]["VctoFeriado"] = { "id": int(idArrematante)}
        
        if idImoveis:
            objeto["content"]["idImoveis"] = { "id": int(idImoveis)}
        
        if idCartorios:
            objeto["content"]["idCartorios"] = { "id": int(idCartorios)}
        
        if idLocalidades:
            objeto["content"]["idLocalidades"] = { "id": int(idLocalidades)}
        
        if vlVenalBenfeitoriasUnidade:
            objeto["content"]["vlVenalBenfeitoriasUnidade"] = f"{vlVenalBenfeitoriasUnidade}"
        
        if vlVenalConstruidoUnidade:
            objeto["content"]["vlVenalConstruidoUnidade"] = f"{vlVenalConstruidoUnidade}"
        
        if idMotivos:
            objeto["content"]["idMotivos"] = { "id": int(idMotivos)}
        
        if idProprietario:
            objeto["content"]["idProprietario"] = { "id": int(idProprietario)}
        
        if vlVenalTerritorialUnidade:
            objeto["content"]["vlVenalTerritorialUnidade"] = f"{vlVenalTerritorialUnidade}"       

        if percBenfeitoria:
            objeto["content"]["percBenfeitoria"] = { "id": int(percBenfeitoria) }
        
        if vlArrematacao:
            objeto["content"]["vlArrematacao"] = f"{vlArrematacao}" 

        if vlVenalUnidade:
            objeto["content"]["vlVenalUnidade"] = f"{vlVenalUnidade}"

        if percAvista:
            objeto["content"]["percAvista"] = f"{percAvista}"

        if idPagadores:
            objeto["content"]["idPagadores"] = { "id": int(idPagadores)}     

        if denominacao:
            objeto["content"]["denominacao"] = f"{denominacao}"    

        if dtArrematacao:
            objeto["content"]["dtArrematacao"] = f"{dtArrematacao}"

        if inscricaoIncra:
            objeto["content"]["inscricaoIncra"] = f"{inscricaoIncra}"

        if obsArrematacao:
            objeto["content"]["obsArrematacao"] = f"{obsArrematacao}"

        if percFinanciado:
            objeto["content"]["percFinanciado"] = f"{percFinanciado}"     

        if percOutros:
            objeto["content"]["percOutros"] = f"{percOutros}"    

        if benfeitorias:
            objeto["content"]["benfeitorias"] = f"{benfeitorias}"

        if definicaoPagador:
            objeto["content"]["definicaoPagador"] = f"{definicaoPagador}"

        if financiado:
            objeto["content"]["financiado"] = f"{financiado}"  

        if outros:
            objeto["content"]["outros"] = f"{outros}"

        if tipoVenda:
            objeto["content"]["tipoVenda"] = f"{tipoVenda}"

        if unidadeFutura:
            objeto["content"]["unidadeFutura"] = f"{unidadeFutura}"
        
        if vlAreaTotalTerrenoUnidade != None:
            objeto[0]["calculotributario"]["creditotributario"] = f"{vlAreaTotalTerrenoUnidade}"  
        
        if vlAreaConstruidaUnidade:
            objeto["content"]["vlAreaConstruidaUnidade"] = f"{vlAreaConstruidaUnidade}"   

        envio = api_post("transfImoveisItens", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

transfImoveisItens = transfImoveisItens()