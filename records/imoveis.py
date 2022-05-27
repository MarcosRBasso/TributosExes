from samples import *
import json

class imoveis(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idAgrupamento, idBairro, idCondominio, idCorresponsavel, idDistrito, idFace, idReceitaTaxaExpediente, idImovel, 
                  idLocalidade, idLogradouro, idLoteamento, idPessoa, idPessoasEnderecos, idSecoes, iImoveis, campo1, campo2, campo3,
                  campo4, campo5, campo6, campo7, campo8, campo9, campo10, apartamento, 
                  bloco, cep, complemento, denominacao, 
                  enderecoCorrespondencia, inscricaoAnterior, inscricaoIncra, latitude, longitude, lote, matricula, nroImovel, quadra,
                  setor, tipoImovel, unidade, situacao, garagem, sala, loja, dtConstrucao):
        try: 
            sql = """
                INSERT INTO imoveis (                    
                    idIntegracao,                   
                    id_cloud, 
                    idAgrupamento,
                    idBairro,                                               
                    idCondominio, 
                    idCorresponsavel,
                    idDistrito,
                    idReceitaTaxaExpediente,
                    idImovel,
                    idFace,
                    idLocalidade,                    
                    idLogradouro,
                    idLoteamento,
                    idPessoa,
                    idPessoasEnderecos,
                    idSecoes,
                    iImoveis,
                    campo1,
                    campo2,
                    campo3,
                    campo4,
                    campo5,
                    campo6, 
                    campo7,
                    campo8, 
                    campo9,
                    campo10,
                    apartamento, 
                    bloco, 
                    cep,
                    complemento,
                    denominacao,
                    enderecoCorrespondencia,
                    inscricaoAnterior,
                    inscricaoIncra,
                    latitude,
                    longitude,
                    lote, 
                    matricula, 
                    nroImovel, 
                    quadra, 
                    setor, 
                    tipoImovel, 
                    unidade, 
                    situacao,
                    garagem, 
                    sala, 
                    loja, 
                    dtConstrucao
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idAgrupamento)s,
                    %(idBairro)s,
                    %(idCondominio)s,
                    %(idCorresponsavel)s,
                    %(idDistrito)s,
                    %(idReceitaTaxaExpediente)s,
                    %(idImovel)s,
                    %(idFace)s,
                    %(idLocalidade)s,                    
                    %(idLogradouro)s,
                    %(idLoteamento)s,
                    %(idPessoa)s,
                    %(idPessoasEnderecos)s,
                    %(idSecoes)s,
                    %(iImoveis)s,
                    %(campo1)s,
                    %(campo4)s,
                    %(campo3)s,                    
                    %(campo2)s,
                    %(campo4)s,                    
                    %(campo5)s,
                    %(campo6)s,
                    %(campo7)s,
                    %(campo8)s,
                    %(campo9)s,
                    %(campo10)s,
                    %(apartamento)s,
                    %(bloco)s,
                    %(cep)s,
                    %(complemento)s,                    
                    %(denominacao)s,
                    %(enderecoCorrespondencia)s,
                    %(inscricaoAnterior)s,
                    %(inscricaoIncra)s,
                    %(latitude)s,
                    %(longitude)s,
                    %(lote)s,
                    %(matricula)s,
                    %(nroImovel)s,
                    %(quadra)s,                    
                    %(setor)s,
                    %(tipoImovel)s,
                    %(unidade)s,
                    %(situacao)s,
                    %(garagem)s, 
                    %(sala)s, 
                    %(loja)s, 
                    %(dtConstrucao)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idAgrupamento = idAgrupamento,
                idBairro = idBairro,
                idCondominio = idCondominio,                               
                idCorresponsavel = idCorresponsavel,
                idDistrito = idDistrito,
                idReceitaTaxaExpediente = idReceitaTaxaExpediente,                               
                idImovel = idImovel,
                idFace = idFace,
                idLocalidade = idLocalidade,                                               
                idLogradouro = idLogradouro,
                idLoteamento = idLoteamento,                               
                idPessoa = idPessoa,
                idPessoasEnderecos = idPessoasEnderecos,
                idSecoes = idSecoes,                               
                iImoveis = iImoveis,
                campo1 = campo1,
                campo4 = campo4,
                campo3 = campo3,
                campo2 = campo2,
                campo5 = campo5,
                campo6 = campo6, 
                campo7 = campo7, 
                campo8 = campo8, 
                campo9 = campo9, 
                campo10 = campo10, 
                apartamento = apartamento, 
                bloco = bloco, 
                cep = cep, 
                complemento = complemento, 
                denominacao = denominacao, 
                enderecoCorrespondencia = enderecoCorrespondencia, 
                inscricaoAnterior = inscricaoAnterior, 
                inscricaoIncra = inscricaoIncra,   
                latitude = latitude, 
                longitude = longitude, 
                lote = lote, 
                matricula = matricula, 
                nroImovel = nroImovel, 
                quadra = quadra, 
                setor = setor, 
                tipoImovel = tipoImovel, 
                unidade = unidade, 
                situacao = situacao,
                garagem = garagem, 
                sala = sala, 
                loja = loja, 
                dtConstrucao = dtConstrucao
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {imoveis} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao inserir o anistias {imoveis}. {contribuintesr}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM imoveis"
            if not self.query(sql_s):
                send_log_warning(f"imoveis não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM imoveis WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de exclusão do atividades econômicas. {contribuintesr}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM imoveis WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    imoveis 
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
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de atualização da atividades Economicas. {contribuintesr}")

    def db_search(self, id):
        try:
            sql = f"SELECT * FROM imoveis WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def db_list(self):
        try:
            sql = "SELECT * FROM imoveis WHERE id_cloud is null"
            data = self.query(sql)
            if data:
                send_log_info("Consulta de todos os atividades Economicas realizada com sucesso.")
                return data
            return None
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def get_id_cloud(self, id):
        if (id == None):
            return None
        try:
            sql = f"SELECT id_cloud FROM imoveis WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def send_post(self, id, idAgrupamento, idBairro, idCondominio, idCorresponsavel, idDistrito, idFace, idReceitaTaxaExpediente, idImovel, 
                  idLocalidade, idLogradouro, idLoteamento, idPessoa, idPessoasEnderecos, idSecoes, iImoveis, campo1, campo2, campo3,
                  campo4, campo5, campo6, campo7, campo8, campo9, campo10, apartamento, bloco, cep, complemento, denominacao, 
                  enderecoCorrespondencia, inscricaoAnterior, inscricaoIncra, latitude, longitude, lote, matricula, nroImovel, quadra, setor, tipoImovel, unidade,
                  situacao, garagem, sala, loja, dtConstrucao):
        objeto = {
            "idIntegracao": f"Atos{id}",
            "content": {}
        }
        if garagem:
            objeto["content"]["garagem"] = f"{garagem}"
        
        if sala:
            objeto["content"]["sala"] = f"{sala}" 

        if loja:
            objeto["content"]["loja"] = f"{loja}"

        if dtConstrucao:
            objeto["content"]["dtConstrucao"] = f"{dtConstrucao}"    
        
        if idAgrupamento:
            objeto["content"]["VctoFeriado"] = { "id": int(idAgrupamento)}
        
        if idCondominio:
            objeto["content"]["idCondominio"] = { "id": int(idCondominio)}
        
        if idBairro:
            objeto["content"]["idBairro"] = { "id": int(idBairro)}
        
        if idCorresponsavel:
            objeto["content"]["idCorresponsavel"] = { "id": int(idCorresponsavel)}
        
        if iImoveis:
            objeto["content"]["iImoveis"] = f"{iImoveis}"
        
        if campo1:
            objeto["content"]["campo1"] = f"{campo1}"
        
        if idDistrito:
            objeto["content"]["idDistrito"] = { "id": int(idDistrito)}
        
        if idReceitaTaxaExpediente:
            objeto["content"]["idReceitaTaxaExpediente"] = { "id": int(idReceitaTaxaExpediente)}
        
        if campo2:
            objeto["content"]["campo2"] = f"{campo2}"       

        if campo5:
            objeto["content"]["campo5"] = f"{campo5}"
        
        if idSecoes:
            objeto["content"]["idSecoes"] = { "id": int(idSecoes)} 

        if campo3:
            objeto["content"]["campo3"] = f"{campo3}"

        if campo4:
            objeto["content"]["campo4"] = f"{campo4}"

        if idFace:
            objeto["content"]["idFace"] = { "id": int(idFace)}     

        if idImovel:
            objeto["content"]["idImovel"] = { "id": int(idImovel)}    

        if idLocalidade:
            objeto["content"]["idLocalidade"] = { "id": int(idLocalidade)}

        if idLogradouro:
            objeto["content"]["idLogradouro"] = { "id": int(idLogradouro)}

        if idLoteamento:
            objeto["content"]["idLoteamento"] = { "id": int(idLoteamento)}

        if campo6:
            objeto["content"]["campo6"] = f"{campo6}"     

        if campo7:
            objeto["content"]["campo7"] = f"{campo7}"    

        if campo8:
            objeto["content"]["campo8"] = f"{campo8}"

        if campo9:
            objeto["content"]["campo9"] = f"{campo9}"

        if campo10:
            objeto["content"]["campo10"] = f"{campo10}"  

        if apartamento:
            objeto["content"]["apartamento"] = f"{apartamento}"

        if bloco:
            objeto["content"]["bloco"] = f"{bloco}"

        if cep:
            objeto["content"]["cep"] = f"{cep}"

        if complemento:
            objeto["content"]["complemento"] = f"{complemento}"             
        
        if denominacao:
            objeto["content"]["denominacao"] = f"{denominacao}"
        
        if enderecoCorrespondencia:
            objeto["content"]["enderecoCorrespondencia"] = f"{enderecoCorrespondencia}"

        if inscricaoAnterior:
            objeto["content"]["inscricaoAnterior"] = f"{inscricaoAnterior}"    

        if inscricaoIncra:
            objeto["content"]["inscricaoIncra"] = f"{inscricaoIncra}"

        if latitude:
            objeto["content"]["latitude"] = f"{latitude}"

        if longitude:
            objeto["content"]["longitude"] = f"{longitude}"  

        if lote:
            objeto["content"]["lote"] = f"{lote}"

        if matricula:
            objeto["content"]["matricula"] = f"{matricula}"

        if nroImovel:
            objeto["content"]["nroImovel"] = f"{nroImovel}"

        if quadra:
            objeto["content"]["quadra"] = f"{quadra}"             
        
        if setor:
            objeto["content"]["setor"] = f"{setor}"
        
        if tipoImovel:
            objeto["content"]["campo70"] = f"{tipoImovel}"            
        
        if unidade:
            objeto["content"]["unidade"] = f"{unidade}"
        
        if situacao:
            objeto["content"]["situacao"] = f"{situacao}"      
        
        if idPessoasEnderecos != None:
            objeto[0]["calculotributario"]["creditotributario"] = { "id": int(idPessoasEnderecos)}  
        
        if idPessoa:
            objeto["content"]["idPessoa"] = { "id": int(idPessoa)}   

        envio = api_post("imoveis", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

imoveis = imoveis()