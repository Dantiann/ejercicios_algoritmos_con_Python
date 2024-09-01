catA,catB=float(input('Ingrese el cateto A: ')),float(input('Ingrese el cateto B: '))
import math
hipotenusa = round(math.sqrt(catA**2+catB**2),2)
print('La hipotenusa del triángulo es: ', hipotenusa)
