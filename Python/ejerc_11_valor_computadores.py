cantidad=int(input('Digite el número de computadores comprados: '))
valorEquipos=float(input('Digite el valor unidad del equipo: '))
total=cantidad*valorEquipos

if cantidad<5:
    subtotal= total
if cantidad >5 and cantidad <9:
    subtotal= total*(1-0.05)
elif cantidad >=10: 
    subtotal= total*(1-0.01)

print('El total a pagar es: ',subtotal)    
