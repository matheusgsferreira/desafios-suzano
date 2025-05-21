# Desafio - Sistema Bancário
banco = " Banco da DIO "
print(banco.center(30,'-'))

saldo = 1000
VALOR_SAQUE_MAXIMO = 500
SAQUE_MAXIMO_DIARIO = 3
saques_dia = 0
extrato="Extrato".center(50,'#') + f"\n+ R$ {saldo:0.2f}"
saques = ""
depositos = ""

menu = '''
Digite a Opção:

[A] Saque
[B] Depósito
[C] Extrato
[D] Sair

'''
while True:
    opcao = input(menu)

    if (opcao) == 'A':       
        if (saques_dia < SAQUE_MAXIMO_DIARIO):
            valor_saque = int(input("Digite o valor do Saque: R$ "))
            if valor_saque > saldo:
                print("\nSaldo insuficiente. \nConsulte seu extrato.")
            elif valor_saque > VALOR_SAQUE_MAXIMO:
                print(f"Valor máximo de {VALOR_SAQUE_MAXIMO}")
            else:
                extrato = extrato + f"\n- R$ {valor_saque:0.2f}"
                saques = saques + f"\n- R$ {valor_saque:0.2f}"
                saldo -= valor_saque
                saques_dia+=1
                print(f"Retire seu dinheiro.")
        else:
            print("\nLimite de Saque Diário Alcançado.")
   
    elif (opcao) == 'B':
        valor_deposito = int(input("Digite o valor do Depósito: R$ "))
        extrato = extrato + f"\n+ R$ {valor_deposito:0.2f}"
        depositos = depositos + f"\n+ R$ {valor_deposito:0.2f}"
        saldo += valor_deposito
        print("Depósito Efetuado.")

    elif (opcao) == 'C':
        print(extrato + f"\n Saldo Atual: R$ {saldo:0.2f}")

    elif (opcao) == 'D':
        break
    
    else:
        continue