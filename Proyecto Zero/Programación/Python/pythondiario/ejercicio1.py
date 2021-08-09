def max(numero1, numero2):
    devolucion = 0
    if numero1 > numero2:
        devolucion = numero1
    elif numero2 > numero1:
        devolucion = numero2
    return devolucion

numero1 = int(input('>>>    '))
numero2 = int(input('>>>    '))

devolucion = max(numero1, numero2)
print(devolucion)