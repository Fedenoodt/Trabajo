listaA = []
listaB = []

def ingresar(valor):
    ingreso = ''
    pase = True
    while pase:
        ingreso = input('Ingrese algo... ("*" para parar)')
        if ingreso != '*':
            valor.append(ingreso)
        else:
            pase = False
    return valor

lista1 = ingresar(listaA)
print('Ahora la otra lista...')
lista2 = ingresar(listaB)


print(lista1)
print(lista2)

def lectura(valor1, valor2):
    for i in range(0, len(valor1)):
        for j in range(0, len(valor2)):
            if valor1[i] == valor2[i]:
                print('a')

lectura(lista1, lista2)