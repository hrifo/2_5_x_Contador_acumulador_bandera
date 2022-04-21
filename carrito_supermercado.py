agua=600
azucar = 1200
aceite = 1500

contador=0
productos=[]
p1=input('Quieer llevar agua?: ')
if p1 == 'si':
    c=int(input('Cuanto?'))
    contador=contador+(agua*c)
    productos.append(f'Agua: {agua}*{c}')
p2=input('Quieer llevar azucar?: ')
if p2 == 'si':
    c=int(input('Cuanto?'))
    contador=contador+(azucar*c)
    productos.append(f'Azucar:{azucar}*{c} ')
p3=input('Quieer llevar aceite?: ')
if p3 == 'si':
    c=int(input('Cuanto?'))
    contador=contador+(aceite*c)
    productos.append(f'Aceite: {aceite}*{c}')
