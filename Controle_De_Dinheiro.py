transacoes = []
valor_conta = 0
def Mostrar_Menu():
        print()
        print('''[1] Nova transação
[2] Ver saldo
[3] Ver transações
[4] Sair         
''')
def escolher_opcao():
      while True:
            try:
                  opcao = int(input('Digite sua opção: '))
                  if opcao in [1,2,3,4]:
                        return opcao
                  elif opcao in [999]:
                       return opcao
                  else:
                        print('Erro! Digite um valor válido (digite de 999 pra voltar ao menu)')
            except ValueError:
                  print('Erro! Digite apenas números. (digite de 999 pra voltar ao menu)')
def escolher_tipo_transacao():
    print('[1] Para Adicionar \n[2] Para retirar')
    opcao_transacao = int(input('Escolha sua opção: '))
    try:
        if opcao_transacao in [1, 2]:
            return opcao_transacao
        else:
            print('Erro! Digite um valor válido.')
    except ValueError:
        print('Erro! Digite apenas Números.')
     

while True:
    Mostrar_Menu()
    opcao = escolher_opcao()
    if opcao == 1:
        tipo = escolher_tipo_transacao()
        valor = float(input('Digite o valor: '))
        try:    
            if tipo == 1:
                valor_conta += valor
            elif tipo == 2:
                valor_conta += valor
            else:
                print('Houve um erro, o programa será encerrado.')
                break
        except:
            print('Houve um erro, o programa será encerrado.')
            break    
    elif opcao == 2:
        print(f'Seu saldo atual é de R${valor_conta}')