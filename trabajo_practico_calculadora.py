cuenta_elegida = input('Eliga una operacion a realizar (Sumar / Restar / Multiplicar / Dividir): ')

resultado_final = 0
primer_numero = 0
segundo_numero = 0

primer_numero = int(input('Eliga un numero: '))
segundo_numero = int(input('Elija el segundo numero: '))

if cuenta_elegida == 'Sumar':
    resultado_final = primer_numero + segundo_numero
    print('Tu resultado es {}'.format(resultado_final))

elif cuenta_elegida == 'Restar':
    resultado_final = primer_numero - segundo_numero
    print('Tu resultado es {}'.format(resultado_final))

elif cuenta_elegida == 'Multiplicar':
    resultado_final = primer_numero * segundo_numero
    print('Tu resultado es {}'.format(resultado_final))

elif cuenta_elegida == 'Dividir':
    resultado_final = primer_numero / segundo_numero
    print('Tu resultado es {}'.format(resultado_final))






























