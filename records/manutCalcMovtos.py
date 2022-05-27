from samples import *
import json

class manutCalcMovtos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idManutencoesCalculos, audCriadoPor, audDhCriacao, audAlteradoPor, audDhAlteracao, descricao, tiposMovimentacoes, tipoManutencao, 
                situacao, situacaoAnterior, dhMovimentacao, usuarioMovimentacao):
        try:
            sql = """
                INSERT INTO manutCalcMovtos (                    
                    idIntegracao,                   
                    id_cloud, 
                    idManutencoesCalculos,
                    audCriadoPor,                                               
                    audDhCriacao, 
                    audAlteradoPor,
                    audDhAlteracao,
                    tiposMovimentacoes,
                    tipoManutencao,
                    descricao,
                    situacao,                    
                    situacaoAnterior,
                    usuarioMovimentacao           
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idManutencoesCalculos)s,
                    %(audCriadoPor)s,
                    %(audDhCriacao)s,
                    %(audAlteradoPor)s,
                    %(audDhAlteracao)s,
                    %(tiposMovimentacoes)s,
                    %(tipoManutencao)s,
                    %(descricao)s,
                    %(situacao)s,                    
                    %(situacaoAnterior)s,
                    %(usuarioMovimentacao)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idManutencoesCalculos = idManutencoesCalculos,
                audCriadoPor = audCriadoPor,
                audDhCriacao = audDhCriacao,                               
                audAlteradoPor = audAlteradoPor,
                audDhAlteracao = audDhAlteracao,
                tiposMovimentacoes = tiposMovimentacoes,                               
                tipoManutencao = tipoManutencao,
                descricao = descricao,
                situacao = situacao,                                               
                situacaoAnterior = situacaoAnterior,
                usuarioMovimentacao = usuarioMovimentacao,                               
                dhMovimentacao = dhMovimentacao
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {manutCalcMovtos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {manutCalcMovtos}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM manutCalcMovtos"
            if not self.query(sql_s):
                send_log_warning(f"manutCalcMovtos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM manutCalcMovtos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM manutCalcMovtos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    manutCalcMovtos 
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
            sql = f"SELECT * FROM manutCalcMovtos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM manutCalcMovtos WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM manutCalcMovtos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idManutencoesCalculos, audCriadoPor, audDhCriacao, audAlteradoPor, audDhAlteracao, descricao, tiposMovimentacoes, tipoManutencao, 
                situacao, situacaoAnterior, dhMovimentacao, usuarioMovimentacao):
        objeto = {
            "idIntegracao": f"manutCalcMovtos{id}",
            "content": {}                                 
        }
        if idManutencoesCalculos:
            objeto["content"]["idManutencoesCalculos"] = { "id": int(idManutencoesCalculos)}
        
        if tipoManutencao:
            objeto["content"]["tipoManutencao"] = f"{tipoManutencao}"

        if audCriadoPor:
            objeto["content"]["audCriadoPor"] = f"{audCriadoPor}"
        
        if audAlteradoPor:
            objeto["content"]["audAlteradoPor"] = f"{audAlteradoPor}" 

        if usuarioMovimentacao:
            objeto["content"]["usuarioMovimentacao"] = f"{usuarioMovimentacao}"       
       
        if audDhAlteracao:
            objeto["content"]["audDhAlteracao"] = f"{audDhAlteracao}"

        if tiposMovimentacoes:
            objeto["content"]["tiposMovimentacoes"] = f"{tiposMovimentacoes}"   

        if situacaoAnterior:
            objeto["content"]["situacaoAnterior"] = f"{situacaoAnterior}"
        
        if situacao:
            objeto["content"]["situacao"] = f"{situacao}"
           
        if dhMovimentacao:
            objeto["content"]["dhMovimentacao"] = f"{dhMovimentacao}"

        if descricao:
            objeto["content"]["descricao"] = f"{descricao}"

        if audDhCriacao != None:
            objeto[0]["content"]["audDhCriacao"] = f"{audDhCriacao}"    
            
        envio = api_post("manutCalcMovtos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

manutCalcMovtos = manutCalcMovtos()