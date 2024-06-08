def menu():
    saldo = 1000
    max_retiradas = 3
    contador_retiradas = 0
    
    while True:
        print("Qual operação você deseja realizar?")
        print("[1] - Saldo")
        print("[2] - Depósito")
        print("[3] - Retirada")
        print("[4] - Encerrar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print(f"Seu saldo é: {saldo}")
            outra_operacao = input("Deseja realizar outra operação? [S/N] ").strip().upper()
            if outra_operacao != "S":
                print("Muito obrigado, é bom ter você por perto.")
                break

        elif opcao == "2":
            deposito = int(input("Qual o valor do depósito? "))
            saldo += deposito
            print(f"Novo saldo: {saldo}")
            outra_operacao = input("Deseja realizar outra operação? [S/N] ").strip().upper()
            if outra_operacao != "S":
                print("Muito obrigado, é bom ter você por perto.")
                break

        elif opcao == "3":
            if contador_retiradas >= max_retiradas:
                print("Você já realizou o número máximo de retiradas permitidas para hoje.")
            else:
                retirada = int(input("Qual o valor da retirada? "))
                if retirada > saldo:
                    print(f"Operação cancelada: O valor da retirada é superior ao saldo em conta. Seu saldo é de {saldo}")
                else:
                    saldo -= retirada
                    contador_retiradas += 1
                    print(f"Novo saldo: {saldo}")
            outra_operacao = input("Deseja realizar outra operação? [S/N] ").strip().upper()
            if outra_operacao != "S":
                print("Muito obrigado, é bom ter você por perto.")
                break

        elif opcao == "4":
            print("Muito obrigado, é bom ter você por perto.")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    menu()

