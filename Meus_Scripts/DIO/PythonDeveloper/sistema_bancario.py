from datetime import datetime

saldo = 0
limite = 500
saques_realizados = 0
depositos_realizados = 0
total_depositos = 0
total_saques = 0
LIMITE_SAQUES = 3
TRANSACOES_LIMITE = 10
transacoes_realizadas = []
data_atual = datetime.today()

def registrar_transacao(valor, natureza):
    global data_atual, TRANSACOES_LIMITE, transacoes_realizadas
    transacoes_hoje = [t for t in transacoes_realizadas if t == data_atual]
    if len(transacoes_hoje) > TRANSACOES_LIMITE:
        print("Limite de transações diárias atingido. Tente novamente amanhã.")
    else:
        transacoes_realizadas.append(f"{natureza} - R$ {valor:.2f} - {data_atual.strftime('%d/%m/%Y %H:%M')}")

def depositar(valor, natureza="Crédito"):
    global saldo, total_depositos, depositos_realizados
    while valor <= 0:
        print("-"*80)
        print("[ERROR] Digite um valor válido !!!")
        print("-"*80)
        valor = float(
            input("Digite novamente o valor que desejas depositar em sua conta: "))
        print("-"*80)
    saldo += valor
    total_depositos += valor
    depositos_realizados += 1
    registrar_transacao(valor, natureza)
    return "Depósito efetuado com sucesso."

def saque(valor, natureza="Débito"):
    global saldo, saques_realizados, total_saques
    if saques_realizados > LIMITE_SAQUES:
        print("-"*80)
        return "[ERROR] Você atingiu o limite de saques diário."
    while valor <= 0 or valor > limite:
        print("-"*80)
        print(
            f"[ERROR] Digite um valor válido, mas que seja abaixo do seu limite que é de R$ {limite} !!!")
        print("-"*80)
        valor = float(
            input("Digite novamente o valor que desejas sacar de sua conta: "))
        print("-"*80)
    if valor > saldo:
        print("-"*80)
        return "Não é possível sacar o dinheiro pois seu saldo no momento é insuficiente."
    else:
        saldo -= valor
        saques_realizados += 1
        total_saques += valor
        registrar_transacao(valor, natureza)
        return "Saque efetuado com sucesso."

def extrato():
    print("---------- EXTRATO BANCÁRIO ----------")
    for transacao in transacoes_realizadas:
        print(transacao)
    print("-"*80)
    print(f"DEPÓSITOS: R$ {total_depositos:.2f}")
    print(f"SAQUES: R$ {total_saques:.2f}")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("-"*80)
    print(f"Total de saques realizados: {saques_realizados}")
    print(f"Total de depósitos realizados: {depositos_realizados}")
    print("-"*80)

def menu():
    system = "Sistema Bancário"
    print()
    print(f"{'>'*10} {system} {'<'*10}")
    print("""
    [0] - SAIR
    [1] - DEPOSITAR
    [2] - SACAR
    [3] - EXTRATO
    """)
    print(f"{'>'*19}{'<'*19}")
    print()

while True:
    menu()
    opcao = input("Digite o número da opção desejada -> ")
    print()

    if opcao.isdigit():
        opcao = int(opcao)
        if opcao == 0:
            print("-"*80)
            print("Obrigado por utilizar o sistema bancário")
            print("-"*80)
            print()
            break
        elif opcao == 1:
            print(f"{'>'*14} [DEPÓSITO] {'<'*14}")
            print("-"*80)
            valor = float(
                input("Digite o valor em dinheiro que desejas DEPOSITAR em sua conta -> "))
            print("-"*80)
            print("="*80)
            mensagem_deposito = depositar(valor)
            print(f"| {mensagem_deposito} |")
            print("="*80)
        elif opcao == 2:
            print(f"{'>'*14} [SAQUE] {'<'*14}")
            print("-"*80)
            valor = float(
                input("Digite o valor em dinheiro que desejas SACAR em sua conta -> "))
            print("-"*80)
            mensagem_saque = saque(valor)
            print("="*80)
            print(f"| {mensagem_saque} |")
            print("="*80)
        elif opcao == 3:
            print("-"*80)
            extrato()
            print("-"*80)
        else:
            print("Opção digitada é inválida, Digite novamente a opção desejada !!!")
    else:
        print("Digito inválido, favor digitar corretamente uma opção !!!")