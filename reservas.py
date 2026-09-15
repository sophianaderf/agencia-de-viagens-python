reservas = []


def fazer_reserva():
    id_cliente = int(input("ID do cliente: "))
    id_pacote = int(input("ID do pacote: "))
    id_funcionario = int(input("ID do funcionário: "))
    data_reserva = input("Data da reserva: ")
    quantidade_pessoas = int(input("Quantidade de pessoas: "))

    reserva = {
        "id": len(reservas) + 1,
        "id_cliente": id_cliente,
        "id_pacote": id_pacote,
        "id_funcionario": id_funcionario,
        "data_reserva": data_reserva,
        "quantidade_pessoas": quantidade_pessoas
    }

    reservas.append(reserva)

    print("Reserva realizada com sucesso!")


def listar_reservas():
    if len(reservas) == 0:
        print("Nenhuma reserva cadastrada.")
    else:
        for reserva in reservas:
            print(f"\nID: {reserva['id']}")
            print(f"ID do cliente: {reserva['id_cliente']}")
            print(f"ID do pacote: {reserva['id_pacote']}")
            print(f"ID do funcionário: {reserva['id_funcionario']}")
            print(f"Data da reserva: {reserva['data_reserva']}")
            print(f"Quantidade de pessoas: {reserva['quantidade_pessoas']}")

