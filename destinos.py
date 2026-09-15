destinos = []


def cadastrar_destino():
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    pais = input("País: ")
    descricao = input("Descrição: ")

    destino = {
        "id": len(destinos) + 1,
        "cidade": cidade,
        "estado": estado,
        "pais": pais,
        "descricao": descricao
    }

    destinos.append(destino)

    print("Destino cadastrado com sucesso!")


def listar_destinos():
    if len(destinos) == 0:
        print("Nenhum destino cadastrado.")
    else:
        for destino in destinos:
            print(f"\nID: {destino['id']}")
            print(f"Cidade: {destino['cidade']}")
            print(f"Estado: {destino['estado']}")
            print(f"País: {destino['pais']}")
            print(f"Descrição: {destino['descricao']}")

cadastrar_destino()
listar_destinos()