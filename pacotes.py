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

            dados_pacote = {
                "id": pacote[0],
                "nome": pacote[1],
                "descricao": pacote[2],
                "preco": pacote[3],
                "dias": pacote[4],
                "id_destino": pacote[5]
            }

            print(f"\nID: {dados_pacote['id']}")
            print(f"Nome: {dados_pacote['nome']}")
            print(f"Descrição: {dados_pacote['descricao']}")
            print(f"Preço: R$ {dados_pacote['preco']:.2f}")
            print(f"Quantidade de dias: {dados_pacote['dias']}")
            print(f"ID do destino: {dados_pacote['id_destino']}")