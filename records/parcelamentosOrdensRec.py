from samples import *
import json

class parcelamentosOrdensRec(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idParcelamentos, idGuias, idDividas, idReceitas, vlTributo, vlCorrecao, vlJuro, vlMulta, 
                vlDescontoTributo, vlDescontoCorrecao, vlDescontoJuro, vlDescontoMulta, vlPagoTributo, vlPagoCorrecao, vlPagoJuro, vlPagoMulta, vlPagoDescontoTributo, 
                vlPagoDescontoCorrecao, vlPagoDescontoJuro, vlPagoDescontoMulta, vlSaldoTributo, vlSaldoCorrecao , vlSaldoJuro, vlSaldoMulta, vlSaldoDescontoTributo,
                vlSaldoDescontoCorrecao, vlSaldoDescontoJuro, vlSaldoDescontoMulta):
        try:
            sql = """
                INSERT INTO parcelamentosOrdensRec (                    
                    idIntegracao,                   
                    id_cloud, 
                    idParcelamentos,
                    idGuias,                                               
                    idDividas, 
                    idReceitas,
                    vlTributo,
                    vlJuro,
                    vlMulta,
                    vlCorrecao,
                    vlDescontoTributo,                    
                    vlDescontoCorrecao,
                    vlDescontoJuro,
                    vlDescontoMulta,
                    vlPagoTributo,
                    vlPagoCorrecao,
                    vlPagoJuro, 
                    vlPagoMulta, 
                    vlPagoDescontoTributo, 
                    vlPagoDescontoCorrecao, 
                    vlPagoDescontoJuro,
                    vlPagoDescontoMulta, 
                    vlSaldoTributo, 
                    vlSaldoCorrecao, 
                    vlSaldoJuro, 
                    vlSaldoMulta, 
                    vlSaldoDescontoTributo,
                    vlSaldoDescontoCorrecao, 
                    vlSaldoDescontoJuro, 
                    vlSaldoDescontoMulta                 
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idParcelamentos)s,
                    %(idGuias)s,
                    %(idDividas)s,
                    %(idReceitas)s,
                    %(vlTributo)s,
                    %(vlJuro)s,
                    %(vlMulta)s,
                    %(vlCorrecao)s,
                    %(vlDescontoTributo)s,                    
                    %(vlDescontoCorrecao)s,
                    %(vlDescontoJuro)s,
                    %(vlDescontoMulta)s,
                    %(vlPagoTributo)s,
                    %(vlPagoCorrecao)s,
                    %(vlPagoJuro)s, 
                    %(vlPagoMulta)s, 
                    %(vlPagoDescontoTributo)s, 
                    %(vlPagoDescontoCorrecao)s, 
                    %(vlPagoDescontoJuro)s,
                    %(vlPagoDescontoMulta)s, 
                    %(vlSaldoTributo)s, 
                    %(vlSaldoCorrecao)s, 
                    %(vlSaldoJuro)s, 
                    %(vlSaldoMulta)s, 
                    %(vlSaldoDescontoTributo)s,
                    %(vlSaldoDescontoCorrecao)s, 
                    %(vlSaldoDescontoJuro)s, 
                    %(vlSaldoDescontoMulta)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idParcelamentos = idParcelamentos,
                idGuias = idGuias,
                idDividas = idDividas,                               
                idReceitas = idReceitas,
                vlTributo = vlTributo,
                vlJuro = vlJuro,                               
                vlMulta = vlMulta,
                vlCorrecao = vlCorrecao,
                vlDescontoTributo = vlDescontoTributo,                                               
                vlDescontoCorrecao = vlDescontoCorrecao,
                vlDescontoJuro = vlDescontoJuro,                               
                vlDescontoMulta = vlDescontoMulta,
                vlPagoTributo = vlPagoTributo,
                vlPagoCorrecao = vlPagoCorrecao,
                vlPagoJuro = vlPagoJuro, 
                vlPagoMulta = vlPagoMulta, 
                vlPagoDescontoTributo = vlPagoDescontoTributo, 
                vlPagoDescontoCorrecao = vlPagoDescontoCorrecao, 
                vlPagoDescontoJuro = vlPagoDescontoJuro,
                vlPagoDescontoMulta = vlPagoDescontoMulta, 
                vlSaldoTributo = vlSaldoTributo, 
                vlSaldoCorrecao = vlSaldoCorrecao, 
                vlSaldoJuro = vlSaldoJuro, 
                vlSaldoMulta = vlSaldoMulta, 
                vlSaldoDescontoTributo = vlSaldoDescontoTributo,
                vlSaldoDescontoCorrecao = vlSaldoDescontoCorrecao, 
                vlSaldoDescontoJuro = vlSaldoDescontoJuro, 
                vlSaldoDescontoMulta = vlSaldoDescontoMulta
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {parcelamentosOrdensRec} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {parcelamentosOrdensRec}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM parcelamentosOrdensRec"
            if not self.query(sql_s):
                send_log_warning(f"parcelamentosOrdensRec não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM parcelamentosOrdensRec WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM parcelamentosOrdensRec WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    parcelamentosOrdensRec 
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
            sql = f"SELECT * FROM parcelamentosOrdensRec WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM parcelamentosOrdensRec WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM parcelamentosOrdensRec WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idParcelamentos, idGuias, idDividas, idReceitas, vlTributo, vlCorrecao, vlJuro, vlMulta, 
                vlDescontoTributo, vlDescontoCorrecao, vlDescontoJuro, vlDescontoMulta, vlPagoTributo, vlPagoCorrecao, 
                vlPagoJuro, vlPagoMulta, vlPagoDescontoTributo, vlPagoDescontoCorrecao, vlPagoDescontoJuro,vlPagoDescontoMulta, vlSaldoTributo, vlSaldoCorrecao ,
                vlSaldoJuro, vlSaldoMulta, vlSaldoDescontoTributo,
                vlSaldoDescontoCorrecao, vlSaldoDescontoJuro, vlSaldoDescontoMulta):
        objeto = {
            "idIntegracao": f"parcelamentosOrdensRec{id}",
            "content": {}                                 
        }
        if vlPagoDescontoJuro:
            objeto["content"]["vlPagoDescontoJuro"] = f"{vlPagoDescontoJuro}" 

        if vlPagoDescontoMulta:
            objeto["content"]["vlPagoDescontoMulta"] = f"{vlPagoDescontoMulta}"   

        if vlSaldoTributo:
            objeto["content"]["vlSaldoTributo"] = f"{vlSaldoTributo}"
        
        if vlSaldoCorrecao:
            objeto["content"]["vlSaldoCorrecao"] = f"{vlSaldoCorrecao}"
           
        if vlSaldoJuro:
            objeto["content"]["vlSaldoJuro"] = f"{vlSaldoJuro}"            
        
        if vlSaldoMulta:
            objeto["content"]["vlSaldoMulta"] = f"{vlSaldoMulta}"

        if vlSaldoDescontoTributo:
            objeto["content"]["vlSaldoDescontoTributo"] = f"{vlSaldoDescontoTributo}"           
        
        if vlSaldoDescontoCorrecao:
            objeto["content"]["vlSaldoDescontoCorrecao"] = f"{vlSaldoDescontoCorrecao}" 

        if vlSaldoDescontoJuro:
            objeto["content"]["vlSaldoDescontoJuro"] = f"{vlSaldoDescontoJuro}" 

        if vlSaldoDescontoMulta:
            objeto["content"]["vlSaldoDescontoMulta"] = f"{vlSaldoDescontoMulta}"  

        if idParcelamentos:
            objeto["content"]["idParcelamentos"] = { "id": int(idParcelamentos)}

        if vlPagoJuro:
            objeto["content"]["vlPagoJuro"] = f"{vlPagoJuro}"   

        if vlPagoMulta:
            objeto["content"]["vlPagoMulta"] = f"{vlPagoMulta}"
        
        if vlPagoDescontoTributo:
            objeto["content"]["vlPagoDescontoTributo"] = f"{vlPagoDescontoTributo}"
           
        if vlPagoDescontoCorrecao:
            objeto["content"]["vlPagoDescontoCorrecao"] = f"{vlPagoDescontoCorrecao}"            
        
        if vlMulta:
            objeto["content"]["vlMulta"] = f"{vlMulta}"

        if idGuias:
            objeto["content"]["idGuias"] = f"{idGuias}"           
        
        if idReceitas:
            objeto["content"]["idReceitas"] = f"{idReceitas}" 

        if vlDescontoJuro:
            objeto["content"]["vlDescontoJuro"] = f"{vlDescontoJuro}"  

        if vlTributo:
            objeto["content"]["vlTributo"] = f"{vlTributo}"

        if vlJuro:
            objeto["content"]["vlJuro"] = f"{vlJuro}"   

        if vlDescontoCorrecao:
            objeto["content"]["vlDescontoCorrecao"] = f"{vlDescontoCorrecao}"
        
        if vlDescontoTributo:
            objeto["content"]["vlDescontoTributo"] = f"{vlDescontoTributo}"
           
        if vlDescontoMulta:
            objeto["content"]["vlDescontoMulta"] = f"{vlDescontoMulta}"
        
        if vlPagoCorrecao:
            objeto["content"]["vlPagoCorrecao"] = f"{vlPagoCorrecao}"
        
        if vlCorrecao:
            objeto["content"]["vlCorrecao"] = f"{vlCorrecao}"

        if idDividas != None:
            objeto[0]["content"]["idDividas"] = { "id": int(idDividas) }               

        if vlPagoTributo != None:
            objeto[0]["content"]["vlPagoTributo"] = f"{vlPagoTributo}"        
            
        envio = api_post("parcelamentosOrdensRec", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

parcelamentosOrdensRec = parcelamentosOrdensRec()