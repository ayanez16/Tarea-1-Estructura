#Diseñe un pseudocódigo para calcular la suma y producto de N números enteros, utilizando un bucle controlado por el usuario.
class SumProdt:
    def __init__(self):
        pass
    def control_condicion(self):
        suma=0
        produc=1
        resp=input("Desea ingresar (S/N)?: ")
        while(resp != "N") and (resp !=  "n"):
            num = int(input("Ingrese numero: "))
            suma = suma + num
            produc = produc * num
            print( "Desea continuar (S/N)?: ")
            resp = input("Ingrese: ")
        print("controlado por condicion: Total suma: {} - Total producto: {}".format(suma,produc))
        
bucles = SumProdt()
bucles.control_condicion()
