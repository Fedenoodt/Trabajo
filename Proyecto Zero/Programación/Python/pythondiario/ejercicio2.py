def max(numero1, numero2, numero3):
    devolucion = 0
    if numero1 > numero2 and numero1 > numero3:
        devolucion = numero1
    elif numero2 > numero1 and numero2 > numero3:
        devolucion = numero2
    elif numero3 > numero1 and numero3 > numero2:
        devolucion = numero3
    return devolucion

numero1 = int(input('>>>    '))
numero2 = int(input('>>>    '))
numero3 = int(input('>>>    '))

devolucion = max(numero1, numero2, numero3)
print(devolucion)