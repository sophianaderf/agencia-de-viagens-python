from clientes import cadastrar_cliente, listar_clientes
from funcionarios import cadastrar_funcionario, listar_funcionarios
from destinos import cadastrar_destino, listar_destinos
from hoteis import cadastrar_hotel, listar_hoteis
from pacotes import cadastrar_pacote, listar_pacotes
from reservas import fazer_reserva, listar_reservas
from pagamentos import registrar_pagamento, listar_pagamentos

from consultas import (
    mostrar_tabelas,
    informacoes_clientes,
    pacotes_caros,
    atualizar_funcionario,
    deletar_pagamento
)


def menu():
    while True:
        print("\n===== AGÊNCIA DE VIAGENS =====")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Cadastrar funcionário")
        print("4 - Listar funcionários")
        print("5 - Cadastrar destino")
        print("6 - Listar destinos")
        print("7 - Cadastrar hotel")
        print("8 - Listar hotéis")
        print("9 - Cadastrar pacote")
        print("10 - Listar pacotes")
        print("11 - Fazer reserva")
        print("12 - Listar reservas")
        print("13 - Registrar pagamento")
        print("14 - Listar pagamentos")
        print("15 - Mostrar todas as tabelas")
        print("16 - Informações dos clientes")
        print("17 - Pacotes acima de R$ 3.000")
        print("18 - Atualizar funcionário")
        print("19 - Deletar pagamento")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()

        elif opcao == "2":
            listar_clientes()

        elif opcao == "3":
            cadastrar_funcionario()

        elif opcao == "4":
            listar_funcionarios()

        elif opcao == "5":
            cadastrar_destino()

        elif opcao == "6":
            listar_destinos()

        elif opcao == "7":
            cadastrar_hotel()

        elif opcao == "8":
            listar_hoteis()

        elif opcao == "9":
            cadastrar_pacote()

        elif opcao == "10":
            listar_pacotes()

        elif opcao == "11":
            fazer_reserva()

        elif opcao == "12":
            listar_reservas()

        elif opcao == "13":
            registrar_pagamento()

        elif opcao == "14":
            listar_pagamentos()

        elif opcao == "15":
            mostrar_tabelas()

        elif opcao == "16":
            informacoes_clientes()

        elif opcao == "17":
            pacotes_caros()

        elif opcao == "18":
            atualizar_funcionario()

        elif opcao == "19":
            deletar_pagamento()

        elif opcao == "0":
            print("Sistema encerrado!")
            break

        else:
            print("Opção inválida!")


menu()