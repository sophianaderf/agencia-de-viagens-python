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
            print(f"\nID: {destino[0]}")
            print(f"Cidade: {destino[1]}")
            print(f"Estado: {destino[2]}")
            print(f"País: {destino[3]}")
            print(f"Descrição: {destino[4]}")