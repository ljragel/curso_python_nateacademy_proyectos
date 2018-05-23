
numero_del_usuario = int(input('De que numero quieres la tabla de multiplicar?: '))


for multiplo in range(1,11):
    print('{} x {} = {}'.format(numero_del_usuario, multiplo, (numero_del_usuario * multiplo)))

