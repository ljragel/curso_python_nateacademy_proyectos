
lista_de_vocales = []
frase_del_usuario = input('Dime una frase y te dire que vocales que tiene: ')
vocales = ['a', 'e', 'i', 'o', 'u']

for letra in frase_del_usuario:
    if letra in vocales:
        lista_de_vocales.append(letra)

print('Tus vocales son: {} '.format(lista_de_vocales))




