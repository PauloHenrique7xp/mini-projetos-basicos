import emoji

print('=================== SISTEMA DE CADASTRO ===============')
nome_cadastrado = input('Informe um nome para cadastro: ')
senha_cadastrada = input('Informe uma senha para cadastro (6 a 12 caracteres): ')
print('=======================================================')

tentativa = 0
while tentativa < 3:
    print('\n=================== LOGIN ===================')
    nome = input('Informe o nome cadastrado: ')
    senha = input('Informe a senha cadastrada: ')
    print('=============================================')
    if nome == nome_cadastrado and senha == senha_cadastrada and 6 <= len(senha) <= 12:
        print(emoji.emojize(':check_mark_button: LOGIN REALIZADO COM SUCESSO'))
        exit()  
    elif nome != nome_cadastrado and senha != senha_cadastrada:
        print(emoji.emojize('ERRO: :cross_mark: Nome e senha inválidos'))
        tentativa += 1  
    elif nome != nome_cadastrado:
        print(emoji.emojize('ERRO: :cross_mark: Nome incorreto'))
        tentativa += 1 
    elif senha != senha_cadastrada:
        print(emoji.emojize('ERRO: :cross_mark: Senha incorreta'))
        tentativa += 1
else: 
    print('Máximo de tentativas atingidas, tente novamente mais tarde ⚠️')
