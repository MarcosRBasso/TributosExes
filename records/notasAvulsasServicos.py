from samples import *
import json

class notasAvulsasServicos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idListaServicos, idNotasAvulsas, descricaoServico, aliquotaIbpt, aliquotaServico, quantidade, valorUnitario, valorReducao, valorServico):
        try:
            sql = """
                INSERT INTO notasAvulsasServicos (                    
                    idIntegracao,                   
                    id_cloud, 
                    idListaServicos,
                    idNotasAvulsas,                                               
                    descricaoServico, 
                    aliquotaIbpt,
                    aliquotaServico,
                    valorUnitario,
                    quantidade,
                    valorReducao, 
                    valorServico                
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idListaServicos)s,
                    %(idNotasAvulsas)s,
                    %(descricaoServico)s,
                    %(aliquotaIbpt)s,
                    %(aliquotaServico)s,
                    %(valorUnitario)s,
                    %(quantidade)s,
                    %(valorReducao)s, 
                    %(valorServico)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idListaServicos = idListaServicos,
                idNotasAvulsas = idNotasAvulsas,
                descricaoServico = descricaoServico,                               
                aliquotaIbpt = aliquotaIbpt,
                aliquotaServico = aliquotaServico,
                valorUnitario = valorUnitario,
                quantidade = quantidade,
                valorReducao = valorReducao, 
                valorServico = valorServico
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {notasAvulsasServicos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {notasAvulsasServicos}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM notasAvulsasServicos"
            if not self.query(sql_s):
                send_log_warning(f"notasAvulsasServicos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM notasAvulsasServicos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM notasAvulsasServicos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    notasAvulsasServicos 
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
            sql = f"SELECT * FROM notasAvulsasServicos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM notasAvulsasServicos WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM notasAvulsasServicos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idListaServicos, idNotasAvulsas, descricaoServico, aliquotaIbpt, aliquotaServico, quantidade, valorUnitario, valorReducao, valorServico):
        objeto = {
            "idIntegracao": f"notasAvulsasServicos{id}",
            "content": {}                                 
        }
        if valorReducao:
            objeto["content"]["valorReducao"] = f"{valorReducao}"       
       
        if valorServico:
            objeto["content"]["valorServico"] = f"{valorServico}"

        if idListaServicos:
            objeto["content"]["idListaServicos"] = { "id": int(idListaServicos)}

        if idNotasAvulsas:
            objeto["content"]["idNotasAvulsas"] = { "id": int(idNotasAvulsas)}        
       
        if aliquotaIbpt:
            objeto["content"]["aliquotaIbpt"] = f"{aliquotaIbpt}"       
       
        if aliquotaServico:
            objeto["content"]["aliquotaServico"] = f"{aliquotaServico}"

        if valorUnitario:
            objeto["content"]["valorUnitario"] = f"{valorUnitario}"  
        
        if quantidade:
            objeto["content"]["quantidade"] = f"{quantidade}"              

        if descricaoServico != None:
            objeto[0]["content"]["descricaoServico"] = f"{descricaoServico}"    
            
        envio = api_post("notasAvulsasServicos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

notasAvulsasServicos = notasAvulsasServicos()