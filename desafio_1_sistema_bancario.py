menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor que deseja depositar: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            print("Deposite apenas valores maiores que zero")

    elif opcao == "2":
        valor = float(input("Informe o valor que deseja sacar: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print("Operação inválida! Você excedeu seu saldo.")
        elif excedeu_limite:
            print("Operação inválida! O valor do saque excedeu o limite.")
        elif excedeu_saque:
            print("Operação inválida! Você excedeu o número máximo de saques.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação inválida! O valor informado está inválido.")

    elif opcao == "3":
        print("=============Extrato=============")
        print("Não foram feitas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}") 
        print("====================================")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada")