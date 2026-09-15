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
            print(f"\nID: {pagamento[0]}")
            print(f"Valor total: R$ {pagamento[1]:.2f}")
            print(f"Forma de pagamento: {pagamento[2]}")
            print(f"Quantidade de parcelas: {pagamento[3]}")
            print(f"Valor da parcela: R$ {pagamento[4]:.2f}")
            print(f"Data do pagamento: {pagamento[5]}")
            print(f"Status: {pagamento[6]}")
            print(f"ID da reserva: {pagamento[7]}")