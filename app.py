from flask import Flask
from flask_mysqldb import MySQL
from views.BolsaView import init_bolsa_routes
from views.SimulacaoView import init_simulacao_routes
from views.EmpresaView import init_empresa_routes


# criar a aplicacao
def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db = MySQL(app)
    init_bolsa_routes(app, db)
    init_simulacao_routes(app, db)
    init_empresa_routes(app, db)

    return app, db

if __name__ == '__main__':
    app, db = create_app()
    #rodar
    app.run(debug=True)
