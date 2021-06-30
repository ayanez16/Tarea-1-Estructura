#Sea un vector “Calificaciones” de 100 componentes:
#En forma de columna se representaría así:
class Ejercicio18:
    def __init__(self) -> None:
        pass
    def arrg1(self):
        calificaciones = []
        for i in range(10):
            nuevoDato = int(input("Diga el dato numero {}: ".format(i)))
            calificaciones.append(nuevoDato)
        print("Las calificaciones son: {}".format(calificaciones))
resultado=Ejercicio18()
resultado.arrg1()

            