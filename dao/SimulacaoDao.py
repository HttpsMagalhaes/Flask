from model import Simulacao

SQL_SELECT_SIMULACAO = 'SELECT * FROM simulacao'
SQL_SELECT_SIMULACAO_ID = 'SELECT * FROM simulacao WHERE idSimulacao=%s'

SQL_INSERT_SIMULACAO = ('INSERT INTO simulacao '
'(data_inicial, data_final, preco_unitario, quantidade, preco_final, sigla_bolsa_valor) '
'VALUES (%s, %s, %s, %s, %s, %s)')

SQL_UPDATE_SIMULACAO = ('UPDATE simulacao SET data_inicial=%s, '
    'data_final=%s, preco_unitario=%s, quantidade=%s, preco_final=%s, sigla_bolsa_valor=%s'
    'WHERE idSimulacao=%s')

SQL_DELETE_SIMULACAO = 'DELETE FROM simulacao WHERE idSimulacao=%s'

class SimulacaoDao:

    def __init__(self, db):
        self.__db = db #passa o banco

    def salvar(self, simulacao):
        cursor = self.__db.connection.cursor() #banco chama a conexao
        # insert
        if simulacao.idSimulacao is None:
            cursor.execute(SQL_INSERT_SIMULACAO,
                (simulacao.data_inicial, simulacao.data_final,
                 simulacao.preco_unitario, simulacao.quantidade,
                 simulacao.preco_final, simulacao.sigla_bolsa_valor))
            simulacao.idSimulacao = cursor.lastrowid
        else: # update
            cursor.execute(SQL_UPDATE_SIMULACAO,
                (simulacao.data_inicial, simulacao.data_final,
                 simulacao.preco_unitario, simulacao.quantidade,
                 simulacao.preco_final, simulacao.sigla_bolsa_valor, simulacao.id))

        self.__db.connection.commit()
        return simulacao

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_SIMULACAO)
        lista_tuplas = cursor.fetchall()
        lista_simulacoes = self.__traduz_simulacoes(lista_tuplas)
        return lista_simulacoes

    def listar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_SIMULACAO_ID, (id,))
        tupla = cursor.fetchone()
        sim = self.__traduz_simulacao(tupla)
        return sim

    def deletar(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_DELETE_SIMULACAO, (id,))
        self.__db.connection.commit()

    def __traduz_simulacao(self, tupla):
        # tupla[0] é o idSimulacao, os outros campos seguem a ordem do banco
        sim = Simulacao(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[0])
        return sim

    def __traduz_simulacoes(self, lista):
        lista_simulacoes = []
        for tupla in lista:
            sim = self.__traduz_simulacao(tupla)
            lista_simulacoes.append(sim)
        return lista_simulacoes