from samples import *
import json

class economicos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idAgrupamento, idBairro, idBanco, idCondominio, idContador, idDistrito, idEconomico, idHorarioFuncionamento, 
                  idImovel, idLogradouro, idLoteamento, idMunicipios, idPessoa, idPessoasEnderecos, idTipoEntidadeEspecial, dataValidadeAlvara, apartamento, bloco,
                  cep, complemento, descricaoEndereco, numero, iEconomicos, economicoPrincipal, regimeCobrancaIss, situacaoEconomico, tipoContribuinte):
        try: 
            sql = """
                INSERT INTO economicos (                    
                    idIntegracao,                   
                    id_cloud, 
                    idAgrupamento,
                    idBairro,                                               
                    idBanco, 
                    idCondominio,
                    idContador,
                    idEconomico,
                    idHorarioFuncionamento,
                    idDistrito,
                    idImovel,                    
                    idLogradouro,
                    idLoteamento,
                    idMunicipios,
                    idPessoa,
                    idPessoasEnderecos,
                    idTipoEntidadeEspecial,
                    dataValidadeAlvara,
                    apartamento,
                    bloco,
                    cep,
                    complemento,
                    descricaoEndereco, 
                    numero,
                    iEconomicos, 
                    economicoPrincipal,
                    regimeCobrancaIss,
                    situacaoEconomico, 
                    tipoContribuinte
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idAgrupamento)s,
                    %(idBairro)s,
                    %(idBanco)s,
                    %(idCondominio)s,
                    %(idContador)s,
                    %(idEconomico)s,
                    %(idHorarioFuncionamento)s,
                    %(idDistrito)s,
                    %(idImovel)s,                    
                    %(idLogradouro)s,
                    %(idLoteamento)s,
                    %(idMunicipios)s,
                    %(idPessoa)s,
                    %(idPessoasEnderecos)s,
                    %(idTipoEntidadeEspecial)s,
                    %(dataValidadeAlvara)s,
                    %(bloco)s,                    
                    %(apartamento)s,
                    %(cep)s,                    
                    %(complemento)s,
                    %(descricaoEndereco)s,
                    %(numero)s,
                    %(iEconomicos)s,
                    %(economicoPrincipal)s,
                    %(regimeCobrancaIss)s,
                    %(situacaoEconomico)s,
                    %(tipoContribuinte)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idAgrupamento = idAgrupamento,
                idBairro = idBairro,
                idBanco = idBanco,                               
                idCondominio = idCondominio,
                idContador = idContador,
                idEconomico = idEconomico,                               
                idHorarioFuncionamento = idHorarioFuncionamento,
                idDistrito = idDistrito,
                idImovel = idImovel,                                               
                idLogradouro = idLogradouro,
                idLoteamento = idLoteamento,                               
                idMunicipios = idMunicipios,
                idPessoa = idPessoa,
                idPessoasEnderecos = idPessoasEnderecos,                               
                idTipoEntidadeEspecial = idTipoEntidadeEspecial,
                dataValidadeAlvara = dataValidadeAlvara,
                cep = cep,
                bloco = bloco,
                apartamento = apartamento,
                complemento = complemento,
                descricaoEndereco = descricaoEndereco, 
                numero = numero, 
                iEconomicos = iEconomicos, 
                economicoPrincipal = economicoPrincipal, 
                regimeCobrancaIss = regimeCobrancaIss, 
                situacaoEconomico = situacaoEconomico, 
                tipoContribuinte = tipoContribuinte
            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {economicos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao inserir o anistias {economicos}. {contribuintesr}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM economicos"
            if not self.query(sql_s):
                send_log_warning(f"economicos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM economicos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de exclusão do atividades econômicas. {contribuintesr}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM economicos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    economicos 
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
            sql = f"SELECT * FROM economicos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def db_list(self):
        try:
            sql = "SELECT * FROM economicos WHERE id_cloud is null"
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
            sql = f"SELECT id_cloud FROM economicos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as contribuintesr:
            send_log_error(f"contribuintes ao executar a operação de busca. {contribuintesr}")

    def send_post(self, id, idAgrupamento, idBairro, idBanco, idCondominio, idContador, idDistrito, idEconomico, idHorarioFuncionamento, 
                  idImovel, idLogradouro, idLoteamento, idMunicipios, idPessoa, idPessoasEnderecos, idTipoEntidadeEspecial, dataValidadeAlvara, apartamento, bloco,
                  cep, complemento, descricaoEndereco, numero, iEconomicos, economicoPrincipal, regimeCobrancaIss, situacaoEconomico, tipoContribuinte):
        objeto = {
            "idIntegracao": f"Atos{id}",
            "content": {}
        }
        if idAgrupamento:
            objeto["content"]["VctoFeriado"] = { "id": int(idAgrupamento)}
        
        if idBanco:
            objeto["content"]["idBanco"] = { "id": int(idBanco)}
        
        if idBairro:
            objeto["content"]["idBairro"] = { "id": int(idBairro)}
        
        if idCondominio:
            objeto["content"]["idCondominio"] = { "id": int(idCondominio)}
        
        if idTipoEntidadeEspecial:
            objeto["content"]["idTipoEntidadeEspecial"] = { "id": int(idTipoEntidadeEspecial)}
        
        if dataValidadeAlvara:
            objeto["content"]["dataValidadeAlvara"] = f"{dataValidadeAlvara}"
        
        if idContador:
            objeto["content"]["idContador"] = { "id": int(idContador)}
        
        if idEconomico:
            objeto["content"]["idEconomico"] = { "id": int(idEconomico)}
        
        if apartamento:
            objeto["content"]["apartamento"] = f"{apartamento}"       

        if complemento:
            objeto["content"]["complemento"] = f"{complemento}"
        
        if idPessoasEnderecos:
            objeto["content"]["idPessoasEnderecos"] = { "id": int(idPessoasEnderecos)} 

        if bloco:
            objeto["content"]["bloco"] = f"{bloco}"

        if cep:
            objeto["content"]["cep"] = f"{cep}"

        if idDistrito:
            objeto["content"]["idDistrito"] = { "id": int(idDistrito)}     

        if idHorarioFuncionamento:
            objeto["content"]["idHorarioFuncionamento"] = { "id": int(idHorarioFuncionamento)}    

        if idImovel:
            objeto["content"]["idImovel"] = { "id": int(idImovel)}

        if idLogradouro:
            objeto["content"]["idLogradouro"] = { "id": int(idLogradouro)}

        if idLoteamento:
            objeto["content"]["idLoteamento"] = { "id": int(idLoteamento)}

        if descricaoEndereco:
            objeto["content"]["descricaoEndereco"] = f"{descricaoEndereco}"     

        if numero:
            objeto["content"]["numero"] = f"{numero}"    

        if iEconomicos:
            objeto["content"]["iEconomicos"] = f"{iEconomicos}"

        if economicoPrincipal:
            objeto["content"]["economicoPrincipal"] = f"{economicoPrincipal}"

        if regimeCobrancaIss:
            objeto["content"]["regimeCobrancaIss"] = f"{regimeCobrancaIss}"  

        if situacaoEconomico:
            objeto["content"]["situacaoEconomico"] = f"{situacaoEconomico}"

        if tipoContribuinte:
            objeto["content"]["tipoContribuinte"] = f"{tipoContribuinte}"
        if idPessoa != None:
            objeto[0]["calculotributario"]["creditotributario"] = { "id": int(idPessoa)}  
        
        if idMunicipios:
            objeto["content"]["idMunicipios"] = { "id": int(idMunicipios)}   

        envio = api_post("economicos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

economicos = economicos()