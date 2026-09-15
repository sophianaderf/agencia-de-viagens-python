from banco import conectar


def cadastrar_destino():
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    pais = input("País: ")
    descricao = input("Descrição: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO destino
        (cidade, estado, pais, descricao)
        VALUES (?, ?, ?, ?)
    """, (cidade, estado, pais, descricao))

    conexao.commit()
    conexao.close()

    print("Destino cadastrado com sucesso!")


def listar_destinos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, cidade, estado, pais, descricao
        FROM destino
    """)

    destinos = cursor.fetchall()

    conexao.close()

    if len(destinos) == 0:
        print("Nenhum destino cadastrado.")
    else:
        for destino in destinos:

            dados_destino = {
                "id": destino[0],
                "cidade": destino[1],
                "estado": destino[2],
                "pais": destino[3],
                "descricao": destino[4]
            }

            print(f"\nID: {dados_destino['id']}")
            print(f"Cidade: {dados_destino['cidade']}")
            print(f"Estado: {dados_destino['estado']}")
            print(f"País: {dados_destino['pais']}")
            print(f"Descrição: {dados_destino['descricao']}")