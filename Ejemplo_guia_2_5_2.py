print('-----Venta de cursos EDUCATE-ONLINE-----')

bandera = True
contador = 0
while bandera == True:
    print('Cursos a la venta: ')
    print('Nombre de curso\t\tValor')
    print('1.- Programación\t$250.000')
    print('2.- Base de datos\t$310.000')
    print('3.- Robótica\t\t$280.000')
    numero = int(input('¿Qué curso desea comprar? (Seleccione el numero)'))
    if numero in (1,2,3):
        print('Numero correcto')
    else:
        print('Numero no existe, reintente')
        contador+=1
    if contador == 3:
        print('Se solicita el fin del programa, 3 intentos fallidos.')
        bandera = False

    