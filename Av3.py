av1 = float(input('Nota da AV1: '))
av2 = float(input('Nota da AV2: '))
edag = float(input('Nota do EDAG: '))

av3 = ( 7 - ((av1*0.25) + (av2*0.25) + (edag*0.2)) ) / 0.3

print('Precisará de {:.2f} na av3'.format(av3))