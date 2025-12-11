from flask import flash, render_template, request, redirect
from dao.EmpresaDao import EmpresaDao
from model import Empresa
from utils.ValidaDados import ValidaDados

def init_empresa_routes(app, db):
    dao = EmpresaDao(db)

    @app.route('/inicio_empresa')
    def listar_empresa():
        lista_empresas = dao.listar()
        return render_template('listar_empresa.html', titulo='Empresas', lista=lista_empresas)

    @app.route('/novo_empresa')
    def novo_empresa():
        return render_template('criar_empresa.html', titulo='Nova Empresa', empresa=None)

    @app.route('/criar_empresa', methods=['POST'])
    def criar_empresa():
        nome = request.form['nome']
        sigla = request.form['sigla']
        cnpj = request.form['cnpj']
        descricao = request.form['descricao']

        empresa = Empresa(nome, sigla, cnpj, descricao)

        # VALIDAÇÃO
        if ValidaDados.eh_cnpj(cnpj):
            dao.salvar(empresa)
            flash('Empresa cadastrada com sucesso!')
            return redirect('/inicio_empresa')
        else:
            flash('CNPJ Inválido! Verifique os números.')
            return render_template('criar_empresa.html', titulo='Nova Empresa', empresa=empresa)

    @app.route('/editar_empresa/<int:id>')
    def editar_empresa(id):
        empresa = dao.listar_por_id(id)
        return render_template('editar_empresa.html', titulo='Editar Empresa', empresa=empresa)

    @app.route('/atualizar_empresa', methods=['POST'])
    def atualizar_empresa():

        id_empresa = request.form['id']
        nome = request.form['nome']
        sigla = request.form['sigla']
        cnpj = request.form['cnpj']
        descricao = request.form['descricao']

        empresa = Empresa(nome, sigla, cnpj, descricao, idEmpresa=id_empresa)

        dao.salvar(empresa)
        flash('Empresa atualizada com sucesso!')
        return redirect('/inicio_empresa')

    @app.route('/deletar_empresa/<int:id>')
    def deletar_empresa(id):
        dao.deletar(id)
        flash('Empresa deletada com sucesso!')
        return redirect('/inicio_empresa')