menu = """
[d] DEPOSITAR
[s] SACAR
[e] EXTRATO
[q] SAIR

Opção: """
bem_vindo = 'Bem-Vindo ao seu sistema bancário'
saldo = 0
limite = 500 #limite por saque
extrato = ""
numero_saques = 0 #contador do número de saques
LIMITE_SAQUES = 3 #constante da quantidade máxima de saques

print('=-' * 20)
print(f'{bem_vindo}')
print('=-' * 20)

while True:

    print('Qual operaçao deseja fazer?')
    opcao = input(menu).strip().lower()[0]
    if opcao not in 'dseq':
        while opcao not in 'dseq':
            print('Informe a opção correta:')
            opcao = input(menu)

    if opcao == 'd':
        valor = float(input('VALOR DO DEPÓSITO R$: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print('FALHA NA OPERAÇÃO! VALOR INVÁLIDO.')

    elif opcao == 's':
        valor = float(input('VALOR DO SAQUE: '))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('FALHA NA OPERAÇÃO! SALDO INSUFICIENTE.')

        elif excedeu_limite:
            print('FALHA NA OPERAÇÃO! VALOR DO SAQUE EXCEDE LIMITE')

        elif excedeu_saques:
            print('FALHA NA OPERAÇÃO! QUANTIDADE DE SAQUES EXCEDIDO')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1

        else:
            print('FALHA NA OPERAÇÃO! VALOR INVÁLIDO.')

    elif opcao == 'e':
        print()
        print('='*8, 'EXTRATO', '='*8)
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'Saldo: R$ {saldo:.2f}')
        print('='*25)

    elif opcao == 'q':
        break
