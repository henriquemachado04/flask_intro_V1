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
def lista_dicionarios():
    usuarios = {
        ["nome": "Henrique", "idade": 20, "cidade": "Jaraguá do Sul"],
        ["nome": "Gabrieli", "idade": 18, "cidade": "Guaramirim"]
        ["nome": "Paula", "idade": 9, "cidade": "Jaraguá do Sul"]
    }
    return render_template('listas_dicionarios', usuarios = usuarios)

if __name__ == '__main__':
    app.run(debug=True)
