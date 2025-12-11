from flask import flash, render_template, request, redirect
from dao.BolsaDao import BolsaDao
from model import Bolsa_valores

def init_bolsa_routes(app, db):
    dao = BolsaDao(db)

    @app.route('/inicio_bolsa')
    def listar_bolsa():
        lista_bolsas = dao.listar()
        return render_template('listar_bolsa.html', titulo='Bolsas de Valores', lista=lista_bolsas)

    @app.route('/novo_bolsa')
    def novo_bolsa():
        return render_template('criar_bolsa.html', titulo='Nova Bolsa', bolsa=None)

    @app.route('/criar_bolsa', methods=['POST'])
    def criar_bolsa():
        sigla = request.form['sigla']
        descricao = request.form['descricao']
        setor = request.form['setor']
        empresa = request.form['empresa']

        bolsa = Bolsa_valores(sigla, descricao, setor, empresa)

        dao.salvar(bolsa)
        flash('Bolsa cadastrada com sucesso!')
        return redirect('/inicio_bolsa')

    @app.route('/editar_bolsa/<int:id>')
    def editar_bolsa(id):
        bolsa = dao.listar_por_id(id)
        return render_template('editar_bolsa.html', titulo='Editar Bolsa', bolsa=bolsa)

    @app.route('/atualizar_bolsa', methods=['POST'])
    def atualizar_bolsa():
        id_bolsa = request.form['id']
        sigla = request.form['sigla']
        descricao = request.form['descricao']
        setor = request.form['setor']
        empresa = request.form['empresa']

        bolsa = Bolsa_valores(sigla, descricao, setor, empresa, idBolsa_valores=id_bolsa)

        dao.salvar(bolsa)
        flash('Bolsa atualizada com sucesso!')
        return redirect('/inicio_bolsa')

    @app.route('/deletar_bolsa/<int:id>')
    def deletar_bolsa(id):
        dao.deletar(id)
        flash('Bolsa deletada com sucesso!')
        return redirect('/inicio_bolsa')