from samples import *
import json

class errosCalculo(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idCalculosTributarios, idEconomicos, idImoveis, idMelhorias, mensagem, idReceitasDiversasLanctos, idNotasAvulsas, statusErro):
        try:
            sql = """
                INSERT INTO errosCalculo (                    
                    idIntegracao,                   
                    id_cloud,                                                           
                    idCalculosTributarios, 
                    idEconomicos,
                    idImoveis,
                    idMelhorias,
                    mensagem,
                    idReceitasDiversasLanctos,
                    idNotasAvulsas,    
                    statusErro                                 
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,                                                            
                    %(idCalculosTributarios)s,
                    %(idEconomicos)s,
                    %(idImoveis)s,
                    %(idMelhorias)s,
                    %(idReceitasDiversasLanctos)s,
                    %(mensagem)s,
                    %(idNotasAvulsas)s,
                    %(statusErro)s,
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                                                               
                idCalculosTributarios = idCalculosTributarios,                               
                idEconomicos = idEconomicos,
                idImoveis = idImoveis,
                idMelhorias = idMelhorias,
                idReceitasDiversasLanctos = idReceitasDiversasLanctos,                               
                mensagem = mensagem,
                idNotasAvulsas = idNotasAvulsas,
                statusErro = statusErro                
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {errosCalculo} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {errosCalculo}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM errosCalculo"
            if not self.query(sql_s):
                send_log_warning(f"errosCalculo não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM errosCalculo WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM errosCalculo WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    errosCalculo 
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
            sql = f"SELECT * FROM errosCalculo WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM errosCalculo WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM errosCalculo WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idCalculosTributarios,  idEconomicos, idImoveis, idMelhorias, mensagem, idReceitasDiversasLanctos, idNotasAvulsas, statusErro):
        objeto =  {
            "idIntegracao": f"errosCalculo{id}",
            "content": {}                                 
        }
        if mensagem:
            objeto["content"]["mensagem"] = f"{mensagem}"
        
        if statusErro:
            objeto["content"]["statusErro"] = f"{statusErro}"

        if idMelhorias != None:
            objeto[0]["content"]["idMelhorias"] = { "id": int(idMelhorias) }

        if idNotasAvulsas != None:
            objeto[0]["camposadicionais"]["idNotasAvulsas"] = { "id": int(idNotasAvulsas) }        
               
        if idReceitasDiversasLanctos != None:
            objeto[0]["camposadicionais"]["idReceitasDiversasLanctos"] = { "id": int(idReceitasDiversasLanctos) }    

        if idEconomicos != None:
            objeto[0]["content"]["idEconomicos"] = { "id": int(idEconomicos) }

        if idCalculosTributarios != None:
            objeto[0]["camposadicionais"]["idCalculosTributarios"] = { "id": int(idCalculosTributarios) }        
               
        if idImoveis != None:
            objeto[0]["camposadicionais"]["idImoveis"] = { "id": int(idImoveis) }
        envio = api_post("errosCalculo", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

errosCalculo = errosCalculo()