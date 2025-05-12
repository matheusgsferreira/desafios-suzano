# Desafio
banco = " Banco da DIO "
print(banco.center(30,'-'))

saldo = float(1000)
extrato=""
saques = ""
depositos = ""
VALOR_SAQUE_MAXIMO = 500
SAQUE_MAXIMO_DIARIO = 3
saques_dia = 0
menu = '''
Digite a Opção:

[1] Saque
[2] Depósito
[3] Extrato
[4] Sair
-->
'''
while True:
    opcao = int(input(menu))

    if (opcao) == 1 and saques_dia <= SAQUE_MAXIMO:
        valor_saque = float(input("Digite o valor do Saque: R$ "))
        if valor_saque > saldo:
            print("\nSaldo insuficiente ou Limite Diário Alcançado. \nConsulte seu extrato.")
        elif:
            extrato = extrato + "- R$ " + str(valor_saque) 
            saques = saques + "- R$ " + str(valor_saque)
            saldo -= valor_saque
            saques_dia+=1
            print(f"Retire seu dinheiro.")
    elif saques_dia == SAQUE_MAXIMO SAQUE_MAXIMO_DIARIO
        print("Limite Diário Alcançado.")
    # elif (opcao) == 