from samples import *
import json

class receitas(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idAtoExecucaoFiscal, idAtoInscrito, idAtoNaoInscrito, descricao, abreviatura, codigoTCE, classificacao, tipoVinculoAtoInscrito, 
                tipoVinculoAtoNaoInscrito, inscDividaAtiva):
        try:
            sql = """
                INSERT INTO receitas (                    
                    idIntegracao,                   
                    id_cloud, 
                    idAtoExecucaoFiscal,
                    idAtoInscrito,                                               
                    idAtoNaoInscrito, 
                    descricao,
                    abreviatura,
                    classificacao,
                    tipoVinculoAtoInscrito,
                    codigoTCE,
                    tipoVinculoAtoNaoInscrito,                    
                    inscDividaAtiva
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idAtoExecucaoFiscal)s,
                    %(idAtoInscrito)s,
                    %(idAtoNaoInscrito)s,
                    %(descricao)s,
                    %(abreviatura)s,
                    %(classificacao)s,
                    %(tipoVinculoAtoInscrito)s,
                    %(codigoTCE)s,
                    %(tipoVinculoAtoNaoInscrito)s,                    
                    %(inscDividaAtiva)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idAtoExecucaoFiscal = idAtoExecucaoFiscal,
                idAtoInscrito = idAtoInscrito,
                idAtoNaoInscrito = idAtoNaoInscrito,                               
                descricao = descricao,
                abreviatura = abreviatura,
                classificacao = classificacao,                               
                tipoVinculoAtoInscrito = tipoVinculoAtoInscrito,
                codigoTCE = codigoTCE,
                tipoVinculoAtoNaoInscrito = tipoVinculoAtoNaoInscrito,                                               
                inscDividaAtiva = inscDividaAtiva
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {receitas} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {receitas}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM receitas"
            if not self.query(sql_s):
                send_log_warning(f"receitas n??o encontrado para excluir.")
                return
            sql_d = f"DELETE FROM receitas WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias exclu??dos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de exclus??o do atividades econ??micas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM receitas WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} n??o encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    receitas 
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
            send_log_error(f"Erro ao executar a opera????o de atualiza????o da atividades Economicas. {error}")

    def db_search(self, id):
        try:
            sql = f"SELECT * FROM receitas WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} n??o encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM receitas WHERE id_cloud is null"
            data = self.query(sql)
            if data:
                send_log_info("Consulta de todos os atividades Economicas realizada com sucesso.")
                return data
            return None
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de busca. {error}")

    def get_id_cloud(self, id):
        if (id == None):
            return None
        try:
            sql = f"SELECT id_cloud FROM receitas WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} n??o encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a opera????o de busca. {error}")

    def send_post(self, id, idAtoExecucaoFiscal, idAtoInscrito, idAtoNaoInscrito, descricao, abreviatura, codigoTCE, classificacao, tipoVinculoAtoInscrito, 
                tipoVinculoAtoNaoInscrito, inscDividaAtiva):
        objeto = {
            "idIntegracao": f"receitas{id}",
            "content": {}                                 
        }
        if idAtoExecucaoFiscal:
            objeto["content"]["idAtoExecucaoFiscal"] = { "id": int(idAtoExecucaoFiscal)}          
        
        if tipoVinculoAtoInscrito:
            objeto["content"]["tipoVinculoAtoInscrito"] = f"{tipoVinculoAtoInscrito}"

        if idAtoInscrito:
            objeto["content"]["idAtoInscrito"] = { "id": int(idAtoInscrito)}           
        
        if descricao:
            objeto["content"]["descricao"] = f"{descricao}"  

        if abreviatura:
            objeto["content"]["abreviatura"] = f"{abreviatura}"

        if classificacao:
            objeto["content"]["classificacao"] = f"{classificacao}"   

        if inscDividaAtiva:
            objeto["content"]["inscDividaAtiva"] = f"{inscDividaAtiva}"
        
        if tipoVinculoAtoNaoInscrito:
            objeto["content"]["tipoVinculoAtoNaoInscrito"] = f"{tipoVinculoAtoNaoInscrito}"
        
        if codigoTCE:
            objeto["content"]["codigoTCE"] = f"{codigoTCE}"

        if idAtoNaoInscrito != None:
            objeto[0]["content"]["idAtoNaoInscrito"] = { "id": int(idAtoNaoInscrito) }               
            
        envio = api_post("receitas", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

receitas = receitas()