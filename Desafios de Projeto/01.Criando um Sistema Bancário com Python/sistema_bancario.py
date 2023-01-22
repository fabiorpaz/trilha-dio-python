menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == 'd':
        valor = float(input("Por favor, informe qual o valor a ser depositado: "))
        if valor > 0:
            saldo+=valor
            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            print ("Operação de depósito inválida")

    elif opcao == 's':
        print ("Por favor, informe o valor do saque: ")
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print ("Operação inválida, você não possui saldo suficiente")
        elif excedeu_limite:
            print ("Operação inválida, você não possui limite suficiente")
        elif excedeu_saques:
            print ("Operação inválida, você excedeu o limite de saques")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
        else:
            print ("Operação inválida")

    elif opcao =='e':
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimetações na conta." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("=============================")

    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')
    