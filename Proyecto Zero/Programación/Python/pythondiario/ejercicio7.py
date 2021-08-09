from ejercicio6 import inversa
print('linea2')

palabra = input('Ingrese una palabra\n\n\n')
inversa = inversa(palabra)

letra = 0
palindromo = False
for i in range(0, len(palabra)):
    if palabra[i] == inversa[i]:
        letra += 1
    if letra == len(palabra):
        palindromo = True

if palindromo:
    print('La palabra que usted ingresó, es un palindromo.')
else:
    print('Su palabra no esta registrada como palindromo.')