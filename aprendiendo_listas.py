
mi_lista = []
respuesta_usuario = 0

while respuesta_usuario != 'Fin':
    respuesta_usuario = input('Que necesitas comprar? (Escribe Fin para terminar): ')
    mi_lista.append(respuesta_usuario)

for item in mi_lista:
    print('Tengo que comprar {}'.format(item))

print('Esta es la lista de la compra')