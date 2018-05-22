
texto_usuario = input('Dime una frase: ')

mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numero_mayusculas = 0

for letra in texto_usuario:
    if letra in mayusculas:
        numero_mayusculas += 1

print('El numero de mayusculas es {}'.format(numero_mayusculas))

