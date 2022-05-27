from samples import *
import json

class transfImoveisItensCompra(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idComprador, idTransfImoveisItensVenda, percCompra, vlAreaConstruida, vlAreaTerreno, vlBenfeitorias, vlDeclarado, vlFinanciado, 
                vlItbi, vlOutros, vlVendaAVista, transferido):
        try:
            sql = """
                INSERT INTO transfImoveisItensCompra (                    
                    idIntegracao,                   
                    id_cloud, 
                    idComprador,
                    idTransfImoveisItensVenda,                                               
                    percCompra, 
                    vlAreaConstruida,
                    vlAreaTerreno,
                    vlDeclarado,
                    vlFinanciado,
                    vlBenfeitorias,
                    vlItbi,                    
                    vlOutros,
                    vlVendaAVista,
                    transferido        
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idComprador)s,
                    %(idTransfImoveisItensVenda)s,
                    %(percCompra)s,
                    %(vlAreaConstruida)s,
                    %(vlAreaTerreno)s,
                    %(vlDeclarado)s,
                    %(vlFinanciado)s,
                    %(vlBenfeitorias)s,
                    %(vlItbi)s,                    
                    %(vlOutros)s,
                    %(vlVendaAVista)s,
                    %(transferido)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idComprador = idComprador,
                idTransfImoveisItensVenda = idTransfImoveisItensVenda,
                percCompra = percCompra,                               
                vlAreaConstruida = vlAreaConstruida,
                vlAreaTerreno = vlAreaTerreno,
                vlDeclarado = vlDeclarado,                               
                vlFinanciado = vlFinanciado,
                vlBenfeitorias = vlBenfeitorias,
                vlItbi = vlItbi,                                               
                vlOutros = vlOutros,
                vlVendaAVista = vlVendaAVista,                               
                transferido = transferido
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {transfImoveisItensCompra} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {transfImoveisItensCompra}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM transfImoveisItensCompra"
            if not self.query(sql_s):
                send_log_warning(f"transfImoveisItensCompra não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM transfImoveisItensCompra WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM transfImoveisItensCompra WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    transfImoveisItensCompra 
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
            sql = f"SELECT * FROM transfImoveisItensCompra WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM transfImoveisItensCompra WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM transfImoveisItensCompra WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idComprador, idTransfImoveisItensVenda, percCompra, vlAreaConstruida, vlAreaTerreno, vlBenfeitorias, vlDeclarado, vlFinanciado, 
                vlItbi, vlOutros, vlVendaAVista, transferido):
        objeto = {
            "idIntegracao": f"transfImoveisItensCompra{id}",
            "content": {}                                 
        }
        if idComprador:
            objeto["content"]["idComprador"] = { "id": int(idComprador)}          
        
        if vlFinanciado:
            objeto["content"]["vlFinanciado"] = f"{vlFinanciado}"

        if idTransfImoveisItensVenda:
            objeto["content"]["idTransfImoveisItensVenda"] = { "id": int(idTransfImoveisItensVenda)}           
        
        if vlAreaConstruida:
            objeto["content"]["vlAreaConstruida"] = f"{vlAreaConstruida}" 

        if vlVendaAVista:
            objeto["content"]["vlVendaAVista"] = f"{vlVendaAVista}"  

        if vlAreaTerreno:
            objeto["content"]["vlAreaTerreno"] = f"{vlAreaTerreno}"

        if vlDeclarado:
            objeto["content"]["vlDeclarado"] = f"{vlDeclarado}"   

        if vlOutros:
            objeto["content"]["vlOutros"] = f"{vlOutros}"
        
        if vlItbi:
            objeto["content"]["vlItbi"] = f"{vlItbi}"
           
        if transferido:
            objeto["content"]["transferido"] = f"{transferido}"
        
        if vlBenfeitorias:
            objeto["content"]["vlBenfeitorias"] = f"{vlBenfeitorias}"

        if percCompra != None:
            objeto[0]["content"]["percCompra"] = { "id": int(percCompra) }           
            
        envio = api_post("transfImoveisItensCompra", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

transfImoveisItensCompra = transfImoveisItensCompra()