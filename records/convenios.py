from samples import *
import json

class convenios(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idAgenciasBancarias, idBancos, carteira, cedente, contaBancaria, descCarteira, descricao, disponivelUso, 
                dvCedente, dvContaBancaria, nroConvenio, utilizarParcelamento, tipoValidadeNroBaixa, valorValidadeNroBaixa):
        try:
            sql = """
                INSERT INTO convenios (                    
                    idIntegracao,                   
                    id_cloud, 
                    idAgenciasBancarias,
                    idBancos,                                               
                    carteira, 
                    cedente,
                    contaBancaria,
                    descricao,
                    disponivelUso,
                    descCarteira,
                    dvCedente,                    
                    dvContaBancaria,
                    nroConvenio,
                    utilizarParcelamento,
                    tipoValidadeNroBaixa,
                    valorValidadeNroBaixa                  
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idAgenciasBancarias)s,
                    %(idBancos)s,
                    %(carteira)s,
                    %(cedente)s,
                    %(contaBancaria)s,
                    %(descricao)s,
                    %(disponivelUso)s,
                    %(descCarteira)s,
                    %(dvCedente)s,                    
                    %(dvContaBancaria)s,
                    %(nroConvenio)s,
                    %(utilizarParcelamento)s,
                    %(tipoValidadeNroBaixa)s,
                    %(valorValidadeNroBaixa)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idAgenciasBancarias = idAgenciasBancarias,
                idBancos = idBancos,
                carteira = carteira,                               
                cedente = cedente,
                contaBancaria = contaBancaria,
                descricao = descricao,                               
                disponivelUso = disponivelUso,
                descCarteira = descCarteira,
                dvCedente = dvCedente,                                               
                dvContaBancaria = dvContaBancaria,
                nroConvenio = nroConvenio,                               
                utilizarParcelamento = utilizarParcelamento,
                tipoValidadeNroBaixa = tipoValidadeNroBaixa,
                valorValidadeNroBaixa = valorValidadeNroBaixa
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {convenios} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {convenios}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM convenios"
            if not self.query(sql_s):
                send_log_warning(f"convenios não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM convenios WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM convenios WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    convenios 
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
            sql = f"SELECT * FROM convenios WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM convenios WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM convenios WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idAgenciasBancarias, idBancos, carteira, cedente, contaBancaria, descCarteira, descricao, disponivelUso, 
                dvCedente, dvContaBancaria, nroConvenio, utilizarParcelamento, tipoValidadeNroBaixa, valorValidadeNroBaixa):
        objeto = {
            "idIntegracao": f"convenios{id}",
            "content": {}                                 
        }
        if valorValidadeNroBaixa:
            objeto["content"]["valorValidadeNroBaixa"] = f"{valorValidadeNroBaixa}"

        if idAgenciasBancarias:
            objeto["content"]["idAgenciasBancarias"] = { "id": int(idAgenciasBancarias)}
        
        if disponivelUso:
            objeto["content"]["disponivelUso"] = f"{disponivelUso}"

        if idBancos:
            objeto["content"]["idBancos"] = { "id": int(idBancos)}
        
        if cedente:
            objeto["content"]["cedente"] = f"{cedente}" 

        if nroConvenio:
            objeto["content"]["nroConvenio"] = { "id": int(nroConvenio)}       
       
        if contaBancaria:
            objeto["content"]["contaBancaria"] = { "id": int(contaBancaria)}

        if descricao:
            objeto["content"]["descricao"] = f"{descricao}"   

        if dvContaBancaria:
            objeto["content"]["dvContaBancaria"] = f"{dvContaBancaria}"
        
        if dvCedente:
            objeto["content"]["dvCedente"] = f"{dvCedente}"
           
        if utilizarParcelamento:
            objeto["content"]["utilizarParcelamento"] = f"{utilizarParcelamento}"
        
        if descCarteira:
            objeto["content"]["descCarteira"] = f"{descCarteira}"

        if carteira != None:
            objeto[0]["content"]["carteira"] = { "id": int(carteira) }               

        if tipoValidadeNroBaixa != None:
            objeto[0]["content"]["tipoValidadeNroBaixa"] = f"{tipoValidadeNroBaixa}"    
            
        envio = api_post("convenios", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

convenios = convenios()