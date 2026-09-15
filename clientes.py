from banco import conectar


def cadastrar_cliente():
    nome = input("Nome: ")
    email = input("E-mail: ")
    telefone = input("Telefone: ")
    data_nascimento = input("Data de nascimento: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO cliente
        (nome, email, telefone, data_de_nascimento)
        VALUES (?, ?, ?, ?)
    """, (nome, email, telefone, data_nascimento))

    conexao.commit()
    conexao.close()

    print("Cliente cadastrado com sucesso!")


def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, email, telefone, data_de_nascimento
        FROM cliente
    """)

    clientes = cursor.fetchall()

    conexao.close()

    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
    else:
        for cliente in clientes:
            print(f"\nID: {cliente[0]}")
            print(f"Nome: {cliente[1]}")
            print(f"E-mail: {cliente[2]}")
            print(f"Telefone: {cliente[3]}")
            print(f"Data de nascimento: {cliente[4]}")