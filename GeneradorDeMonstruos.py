numMonstruos = int(input)("¿Cuantos monstruos necesitas?: ")
if numMonstruos == 1:
    nomMonstruo = input("Dale nombre al monstruo: ")
    fuerzaMonstruo = int(input("Dale la fuerza al monstruo: ")
elif numMonstruos == 2:
    nomMonstruo1 = input("Dale nombre al monstruo: ")
    fuerzaMonstruo1 = int(input("Dale la fuerza al monstruo: ")
    nomMonstruo2 = input("Dale nombre al monstruo: ")
    fuerzaMonstruo2 = int(input("Dale la fuerza al monstruo: ")
elif numMonstruos == 3:
    nomMonstruo1 = input("Dale nombre al monstruo: ")
    fuerzaMonstruo1 = int(input("Dale la fuerza al monstruo: "))
    nomMonstruo2 = input("Dale nombre al monstruo: ")
    fuerzaMonstruo2 = int(input("Dale la fuerza al monstruo: "))
    nomMonstruo3 = input("Dale nombre al monstruo: ")
    fuerzaMonstruo3 = int(input("Dale la fuerza al monstruo: "))
else:   
    print ("Si quieres mas de 3 o menos de 1, ve a buscar monstruos a otro lado: ")
# Funciones
def generarMonstruos(numMonstruosAGenerar):
    for monstruo in range(numMonstruosAGenerar):
        nomMonstruo = input("Dale nombre al monstruo: ")
        fuerzaMonstruo = int(input("Dale fuerza al monstruo: "))
        print (f"Toma un monstruo llamado {nomMonstruo} de fuerza {fuerzaMonstruo}: ")

numMonstruos = int(input("¿Cuantos monstruos necesitas?: "))
generarMonstruos (numMonstruos)