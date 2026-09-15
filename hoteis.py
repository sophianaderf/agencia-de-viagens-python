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
            print(f"\nID: {hotel[0]}")
            print(f"Nome: {hotel[1]}")
            print(f"Endereço: {hotel[2]}")
            print(f"Telefone: {hotel[3]}")
            print(f"ID do destino: {hotel[4]}")