menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
"""

saldo = 0;
limite = 500;
extrato = "";
LIMITE_SAQUES = 3



while True:
    print ("---Bem vindo ao Banco V---")
    opcao = input(menu)
    

    if opcao == "1":
        
        try:
            print("Operação: depósito");
            deposito = float(input("Insira o valor que deseja depositar: "));
        except ValueError:
            print("Erro. Insira um valor válido.")
        

    elif opcao == "2":
        print("Sacar");

    elif opcao == "3":
        print("Extrato");

    elif opcao == "0":
        print ("Obrigado por utilizar nossos serviços.")
        break

    else:
        print ("Operação inválida. Por favor, confira o número da opção e digite novamente.")
