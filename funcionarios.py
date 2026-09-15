funcionarios = []


def cadastrar_funcionario():
    nome = input("Nome: ")
    cargo = input("Cargo: ")
    email = input("E-mail: ")
    telefone = input("Telefone: ")

    funcionario = {
        "id": len(funcionarios) + 1,
        "nome": nome,
        "cargo": cargo,
        "email": email,
        "telefone": telefone
    }

    funcionarios.append(funcionario)

    print("Funcionário cadastrado com sucesso!")


def listar_funcionarios():
    if len(funcionarios) == 0:
        print("Nenhum funcionário cadastrado.")
    else:
        for funcionario in funcionarios:
            print(f"\nID: {funcionario['id']}")
            print(f"Nome: {funcionario['nome']}")
            print(f"Cargo: {funcionario['cargo']}")
            print(f"E-mail: {funcionario['email']}")
            print(f"Telefone: {funcionario['telefone']}")