lista = []

def longitud(lista):
    contador = 0
    for l in lista:
        contador += 1
    return contador

ingreso = ''

while ingreso != 'Hasta aca.':
    ingreso = input('Ingrese algo...\n  Cuando se canse, escriba "Hasta aca."\n\n')
    if ingreso != 'Hasta aca.':
        lista.append(ingreso)
for l in lista:
    if l != '[' and l != ']' and l != "'":
        print(l, end='    ')

largo = longitud(lista)

print('\nEl largo de la lista es de', largo, 'objetos.')