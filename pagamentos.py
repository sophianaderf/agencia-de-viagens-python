pagamentos = []


def registrar_pagamento():
    valor_total = float(input("Valor total: R$ "))
    forma_pagamento = input("Forma de pagamento: ")
    quantidade_parcelas = int(input("Quantidade de parcelas: "))
    data_pagamento = input("Data do pagamento: ")
    status = input("Status: ")
    id_reserva = int(input("ID da reserva: "))

    valor_parcela = valor_total / quantidade_parcelas

    pagamento = {
        "id": len(pagamentos) + 1,
        "valor_total": valor_total,
        "forma_pagamento": forma_pagamento,
        "quantidade_parcelas": quantidade_parcelas,
        "valor_parcela": valor_parcela,
        "data_pagamento": data_pagamento,
        "status": status,
        "id_reserva": id_reserva
    }

    pagamentos.append(pagamento)

    print("Pagamento registrado com sucesso!")
    print(f"Valor total: R$ {valor_total:.2f}")
    print(f"Quantidade de parcelas: {quantidade_parcelas}")
    print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")


def listar_pagamentos():
    if len(pagamentos) == 0:
        print("Nenhum pagamento cadastrado.")
    else:
        for pagamento in pagamentos:
            print(f"\nID: {pagamento['id']}")
            print(f"Valor total: R$ {pagamento['valor_total']:.2f}")
            print(f"Forma de pagamento: {pagamento['forma_pagamento']}")
            print(f"Quantidade de parcelas: {pagamento['quantidade_parcelas']}")
            print(f"Valor da parcela: R$ {pagamento['valor_parcela']:.2f}")
            print(f"Data do pagamento: {pagamento['data_pagamento']}")
            print(f"Status: {pagamento['status']}")
            print(f"ID da reserva: {pagamento['id_reserva']}")