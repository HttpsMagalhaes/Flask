class Bolsa_valores:
    def __init__(self, sigla, descricao, setor, empresa, idBolsa_valores=None):
        self.sigla = sigla
        self.descricao = descricao
        self.setor = setor
        self.empresa = empresa
        self.idBolsa_valores = idBolsa_valores

    def __str__(self):
        return self.sigla

class Simulacao:
    def __init__(self, data_inicial, data_final, preco_unitario, quantidade, preco_final, sigla_bolsa_valor, idSimulacao=None):
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade
        self.preco_final = preco_final
        self.sigla_bolsa_valor = sigla_bolsa_valor
        self.idSimulacao = idSimulacao

    def __str__(self):
        return self.preco_final

class Empresa:
    def __init__(self, nome, sigla, cnpj, descricao, idEmpresa=None):
        self.nome = nome
        self.sigla = sigla
        self.cnpj = cnpj
        self.descricao = descricao
        self.idEmpresa = idEmpresa

    def __str__(self):
        return self.nome