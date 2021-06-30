#Diseñe un pseudocódigo para calcular la suma y producto de N números enteros, utilizando un bucle controlado por centinela.
class Bucles:
    def __init__(self):
        pass
    def control_centinela(self):
        suma = 0
        prod = 1
        n = int(input("Ingrese numero: "))
        while n != -1:
            suma = suma + n
            prod = prod * n
            print ("Controlado por centinela: Total suma: {} - Total producto: {}".format(suma,prod))
            n = int(input("Ingrese numero: "))
Bucles = Bucles()
Bucles.control_centinela()