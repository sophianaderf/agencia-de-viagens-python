import hmac
import os

from flask import Flask, flash, redirect, render_template, request, session, url_for
import psycopg
from psycopg.rows import dict_row

from database import criar_conexao

app = Flask(__name__)
app.secret_key = os.getenv("SESSION_SECRET", "agencia-viagens-funcionarios")

USUARIO_FUNCIONARIO = "agenciadeviagens"
SENHA_FUNCIONARIO = "agencia123"


@app.before_request
def exigir_login():
    if request.endpoint in {"login", "logout", "static"}:
        return None
    if not session.get("funcionario_autenticado"):
        return redirect(url_for("login", next=request.path))
    return None


@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("funcionario_autenticado"):
        return redirect(url_for("index"))

    if request.method == "POST":
        usuario = request.form.get("usuario", "")
        senha = request.form.get("senha", "")

        usuario_valido = hmac.compare_digest(usuario, USUARIO_FUNCIONARIO)
        senha_valida = hmac.compare_digest(senha, SENHA_FUNCIONARIO)

        if usuario_valido and senha_valida:
            session.clear()
            session["funcionario_autenticado"] = True
            session["usuario_funcionario"] = USUARIO_FUNCIONARIO
            destino = request.args.get("next") or url_for("index")
            if not destino.startswith("/") or destino.startswith("//"):
                destino = url_for("index")
            return redirect(destino)

        flash("Usuário ou senha inválidos.", "erro")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("Sessão encerrada com sucesso.", "sucesso")
    return redirect(url_for("login"))


def buscar_registros(query, parametros=None):
    conn = criar_conexao()
    try:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute(query, parametros)
            return cursor.fetchall()
    finally:
        conn.close()


def executar_comando(query, parametros=None):
    conn = criar_conexao()
    try:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute(query, parametros)
        conn.commit()
        return True, None
    except psycopg.Error as erro:
        conn.rollback()
        return False, str(erro)
    finally:
        conn.close()


def buscar_opcoes_funcionario():
    return {
        "clientes_opcoes": buscar_registros(
            "SELECT id, nome FROM cliente ORDER BY nome"
        ),
        "destinos_opcoes": buscar_registros(
            "SELECT id, cidade, estado, pais FROM destino ORDER BY cidade"
        ),
        "funcionarios_opcoes": buscar_registros(
            "SELECT id, nome, cargo FROM funcionario ORDER BY nome"
        ),
        "pacotes_opcoes": buscar_registros(
            "SELECT id, nome_pacote, preco FROM pacote ORDER BY nome_pacote"
        ),
        "reservas_opcoes": buscar_registros(
            """
            SELECT r.id, c.nome AS cliente, p.nome_pacote
            FROM reserva r
            JOIN cliente c ON c.id = r.id_cliente
            JOIN pacote p ON p.id = r.id_pacote
            ORDER BY r.id DESC
            """
        ),
    }


@app.route("/")
def index():
    destinos = []
    pacotes = []
    try:
        destinos = buscar_registros(
            """
            SELECT id, cidade, estado, pais, descricao
            FROM destino ORDER BY id ASC LIMIT 4
            """
        )
        pacotes = buscar_registros(
            """
            SELECT p.id, p.nome_pacote, p.descricao, p.preco,
                   p.quantidade_dias, d.cidade AS destino
            FROM pacote p
            LEFT JOIN destino d ON p.id_destino = d.id
            ORDER BY p.id ASC LIMIT 3
            """
        )
    except (psycopg.Error, UnicodeDecodeError):
        pass
    return render_template("index.html", destinos=destinos, pacotes=pacotes)


@app.route("/clientes")
def clientes():
    registros = buscar_registros(
        "SELECT id, nome, email, telefone, data_de_nascimento "
        "FROM cliente ORDER BY id DESC"
    )
    return render_template("clientes.html", clientes=registros)


@app.route("/funcionarios")
def funcionarios():
    registros = buscar_registros(
        "SELECT id, nome, cargo, email, telefone "
        "FROM funcionario ORDER BY id DESC"
    )
    return render_template("funcionarios.html", funcionarios=registros)


@app.route("/destinos")
def destinos():
    registros = buscar_registros(
        "SELECT id, cidade, estado, pais, descricao "
        "FROM destino ORDER BY id DESC"
    )
    return render_template("destinos.html", destinos=registros)


