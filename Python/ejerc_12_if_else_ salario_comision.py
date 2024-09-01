# Ingreso de datos
salarioBase=float(input('A. Digite el salario base: '))
ventas1,ventas2,ventas3=input('B. Digite las ventas de cada vendedor\n separadas por un espacio: ').split()
ventas1=float(ventas1)
ventas2=float(ventas2)
ventas3=float(ventas3)

# Proceso comisión por ventas >= $1.000.000
if ventas1 >= 1E6:  
    comision1=0.05
else:
    comision1=0
if ventas2 >= 1E6:  
    comision2=0.05
else:
    comision2=0
if ventas3 >= 1E6:  
    comision3=0.05
else:
    comision3=0

# Proceso bono por vendedor con > ventas durante el mes
if ventas1>ventas2 and ventas1>ventas3:
    bono1=0.02
else:
    bono1=0
if ventas2>ventas1 and ventas2>ventas3:
    bono2=0.02
else:
    bono2=0
if ventas3>ventas1 and ventas3>ventas2:
    bono3=0.02
else:
    bono3=0


print('ventas de cada vendedor:\n','Vendedor 1: $', ventas1, '\n vendedor 2: $', ventas2,'\n Vendedor 3: $',ventas3)
print()
print('Vendedor 1. Salario Total: $', salarioBase+ventas1+ventas1*comision1+ventas1*bono1)
print(f'Vendedor 1 Salario Base: ${salarioBase}; Ventas: $ {ventas1}; Comisión: $ {ventas1*comision1}; Bono :${ventas1*bono1}')
print()

print('Vendedor 2. Salario Total: $', salarioBase+ventas2+ventas2*comision2+ventas2*bono2)
print(f'Vendedor 2 Salario Base: ${salarioBase}; Ventas: $ {ventas2}; Comisión: $ {ventas2*comision2}; Bono :${ventas2*bono2}')
print()
print('Vendedor 3. Salario Total: $', salarioBase+ventas3+ventas3*comision3+ventas3*bono3)
print(f'Vendedor 2 Salario Base: ${salarioBase}; Ventas: $ {ventas3}; Comisión: $ {ventas3*comision3}; Bono :${ventas3*bono3}')


