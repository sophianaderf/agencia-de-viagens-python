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

            dados_cliente = {
                "id": cliente[0],
                "nome": cliente[1],
                "email": cliente[2],
                "telefone": cliente[3],
                "data_nascimento": cliente[4]
            }

            print(f"\nID: {dados_cliente['id']}")
            print(f"Nome: {dados_cliente['nome']}")
            print(f"E-mail: {dados_cliente['email']}")
            print(f"Telefone: {dados_cliente['telefone']}")
            print(f"Data de nascimento: {dados_cliente['data_nascimento']}")