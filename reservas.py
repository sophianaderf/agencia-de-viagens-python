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
            print(f"\nID: {reserva[0]}")
            print(f"Data da reserva: {reserva[1]}")
            print(f"Quantidade de pessoas: {reserva[2]}")
            print(f"ID do cliente: {reserva[3]}")
            print(f"ID do pacote: {reserva[4]}")
            print(f"ID do funcionário: {reserva[5]}")