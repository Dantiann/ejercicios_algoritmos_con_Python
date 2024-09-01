radio,altura=float(input('Ingrese el radio del cilindro: ')),float(input('Ingrese la altura del cilindro: '))
import math
volumen = round((math.pi*radio**2*altura),2)
area = round((2*math.pi*radio*altura+2*math.pi*radio**2),2)
print('El volumen del cilindro es: ',volumen,'\n& el área del cilindro es: ',area)
