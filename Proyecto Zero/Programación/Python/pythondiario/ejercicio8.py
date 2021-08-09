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

def lectura(valor1, valor2):
    control = 'No'
    miembroComun = False
    for i in range(0, len(valor1)):
        for j in range(0, len(valor2)):
            if valor1[i] == valor2[j]:
                control = 'Si'
    if control == 'Si':
        miembroComun = True
    return miembroComun

miembroComun = lectura(lista1, lista2)
print('¿Habrá miembros en común?...\n\n\n\n' + str(miembroComun) + '.')