from samples import *
import json

class desmembramentos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idCampoIncrementar, idEngenheiroArquiteto, idImovel, descricao, codigoARTRRT, dataAprovacao, dataCancelamento, dataDesmembramento, 
                nrProcessoAprovacao, nrProcessoCancelamento, observacao, metragemMinimaLotes, qtdadeLotesGerar, situacaoProjeto):
        try:
            sql = """
                INSERT INTO desmembramentos (                    
                    idIntegracao,                   
                    id_cloud, 
                    idCampoIncrementar,
                    idEngenheiroArquiteto,                                               
                    idImovel, 
                    descricao,
                    codigoARTRRT,
                    dataCancelamento,
                    dataDesmembramento,
                    dataAprovacao,
                    nrProcessoAprovacao,                    
                    nrProcessoCancelamento,
                    observacao,
                    metragemMinimaLotes,
                    qtdadeLotesGerar,
                    situacaoProjeto                 
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idCampoIncrementar)s,
                    %(idEngenheiroArquiteto)s,
                    %(idImovel)s,
                    %(descricao)s,
                    %(codigoARTRRT)s,
                    %(dataCancelamento)s,
                    %(dataDesmembramento)s,
                    %(dataAprovacao)s,
                    %(nrProcessoAprovacao)s,                    
                    %(nrProcessoCancelamento)s,
                    %(observacao)s,
                    %(metragemMinimaLotes)s,
                    %(qtdadeLotesGerar)s,
                    %(situacaoProjeto)s
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idCampoIncrementar = idCampoIncrementar,
                idEngenheiroArquiteto = idEngenheiroArquiteto,
                idImovel = idImovel,                               
                descricao = descricao,
                codigoARTRRT = codigoARTRRT,
                dataCancelamento = dataCancelamento,                               
                dataDesmembramento = dataDesmembramento,
                dataAprovacao = dataAprovacao,
                nrProcessoAprovacao = nrProcessoAprovacao,                                               
                nrProcessoCancelamento = nrProcessoCancelamento,
                observacao = observacao,                               
                metragemMinimaLotes = metragemMinimaLotes,
                qtdadeLotesGerar = qtdadeLotesGerar,
                situacaoProjeto = situacaoProjeto
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {desmembramentos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao inserir o anistias {desmembramentos}. {error}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM desmembramentos"
            if not self.query(sql_s):
                send_log_warning(f"desmembramentos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM desmembramentos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de exclusão do atividades econômicas. {error}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM desmembramentos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    desmembramentos 
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
            sql = f"SELECT * FROM desmembramentos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def db_list(self):
        try:
            sql = "SELECT * FROM desmembramentos WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM desmembramentos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as error:
            send_log_error(f"Erro ao executar a operação de busca. {error}")

    def send_post(self, id, idCampoIncrementar, idEngenheiroArquiteto, idImovel, descricao, codigoARTRRT, dataAprovacao, dataCancelamento, dataDesmembramento, 
                nrProcessoAprovacao, nrProcessoCancelamento, observacao, metragemMinimaLotes, qtdadeLotesGerar, situacaoProjeto):
        objeto = {
            "idIntegracao": f"desmembramentos{id}",
            "content": {}                                 
        }
        if idCampoIncrementar:
            objeto["content"]["idCampoIncrementar"] = { "id": int(idCampoIncrementar)}
        
        if dataDesmembramento:
            objeto["content"]["dataDesmembramento"] = f"{dataDesmembramento}"

        if idEngenheiroArquiteto:
            objeto["content"]["idEngenheiroArquiteto"] = { "id": int(idEngenheiroArquiteto)}           
        
        if descricao:
            objeto["content"]["descricao"] = f"{descricao}" 

        if observacao:
            objeto["content"]["observacao"] = f"{observacao}"  

        if codigoARTRRT:
            objeto["content"]["codigoARTRRT"] = f"{codigoARTRRT}"

        if dataCancelamento:
            objeto["content"]["dataCancelamento"] = f"{dataCancelamento}"   

        if nrProcessoCancelamento:
            objeto["content"]["nrProcessoCancelamento"] = f"{nrProcessoCancelamento}"
        
        if nrProcessoAprovacao:
            objeto["content"]["nrProcessoAprovacao"] = f"{nrProcessoAprovacao}"
           
        if metragemMinimaLotes:
            objeto["content"]["metragemMinimaLotes"] = f"{metragemMinimaLotes}"
        
        if situacaoProjeto:
            objeto["content"]["situacaoProjeto"] = f"{situacaoProjeto}"
        
        if dataAprovacao:
            objeto["content"]["dataAprovacao"] = f"{dataAprovacao}"

        if idImovel != None:
            objeto[0]["content"]["idImovel"] = { "id": int(idImovel) }               

        if qtdadeLotesGerar != None:
            objeto[0]["content"]["qtdadeLotesGerar"] = { "id": int(qtdadeLotesGerar) }        
            
        envio = api_post("desmembramentos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

desmembramentos = desmembramentos()