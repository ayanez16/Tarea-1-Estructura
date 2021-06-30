#Calcular la suma de los cuadrados de los primeros 100 enteros y escribir el resultado.
class Ejercicio11:
    def __init__(self):
        pass
    def cicloFor(self):
        i = 1
        suma = 0
        for i in range(100):
            suma=suma+i*1
            print("La suma de los cuadrados es: ",suma)
resultado=Ejercicio11()
resultado.cicloFor()
