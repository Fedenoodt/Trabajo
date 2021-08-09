cadena = input('Ingrese cualquier frase.\n\n\n')

def inversa(valor):
    largo = len(valor)
    reves = ''
    for c in range (0, largo):
        reves += valor[largo - 1]
        largo -= 1
    return reves