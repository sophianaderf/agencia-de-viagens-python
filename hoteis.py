from banco import conectar


def cadastrar_hotel():
    nome = input("Nome do hotel: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    id_destino = int(input("ID do destino: "))

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO hotel
        (nome, endereco, telefone, id_destino)
        VALUES (?, ?, ?, ?)
    """, (nome, endereco, telefone, id_destino))

    conexao.commit()
    conexao.close()

    print("Hotel cadastrado com sucesso!")


def listar_hoteis():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, endereco, telefone, id_destino
        FROM hotel
    """)

    hoteis = cursor.fetchall()

    conexao.close()

    if len(hoteis) == 0:
        print("Nenhum hotel cadastrado.")
    else:
        for hotel in hoteis:

            dados_hotel = {
                "id": hotel[0],
                "nome": hotel[1],
                "endereco": hotel[2],
                "telefone": hotel[3],
                "id_destino": hotel[4]
            }

            print(f"\nID: {dados_hotel['id']}")
            print(f"Nome: {dados_hotel['nome']}")
            print(f"Endereço: {dados_hotel['endereco']}")
            print(f"Telefone: {dados_hotel['telefone']}")
            print(f"ID do destino: {dados_hotel['id_destino']}")