# Mini projeto: Agenda de contatos
# funcionalidades
# Adicionar contato: Usuário digita o nome e telefone.
# lista de contatos: Mostra todos os contatos cadastrados.
# Sair do programa: Encerra o loop
from time import sleep
contatos = []
while True:
    print('[1] adicionar contato '
    '      [2] Mostra a lista de contato '
    '      [3] Sair do programa')

    opcao = int(input('Informe qual sua escolha: '))
    
    if opcao == 1:
        print('=====Adicionando contatos=====')
        nome = input('Informe o nome: ')
        telefone = input('Informe o telefone: ')
        contatos.append(f'Nome: {nome} Telefone: {telefone}')
        print('Contato adicionado com sucesso')
    elif opcao == 2:
        print('=====Lista de Contatos=====')
        if len(contatos) == 0:
            print('Nenhum contato cadastrado')
        else:
            for listas in contatos:
                print(listas)
    elif opcao == 3:
        sleep(1)
        print('Saindo do programa....')
        sleep(1)
        break
    else:
        print('Opção inválida, tente novamente.')