from samples import *
import json

class declaracoes(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idCompetencia, idCreditosTributariosRec, idCreditoTributario, idEconomico, idGuia, idRetificada, idTaxaExpediente, daf, 
                das, dtDeclaracao, exercicio, vlBaseCalculo, vlImposto, vlServico, vlTaxa, tipo, situacao, calcular):
        try:
            sql = """
                INSERT INTO declaracoes (                    
                    idIntegracao,                   
                    id_cloud, 
                    idCompetencia,
                    idCreditosTributariosRec,                                               
                    idCreditoTributario, 
                    idEconomico,
                    idGuia,
                    idTaxaExpediente,
                    daf,
                    idRetificada,
                    das,                    
                    dtDeclaracao,
                    exercicio,
                    vlBaseCalculo,
                    vlImposto,
                    vlServico,
                    vlTaxa,
                    tipo,
                    situacao,
                    calcular                   
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idCompetencia)s,
                    %(idCreditosTributariosRec)s,
                    %(idCreditoTributario)s,
                    %(idEconomico)s,
                    %(idGuia)s,
                    %(idTaxaExpediente)s,
                    %(daf)s,
                    %(idRetificada)s,
                    %(das)s,                    
                    %(dtDeclaracao)s,
                    %(exercicio)s,
                    %(vlBaseCalculo)s,
                    %(vlImposto)s,
                    %(vlServico)s,
                    %(vlTaxa)s,
                    %(tipo)s,
                    %(usuarioEstorno)s,
                    %(calcular)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idCompetencia = idCompetencia,
                idCreditosTributariosRec = idCreditosTributariosRec,
                idCreditoTributario = idCreditoTributario,                               
                idEconomico = idEconomico,
                idGuia = idGuia,
                idTaxaExpediente = idTaxaExpediente,                               
                daf = daf,
                idRetificada = idRetificada,
                das = das,                                               
                dtDeclaracao = dtDeclaracao,
                exercicio = exercicio,                               
                vlBaseCalculo = vlBaseCalculo,
                vlImposto = vlImposto,
                vlServico = vlServico,                               
                vlTaxa = vlTaxa,
                tipo = tipo,
                calcular = calcular,
                situacao = situacao
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {declaracoes} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {declaracoes}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM declaracoes"
            if not self.query(sql_s):
                send_log_warning(f"declaracoes não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM declaracoes WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM declaracoes WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    declaracoes 
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
            sql = f"SELECT * FROM declaracoes WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM declaracoes WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM declaracoes WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idCompetencia, idCreditosTributariosRec, idCreditoTributario, idEconomico, idGuia, idRetificada, idTaxaExpediente, daf, 
                das, dtDeclaracao, exercicio, vlBaseCalculo, vlImposto, vlServico, vlTaxa, tipo, situacao, calcular):
        objeto = {
            "idIntegracao": f"declaracoes{id}",
            "content": {}                                 
        }
        if idCompetencia:
            objeto["content"]["idCompetencia"] = { "id": int(idCompetencia)}
        
        if daf:
            objeto["content"]["daf"] = f"{daf}"

        if idCreditosTributariosRec:
            objeto["content"]["idCreditosTributariosRec"] = { "id": int(idCreditosTributariosRec)}
           
        if situacao:
            objeto["content"]["situacao"] = f"{situacao}"
        
        if idEconomico:
            objeto["content"]["idEconomico"] = { "id": int(idEconomico)} 

        if exercicio:
            objeto["content"]["exercicio"] = f"{exercicio}"  

        if vlTaxa:
            objeto["content"]["vlTaxa"] = f"{vlTaxa}"       
       
        if idGuia:
            objeto["content"]["idGuia"] = { "id": int(idGuia)}

        if idTaxaExpediente:
            objeto["content"]["idTaxaExpediente"] = { "id": int(idTaxaExpediente)}   

        if dtDeclaracao:
            objeto["content"]["dtDeclaracao"] = f"{dtDeclaracao}"
        
        if das:
            objeto["content"]["das"] = f"{das}"
           
        if vlBaseCalculo:
            objeto["content"]["vlBaseCalculo"] = f"{vlBaseCalculo}"
        
        if vlServico:
            objeto["content"]["vlServico"] = f"{vlServico}"
        
        if calcular:
            objeto["content"]["calcular"] = f"{calcular}"  

        if idRetificada:
            objeto["content"]["idRetificada"] = { "id": int(idRetificada)}

        if idCreditoTributario != None:
            objeto[0]["content"]["idCreditoTributario"] = { "id": int(idCreditoTributario) }               

        if vlImposto != None:
            objeto[0]["content"]["vlImposto"] = f"{vlImposto}"        

        if tipo != None:
            objeto[0]["content"]["tipo"] = f"{tipo}"
            
        envio = api_post("declaracoes", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

declaracoes = declaracoes()