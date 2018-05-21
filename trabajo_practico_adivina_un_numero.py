
numero_elegido = int(input('Bienvenido, elige un numero para que adivine tu companero: '))
numero_dicho = 'x'

numero_dicho = int(input('Adivina el numero: '))

while numero_elegido != numero_dicho:

       numero_dicho = int(input('No es ese el numero, dime otro: '))

if numero_dicho == numero_elegido:
    print('Has ganado, el numero es:{}'.format(numero_elegido))
