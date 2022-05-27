from samples import *
import json

class pagamentosReceitas(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idCreditosTributariosRec, idPagamento, vlTributoDevido, vlCorrecaoDevido, vlJuroDevido, vlMultaDevido, vlTributoPago, vlCorrecao, 
                vlJuro, vlMulta, vlDescontoTributo, vlDescontoCorrecao, vlDescontoJuro, vlDescontoMulta, vlBeneficios, vlDiferenca, vlPago):
        try:
            sql = """
                INSERT INTO pagamentosReceitas (                    
                    idIntegracao,                   
                    id_cloud, 
                    idCreditosTributariosRec,
                    idPagamento,                                               
                    vlTributoDevido, 
                    vlCorrecaoDevido,
                    vlJuroDevido,
                    vlTributoPago,
                    vlCorrecao,
                    vlMultaDevido,
                    vlJuro,                    
                    vlMulta,
                    vlDescontoCorrecao,
                    vlDescontoTributo,
                    vlDescontoJuro,
                    vlDescontoMulta,
                    vlBeneficios,
                    vlDiferenca, 
                    vlPago               
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idCreditosTributariosRec)s,
                    %(idPagamento)s,
                    %(vlTributoDevido)s,
                    %(vlCorrecaoDevido)s,
                    %(vlJuroDevido)s,
                    %(vlTributoPago)s,
                    %(vlCorrecao)s,
                    %(vlMultaDevido)s,
                    %(vlJuro)s,                    
                    %(vlMulta)s,
                    %(vlDescontoCorrecao)s,
                    %(vlDescontoTributo)s,
                    %(vlDescontoJuro)s,
                    %(vlDescontoMulta)s,
                    %(vlBeneficios)s,
                    %(vlDiferenca)s, 
                    %(vlPago)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idCreditosTributariosRec = idCreditosTributariosRec,
                idPagamento = idPagamento,
                vlTributoDevido = vlTributoDevido,                               
                vlCorrecaoDevido = vlCorrecaoDevido,
                vlJuroDevido = vlJuroDevido,
                vlTributoPago = vlTributoPago,                               
                vlCorrecao = vlCorrecao,
                vlMultaDevido = vlMultaDevido,
                vlJuro = vlJuro,                                               
                vlMulta = vlMulta,
                vlDescontoCorrecao = vlDescontoCorrecao,                               
                vlDescontoTributo = vlDescontoTributo,
                vlDescontoJuro = vlDescontoJuro,
                vlDescontoMulta = vlDescontoMulta,                               
                vlBeneficios = vlBeneficios,
                vlDiferenca = vlDiferenca, 
                vlPago = vlPago
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {pagamentosReceitas} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {pagamentosReceitas}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM pagamentosReceitas"
            if not self.query(sql_s):
                send_log_warning(f"pagamentosReceitas não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM pagamentosReceitas WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM pagamentosReceitas WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    pagamentosReceitas 
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
            sql = f"SELECT * FROM pagamentosReceitas WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM pagamentosReceitas WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM pagamentosReceitas WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idCreditosTributariosRec, idPagamento, vlTributoDevido, vlCorrecaoDevido, vlJuroDevido, vlMultaDevido, vlTributoPago, vlCorrecao, 
                vlJuro, vlMulta, vlDescontoTributo, vlDescontoCorrecao, vlDescontoJuro, vlDescontoMulta, vlBeneficios, vlDiferenca, vlPago):
        objeto = {
            "idIntegracao": f"pagamentosReceitas{id}",
            "content": {}                                 
        }
        if vlPago:
            objeto["content"]["vlPago"] = f"{vlPago}"

        if idCreditosTributariosRec:
            objeto["content"]["idCreditosTributariosRec"] = { "id": int(idCreditosTributariosRec)}
        
        if vlCorrecao:
            objeto["content"]["vlCorrecao"] = f"{vlCorrecao}"

        if idPagamento:
            objeto["content"]["idPagamento"] = { "id": int(idPagamento)}
        
        if vlCorrecaoDevido:
            objeto["content"]["vlCorrecaoDevido"] = f"{vlCorrecaoDevido}" 

        if vlDescontoCorrecao:
            objeto["content"]["vlDescontoCorrecao"] = f"{vlDescontoCorrecao}"  

        if vlBeneficios:
            objeto["content"]["vlBeneficios"] = f"{vlBeneficios}"       
       
        if vlJuroDevido:
            objeto["content"]["vlJuroDevido"] = f"{vlJuroDevido}"

        if vlTributoPago:
            objeto["content"]["vlTributoPago"] = f"{vlTributoPago}"   

        if vlMulta:
            objeto["content"]["vlMulta"] = f"{vlMulta}"
        
        if vlJuro:
            objeto["content"]["vlJuro"] = f"{vlJuro}"
           
        if vlDescontoTributo:
            objeto["content"]["vlDescontoTributo"] = f"{vlDescontoTributo}"
        
        if vlDescontoMulta:
            objeto["content"]["vlDescontoMulta"] = f"{vlDescontoMulta}"

        if vlMultaDevido:
            objeto["content"]["vlMultaDevido"] = f"{vlMultaDevido}"

        if vlTributoDevido != None:
            objeto[0]["content"]["vlTributoDevido"] = f"{vlTributoDevido}"               

        if vlDescontoJuro != None:
            objeto[0]["content"]["vlDescontoJuro"] = f"{vlDescontoJuro}"

        if vlDiferenca != None:
            objeto[0]["content"]["vlDiferenca"] = f"{vlDiferenca}"
            
        envio = api_post("pagamentosReceitas", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

pagamentosReceitas = pagamentosReceitas()