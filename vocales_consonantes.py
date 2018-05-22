
frase_del_usuario = input('Introduce una frase y te dire cuantas vocales y cuantas consonantes tiene: ')
vocales = ['a', 'e', 'i', 'o', 'u']

n_vocales = 0
n_consonantes = 0

for letra in frase_del_usuario:
    if letra in vocales:
        n_vocales += 1
    else:
        n_consonantes += 1

print('El numero de vocales es {}, y el numero de consonantes es {}'.format(n_vocales, n_consonantes))

