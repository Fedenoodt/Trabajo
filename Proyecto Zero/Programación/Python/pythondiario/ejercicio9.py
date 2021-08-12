caracterActual = input('Ingrese un caracter: \n\n')

def generar_n_caracteres(caracter):
    multiplica = int(input('¿Por cuánto desea multiplicar este caracter? \n\n'))
    resultado = caracter * multiplica
    return resultado

resultado = generar_n_caracteres(caracterActual)

def mostrar(resultado):
    print('El resultado es este ' + resultado)

mostrar(resultado)