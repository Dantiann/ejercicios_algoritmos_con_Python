print('"Digite dos números diferentes"')
temporal=0
a,b=int(input('Digite el primer número: ')),int(input('Digite el segundo número: '))
if a<b:
    print('Orden = ',a,', ',b)
else:
    temporal=b
    b=a
    a=temporal
    print('Orden = ',a,', ',b)


