#Diseñar un algoritmo tal que dados como datos dos variables de tipo entero, obtenga el resultado de la siguiente funcion:
class Ejercicio9:
    def __init__(self):
        pass
    def Variables(self):
        nu = float(input("Ingrese la primera variable" ))
        v = float(input("Ingrese la segunda variable" ))
        print()
        if nu ==1:
            rp=(100*v)
        elif nu ==2:
            rp=pow(100^v)
        elif nu ==3:
            rp=(100/v)
        else:
            rp=0
        print("El resultado es: ", rp)
        print()
resultado = Ejercicio9()
resultado.Variables()

        
            