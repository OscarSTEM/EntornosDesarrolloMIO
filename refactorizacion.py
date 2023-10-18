"""
Refactorizacion: Facilitar la mantenibilidad. -> Hacer funciones
Refactorizacion: Mejorar la legibilidad -> Poner nombres intuitivos
Refactorizacion: simplificar la logica ->Evitar redundancias
Refactorizacion: Facilitar las pruebas ->Automatizar/facilitar los valores de entrada.
"""
# Funcion

def calcularDoble(num1):
    return num1*2
def probandoCalcularDoble():
    listaDeNumeros = [-1,0,1,25.5,200]
    listaNumerosEsperados= [-2,0,2,51,500]
    for numero in listaDeNumeros:
        dobleDeNumero = calcularDoble(numero)
        print (f"El doble  de {numero} es {dobleDeNumero}")

"""
Para hacer pruebas ahora mismo tengo que entrar en el codigo
y cambiar el valor con el que llamo a la funcion.
Una forma de hacer la prueba (con lo que sabemos) es solicitando ese numero
con input
"""
#Para probar si calcularDoble(numero)

"""
Bateria de pruebas simplificadas:
Crear una funcion que se llama probandoCalcularDoble() que va a tener
una lista de numeros "aleatorios" [introducidos por nosotros manualmente]
Que vamos a recorrer con un bucle for. Para cada numero de la lista va a llamar a la funcion calcularDoble(numero) y a imprimir por pantalla:
"El doble de {numero} es {dobleDeNumero}
"""

#Codigo Principal
numEntrada = int(input("Dame un numero: "))
print (calcularDoble(numEntrada))
#Para llamar a la funcion debes ponerla abajo como en este caso:
probandoCalcularDoble()