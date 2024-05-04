menu = """

*SELECIONE UMA OPÇÃO*

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

    opcao = input(menu) #ACESSA MEU MENU

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: ")) #FLOAT NÚMERO RACIONAIS

        if valor > 0:
            saldo += valor #ADICIONA O VALOR AO MEU SALDO
            extrato += f"Depósito: R$ {valor:.2f}\n" #REGISTRA NO MEU EXTRATO. {.2f}COLOCA DUAS CASAS DECIMAIS. \n SALTA A LINHA. AS f-strings PERMITEM INSERIR VALORES DE VARIÁVEIS DIRETAMENTE EM UMA STRING FORMATADA.

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor #DIMINUI O VALOR NO MEU SALDO
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1 #ADICIONA MAIS UM SAQUE.

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato) #IF TERNÁRIO: AVALIA A EXPRESSÃO CONDICIONAL E RETORNA UM VALOR COM BASE NESSA CONDIÇÃO. 
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break #FINALIZA UMA EXECUÇÃO.

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")