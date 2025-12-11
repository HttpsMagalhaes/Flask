from model import Empresa

SQL_SELECT_EMPRESA = 'SELECT * FROM empresa'
SQL_SELECT_EMPRESA_ID = 'SELECT * FROM empresa WHERE idEmpresa=%s'

SQL_INSERT_EMPRESA = ('INSERT INTO empresa '
'(nome, sigla, cnpj, descricao) '
'VALUES (%s, %s, %s, %s)')

SQL_UPDATE_EMPRESA = ('UPDATE empresa SET nome=%s, '
    'sigla=%s, cnpj=%s, descricao=%s '
    'WHERE idEmpresa=%s')

SQL_DELETE_EMPRESA = 'DELETE FROM empresa WHERE idEmpresa=%s'

class EmpresaDao:

    def __init__(self, db):
        self.__db = db #passa o banco

    def salvar(self, empresa):
        cursor = self.__db.connection.cursor() #banco chama a conexao
        # insert
        if empresa.id is None:
            cursor.execute(SQL_INSERT_EMPRESA,
                (empresa.nome, empresa.sigla,
                 empresa.cnpj, empresa.descricao))
            empresa.id = cursor.lastrowid
        else:# update
            cursor.execute(SQL_UPDATE_EMPRESA,
                (empresa.nome, empresa.sigla,
                 empresa.cnpj, empresa.descricao, empresa.id))

        self.__db.connection.commit()
        return empresa

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_EMPRESA)
        lista_tuplas = cursor.fetchall()
        lista_empresas = self.__traduz_empresas(lista_tuplas)
        return lista_empresas

    def listar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_EMPRESA_ID, (id,))
        tupla = cursor.fetchone()
        em = self.__traduz_empresa(tupla)
        return em

    def deletar(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_DELETE_EMPRESA, (id,))
        self.__db.connection.commit()

    def __traduz_empresa(self, tupla):
        em = Empresa(tupla[1], tupla[2], tupla[3], tupla[4], tupla[0])
        return em

    def __traduz_empresas(self, lista):
        lista_empresas = []
        for tupla in lista:
            cont = self.__traduz_empresa(tupla)
            lista_empresas.append(cont)
        return lista_empresas

