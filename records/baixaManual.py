from samples import *
import json

class baixaManual(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, ano, codigoBarras, representacaoNumerica, idsContribuintes, idsCreditosTributarios, idsConfiguracaoGeracaoParcelas, dtBaixa, nroParcela, 
                  guiaUnificada, tipo, tipoLancamento):
        try:
            sql = """
                INSERT INTO baixaManual (                    
                    idIntegracao,                   
                    id_cloud, 
                    ano,
                    codigoBarras,                                               
                    representacaoNumerica, 
                    idsContribuintes,
                    idsCreditosTributarios,
                    idsConfiguracaoGeracaoParcelas,
                    dtBaixa,
                    nroParcela,
                    guiaUnificada,                    
                    tipo,
                    tipoLancamento                   
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(ano)s,
                    %(baixaRetroativa)s,
                    %(codigoBarras)s,
                    %(representacaoNumerica)s,
                    %(idsContribuintes)s,
                    %(idsCreditosTributarios)s,
                    %(idsConfiguracaoGeracaoParcelas)s,
                    %(dtBaixa)s,
                    %(nroParcela)s,                    
                    %(guiaUnificada)s,
                    %(tipoLancamento)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                ano = ano,
                codigoBarras = codigoBarras,
                representacaoNumerica = representacaoNumerica,                               
                idsContribuintes = idsContribuintes,
                idsCreditosTributarios = idsCreditosTributarios,
                idsConfiguracaoGeracaoParcelas = idsConfiguracaoGeracaoParcelas,                               
                dtBaixa = dtBaixa,
                nroParcela = nroParcela,
                guiaUnificada = guiaUnificada,                                               
                tipo = tipo,
                tipoLancamento = tipoLancamento
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {baixaManual} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {baixaManual}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM baixaManual"
            if not self.query(sql_s):
                send_log_warning(f"baixaManual não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM baixaManual WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM baixaManual WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    baixaManual 
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
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de atualização da atividades Economicas. {error}")

    def db_search(self, id):
        try:
            sql = f"SELECT * FROM baixaManual WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM baixaManual WHERE id_cloud is null"
            data = self.query(sql)
            if data:
                send_log_info("Consulta de todos os atividades Economicas realizada com sucesso.")
                return data
            return None
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def get_id_cloud(self, id):
        if (id == None):
            return None
        try:
            sql = f"SELECT id_cloud FROM baixaManual WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, ano, codigoBarras, representacaoNumerica, idsContribuintes, idsCreditosTributarios, idsConfiguracaoGeracaoParcelas, dtBaixa, nroParcela, 
                  guiaUnificada, tipo, tipoLancamento):
        objeto = {
            "idIntegracao": f"baixaManual{id}",
            "content": {}                                 
        }
        if ano:
            objeto["content"]["ano"] = f"{ano}"
        
        if codigoBarras:
            objeto["content"]["codigoBarras"] = f"{codigoBarras}"

        if representacaoNumerica:
            objeto["content"]["representacaoNumerica"] = f"{representacaoNumerica}"
           
        if tipoLancamento:
            objeto["content"]["tipoLancamento"] = f"{tipoLancamento}"
        
        if dtBaixa:
            objeto["content"]["dtBaixa"] = f"{dtBaixa}"
        
        if nroParcela:
            objeto["content"]["nroParcela"] = f"{nroParcela}" 

        if guiaUnificada:
            objeto["content"]["guiaUnificada"] = f"{guiaUnificada}"  

        if tipo:
            objeto["content"]["tipo"] = f"{tipo}"       
       
        if arquivo:
            objeto["content"]["arquivo"] = f"{arquivo}"

        if idsContribuintes != None:
            objeto[0]["content"]["idsContribuintes"] = { "id": int(idsContribuintes) }               

        if idsCreditosTributarios != None:
            objeto[0]["content"]["idsCreditosTributarios"] = { "id": int(idsCreditosTributarios) }

        if idsConfiguracaoGeracaoParcelas != None:
            objeto[0]["content"]["idsConfiguracaoGeracaoParcelas"] = { "id": int(idsConfiguracaoGeracaoParcelas) }

        envio = api_post("baixaManual", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

baixaManual = baixaManual()