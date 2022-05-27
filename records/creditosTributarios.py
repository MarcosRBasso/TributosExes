from samples import *
import json

class creditosTributarios(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, iReceitas, idIndexadores, abreviatura, calculaImoveisRurais, emUso, flyProtocolo, descricao, tipoCadastro):
        try:
            sql = """
                INSERT INTO creditosTributarios (                    
                    idIntegracao,                   
                    id_cloud, 
                    iReceitas,
                    idIndexadores,                                               
                    abreviatura, 
                    calculaImoveisRurais,
                    emUso,
                    descricao,
                    tipoCadastro                 
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(iReceitas)s,
                    %(idIndexadores)s,
                    %(abreviatura)s,
                    %(calculaImoveisRurais)s,
                    %(emUso)s,
                    %(descricao)s,
                    %(tipoCadastro)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                iReceitas = iReceitas,
                idIndexadores = idIndexadores,
                abreviatura = abreviatura,                               
                calculaImoveisRurais = calculaImoveisRurais,
                emUso = emUso,
                descricao = descricao,                               
                tipoCadastro = tipoCadastro,
                flyProtocolo = flyProtocolo
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {creditosTributarios} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {creditosTributarios}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM creditosTributarios"
            if not self.query(sql_s):
                send_log_warning(f"creditosTributarios não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM creditosTributarios WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM creditosTributarios WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    creditosTributarios 
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
            sql = f"SELECT * FROM creditosTributarios WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM creditosTributarios WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM creditosTributarios WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, iReceitas, idIndexadores, abreviatura, calculaImoveisRurais, emUso, flyProtocolo, descricao, tipoCadastro):
        objeto = {
            "idIntegracao": f"creditosTributarios{id}",
            "content": {}                                 
        }
        if iReceitas:
            objeto["content"]["iReceitas"] = { "id": int(iReceitas)}
        
        if tipoCadastro:
            objeto["content"]["tipoCadastro"] = f"{tipoCadastro}"

        if idIndexadores:
            objeto["content"]["idIndexadores"] = { "id": int(idIndexadores)}        
       
        if calculaImoveisRurais:
            objeto["content"]["calculaImoveisRurais"] = f"{calculaImoveisRurais}"       
       
        if emUso:
            objeto["content"]["emUso"] = f"{emUso}"

        if descricao:
            objeto["content"]["descricao"] = f"{descricao}"  
        
        if flyProtocolo:
            objeto["content"]["flyProtocolo"] = f"{flyProtocolo}"              

        if abreviatura != None:
            objeto[0]["content"]["abreviatura"] = f"{abreviatura}"    
            
        envio = api_post("creditosTributarios", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

creditosTributarios = creditosTributarios()