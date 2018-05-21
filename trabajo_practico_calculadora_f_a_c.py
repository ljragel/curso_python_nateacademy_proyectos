
dato_a_transformar = (input('Dime a que quieres transformar ( Celsius / Farenheit ): '))

if dato_a_transformar == 'Celsius':
    medida_resultado = 'Celsius'
    dato_a_transformar = int(input('Decime el valor a transformar: '))
    resultado_de_la_cuenta = int((dato_a_transformar - 32) / 1.800)


else:
    medida_resultado = 'Farenheit'
    dato_a_transformar = int(input('Decime el valor a transformar: '))
    resultado_de_la_cuenta = int((dato_a_transformar * 1.800 + 32))


print('El resultado es: {} grados {}'.format(resultado_de_la_cuenta, medida_resultado))

