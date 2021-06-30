#Leer tres numeros enteros diferentres entre si y determinar el numero mayor de los tres.
class Ejercicio8:
    def __init__(self):
        pass
    def NumMayor(self):
        print("")
        n1 = int(input("Ingrese el primer numero entero: "))
        n2 = int(input("Ingrese el segundo numero entero: "))
        n3 = int(input("Ingrese el tercer numero entero: "))
        print()
        if n1 > n2 and n1 > n3:
            nM = n1
        else:
            if n2 > n3:
                nM = n2
            else:
                nM = n3
        print ("El numero mayor es:", nM)
        print()
ejercicio = Ejercicio8()
ejercicio.NumMayor()

 
        