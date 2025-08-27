palavra_proibida = ('carro', 'linguiça', 'abajuor', 'garrafa', 'guarda-chuva')
barra = str(input('Digite palavras permitidas: '))

if barra in palavra_proibida :
    print('está palavra é proibida')
elif barra not in palavra_proibida :
    print('palavra liberada')
else :
    print('nenhuma palavra digitada')