@app.route("/hoteis")
def hoteis():
    registros = buscar_registros(
        """
        SELECT h.id, h.nome, h.endereco, h.telefone, d.cidade
        FROM hotel h
        LEFT JOIN destino d ON h.id_destino = d.id
        ORDER BY h.id DESC
        """
    )
    return render_template("hoteis.html", hoteis=registros)


@app.route("/pacotes")
def pacotes():
    registros = buscar_registros(
        """
        SELECT p.id, p.nome_pacote, p.descricao, p.preco,
               p.quantidade_dias, d.cidade AS destino
        FROM pacote p
        LEFT JOIN destino d ON p.id_destino = d.id
        ORDER BY p.id DESC
        """
    )
    return render_template("pacotes.html", pacotes=registros)


@app.route("/reservas")
def reservas():
    registros = buscar_registros(
        """
        SELECT r.id, r.data_reserva, r.quantidade_pessoas,
               c.nome AS cliente_nome, p.nome_pacote,
               f.nome AS func_nome
        FROM reserva r
        JOIN cliente c ON r.id_cliente = c.id
        JOIN pacote p ON r.id_pacote = p.id
        JOIN funcionario f ON r.id_funcionario = f.id
        ORDER BY r.id DESC
        """
    )
    return render_template("reservas.html", reservas=registros)


@app.route("/pagamentos")
def pagamentos():
    registros = buscar_registros(
        """
        SELECT id, valor_total, forma_pagamento, quantidade_parcelas,
               valor_parcela, data_pagamento, status, id_reserva
        FROM pagamento
        ORDER BY id DESC
        """
    )
    return render_template("pagamentos.html", pagamentos=registros)


@app.route("/area-funcionario")
def area_funcionario():
    dados = {
        "clientes": buscar_registros(
            "SELECT id, nome, email, telefone, data_de_nascimento FROM cliente ORDER BY id DESC"
        ),
        "destinos": buscar_registros(
            "SELECT id, cidade, estado, pais, descricao FROM destino ORDER BY id DESC"
        ),
        "hoteis": buscar_registros(
            """
            SELECT h.id, h.nome, h.endereco, h.telefone, h.id_destino, d.cidade
            FROM hotel h LEFT JOIN destino d ON d.id = h.id_destino
            ORDER BY h.id DESC
            """
        ),
        "pacotes": buscar_registros(
            """
            SELECT p.id, p.nome_pacote, p.descricao, p.preco,
                   p.quantidade_dias, p.id_destino, d.cidade AS destino
            FROM pacote p LEFT JOIN destino d ON d.id = p.id_destino
            ORDER BY p.id DESC
            """
        ),
        "reservas": buscar_registros(
            """
            SELECT r.id, r.data_reserva, r.quantidade_pessoas,
                   r.id_cliente, r.id_pacote, r.id_funcionario,
                   c.nome AS cliente_nome, p.nome_pacote, f.nome AS func_nome
            FROM reserva r
            JOIN cliente c ON c.id = r.id_cliente
            JOIN pacote p ON p.id = r.id_pacote
            JOIN funcionario f ON f.id = r.id_funcionario
            ORDER BY r.id DESC
            """
        ),
        "pagamentos": buscar_registros(
            """
            SELECT id, valor_total, forma_pagamento, quantidade_parcelas,
                   valor_parcela, data_pagamento, status, id_reserva
            FROM pagamento ORDER BY id DESC
            """
        ),
    }
    dados.update(buscar_opcoes_funcionario())
    return render_template("area_funcionario.html", **dados)


@app.route("/funcionario/clientes/novo", methods=["POST"])
def novo_cliente():
    sucesso, erro = executar_comando(
        """
        INSERT INTO cliente (nome, email, telefone, data_de_nascimento)
        VALUES (%s, %s, %s, %s)
        """,
        (
            request.form["nome"].strip(),
            request.form["email"].strip(),
            request.form["telefone"].strip(),
            request.form["data_de_nascimento"],
        ),
    )
    flash("Cliente cadastrado com sucesso." if sucesso else f"Não foi possível cadastrar: {erro}", "sucesso" if sucesso else "erro")
    return redirect(url_for("area_funcionario"))


@app.route("/funcionario/destinos/novo", methods=["POST"])
def novo_destino():
    sucesso, erro = executar_comando(
        """
        INSERT INTO destino (cidade, estado, pais, descricao)
        VALUES (%s, %s, %s, %s)
        """,
        tuple(request.form[campo].strip() for campo in ("cidade", "estado", "pais", "descricao")),
    )
    flash("Destino cadastrado com sucesso." if sucesso else f"Não foi possível cadastrar: {erro}", "sucesso" if sucesso else "erro")
    return redirect(url_for("area_funcionario"))


