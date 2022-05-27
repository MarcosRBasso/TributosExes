from samples import *
import json

class alvaras(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, idContribuinte, dtValidade, id_cloud, idEconomico, idEconomicosCnaes, idEconomicosListaServicos,
      idEnderecoContribuinte, idModelo, informacoesComplementares, nroDocumento, ano, situacaoAlvara, tipoAlvara):
        try:
            sql = """
                INSERT INTO alvaras (
                    idIntegracao,                    
                    idContribuinte,
                    id_cloud,
                    dtValidade,
                    idEconomico,
                    idEconomicosCnaes,
                    idEconomicosListaServicos,
                    idEnderecoContribuinte,
                    idModelo,
                    informacoesComplementares,
                    nroDocumento,
                    ano,
                    situacaoAlvara,
                    tipoAlvara
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(idContribuinte)s,
                    %(id_cloud)s,
                    %(dtValidade)s,
                    %(idEconomico)s,
                    %(idEconomicosCnaes)s,
                    %(idEconomicosListaServicos)s,
                    %(idEnderecoContribuinte)s,
                    %(idModelo)s,
                    %(informacoesComplementares)s,
                    %(nroDocumento)s,
                    %(ano)s,
                    %(situacaoAlvara)s,
                    %(tipoAlvara)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,               
                idContribuinte = idContribuinte,
                dtValidade = dtValidade,
                id_cloud = id_cloud,
                idEconomico = idEconomico,
                idEconomicosCnaes = idEconomicosCnaes,
                idEconomicosListaServicos = idEconomicosListaServicos,
                idEnderecoContribuinte = idEnderecoContribuinte,
                idModelo = idModelo,
                informacoesComplementares = informacoesComplementares,
                nroDocumento = nroDocumento,
                ano = ano,
                situacaoAlvara = situacaoAlvara,
                tipoAlvara = tipoAlvara
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {alvaras} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o alvaras {alvaras}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM alvaras"
            if not self.query(sql_s):
                send_log_warning(f"Agências Bancarias não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM alvaras WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"alvaras excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do agrupamentos. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM alvaras WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"alvaras {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    alvaras 
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
            send_log_info(f"alvaras {id} atualizado com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de atualização da alvaras. {error}")

    def db_search(self, id):
        try:
            sql = f"SELECT * FROM alvaras WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"alvaras {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM alvaras WHERE id_cloud is null"
            data = self.query(sql)
            if data:
                send_log_info("Consulta de todos os alvaras realizada com sucesso.")
                return data
            return None
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def get_id_cloud(self, id):
        if (id == None):
            return None
        try:
            sql = f"SELECT id_cloud FROM alvaras WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"alvaras {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idContribuinte, dtValidade, idEconomico, idEconomicosCnaes, idEconomicosListaServicos,
      idEnderecoContribuinte, idModelo, informacoesComplementares, nroDocumento, ano, situacaoAlvara, tipoAlvara):
        objeto = {
            "idIntegracao": f"alvaras{id}",
            "content": {}                                 
        }

        if dtValidade:
            objeto["content"]["validade"] = f"{dtValidade}"
        
        if informacoesComplementares:
            objeto["content"]["informacoesComplementares"] = f"{informacoesComplementares}"
        
        if nroDocumento:
            objeto["content"]["NumeroDocumento"] = f"{nroDocumento}"
        
        if ano:
            objeto["content"]["ano"] = f"{ano}"
        
        if situacaoAlvara:
            objeto["content"]["situacaoAlvara"] = f"{situacaoAlvara}" 

        if tipoAlvara:
            objeto["content"]["tipoAlvara"] = f"{tipoAlvara}"    

        if idModelo != None:
            objeto[0]["content"]["Modelo"] = { "id": int(idModelo) }               

        if idContribuinte != None:
            objeto[0]["content"]["Contribuite"] = { "id": int(idContribuinte) }

        if idEconomico != None:
            objeto[0]["content"]["Economico"] = { "id": int(idEconomico) }
                    
        if idEconomicosCnaes != None:
            objeto[0]["content"]["EconomicoCnaes"] = { "id": int(idEconomicosCnaes) }

        if idEnderecoContribuinte != None:
            objeto[0]["content"]["EnderecoContribuinte"] = { "id": int(idEnderecoContribuinte) }    

        if idEconomicosListaServicos != None:
            objeto[0]["content"]["EconomicosListaServicos"] = { "id": int(idEconomicosListaServicos) }

        envio = api_post("alvaras", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

alvaras = alvaras()