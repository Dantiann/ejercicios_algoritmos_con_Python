# variable
seguro=float(input('Digite el valor del seguro: '))

# proceso
if seguro < 5000000:
    valor_poliza=seguro*0.03
elif seguro >= 5000000 and seguro < 20000000:
    valor_poliza=seguro*0.02
elif seguro >= 20000000:
    valor_poliza=seguro*0.015
else:
    print('Valor incorrecto')    

# resultado
print('El valor de la póliza a pagar es de: ', valor_poliza)

    

