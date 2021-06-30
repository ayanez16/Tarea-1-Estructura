#Determinar si un número entero proporcionado por el usuario es primo. 
# Un número primo es un entero que no tiene más divisores que él mismo y la unidad. Elaborar Pseudocódigo:
class Bucle:
    def __init__(self) -> None:
        pass
    def control_banderas(self):
        primo = True
        divisor = 2
        numero = int(input("Ingrese numero: "))
        while(divisor < numero)and(primo == True):
            res = numero % divisor
            if res == 0:
                primo = False
            else:
                divisor += 1
        if primo == True:
            print("numero {} es primo".format(numero))
        else:
            print("numero {} no es primo".format(numero))
bucles = Bucle()
bucles.control_banderas()
            
