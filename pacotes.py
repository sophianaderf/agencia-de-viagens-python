pacotes = []


def cadastrar_pacote():
    nome = input("Nome do pacote: ")
    descricao = input("Descrição: ")
    preco = float(input("Preço: "))
    quantidade_dias = int(input("Quantidade de dias: "))
    id_destino = int(input("ID do destino: "))

    pacote = {
        "id": len(pacotes) + 1,
        "nome": nome,
        "descricao": descricao,
        "preco": preco,
        "quantidade_dias": quantidade_dias,
        "id_destino": id_destino
    }

    pacotes.append(pacote)

    print("Pacote cadastrado com sucesso!")


def listar_pacotes():
    if len(pacotes) == 0:
        print("Nenhum pacote cadastrado.")
    else:
        for pacote in pacotes:
            print(f"\nID: {pacote['id']}")
            print(f"Nome: {pacote['nome']}")
            print(f"Descrição: {pacote['descricao']}")
            print(f"Preço: R$ {pacote['preco']:.2f}")
            print(f"Quantidade de dias: {pacote['quantidade_dias']}")
            print(f"ID do destino: {pacote['id_destino']}")

