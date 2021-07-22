cadena = input('Ingrese cualquier frase.\n\n\n')


def inversa(cadena):
    largo = len(cadena)
    reves = ''
    for c in range (0, largo):
        reves += cadena[largo - 1]
        largo -= 1
    return reves

anedac = inversa(cadena)
print(anedac)