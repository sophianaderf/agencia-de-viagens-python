def menu():
    while True:
        print("\n===== AGÊNCIA DE VIAGENS =====")
        print("1 - Clientes")
        print("2 - Funcionários")
        print("3 - Destinos")
        print("4 - Pacotes")
        print("5 - Reservas")
        print("6 - Pagamentos")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Área de clientes")

        elif opcao == "2":
            print("Área de funcionários")

        elif opcao == "3":
            print("Área de destinos")

        elif opcao == "4":
            print("Área de pacotes")

        elif opcao == "5":
            print("Área de reservas")

        elif opcao == "6":
            print("Área de pagamentos")

        elif opcao == "0":
            print("Sistema encerrado!")
            break

        else:
            print("Opção inválida!")


menu()