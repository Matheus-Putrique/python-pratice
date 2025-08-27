nome = str(input('digite seu nome completo: '))
idade = int(input('digite sua idade completa: '))
altura = float(input('digite sua altura: '))

if idade >= 18 and altura > 1.50 and nome in 'a':
    print('O senhor %s que contém a idade de %i, e a altura de %.2f, você contém todos os requisitos para a vaga ' % (nome, idade, altura))
else :
    print('O senhor %s que contém a idade de %i, e a altura de %.2f, você não contém todos os requisitos para a vaga ' % (nome, idade, altura)) 