from flask import Flask, render_template, url_for
from banco import conectar

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clientes')
def clientes():
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, email, telefone, data_de_nascimento FROM cliente ORDER BY id DESC")
        lista_clientes = cursor.fetchall()
    return render_template('clientes.html', clientes=lista_clientes)

@app.route('/funcionarios')
def funcionarios():
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, cargo, email, telefone FROM funcionario ORDER BY id DESC")
        lista_funcionarios = cursor.fetchall()
    return render_template('funcionarios.html', funcionarios=lista_funcionarios)

@app.route('/destinos')
def destinos():
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT id, cidade, estado, pais, descricao FROM destino ORDER BY id DESC")
        lista_destinos = cursor.fetchall()
    return render_template('destinos.html', destinos=lista_destinos)

@app.route('/hoteis')
def hoteis():
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT h.id, h.nome, h.endereco, h.telefone, d.cidade 
            FROM hotel h 
            LEFT JOIN destino d ON h.id_destino = d.id
            ORDER BY h.id DESC
        """)
        lista_hoteis = cursor.fetchall()
    return render_template('hoteis.html', hoteis=lista_hoteis)

@app.route('/pacotes')
def pacotes():
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT p.id, p.nome_pacote, p.descricao, p.preco, p.quantidade_dias, d.cidade
            FROM pacote p
            LEFT JOIN destino d ON p.id_destino = d.id
            ORDER BY p.id DESC
        """)
        lista_pacotes = cursor.fetchall()
    return render_template('pacotes.html', pacotes=lista_pacotes)

@app.route('/reservas')
def reservas():
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT r.id, r.data_reserva, r.quantidade_pessoas, c.nome, p.nome_pacote, f.nome
            FROM reserva r
            JOIN cliente c ON r.id_cliente = c.id
            JOIN pacote p ON r.id_pacote = p.id
            JOIN funcionario f ON r.id_funcionario = f.id
            ORDER BY r.id DESC
        """)
        lista_reservas = cursor.fetchall()
    return render_template('reservas.html', reservas=lista_reservas)

@app.route('/pagamentos')
def pagamentos():
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT id, valor_total, forma_pagamento, quantidade_parcelas, valor_parcela, data_pagamento, status, id_reserva
            FROM pagamento
            ORDER BY id DESC
        """)
        lista_pagamentos = cursor.fetchall()
    return render_template('pagamentos.html', pagamentos=lista_pagamentos)




if __name__ == '__main__':
    app.run(debug=True)

