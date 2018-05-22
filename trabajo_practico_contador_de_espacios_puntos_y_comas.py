
frase_del_usuario = input('Escribe una frase: ')

puntos = '.'
espacios = ' '
comas = ','

cantidad_puntos = 0
cantidad_espacios = 0
cantidad_comas = 0

for digito in frase_del_usuario:
    if digito in puntos:
        cantidad_puntos += 1
    elif digito in espacios:
        cantidad_espacios += 1
    elif digito in comas:
        cantidad_comas += 1

print('El numero de puntos es {}'.format(cantidad_puntos))

print('El numero de espacios es {}'.format(cantidad_espacios))

print('El numero de comas es {}'.format(cantidad_comas))

suma_elementos = cantidad_comas + cantidad_espacios + cantidad_puntos

print('El total de los 3 elementos es {}'.format(suma_elementos))



