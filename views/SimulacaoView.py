from flask import flash, render_template, request, redirect
from dao.SimulacaoDao import SimulacaoDao
from model import Simulacao

def init_simulacao_routes(app, db):
    dao = SimulacaoDao(db)

    @app.route('/inicio_simulacao')
    def listar_simulacao():
        lista_simulacoes = dao.listar()
        return render_template('listar_simulacao.html', titulo='Simulações', lista=lista_simulacoes)

    @app.route('/novo_simulacao')
    def novo_simulacao():
        return render_template('criar_simulacao.html', titulo='Nova Simulação', simulacao=None)

    @app.route('/criar_simulacao', methods=['POST'])
    def criar_simulacao():
        data_inicial = request.form['data_inicial']
        data_final = request.form['data_final']
        preco_unitario = request.form['preco_unitario']
        quantidade = request.form['quantidade']
        preco_final = request.form['preco_final']
        sigla_bolsa_valor = request.form['sigla_bolsa_valor']

        simulacao = Simulacao(data_inicial, data_final, preco_unitario, quantidade, preco_final, sigla_bolsa_valor)

        dao.salvar(simulacao)
        flash('Simulação salva com sucesso!')
        return redirect('/inicio_simulacao')

    @app.route('/editar_simulacao/<int:id>')
    def editar_simulacao(id):
        simulacao = dao.listar_por_id(id)
        return render_template('editar_simulacao.html', titulo='Editar Simulação', simulacao=simulacao)

    @app.route('/atualizar_simulacao', methods=['POST'])
    def atualizar_simulacao():
        id_simulacao = request.form['id']
        data_inicial = request.form['data_inicial']
        data_final = request.form['data_final']
        preco_unitario = request.form['preco_unitario']
        quantidade = request.form['quantidade']
        preco_final = request.form['preco_final']
        sigla_bolsa_valor = request.form['sigla_bolsa_valor']

        simulacao = Simulacao(data_inicial, data_final, preco_unitario, quantidade, preco_final, sigla_bolsa_valor, idSimulacao=id_simulacao)

        dao.salvar(simulacao)
        flash('Simulação atualizada com sucesso!')
        return redirect('/inicio_simulacao')

    @app.route('/deletar_simulacao/<int:id>')
    def deletar_simulacao(id):
        dao.deletar(id)
        flash('Simulação deletada com sucesso!')
        return redirect('/inicio_simulacao')