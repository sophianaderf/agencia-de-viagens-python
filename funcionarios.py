from banco import conectar


def cadastrar_funcionario():
    nome = input("Nome: ")
    cargo = input("Cargo: ")
    email = input("E-mail: ")
    telefone = input("Telefone: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO funcionario
        (nome, cargo, email, telefone)
        VALUES (?, ?, ?, ?)
    """, (nome, cargo, email, telefone))

    conexao.commit()
    conexao.close()

    print("Funcionário cadastrado com sucesso!")


def listar_funcionarios():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, cargo, email, telefone
        FROM funcionario
    """)

    funcionarios = cursor.fetchall()

    conexao.close()

    if len(funcionarios) == 0:
        print("Nenhum funcionário cadastrado.")
    else:
        for funcionario in funcionarios:

            dados_funcionario = {
                "id": funcionario[0],
                "nome": funcionario[1],
                "cargo": funcionario[2],
                "email": funcionario[3],
                "telefone": funcionario[4]
            }

            print(f"\nID: {dados_funcionario['id']}")
            print(f"Nome: {dados_funcionario['nome']}")
            print(f"Cargo: {dados_funcionario['cargo']}")
            print(f"E-mail: {dados_funcionario['email']}")
            print(f"Telefone: {dados_funcionario['telefone']}")