from samples import *
import json

class lancamentos(Conexao):
    def __init__(self):
        Conexao.__init__(self)

    def db_insert(self, idIntegracao, id_cloud, idPessoa, idImoveis, idCreditosTributarios, idCalculos, ano, complementar,
                 lancamentoEnglobado, idReceitasDiversasLanctos, idEconomicos, idTransferenciaImoveis, idReceitasDiversas, situacao, idPessoaAtual, idContribuicaoMelhorias,
                 idContribMelhoriasImoveis, idNotasAvulsas, idLancamentoPrincipal,
                 idObras, dhLancamento):
        try:
            sql = """
                INSERT INTO lancamentos (                    
                    idIntegracao,                   
                    id_cloud, 
                    idPessoa,
                    idImoveis,                                               
                    idCreditosTributarios, 
                    idCalculos,
                    ano,
                    complementar,
                    lancamentoEnglobado,
                    idReceitasDiversasLanctos,
                    idEconomicos,                    
                    idTransferenciaImoveis,
                    idReceitasDiversas,
                    situacao,
                    idPessoaAtual,
                    idContribuicaoMelhorias,
                    idContribMelhoriasImoveis,
                    idNotasAvulsas,
                    idLancamentoPrincipal        
                ) VALUES (
                    %(idIntegracao)s,                    
                    %(id_cloud)s,
                    %(idPessoa)s,
                    %(idImoveis)s,
                    %(idCreditosTributarios)s,
                    %(idCalculos)s,
                    %(ano)s,
                    %(complementar)s,
                    %(lancamentoEnglobado)s,
                    %(idReceitasDiversasLanctos)s,
                    %(idEconomicos)s,                    
                    %(idTransferenciaImoveis)s,
                    %(idReceitasDiversas)s,
                    %(situacao)s,
                    %(idPessoaAtual)s,
                    %(idContribuicaoMelhorias)s,
                    %(idContribMelhoriasImoveis)s,
                    %(idNotasAvulsas)s,
                    %(dhLancamento)s,
                    %(idObras)s,                    
                    %(idLancamentoPrincipal)s
                )
            """
            data = dict (
                idIntegracao = idIntegracao,
                id_cloud = id_cloud,                               
                idPessoa = idPessoa,
                idImoveis = idImoveis,
                idCreditosTributarios = idCreditosTributarios,                               
                idCalculos = idCalculos,
                ano = ano,
                complementar = complementar,                               
                lancamentoEnglobado = lancamentoEnglobado,
                idReceitasDiversasLanctos = idReceitasDiversasLanctos,
                idEconomicos = idEconomicos,                                               
                idTransferenciaImoveis = idTransferenciaImoveis,
                idReceitasDiversas = idReceitasDiversas,                               
                situacao = situacao,
                idPessoaAtual = idPessoaAtual,
                idContribuicaoMelhorias = idContribuicaoMelhorias,                               
                idContribMelhoriasImoveis = idContribMelhoriasImoveis,
                idNotasAvulsas = idNotasAvulsas,
                dhLancamento = dhLancamento,
                idObras = idObras,
                idLancamentoPrincipal = idLancamentoPrincipal

            )
            self.execute(sql, data)
            self.commit()
            send_log_info(f"Agrupamentos {lancamentos} (id_cloud: {id_cloud}) inserido com sucesso.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao inserir o anistias {lancamentos}. {intervaloFimr}")

    def db_delete(self):
        try:
            sql_s = f"SELECT * FROM lancamentos"
            if not self.query(sql_s):
                send_log_warning(f"lancamentos não encontrado para excluir.")
                return
            sql_d = f"DELETE FROM lancamentos WHERE id is not null"
            self.execute(sql_d)
            self.commit()
            send_log_info(f"anistias excluídos com sucesso.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao executar a operação de exclusão do atividades econômicas. {intervaloFimr}")

    def db_update(self, id, id_cloud, json, mensagem):
        try:
            sql_s = f"SELECT * FROM lancamentos WHERE id = {id}"
            if not self.query(sql_s):
                send_log_warning(f"atividades Economicas {id} não encontrado para atualizar.")
                return
            sql = """
                UPDATE 
                    lancamentos 
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
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao executar a operação de atualização da atividades Economicas. {intervaloFimr}")

    def db_search(self, id):
        try:
            sql = f"SELECT * FROM lancamentos WHERE id = {id}"
            data = self.query(sql)
            if data:
                return data
            send_log_info(f"atividades Economicas {id} não encontrado.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao executar a operação de busca. {intervaloFimr}")

    def db_list(self):
        try:
            sql = "SELECT * FROM lancamentos WHERE id_cloud is null"
            data = self.query(sql)
            if data:
                send_log_info("Consulta de todos os atividades Economicas realizada com sucesso.")
                return data
            return None
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao executar a operação de busca. {intervaloFimr}")

    def get_id_cloud(self, id):
        if (id == None):
            return None
        try:
            sql = f"SELECT id_cloud FROM lancamentos WHERE id_origem = {id}"
            data = self.query(sql)
            if data:
                return data[0][0]
            send_log_info(f"atosFontesDivulgacoes {id} não encontrado.")
        except Exception as intervaloFimr:
            send_log_error(f"intervaloFim ao executar a operação de busca. {intervaloFimr}")

    def send_post(self, id, idPessoa, idImoveis, idCreditosTributarios, idCalculos, ano, idReceitasDiversasLanctos, complementar, lancamentoEnglobado, idEconomicos, idTransferenciaImoveis, 
                 idReceitasDiversas, situacao, idPessoaAtual, idContribuicaoMelhorias, idContribMelhoriasImoveis, idNotasAvulsas, idLancamentoPrincipal, idObras, 
                 dhLancamento):
        objeto = {
                    "idIntegracao": f"Atos{id}",
                    "content": {}
        }

        if idPessoa:
            objeto["content"]["idPessoa"] = { "id": int(idPessoa)}

        if idReceitasDiversasLanctos:
            objeto["content"]["idReceitasDiversasLanctos"] = { "id": int(idReceitasDiversasLanctos)}

        if lancamentoEnglobado:
            objeto["content"]["compartilhadoContribuinteMelhorias"] = f"{lancamentoEnglobado}"

        if idTransferenciaImoveis:
            objeto["content"]["idTransferenciaImoveis"] = { "id": int(idTransferenciaImoveis)}     

        if idReceitasDiversas:
            objeto["content"]["idReceitasDiversas"] = { "id": int(idReceitasDiversas)}

        if situacao:
            objeto["content"]["situacao"] = f"{situacao}"

        if dhLancamento:
            objeto["content"]["dhLancamento"] = f"{dhLancamento}"

        if idEconomicos:
            objeto["content"]["idEconomicos"] = { "id": int(idEconomicos)}             
        
        if idCalculos:
            objeto["content"]["idCalculos"] = { "id": int(idCalculos)}
        
        if idPessoaAtual:
            objeto["content"]["idPessoaAtual"] = { "id": int(idPessoaAtual)}
        
        if idImoveis:
            objeto["content"]["idImoveis"] = { "id": int(idImoveis)}
        
        if idCreditosTributarios:
            objeto["content"]["idCreditosTributarios"] = { "id": int(idCreditosTributarios)}
        
        if idContribMelhoriasImoveis:
            objeto["content"]["CasasDecimais"] = { "id": int(idContribMelhoriasImoveis)}
        
        if idNotasAvulsas:
            objeto["content"]["MaximoDigitos"] = { "id": int(idNotasAvulsas)}
        
        if ano:
            objeto["content"]["anos"] = f"{ano}"
        
        if complementar:
            objeto["content"]["CompartilhadoCondominio"] = f"{complementar}"
        
        if idLancamentoPrincipal:
            objeto["content"]["idLancamentoPrincipal"] = { "id": int(idLancamentoPrincipal)}
        
        if idContribuicaoMelhorias:
            objeto["content"]["LivroEletronico"] = { "id": int(idContribuicaoMelhorias)}
        
        if idObras:
            objeto["content"]["idObras"] = { "id": int(idObras)}

        envio = api_post("lancamentos", objeto)

        if (envio["code"] == 200 or envio["code"] == 201):
            self.db_update(id, envio["mensagem"], json.dumps(objeto, ensure_ascii=False), None)
        else:
            self.db_update(id, None, json.dumps(objeto), json.dumps(envio["mensagem"], ensure_ascii=False))

lancamentos = lancamentos()