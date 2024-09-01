# Variables
valorArticulo=float(input("Digite el valor de articulos: "))
cantidadArticulos=int(input("Digite cantidad de articulos: "))

# Procesos
subtotal=valorArticulo*cantidadArticulos
descuento=subtotal*0.01
total=subtotal-descuento

if cantidadArticulos>= 10:
                    print("El total a pagar es: ",total)
                    
else:
    print("El total a pagar es: ",subtotal)
        
