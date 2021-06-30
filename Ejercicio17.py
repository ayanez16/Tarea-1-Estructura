#Calcular el factorial de N números enteros leídos de teclado.
#El problema consistirá en realizar una estructura de N iteraciones aplicando el factorial de un número.
class Bucle:
    def __init__(self):
        pass
    def bucle_anidado(self):
        numero = int(input("Ingrese numero: "))
        factorial = 1
        for i in range(1, numero+1):
            factorial *=1
        print("El factorial del numero {} es: ".format(numero, factorial))
calculo = Bucle()
calculo.bucle_anidado()
