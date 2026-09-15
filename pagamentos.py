from banco import conectar


def registrar_pagamento():
    valor_total = float(input("Valor total: R$ "))
    forma_pagamento = input("Forma de pagamento: ")
    quantidade_parcelas = int(input("Quantidade de parcelas: "))
    data_pagamento = input("Data do pagamento: ")
    status = input("Status: ")
    id_reserva = int(input("ID da reserva: "))

    valor_parcela = valor_total / quantidade_parcelas

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO pagamento
        (valor_total, forma_pagamento, quantidade_parcelas,
         valor_parcela, data_pagamento, status, id_reserva)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        valor_total,
        forma_pagamento,
        quantidade_parcelas,
        valor_parcela,
        data_pagamento,
        status,
        id_reserva
    ))

    conexao.commit()
    conexao.close()

    print("Pagamento registrado com sucesso!")
    print(f"Valor total: R$ {valor_total:.2f}")
    print(f"Quantidade de parcelas: {quantidade_parcelas}")
    print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")


def listar_pagamentos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, valor_total, forma_pagamento,
               quantidade_parcelas, valor_parcela,
               data_pagamento, status, id_reserva
        FROM pagamento
    """)

    pagamentos = cursor.fetchall()

    conexao.close()

    if len(pagamentos) == 0:
        print("Nenhum pagamento cadastrado.")
    else:
        for pagamento in pagamentos:

            dados_pagamento = {
                "id": pagamento[0],
                "valor_total": pagamento[1],
                "forma_pagamento": pagamento[2],
                "quantidade_parcelas": pagamento[3],
                "valor_parcela": pagamento[4],
                "data_pagamento": pagamento[5],
                "status": pagamento[6],
                "id_reserva": pagamento[7]
            }

            print(f"\nID: {dados_pagamento['id']}")
            print(f"Valor total: R$ {dados_pagamento['valor_total']:.2f}")
            print(f"Forma de pagamento: {dados_pagamento['forma_pagamento']}")
            print(f"Quantidade de parcelas: {dados_pagamento['quantidade_parcelas']}")
            print(f"Valor da parcela: R$ {dados_pagamento['valor_parcela']:.2f}")
            print(f"Data do pagamento: {dados_pagamento['data_pagamento']}")
            print(f"Status: {dados_pagamento['status']}")
            print(f"ID da reserva: {dados_pagamento['id_reserva']}")