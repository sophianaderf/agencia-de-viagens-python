from banco import conectar


# Ver tabelas com as informações completas
def mostrar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM cliente")
    print("\n===== CLIENTES =====")
    for cliente in cursor.fetchall():
        print(cliente)

    cursor.execute("SELECT * FROM destino")
    print("\n===== DESTINOS =====")
    for destino in cursor.fetchall():
        print(destino)

    cursor.execute("SELECT * FROM hotel")
    print("\n===== HOTEIS =====")
    for hotel in cursor.fetchall():
        print(hotel)

    cursor.execute("SELECT * FROM pacote")
    print("\n===== PACOTES =====")
    for pacote in cursor.fetchall():
        print(pacote)

    cursor.execute("SELECT * FROM funcionario")
    print("\n===== FUNCIONARIOS =====")
    for funcionario in cursor.fetchall():
        print(funcionario)

    cursor.execute("SELECT * FROM reserva")
    print("\n===== RESERVAS =====")
    for reserva in cursor.fetchall():
        print(reserva)

    cursor.execute("SELECT * FROM pagamento")
    print("\n===== PAGAMENTOS =====")
    for pagamento in cursor.fetchall():
        print(pagamento)

    conexao.close()


# Ver informações específicas dos clientes
def informacoes_clientes():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT nome, email, telefone
        FROM cliente
    """)

    clientes = cursor.fetchall()

    print("\n===== INFORMAÇÕES DOS CLIENTES =====")

    for cliente in clientes:
        print(f"Nome: {cliente[0]}")
        print(f"E-mail: {cliente[1]}")
        print(f"Telefone: {cliente[2]}")
        print()

    conexao.close()


# Mostrar pacotes com preço acima de R$ 3.000
def pacotes_caros():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT nome_pacote, preco, quantidade_dias
        FROM pacote
        WHERE preco > 3000
    """)

    pacotes = cursor.fetchall()

    print("\n===== PACOTES ACIMA DE R$ 3.000 =====")

    for pacote in pacotes:
        print(f"Pacote: {pacote[0]}")
        print(f"Preço: R$ {pacote[1]:.2f}")
        print(f"Dias: {pacote[2]}")
        print()

    conexao.close()


# Atualizar cargo de funcionário
def atualizar_funcionario():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE funcionario
        SET cargo = 'Gerente de Vendas'
        WHERE id = 1
    """)

    conexao.commit()
    conexao.close()

    print("Cargo atualizado com sucesso!")


# Deletar pagamento
def deletar_pagamento():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        DELETE FROM pagamento
        WHERE id = 7
    """)

    conexao.commit()
    conexao.close()

    print("Pagamento deletado com sucesso!")