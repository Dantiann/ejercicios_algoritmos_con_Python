a=int(input('Digite el primer valor: '))
b=int(input('Digite el segundo valor: '))
while a==b:
    print('El número ingresado debe ser diferente al número anterior')
    b=int(input('Digite el segundo valor: '))
c=int(input('Digite el tercer valor: '))
while a==c or b==c:
    print('El número ingresado debe ser diferente a los números anteriores')
    c=int(input('Digite el tercer valor: '))
if a>b and a>c:
    print(a,' ES MAYOR')
elif b>a and b>c:
    print(b, 'ES MAYOR')
else:
    print(c, 'ES MAYOR')
    
