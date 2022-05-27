from samples import *
import json

class loteamentos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, areaComum, areaRemanescente, areaTotal, codigo, dtAprovacao, dtCriacao, dtLiberacao, idBairros, idDistritos, 
                  idMunicipios, nome, nroCaucionados, nroLotes, nroQuadras, observacao):
        try:
            sql = """
                INSERT INTO loteamentos (                    
                    idIntegracao,                   
                    id_cloud, 
                    areaComum,
                    areaRemanescente,                                               
                    areaTotal, 
                    codigo,
                    dtAprovacao,
                    dtCriacao,
                    dtLiberacao,
                    idBairros,
                    idDistritos,
                    idMunicipios,
                    nome,
                    nroCaucionados,
                    nroLotes,
                    nroQuadras,
                    observacao                  
                ) VALUES (
                    %(areaComum)s,
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(areaRemanescente)s,
                    %(areaTotal)s,
                    %(codigo)s,
                    %(dtAprovacao)s,
                    %(dtCriacao)s,
                    %(dtLiberacao)s,
                    %(idBairros)s,
                    %(idDistritos)s,
                    %(idMunicipios)s,
                    %(nome)s,
                    %(nroCaucionados)s,
                    %(nroLotes)s,
                    %(nroQuadras)s,
                    %(observacao)s                                    
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                areaComum = areaComum,
                areaRemanescente = areaRemanescente,
                areaTotal = areaTotal,                               
                codigo = codigo,
                dtAprovacao = dtAprovacao,
                dtCriacao = dtCriacao,                               
                dtLiberacao = dtLiberacao,
                idBairros = idBairros,
                idDistritos = idDistritos,                               
                idMunicipios = idMunicipios,
                nome = nome,
                nroCaucionados = nroCaucionados,                               
                nroLotes = nroLotes,
                nroQuadras = nroQuadras,
                observacao = observacao
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {loteamentos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {loteamentos}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM loteamentos"
            if not self.query(sql_s):
                send_log_warning(f"loteamentos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM loteamentos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM loteamentos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    loteamentos 
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
            sql = f"SELECT * FROM loteamentos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM loteamentos WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM loteamentos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, areaComum, areaRemanescente, areaTotal, codigo, dtAprovacao, dtCriacao, dtLiberacao, idBairros, idDistritos, 
                  idMunicipios, nome, nroCaucionados, nroLotes, nroQuadras, observacao):
        objeto = {
            "idIntegracao": f"loteamentos{id}",
            "content": {}                                 
        }
        if dtLiberacao:
            objeto["content"]["dtLiberacao"] = f"{dtLiberacao}"
        
        if nroLotes:
            objeto["content"]["nroLotes"] = { "id": int(nroLotes)}
        
        if nroQuadras:
            objeto["content"]["nroQuadras"] = { "id": int(nroQuadras)}
        
        if dtCriacao:
            objeto["content"]["dtCriacao"] = f"{dtCriacao}"
        
        if idBairros:
            objeto["content"]["idBairros"] = { "id": int(idBairros)}  

        if idDistritos:
            objeto["content"]["idDistritos"] = { "id": int(idDistritos)}
        
        if areaTotal:
            objeto["content"]["areaTotal"] = f"{areaTotal}"
        
        if areaRemanescente:
            objeto["content"]["areaRemanescente"] = f"{areaRemanescente}"
        
        if areaTotal:
            objeto["content"]["areaTotal"] = f"{areaTotal}"
                
        if idMunicipios:
            objeto["content"]["idMunicipios"] = { "id": int(idMunicipios)}
        
        if nome:
            objeto["content"]["nome"] = f"{nome}" 

        if nroCaucionados:
            objeto["content"]["nroCaucionados"] = { "id": int(nroCaucionados)}    

        if areaComum != None:
            objeto[0]["content"]["AgenciaBancaria"] = { "id": int(areaComum) }               

        if codigo != None:
            objeto[0]["content"]["Banco"] = { "id": int(codigo) }

        if dtAprovacao != None:
            objeto[0]["content"]["Convenio"] = f"{dtAprovacao}"
                    
        if observacao != None:
            objeto[0]["content"]["MotivoEstorno"] = f"{observacao}"

        envio = api_post("loteamentos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

loteamentos = loteamentos()