print('Insira a seguir suas notas da Av1, Av2 e do Edag!\n')

av1 = float(input('Notas da Av1: '))
av2 = float(input('Notas da Av2: '))
edag = float(input('Notas do EDAG: '))

av3 = ( 7 - ((av1*0.25) + (av2*0.25) + (edag*0.2)) ) / 0.3

print('\nPrecisará de {:.2f} pontos na av3'.format(av3))