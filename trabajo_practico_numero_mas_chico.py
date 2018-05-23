
numeros_usuario = []
numero_del_usuario = ''

while len(numeros_usuario) < 10:

    while not numero_del_usuario.isdigit():
        numero_del_usuario = input('Dime un numero: ')

    numeros_usuario.append(int(numero_del_usuario))
    numero_del_usuario = ''
    print('Numero anadido!')

numero_chico = numeros_usuario[0]

for numero in numeros_usuario:
    if numero_chico > numero:
        numero_chico = numero

print('El numero mas chico es el: {}'.format(numero_chico))









