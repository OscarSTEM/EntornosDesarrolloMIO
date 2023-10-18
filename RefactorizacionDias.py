"""
Refactorizacion: Facilitar la mantenibilidad. -> Hacer funciones
Refactorizacion: Mejorar la legibilidad -> Poner nombres intuitivos
Refactorizacion: simplificar la logica ->Evitar redundancias
Refactorizacion: Facilitar las pruebas ->Automatizar/facilitar los valores de entrada.
"""
#Funcion
"""
#Estas 3 funciones se quedan resumidas en solicitarNum(texto)
def solicitarDia():
    return int(input("Introduce un día del mes: "))
def solicitarMes():
    return int(input("Introduce un mes: "))
def solicitarAnio():
    return int(input("Introduce un año: "))
"""
def solicitarNum(texto):
	return int(input(f"Introduce un {texto}: "))
def mesNumericoATexto(numMes):
	listaMeses = ["Enero","Febrero","Marzo","Abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
	textoMes = listaMeses[numMes-1] # -1 es porque recoge enero en la lista como el numero 0, pero es el numero 1 en el mes y feb en el numero 2 entonces se lo restamos para que lo recoja 
	#en el codigo
	return textoMes


#Codigo Principal
dia = solicitarNum("dia del mes")
mesNumerico = solicitarNum("mes")
mes = mesNumericoATexto(mesNumerico)
mes = mesNumericoATexto(solicitarNum{"mes"}) 
anio = solicitarNum("año")

esValido = True
#Mejor preguntamos lo mas probable, en este caso el año
if anio < 2025:
	if mes == "febrero" and dia > 28:
		esValido = False
	elif (mes == "septiembre" or mes == "noviembre" or mes == "abril" or mes == "junio")and dia > 30:
		esValido = False
	elif dia > 31:
		esValido = False
else: 
	esValido = False
print (f"El mes {mes} es {mesNumericoATexto(mes)}")
"""
d2 = int(input("Introduce un día del mes: "))
m2 = int(input("Introduce un mes: "))
a2 = int(input("Introduce un año: "))

if m2 == "febrero" and d2 > 28:
	print("No es valido")
elif (m2 == "septiembre" or m2 == "noviembre" or m2 == "abril" or m2 == "junio")and d2 > 30:
	print("No es valido")
elif d2 > 31:
	print("No es valido")
	
if a2 > 2025:
	print("No es valido")
	
d3 = int(input("Introduce un día del mes: "))
m3 = int(input("Introduce un mes: "))
a3 = int(input("Introduce un año: "))

if m3 == "febrero" and d3 > 28:
	print("No es valido")
elif (m3 == "septiembre" or m3 == "noviembre" or m3 == "abril" or m3 == "junio")and d3 > 30:
	print("No es valido")
elif d3 > 31:
	print("No es valido")
	
if a3 > 2025:
	print("No es valido")
	
d4 = int(input("Introduce un día del mes: "))
m4 = int(input("Introduce un mes: "))
a4 = int(input("Introduce un año: "))

if m4 == "febrero" and d4 > 28:
	print("No es valido")
elif (m4 == "septiembre" or m4 == "noviembre" or m4 == "abril" or m4 == "junio")and d4 > 30:
	print("No es valido")
elif d4 > 31:
	print("No es valido")
	
if a4 > 2025:
	print("No es valido")
"""
