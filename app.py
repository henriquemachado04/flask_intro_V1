from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # return "Olá meu nome é Henrique"
    return render_template('index.html')

@app.route('/variaveis')
def variaveis():
    nome = "LindHenrique"
    return render_template('variaveis.html', usuario = nome)

@app.route('/listas')
def listas():
    itens = ['Item 1', 'Item 2', 'Item 3']
    return render_template('listas.html', itens = itens)

@app.route('/dicionarios')
def dicionarios():
    usuario_info= {
        "nome": "Henrique",
        "idade": 20,
        "cidade": "Jaraguá so Sul",
        "interesses": ["Desenho", "Brincar com bloquinhos", "Jogos Vorazes"]
    }
    return render_template('dicionarios.html', usuario=usuario_info)

@app.route('/listas_dicionarios')
def listas_dicionarios():
    usuarios = [
        {"nome": "Henrique", "idade": 20, "cidade": "Jaraguá do Sul"},
        {"nome": "Gabrieli", "idade": 18, "cidade": "Guaramirim"},
        {"nome": "Paula", "idade": 9, "cidade": "Jaraguá do Sul"},
    ]
    return render_template('listas_dicionarios.html', usuarios=usuarios)

@app.route('/controle_fluxo_condicionais')
def controle_fluxo_condicionais():
    usuario = {
        "nome": "Henrique",
        "idade": 20,
        "cidade": "Jaraguá do Sul",
        "premium": True,
    }
    return render_template('controle_fluxo_condicionais.html', usuario=usuario)

@app.route('/filtros_jinja')
def filtros_jinja():
    usuario = {
        "nome": "Henrique",
        "idade": 20,
        "cidade": "Jaraguá do Sul",
    }
    mensagem = "Bem-vindo ao nosso site!"
    return render_template('filtros_jinja.html', usuario=usuario, mensagem=mensagem)

@app.route('/listas_postagem')
def listas_postagem():
    postagens = [
        {"Id": 1, "Título": "A proura do Amor", "Conteúdo": "Palavras de amor."},
        {"Id": 2, "Título": "Encontrando o Amor", "Conteúdo": "Como encontrar o seu amor."},
        {"Id": 3, "Título": "Perdendo o Amor", "Conteúdo": "O que fazer quando perder o amor."},
    ]
    return render_template('listas_postagem.html', postagens=postagens)

if __name__ == '__main__':
    app.run(debug=True)
