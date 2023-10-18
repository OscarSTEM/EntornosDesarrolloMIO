import random
#Funciones

#Codigo Principal
numMaxDeCaramelos = 5
numCaramelos = 50
sonCaramelos = True

while numCaramelos > 0: 
    if numCaramelos < 5: 
        numMaxDeCaramelos = numCaramelos
    print (f"¡Hola gente! ¿Cuantos caramelos quieres?: ")
    numDulcesNinio = random.randrange(numMaxDulcesPorNinio)+1
    print (f"¡Quiero {numDulcesNinio} dulces!: ")
    numCaramelos += 1 
    numCaramelos -= numMaxDeCaramelos
    print (f"¡Nos han visitado {numMaxDeCaramelos} niños y nos quedan {numCaramelos} dulces: ")
