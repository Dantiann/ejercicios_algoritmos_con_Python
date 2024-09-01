var_altura=int(input('¿cuánto mides?: '))

def mostrarbase(peso):
    print('Este será', peso)
def mostrarAltura(altura):
   
    
    resultado=''
    
    if altura >=180:
       resultado='Eres alto'
    
    else: 
        resultado='Eres bajito'
    mostrarbase(18)
    
    return resultado    

print(mostrarAltura(var_altura))        