pagamentos = []


def registrar_pagamento():
    id_reserva = int(input("ID da reserva: "))
    valor_total = float(input("Valor total: R$ "))
    quantidade_parcelas = int(input("Quantidade de parcelas: "))
    forma_pagamento = input("Forma de pagamento: ")
    data_pagamento = input("Data do pagamento: ")

    valor_parcela = valor_total / quantidade_parcelas

    for numero_parcela in range(1, quantidade_parcelas + 1):
        pagamento = {
            "id": len(pagamentos) + 1,
            "id_reserva": id_reserva,
            "numero_parcela": numero_parcela,
            "quantidade_parcelas": quantidade_parcelas,
            "valor_parcela": valor_parcela,
            "forma_pagamento": forma_pagamento,
            "data_pagamento": data_pagamento,
            "status": "Pendente"
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
            print(f"ID da reserva: {pagamento['id_reserva']}")
            print(f"Parcela: {pagamento['numero_parcela']}/{pagamento['quantidade_parcelas']}")
            print(f"Valor da parcela: R$ {pagamento['valor_parcela']:.2f}")
            print(f"Forma de pagamento: {pagamento['forma_pagamento']}")
            print(f"Data do pagamento: {pagamento['data_pagamento']}")
            print(f"Status: {pagamento['status']}")