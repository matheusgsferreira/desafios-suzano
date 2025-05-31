# Desafio - Sistema Bancário
from datetime import datetime
import pytz

banco = " Banco da DIO "
print(banco.center(30,'-'))

saldo = 1000
VALOR_SAQUE_MAXIMO = 500
SAQUE_MAXIMO_DIARIO = 3
TRANSACOES_MAXIMAS_DIARIAS = 10
saques_dia = 0
extrato="Extrato".center(50,'#') + f"\nSaldo Inicial: + R$ {saldo:0.2f}"
saques = ""
depositos = ""
HOJE = datetime.strftime(datetime.now(), "%d/%m/%Y")
datas = {}
datas.setdefault(HOJE, 0)

menu = '''
Digite a Opção:

[A] Saque
[B] Depósito
[C] Extrato
[D] Sair

'''
while True:
    opcao = input(menu)
    if (datas[HOJE] < TRANSACOES_MAXIMAS_DIARIAS) and (opcao == 'A' or opcao == 'B'):
        datas[HOJE] +=1
        if (opcao) == 'A':       
            if (saques_dia < SAQUE_MAXIMO_DIARIO):
                valor_saque = int(input("Digite o valor do Saque: R$ "))
                if valor_saque > saldo:
                    print("\nSaldo insuficiente. \nConsulte seu extrato.")
                    datas[HOJE] -=1
                elif valor_saque > VALOR_SAQUE_MAXIMO:
                    print(f"Valor máximo de {VALOR_SAQUE_MAXIMO}")
                    datas[HOJE] -=1
                else:
                    AGORA = datetime.strftime(datetime.now(pytz.timezone("Brazil/East")), "%d/%m/%Y | %H:%M:%S |")
                    extrato = extrato + f"\n{AGORA} - R$ {valor_saque:0.2f}"
                    saques = saques + f"\n{AGORA} - R$ {valor_saque:0.2f}"
                    saldo -= valor_saque
                    saques_dia+=1
                    print(f"Retire seu dinheiro.")
            else:
                print("\nLimite de Saque Diário Alcançado.".center(50,"!")+"\nTente novamente amanhã".center(50,""))
            
        elif (opcao) == 'B':
            AGORA = datetime.strftime(datetime.now(pytz.timezone("Brazil/East")), "%d/%m/%Y | %H:%M:%S |")
            valor_deposito = int(input("Digite o valor do Depósito: R$ "))
            extrato = extrato + f"\n{AGORA} + R$ {valor_deposito:0.2f}"
            depositos = depositos + f"\n+{AGORA} + R$ {valor_deposito:0.2f}"
            saldo += valor_deposito
            print("Depósito Efetuado.")

    elif (datas[HOJE] == TRANSACOES_MAXIMAS_DIARIAS) and (opcao == 'A' or opcao == 'B'):
        print("Limite Diário de Transações alcançado".center(50,"¨"))
    
    elif (opcao) == 'C':
        print(extrato + f"\n Saldo Atual: R$ {saldo:0.2f}")

    elif (opcao) == 'D':
        break
        
    else:
        continue