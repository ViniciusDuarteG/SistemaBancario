from operator import __neg__

valor_em_conta = float(1000.00)
valor_a_depositar = float(0)
valor_saque = float(0)
quantd_de_saques = 0 
lista_de_transações = []
mensagem_inicial = str("    Bem-vindo ao seu banco")

def deposito():
    global valor_a_depositar, valor_em_conta

    valor_a_depositar = float(input("Quanto deseja depositar: "))
    lista_de_transações.append(valor_a_depositar)
    valor_em_conta = valor_em_conta + valor_a_depositar
    

def sacar():
    global valor_saque, valor_em_conta,quantd_de_saques

    valor_saque = float(input("Quanto deseja sacar: "))
    if valor_saque <= 500:
        if valor_em_conta != 0:
            if quantd_de_saques <= 3:
                if valor_saque <= 500:
                    valor_saque=__neg__(valor_saque)
                    lista_de_transações.append(valor_saque)
                    valor_em_conta = valor_em_conta + valor_saque
                    print("Saque: ",valor_saque)
                    quantd_de_saques = quantd_de_saques + 1
            else:
                print("Desculpe, limite de saque atingido.")
        else:
            print("Saldo insuficiente")
    else: 
        print("Desculpe, mas o valor excede o permitido.")
    
def extrato():
    print(lista_de_transações)
    print(valor_em_conta)

print('='*len(mensagem_inicial))
print(mensagem_inicial)
print('='*len(mensagem_inicial))

escolha = int(9)

while escolha !=0:
    escolha = int(input("Qual opção deseja seguir:\n1- Deposito\n2-Saque\n3-Saldo e Extrato\n0-Sair\n"))
    if escolha == 1:
        deposito()
    elif escolha == 2:
        sacar()
    elif escolha == 3:
        extrato()
    else:
        break
