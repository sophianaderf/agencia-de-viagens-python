pagamentos = []


def registrar_pagamento():
    id_reserva = int(input("ID da reserva: "))
    valor = float(input("Valor: "))
    forma_pagamento = input("Forma de pagamento: ")
    data_pagamento = input("Data do pagamento: ")
    status = input("Status do pagamento: ")

    pagamento = {
        "id": len(pagamentos) + 1,
        "id_reserva": id_reserva,
        "valor": valor,
        "forma_pagamento": forma_pagamento,
        "data_pagamento": data_pagamento,
        "status": status
    }

    pagamentos.append(pagamento)

    print("Pagamento registrado com sucesso!")


def listar_pagamentos():
    if len(pagamentos) == 0:
        print("Nenhum pagamento cadastrado.")
    else:
        for pagamento in pagamentos:
            print(f"\nID: {pagamento['id']}")
            print(f"ID da reserva: {pagamento['id_reserva']}")
            print(f"Valor: R$ {pagamento['valor']:.2f}")
            print(f"Forma de pagamento: {pagamento['forma_pagamento']}")
            print(f"Data do pagamento: {pagamento['data_pagamento']}")
            print(f"Status: {pagamento['status']}")

