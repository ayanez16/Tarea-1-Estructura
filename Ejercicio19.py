#Aplicar las fases  para  la resolución de un problema para leer un vector de números enteros y a
#continuación escribir en un vector A todos los números negativos y en un vector B todos los positivos o iguales a cero.
#Imprimir dichos vectores.
class arreglos:
    def __init__(self):
        pass
    def arreglo1(self):
        nuevo_vector =[]
        A = []
        B = []
        for j in range (0,20):
            numero = int(input("ingrese numero: "))
            nuevo_vector.append(numero)
        for j in nuevo_vector:
            if j >= 0:
                B.append(j)
            else:
                A.append(j)
            print("Vector A con numeros negativos: {}".format(A))
            print("Vector B con numeros positivos: {}".format(B))
mostrar = arreglos()
mostrar.arreglo1()
