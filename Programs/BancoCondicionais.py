saldo = 2000 #define um saldo inicial, nao temos banco de dados.

def sacar(saldo):
    
    try: # para caso o valor inserido nao seja float.
        saque = float(input("informe o valor do saque: "))
    except ValueError:
        print("Por favor, insira um valor válido.")
        return saldo
    if saldo >= saque:
        print("Realizando saque...")
        saldo -= saque
        print("Saque realizado.")
    else:
        print("Saldo insuficiente para o saque!")
        resp1 = input("Você deseja continuar? (sim/não): ")
        if  resp1.lower() == "sim":
            saldo = sacar(saldo) #diz que saldo = a funcao
        elif resp1.lower() == "não":
            print("Certo, operação encerrada.")
        else:
            print("Não entendi, poderia responder 'sim' ou 'não'?")
    return saldo
                  
def deposito(saldo):
    try:
        deposito = float(input("Informe a quantia para depositar: "))
    except ValueError:
        print("Insira um valor válido.")
        return saldo
    print("Realizando depósito...")
    saldo += deposito
    print ("Depósito efetuado.")
    return saldo

def verificar_saldo(saldo):
    print (f"Exibindo seu saldo: {saldo}")

print ("Olá, bem vindo ao banco!")

while True:
    opcao = int(input("\nInsira a opção: [1]Sacar \n[2]Depositar \n[3]Verificar saldo \n[4]Sair\n"))
    if opcao == 1:
        saldo = sacar(saldo)
    elif opcao == 2:
        saldo = deposito(saldo)
    elif opcao == 3:
        verificar_saldo(saldo)
    elif opcao == 4:
        print("Obrigado por utilizar nossos serviços.")
        break
    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")
    