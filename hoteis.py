hoteis = []


def cadastrar_hotel():
    nome = input("Nome do hotel: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    id_destino = int(input("ID do destino: "))

    hotel = {
        "id": len(hoteis) + 1,
        "nome": nome,
        "endereco": endereco,
        "telefone": telefone,
        "id_destino": id_destino
    }

    hoteis.append(hotel)

    print("Hotel cadastrado com sucesso!")


def listar_hoteis():
    if len(hoteis) == 0:
        print("Nenhum hotel cadastrado.")
    else:
        for hotel in hoteis:
            print(f"\nID: {hotel['id']}")
            print(f"Nome: {hotel['nome']}")
            print(f"Endereço: {hotel['endereco']}")
            print(f"Telefone: {hotel['telefone']}")
            print(f"ID do destino: {hotel['id_destino']}")


