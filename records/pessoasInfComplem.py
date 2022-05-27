from samples import *
import json

class pessoasInfComplem(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idPessoa, idCampoAdicional, idCampoAdicionalFilho, idAgrupamento, iInformacoesComplementares, ano, dhCampo, texto, 
                vlCampo):
        try:
            sql = """
                INSERT INTO pessoasInfComplem (                    
                    idIntegracao,                   
                    id_cloud, 
                    idPessoa,
                    idCampoAdicional,                                               
                    idCampoAdicionalFilho, 
                    idAgrupamento,
                    iInformacoesComplementares,
                    dhCampo,
                    texto,
                    ano,
                    vlCampo
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idPessoa)s,
                    %(idCampoAdicional)s,
                    %(idCampoAdicionalFilho)s,
                    %(idAgrupamento)s,
                    %(iInformacoesComplementares)s,
                    %(dhCampo)s,
                    %(texto)s,
                    %(ano)s,
                    %(vlCampo)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idPessoa = idPessoa,
                idCampoAdicional = idCampoAdicional,
                idCampoAdicionalFilho = idCampoAdicionalFilho,                               
                idAgrupamento = idAgrupamento,
                iInformacoesComplementares = iInformacoesComplementares,
                dhCampo = dhCampo,                               
                texto = texto,
                ano = ano,
                vlCampo = vlCampo
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {pessoasInfComplem} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {pessoasInfComplem}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM pessoasInfComplem"
            if not self.query(sql_s):
                send_log_warning(f"pessoasInfComplem não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM pessoasInfComplem WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM pessoasInfComplem WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    pessoasInfComplem 
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
            sql = f"SELECT * FROM pessoasInfComplem WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM pessoasInfComplem WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM pessoasInfComplem WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idPessoa, idCampoAdicional, idCampoAdicionalFilho, idAgrupamento, iInformacoesComplementares, ano, dhCampo, texto, 
                vlCampo):
        objeto = {
            "idIntegracao": f"pessoasInfComplem{id}",
            "content": {}                                 
        }
        if idPessoa:
            objeto["content"]["idPessoa"] = { "id": int(idPessoa)}          
        
        if texto:
            objeto["content"]["texto"] = f"{texto}"

        if idCampoAdicional:
            objeto["content"]["idCampoAdicional"] = { "id": int(idCampoAdicional)}           
        
        if idAgrupamento:
            objeto["content"]["idAgrupamento"] = { "id": int(idAgrupamento)} 

        if iInformacoesComplementares:
            objeto["content"]["iInformacoesComplementares"] = { "id": int(iInformacoesComplementares)}

        if dhCampo:
            objeto["content"]["dhCampo"] = f"{dhCampo}"   
        
        if vlCampo:
            objeto["content"]["vlCampo"] = f"{vlCampo}"
           
        if ano:
            objeto["content"]["ano"] = f"{ano}"

        if idCampoAdicionalFilho != None:
            objeto[0]["content"]["idCampoAdicionalFilho"] = { "id": int(idCampoAdicionalFilho) }   
            
        envio = api_post("pessoasInfComplem", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

pessoasInfComplem = pessoasInfComplem()