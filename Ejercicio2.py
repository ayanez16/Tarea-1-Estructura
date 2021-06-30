#En una tienda se ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto debera pagar finalmente por su compra.

class Ejercicio2:
    def __init__(self):
        pass
def ejecutar():
    C = float(input("Ingrese el total de la compra")) 
    A = C*0.15
    P = C - A
    print("La cantidad a pagar es: ")
    print (P,"$")

ejecutar()