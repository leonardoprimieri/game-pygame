def userInfos():

    log = open('userInfo.txt', 'a')
    name = input('Informe seu nome: ')
    email = input('Informe seu email: ')
    log.write(f' \nNome do jogador: {name} | E-mail do jogador: {email}')
    log.close()
