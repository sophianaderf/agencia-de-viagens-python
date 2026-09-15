from banco import conectar


def fazer_reserva():
    id_cliente = int(input("ID do cliente: "))
    id_pacote = int(input("ID do pacote: "))
    id_funcionario = int(input("ID do funcionário: "))
    data_reserva = input("Data da reserva: ")
    quantidade_pessoas = int(input("Quantidade de pessoas: "))

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO reserva
        (data_reserva, quantidade_pessoas, id_cliente, id_pacote, id_funcionario)
        VALUES (?, ?, ?, ?, ?)
    """, (
        data_reserva,
        quantidade_pessoas,
        id_cliente,
        id_pacote,
        id_funcionario
    ))

    conexao.commit()
    conexao.close()

    print("Reserva realizada com sucesso!")


def listar_reservas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, data_reserva, quantidade_pessoas,
               id_cliente, id_pacote, id_funcionario
        FROM reserva
    """)

    reservas = cursor.fetchall()

    conexao.close()

    if len(reservas) == 0:
        print("Nenhuma reserva cadastrada.")
    else:
        for reserva in reservas:

            dados_reserva = {
                "id": reserva[0],
                "data": reserva[1],
                "quantidade_pessoas": reserva[2],
                "id_cliente": reserva[3],
                "id_pacote": reserva[4],
                "id_funcionario": reserva[5]
            }

            print(f"\nID: {dados_reserva['id']}")
            print(f"Data da reserva: {dados_reserva['data']}")
            print(f"Quantidade de pessoas: {dados_reserva['quantidade_pessoas']}")
            print(f"ID do cliente: {dados_reserva['id_cliente']}")
            print(f"ID do pacote: {dados_reserva['id_pacote']}")
            print(f"ID do funcionário: {dados_reserva['id_funcionario']}")