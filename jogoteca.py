from flask import Flask, render_template, request, redirect, session, flash


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


lista = []


app = Flask(__name__)
app.secret_key = 'teste'


@app.route('/inicio')
def index():
    return render_template('lista.html', title='Jogos', jogos=lista)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login')
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST', ])
def criar():
    nome = request. form['nome']
    categoria = request. form['categoria']
    console = request. form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/inicio')


@app.route('/login')
def login():
    return render_template('login.html', titulo='Login')


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if request.form['senha'] == 'admin':
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' logado com sucesso!')
        return redirect('/inicio')
    else:
        flash('Não logado, tente novamente!')
        return redirect('/login')
    

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout realizado com sucesso!')
    return redirect('/login')


app.run(debug=True)
