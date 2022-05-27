from samples import *
import json

class receitasDiversasLanctos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idReceitaDiversa, qtdDiasMeses, qtdParcelas, dtCriacao, dtVcto, observacao, totalLancado, intervaloVenctos, 
                situacao):
        try:
            sql = """
                INSERT INTO receitasDiversasLanctos (                    
                    idIntegracao,                   
                    id_cloud, 
                    idReceitaDiversa,
                    qtdDiasMeses,                                               
                    qtdParcelas, 
                    dtCriacao,
                    dtVcto,
                    totalLancado,
                    intervaloVenctos,
                    observacao,
                    situacao       
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idReceitaDiversa)s,
                    %(qtdDiasMeses)s,
                    %(qtdParcelas)s,
                    %(dtCriacao)s,
                    %(dtVcto)s,
                    %(totalLancado)s,
                    %(intervaloVenctos)s,
                    %(observacao)s,
                    %(situacao)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idReceitaDiversa = idReceitaDiversa,
                qtdDiasMeses = qtdDiasMeses,
                qtdParcelas = qtdParcelas,                               
                dtCriacao = dtCriacao,
                dtVcto = dtVcto,
                totalLancado = totalLancado,                               
                intervaloVenctos = intervaloVenctos,
                observacao = observacao,
                situacao = situacao
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {receitasDiversasLanctos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {receitasDiversasLanctos}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM receitasDiversasLanctos"
            if not self.query(sql_s):
                send_log_warning(f"receitasDiversasLanctos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM receitasDiversasLanctos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM receitasDiversasLanctos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    receitasDiversasLanctos 
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
            sql = f"SELECT * FROM receitasDiversasLanctos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM receitasDiversasLanctos WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM receitasDiversasLanctos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idReceitaDiversa, qtdDiasMeses, qtdParcelas, dtCriacao, dtVcto, observacao, totalLancado, intervaloVenctos, 
                situacao):
        objeto = {
            "idIntegracao": f"receitasDiversasLanctos{id}",
            "content": {}                                 
        }
        if idReceitaDiversa:
            objeto["content"]["idReceitaDiversa"] = { "id": int(idReceitaDiversa)}          
        
        if intervaloVenctos:
            objeto["content"]["intervaloVenctos"] = f"{intervaloVenctos}"

        if qtdDiasMeses:
            objeto["content"]["qtdDiasMeses"] = { "id": int(qtdDiasMeses)}           
        
        if dtCriacao:
            objeto["content"]["dtCriacao"] = f"{dtCriacao}" 

        if dtVcto:
            objeto["content"]["dtVcto"] = f"{dtVcto}"

        if totalLancado:
            objeto["content"]["totalLancado"] = f"{totalLancado}" 
        
        if situacao:
            objeto["content"]["situacao"] = f"{situacao}"
                   
        if observacao:
            objeto["content"]["observacao"] = f"{observacao}"

        if qtdParcelas != None:
            objeto[0]["content"]["qtdParcelas"] = { "id": int(qtdParcelas) }        
            
        envio = api_post("receitasDiversasLanctos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

receitasDiversasLanctos = receitasDiversasLanctos()