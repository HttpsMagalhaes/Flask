from model import Bolsa_valores

SQL_SELECT_BOLSA = 'SELECT * FROM bolsa_valores'
SQL_SELECT_BOLSA_ID = 'SELECT * FROM bolsa_valores WHERE idBolsa_valores=%s'

SQL_INSERT_BOLSA = ('INSERT INTO bolsa_valores '
'(sigla, descricao, setor, empresa) '
'VALUES (%s, %s, %s, %s)')

SQL_UPDATE_BOLSA = ('UPDATE bolsa_valores SET sigla=%s, '
    'descricao=%s, setor=%s, empresa=%s '
    'WHERE idBolsa_valores=%s')

SQL_DELETE_BOLSA = 'DELETE FROM bolsa_valores WHERE idBolsa_valores=%s'

class BolsaDao:

    def __init__(self, db):
        self.__db = db #passa o banco

    def salvar(self, bolsa):
        cursor = self.__db.connection.cursor() #banco chama a conexao
        # insert
        if bolsa.id is None:
            cursor.execute(SQL_INSERT_BOLSA,
                (bolsa.sigla, bolsa.descricao,
                 bolsa.setor, bolsa.empresa))
            bolsa.id = cursor.lastrowid
        else:# update
            cursor.execute(SQL_UPDATE_BOLSA,
                (bolsa.sigla, bolsa.descricao,
                 bolsa.setor, bolsa.empresa, bolsa.id))

        self.__db.connection.commit()
        return bolsa

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_BOLSA)
        lista_tuplas = cursor.fetchall()
        lista_bolsas = self.__traduz_bolsas(lista_tuplas)
        return lista_bolsas

    def listar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_BOLSA_ID, (id,))
        tupla = cursor.fetchone()
        bl = self.__traduz_bolsa(tupla)
        return bl

    def deletar(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_DELETE_BOLSA, (id,))
        self.__db.connection.commit()

    def __traduz_bolsa(self, tupla):
        bl = Bolsa_valores(tupla[1], tupla[2], tupla[3], tupla[4], tupla[0])
        return bl

    def __traduz_bolsas(self, lista):
        lista_bolsas = []
        for tupla in lista:
            cont = self.__traduz_bolsa(tupla)
            lista_bolsas.append(cont)
        return lista_bolsas

