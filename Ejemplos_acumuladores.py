print('Ejemplo de acumuladores')

palabra='NO'
acumulador=0
while palabra!='SI':
    variable = int(input('Ingrese valores para sumar:'))
    acumulador = acumulador + variable
    palabra = input('Desea salir?: ')

print(f'El valor de las sumas es {acumulador}')