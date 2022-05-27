from samples import *
import json

class obrasMovimentacoes(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idObra, observacao, dhMovimentacao, usuarioMovimentacao, usuariosDestino, tipoMovimentacao, status, statusRotulo, 
                  statusIcone, statusCor, estornado, statusEstornado, statusEstornadoRotulo):
        try:
            sql = """
                INSERT INTO obrasMovimentacoes (                    
                    idIntegracao,                   
                    id_cloud, 
                    idObra,
                    observacao,                                               
                    dhMovimentacao, 
                    usuarioMovimentacao,
                    usuariosDestino,
                    tipoMovimentacao,
                    status,
                    statusRotulo,
                    statusIcone,
                    statusCor,
                    estornado,
                    statusEstornado,
                    statusEstornadoRotulo
                    areaEdificada                    
                ) VALUES (
                    %(idObra)s,
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(observacao)s,
                    %(dhMovimentacao)s,
                    %(usuarioMovimentacao)s,
                    %(usuariosDestino)s,
                    %(tipoMovimentacao)s,
                    %(status)s,
                    %(statusRotulo)s,
                    %(statusIcone)s,
                    %(statusCor)s,
                    %(estornado)s,
                    %(statusEstornado)s,
                    %(statusEstornadoRotulo)s                        
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idObra = idObra,
                observacao = observacao,
                dhMovimentacao = dhMovimentacao,                               
                usuarioMovimentacao = usuarioMovimentacao,
                usuariosDestino = usuariosDestino,
                tipoMovimentacao = tipoMovimentacao,                               
                status = status,
                statusRotulo = statusRotulo,                               
                statusIcone = statusIcone,
                statusCor = statusCor,
                estornado = estornado,                               
                statusEstornado = statusEstornado,
                statusEstornadoRotulo = statusEstornadoRotulo
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {obrasMovimentacoes} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {obrasMovimentacoes}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM obrasMovimentacoes"
            if not self.query(sql_s):
                send_log_warning(f"obrasMovimentacoes não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM obrasMovimentacoes WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM obrasMovimentacoes WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    obrasMovimentacoes 
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
            sql = f"SELECT * FROM obrasMovimentacoes WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM obrasMovimentacoes WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM obrasMovimentacoes WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idObra, observacao, dhMovimentacao, usuarioMovimentacao, usuariosDestino, tipoMovimentacao, status, statusRotulo, 
                  statusIcone, statusCor, estornado, statusEstornado, statusEstornadoRotulo):
        objeto = {
            "idIntegracao": f"obrasMovimentacoes{id}",
            "content": {}                                 
        }
        if status:
            objeto["content"]["status"] = f"{status}"
        
        if statusEstornado:
            objeto["content"]["statusEstornado"] = f"{statusEstornado}"
        
        if statusEstornadoRotulo:
            objeto["content"]["statusEstornadoRotulo"] = f"{statusEstornadoRotulo}"
        
        if tipoMovimentacao:
            objeto["content"]["tipoMovimentacao"] = f"{tipoMovimentacao}"

        if statusRotulo:
            objeto["content"]["statusRotulo"] = f"{statusRotulo}"

        if observacao:
            objeto["content"]["observacao"] = f"{observacao}"
        
        if dhMovimentacao:
            objeto["content"]["dhMovimentacao"] = f"{dhMovimentacao}"
                
        if statusIcone:
            objeto["content"]["statusIcone"] = f"{statusIcone}"
        
        if statusCor:
            objeto["content"]["statusCor"] = f"{statusCor}" 

        if estornado:
            objeto["content"]["estornado"] = f"{estornado}"    

        if idObra != None:
            objeto[0]["content"]["AgenciaBancaria"] = { "id": int(idObra) }               

        if usuarioMovimentacao != None:
            objeto[0]["content"]["Banco"] = f"{usuarioMovimentacao}"

        if usuariosDestino != None:
            objeto[0]["content"]["Convenio"] = f"{usuariosDestino}"

        envio = api_post("obrasMovimentacoes", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

obrasMovimentacoes = obrasMovimentacoes()