"""O objetivo é implementar três operações essenciais:
depósito, saque e extrato. O sistema será desenvolvido para um banco que busca monetizar suas operações.
"""
menu = """
[1] - Depósito
[2] - Saque
[3] - Extrato
[0] - Sair 

=> """

saldo = 0
limite = 500
extrato = ""
LIMITE_SAQUES = 3
saques_realizados = 0

while True:
    print ("======== Bem Vindo ao Vex - Seu Banco digital. ========")
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Digite o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            print ("\nDepósito realizado com sucesso!")
            print ("Saldo atual: R$ {:.2f}".format(saldo))
            extrato += (f"\nDepósito de R$ {valor:.2f}")
        else: print ("São aceitos apenas valores positivos no depósito!")


    elif opcao == "2":
        if saques_realizados < LIMITE_SAQUES:
            valor = float(input("Digite o valor a ser sacado: "))
            if valor <= 0:
                print ("Insira um valor positivo.")
            elif valor > saldo:
                print ("Saldo Insuficiente.")
            elif valor > limite:
                print (f" Limite de {limite}R$ no saque excedido!")
            else:  
                saldo -= valor
                saques_realizados += 1
                print ("\nSaque realizado com sucesso!")
                print ("Saldo atual: R$ {:.2f}".format(saldo))
                extrato += (f"\nSaque de R$ {valor:.2f}")
        else: print (f"Limite maximo de saques ({LIMITE_SAQUES}) feitos!")

    elif opcao == "3":
        print ("\n====== Extrato ======")
        print ("Não foram realizadas movimentações." if not extrato else extrato)
        print (f"Saldo: {saldo:.2f}")
        print ("\n=============================")
    
    elif opcao == "0":
        print ("Obrigado por utilizar nossos serviços.")
        break
    else:
        print("Opção inválida. Tente novamente.")
    