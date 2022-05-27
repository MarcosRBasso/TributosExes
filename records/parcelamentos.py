from samples import *
import json

class parcelamentos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idPessoas, idConfigParcelamentos, nroParcelamento, situacao, vlRendaFamiliar, dhParcelamento, tipoEntrada, vlEntrada, 
                percEntrada, dtVencimento, intervaloVencimento, intervalo, qtdParcela, qtdParcelaOriginal):
        try:
            sql = """
                INSERT INTO parcelamentos (                    
                    idIntegracao,                   
                    id_cloud, 
                    idPessoas,
                    idConfigParcelamentos,                                               
                    nroParcelamento, 
                    situacao,
                    vlRendaFamiliar,
                    tipoEntrada,
                    vlEntrada,
                    dhParcelamento,
                    percEntrada,                    
                    dtVencimento,
                    intervaloVencimento,
                    intervalo,
                    qtdParcela,
                    qtdParcelaOriginal         
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idPessoas)s,
                    %(idConfigParcelamentos)s,
                    %(nroParcelamento)s,
                    %(situacao)s,
                    %(vlRendaFamiliar)s,
                    %(tipoEntrada)s,
                    %(vlEntrada)s,
                    %(dhParcelamento)s,
                    %(percEntrada)s,                    
                    %(dtVencimento)s,
                    %(intervaloVencimento)s,
                    %(intervalo)s,
                    %(qtdParcela)s,
                    %(qtdParcelaOriginal)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idPessoas = idPessoas,
                idConfigParcelamentos = idConfigParcelamentos,
                nroParcelamento = nroParcelamento,                               
                situacao = situacao,
                vlRendaFamiliar = vlRendaFamiliar,
                tipoEntrada = tipoEntrada,                               
                vlEntrada = vlEntrada,
                dhParcelamento = dhParcelamento,
                percEntrada = percEntrada,                                               
                dtVencimento = dtVencimento,
                intervaloVencimento = intervaloVencimento,                               
                intervalo = intervalo,
                qtdParcela = qtdParcela,
                qtdParcelaOriginal = qtdParcelaOriginal
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {parcelamentos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {parcelamentos}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM parcelamentos"
            if not self.query(sql_s):
                send_log_warning(f"parcelamentos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM parcelamentos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM parcelamentos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    parcelamentos 
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
            sql = f"SELECT * FROM parcelamentos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM parcelamentos WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM parcelamentos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idPessoas, idConfigParcelamentos, nroParcelamento, situacao, vlRendaFamiliar, dhParcelamento, tipoEntrada, vlEntrada, 
                percEntrada, dtVencimento, intervaloVencimento, intervalo, qtdParcela, qtdParcelaOriginal):
        objeto = {
            "idIntegracao": f"parcelamentos{id}",
            "content": {}                                 
        }
        if idPessoas:
            objeto["content"]["idPessoas"] = { "id": int(idPessoas)}          
        
        if vlEntrada:
            objeto["content"]["vlEntrada"] = f"{vlEntrada}"

        if idConfigParcelamentos:
            objeto["content"]["idConfigParcelamentos"] = { "id": int(idConfigParcelamentos)}           
        
        if situacao:
            objeto["content"]["situacao"] = f"{situacao}" 

        if intervaloVencimento:
            objeto["content"]["intervaloVencimento"] = f"{intervaloVencimento}"  

        if vlRendaFamiliar:
            objeto["content"]["vlRendaFamiliar"] = f"{vlRendaFamiliar}"

        if tipoEntrada:
            objeto["content"]["tipoEntrada"] = f"{tipoEntrada}"   

        if dtVencimento:
            objeto["content"]["dtVencimento"] = f"{dtVencimento}"
        
        if percEntrada:
            objeto["content"]["percEntrada"] = f"{percEntrada}"
           
        if intervalo:
            objeto["content"]["intervalo"] = f"{intervalo}"
        
        if qtdParcelaOriginal:
            objeto["content"]["qtdParcelaOriginal"] = f"{qtdParcelaOriginal}"
        
        if dhParcelamento:
            objeto["content"]["dhParcelamento"] = f"{dhParcelamento}"

        if nroParcelamento != None:
            objeto[0]["content"]["nroParcelamento"] = { "id": int(nroParcelamento) }               

        if qtdParcela != None:
            objeto[0]["content"]["qtdParcela"] = f"{qtdParcela}"        
            
        envio = api_post("parcelamentos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

parcelamentos = parcelamentos()