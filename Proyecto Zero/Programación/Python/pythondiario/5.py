numeros = []
numero = ''

def sumar(numeros):
    suma = 0
    for i in numeros:
        suma += i
    return suma

def multiplicar(numeros):
    multiplicacion = 1
    for i in numeros:
        multiplicacion *= i
    return multiplicacion

while numero != '*':
    numero = input('Ingrese un número ("*" para finalizar.) :')
    if numero != '*':
        numeros.append(int(numero))

suma = sumar(numeros)
multiplicacion = multiplicar(numeros)
print(suma)
print(multiplicacion)