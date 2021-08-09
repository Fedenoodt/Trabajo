caracter = ''
while caracter != '*':
    caracter = input('Ingrese un caracter...\n(Ingrese "*" cuando deseé finalizar).\n\n')
    vocal = False

    def esVocal(caracter, vocal):
        caracter = caracter.lower()
        if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
            vocal = True

        if vocal:
            print('La letra que ingresó es una vocal. ¡Felicitaciones!')
        else:
            print('Lamentamos informarle que la letra no es una vocal. Lo sentimos mucho.')

    esVocal(caracter, vocal)