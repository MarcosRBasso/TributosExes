from samples import *
import json

class habitese(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, idObra, dtValidade, id_cloud, dtEmissao, restricao, restricaoObservacao,
      ano, idModelo, metragem, nroDocumento, situacaoHabitese):
        try:
            sql = """
                INSERT INTO habitese (
                    idIntegracao,                    
                    idObra,
                    id_cloud,
                    dtValidade,
                    dtEmissao,
                    restricao,
                    restricaoObservacao,
                    ano,
                    idModelo,
                    metragem,
                    nroDocumento,
                    situacaoHabitese
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(idObra)s,
                    %(id_cloud)s,
                    %(dtValidade)s,
                    %(dtEmissao)s,
                    %(restricao)s,
                    %(restricaoObservacao)s,
                    %(ano)s,
                    %(idModelo)s,
                    %(metragem)s,
                    %(nroDocumento)s,
                    %(situacaoHabitese)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,               
                idObra = idObra,
                dtValidade = dtValidade,
                id_cloud = id_cloud,
                dtEmissao = dtEmissao,
                restricao = restricao,
                restricaoObservacao = restricaoObservacao,
                ano = ano,
                idModelo = idModelo,
                metragem = metragem,
                nroDocumento = nroDocumento,
                situacaoHabitese = situacaoHabitese
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {habitese} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o habitese {habitese}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM habitese"
            if not self.query(sql_s):
                send_log_warning(f"Agências Bancarias não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM habitese WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"habitese excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do agrupamentos. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM habitese WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"habitese {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    habitese 
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
            send_log_info(f"habitese {id} atualizado com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de atualização da habitese. {error}")

    def db_search(self, id):
        try:
            sql = f"SELECT * FROM habitese WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"habitese {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM habitese WHERE id_cloud is null"
            data = self.query(sql)
            if data:
                send_log_info("Consulta de todos os habitese realizada com sucesso.")
                return data
            return None
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def get_id_cloud(self, id):
        if (id == None):
            return None
        try:
            sql = f"SELECT id_cloud FROM habitese WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"habitese {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idObra, dtValidade, dtEmissao, restricao, restricaoObservacao,
      ano, idModelo, metragem, nroDocumento, situacaoHabitese):
        objeto = {
            "idIntegracao": f"habitese{id}",
            "content": {}                                 
        }

        if dtValidade:
            objeto["content"]["validade"] = f"{dtValidade}"
        
        if metragem:
            objeto["content"]["metragem"] = f"{metragem}"
        
        if nroDocumento:
            objeto["content"]["NumeroDocumento"] = f"{nroDocumento}"
        
        if ano:
            objeto["content"]["ano"] = f"{ano}"
        
        if situacaoHabitese:
            objeto["content"]["situacaoHabitese"] = f"{situacaoHabitese}"   

        if idModelo != None:
            objeto[0]["content"]["Modelo"] = { "id": int(idModelo) }               

        if idObra != None:
            objeto[0]["content"]["Contribuite"] = { "id": int(idObra) }

        if dtEmissao != None:
            objeto[0]["content"]["Economico"] = f"{dtEmissao}"
                    
        if restricao != None:
            objeto[0]["content"]["EconomicoCnaes"] = f"{restricao}"

        if ano != None:
            objeto[0]["content"]["EnderecoContribuinte"] = { "id": int(ano) }    

        if restricaoObservacao != None:
            objeto[0]["content"]["EconomicosListaServicos"] = f"{restricaoObservacao}"

        envio = api_post("habitese", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

habitese = habitese()