@app.route("/funcionario/hoteis/novo", methods=["POST"])
def novo_hotel():
    sucesso, erro = executar_comando(
        """
        INSERT INTO hotel (nome, endereco, telefone, id_destino)
        VALUES (%s, %s, %s, %s)
        """,
        (
            request.form["nome"].strip(),
            request.form["endereco"].strip(),
            request.form["telefone"].strip(),
            request.form["id_destino"],
        ),
    )
    flash("Hotel cadastrado com sucesso." if sucesso else f"Não foi possível cadastrar: {erro}", "sucesso" if sucesso else "erro")
    return redirect(url_for("area_funcionario"))


@app.route("/funcionario/pacotes/novo", methods=["POST"])
def novo_pacote():
    sucesso, erro = executar_comando(
        """
        INSERT INTO pacote (nome_pacote, descricao, preco, quantidade_dias, id_destino)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            request.form["nome_pacote"].strip(),
            request.form["descricao"].strip(),
            request.form["preco"].replace(",", "."),
            request.form["quantidade_dias"],
            request.form["id_destino"],
        ),
    )
    flash("Pacote cadastrado com sucesso." if sucesso else f"Não foi possível cadastrar: {erro}", "sucesso" if sucesso else "erro")
    return redirect(url_for("area_funcionario"))


@app.route("/funcionario/reservas/nova", methods=["POST"])
def nova_reserva():
    sucesso, erro = executar_comando(
        """
        INSERT INTO reserva (data_reserva, quantidade_pessoas, id_cliente, id_pacote, id_funcionario)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            request.form["data_reserva"],
            request.form["quantidade_pessoas"],
            request.form["id_cliente"],
            request.form["id_pacote"],
            request.form["id_funcionario"],
        ),
    )
    flash("Reserva realizada com sucesso." if sucesso else f"Não foi possível realizar: {erro}", "sucesso" if sucesso else "erro")
    return redirect(url_for("area_funcionario"))


@app.route("/funcionario/pagamentos/novo", methods=["POST"])
def novo_pagamento():
    quantidade = int(request.form["quantidade_parcelas"])
    valor_total = float(request.form["valor_total"].replace(",", "."))
    valor_parcela = valor_total / quantidade
    sucesso, erro = executar_comando(
        """
        INSERT INTO pagamento
        (valor_total, forma_pagamento, quantidade_parcelas, valor_parcela, data_pagamento, status, id_reserva)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        (
            valor_total,
            request.form["forma_pagamento"],
            quantidade,
            round(valor_parcela, 2),
            request.form["data_pagamento"],
            request.form["status"],
            request.form["id_reserva"],
        ),
    )
    flash("Pagamento registrado com sucesso." if sucesso else f"Não foi possível registrar: {erro}", "sucesso" if sucesso else "erro")
    return redirect(url_for("area_funcionario"))


def deletar_registro(tabela, item_id):
    permitido = {"cliente", "destino", "hotel", "pacote", "reserva", "pagamento"}
    if tabela not in permitido:
        return False, "Tabela inválida."
    return executar_comando(f'DELETE FROM "{tabela}" WHERE id = %s', (item_id,))


@app.route("/funcionario/<tabela>/<int:item_id>/deletar", methods=["POST"])
def deletar_item(tabela, item_id):
    sucesso, erro = deletar_registro(tabela, item_id)
    if not sucesso and "violates foreign key constraint" in erro.lower():
        erro = "este registro está ligado a outros dados e não pode ser excluído."
    flash("Registro excluído com sucesso." if sucesso else f"Não foi possível excluir: {erro}", "sucesso" if sucesso else "erro")
    return redirect(url_for("area_funcionario"))


@app.route("/funcionario/pagamentos/<int:item_id>/status", methods=["POST"])
def atualizar_status_pagamento(item_id):
    sucesso, erro = executar_comando(
        "UPDATE pagamento SET status = %s WHERE id = %s",
        (request.form["status"], item_id),
    )
    flash("Status atualizado com sucesso." if sucesso else f"Não foi possível atualizar: {erro}", "sucesso" if sucesso else "erro")
    return redirect(url_for("area_funcionario"))


if __name__ == "__main__":
    app.run(debug=True)
