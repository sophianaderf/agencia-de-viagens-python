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
            print(f"\nID: {funcionario[0]}")
            print(f"Nome: {funcionario[1]}")
            print(f"Cargo: {funcionario[2]}")
            print(f"E-mail: {funcionario[3]}")
            print(f"Telefone: {funcionario[4]}")