clientes = []


def cadastrar_cliente():
    nome = input("Nome: ")
    email = input("E-mail: ")
    telefone = input("Telefone: ")
    data_nascimento = input("Data de nascimento: ")

    cliente = {
        "id": len(clientes) + 1,
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "data_nascimento": data_nascimento
    }

    clientes.append(cliente)

    print("Cliente cadastrado com sucesso!")


def listar_clientes():
    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
    else:
        for cliente in clientes:
            print(f"\nID: {cliente['id']}")
            print(f"Nome: {cliente['nome']}")
            print(f"E-mail: {cliente['email']}")
            print(f"Telefone: {cliente['telefone']}")
            print(f"Data de nascimento: {cliente['data_nascimento']}")


cadastrar_cliente()
listar_clientes()