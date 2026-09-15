from banco import conectar


def cadastrar_pacote():
    nome = input("Nome do pacote: ")
    descricao = input("Descrição: ")
    preco = float(input("Preço: R$ "))
    quantidade_dias = int(input("Quantidade de dias: "))
    id_destino = int(input("ID do destino: "))

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO pacote
        (nome_pacote, descricao, preco, quantidade_dias, id_destino)
        VALUES (?, ?, ?, ?, ?)
    """, (nome, descricao, preco, quantidade_dias, id_destino))

    conexao.commit()
    conexao.close()

    print("Pacote cadastrado com sucesso!")


def listar_pacotes():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome_pacote, descricao, preco, quantidade_dias, id_destino
        FROM pacote
    """)

    pacotes = cursor.fetchall()

    conexao.close()

    if len(pacotes) == 0:
        print("Nenhum pacote cadastrado.")
    else:
        for pacote in pacotes:
            print(f"\nID: {pacote[0]}")
            print(f"Nome: {pacote[1]}")
            print(f"Descrição: {pacote[2]}")
            print(f"Preço: R$ {pacote[3]:.2f}")
            print(f"Quantidade de dias: {pacote[4]}")
            print(f"ID do destino: {pacote[5]}")