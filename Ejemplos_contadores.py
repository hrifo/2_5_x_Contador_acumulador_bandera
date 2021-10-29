print('Ejemplo de contador')

variable = input('Ingrese una palabra para contar:')
contador = 0

for i in variable:
    contador=contador+1

print(f'La palabra "{variable}" tiene  {contador} letras')