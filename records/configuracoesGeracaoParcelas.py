from samples import *
import json

class configuracoesGeracaoParcelas(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idConfigParcelasConfig, idConfiguracoesParcelas, idLeiAtoDesconto, idLeiAtoFormaPagto, qtdDiasMeses, qtdParcelas, descricao, dataVcto,
                  acaoVctoFeriado, intervalo, tipoConfiguracao, tipoDescricao):
        try:
            sql = """
                INSERT INTO configuracoesGeracaoParcelas (                    
                    idIntegracao,                   
                    id_cloud,                     
                    idConfigParcelasConfig,                                               
                    idConfiguracoesParcelas, 
                    idLeiAtoDesconto,
                    idLeiAtoFormaPagto,
                    qtdDiasMeses,
                    qtdParcelas,
                    descricao, 
                    dataVcto, 
                    acaoVctoFeriado, 
                    intervalo,
                    tipoConfiguracao, 
                    tipoDescricao                                 
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,                                        
                    %(idConfigParcelasConfig)s,
                    %(idConfiguracoesParcelas)s,
                    %(idLeiAtoDesconto)s,
                    %(idLeiAtoFormaPagto)s,
                    %(qtdDiasMeses)s,
                    %(qtdParcelas)s,
                    %(descricao)s, 
                    %(dataVcto)s, 
                    %(acaoVctoFeriado)s, 
                    %(intervalo)s,
                    %(tipoConfiguracao)s, 
                    %(tipoDescricao)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                                               
                idConfigParcelasConfig = idConfigParcelasConfig,
                idConfiguracoesParcelas = idConfiguracoesParcelas,                               
                idLeiAtoDesconto = idLeiAtoDesconto,
                idLeiAtoFormaPagto = idLeiAtoFormaPagto,
                qtdDiasMeses = qtdDiasMeses,                               
                qtdParcelas = qtdParcelas,
                descricao = descricao, 
                dataVcto = dataVcto, 
                acaoVctoFeriado = acaoVctoFeriado, 
                intervalo = intervalo,
                tipoConfiguracao = tipoConfiguracao, 
                tipoDescricao = tipoDescricao              
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {configuracoesGeracaoParcelas} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {configuracoesGeracaoParcelas}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM configuracoesGeracaoParcelas"
            if not self.query(sql_s):
                send_log_warning(f"configuracoesGeracaoParcelas não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM configuracoesGeracaoParcelas WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM configuracoesGeracaoParcelas WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    configuracoesGeracaoParcelas 
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
            sql = f"SELECT * FROM configuracoesGeracaoParcelas WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM configuracoesGeracaoParcelas WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM configuracoesGeracaoParcelas WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idConfigParcelasConfig, idConfiguracoesParcelas, idLeiAtoDesconto, idLeiAtoFormaPagto, qtdDiasMeses, qtdParcelas,descricao, dataVcto, acaoVctoFeriado, 
                  intervalo, tipoConfiguracao, tipoDescricao):
        objeto = {
            "idIntegracao": f"configuracoesGeracaoParcelas{id}",
            "content": {}                                 
        }
        if tipoConfiguracao:
            objeto["content"]["tipoConfiguracao"] = f"{tipoConfiguracao}"
           
        if tipoDescricao:
            objeto["content"]["tipoDescricao"] = f"{tipoDescricao}"

        if descricao:
            objeto["content"]["descricao"] = f"{descricao}"
           
        if dataVcto:
            objeto["content"]["dataVcto"] = f"{dataVcto}"
        
        if acaoVctoFeriado:
            objeto["content"]["acaoVctoFeriado"] = f"{acaoVctoFeriado}"
        
        if intervalo:
            objeto["content"]["intervalo"] = f"{intervalo}"

        if idLeiAtoDesconto:
            objeto["content"]["idLeiAtoDesconto"] =  { "id": int(idLeiAtoDesconto)}
        
        if idLeiAtoFormaPagto:
            objeto["content"]["idLeiAtoFormaPagto"] =  { "id": int(idLeiAtoFormaPagto)}

        if idConfigParcelasConfig:
            objeto["content"]["idConfigParcelasConfig"] =  { "id": int(idConfigParcelasConfig)}
           
        if idConfiguracoesParcelas:
            objeto["content"]["idConfiguracoesParcelas"] =  { "id": int(idConfiguracoesParcelas)}
        
        if qtdParcelas:
            objeto["content"]["qtdParcelas"] =  { "id": int(qtdParcelas)}
        
        if qtdDiasMeses:
            objeto["content"]["qtdDiasMeses"] =  { "id": int(qtdDiasMeses)}
        envio = api_post("configuracoesGeracaoParcelas", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

configuracoesGeracaoParcelas = configuracoesGeracaoParcelas()