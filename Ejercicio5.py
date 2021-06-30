#Dado como dato la calificacion de un alumno en un examen, escriba "aprobado" si s calificacion es mayor o igual que 7 y "reprobado" en
#caso contrario.

class Ejercicio5:
    def __init__(self):
        pass
    def run():
        cal = float(input("Ingrese la calificacion "))
        
        if cal >=7:
            print("aprobado")
            print("Felicidades")
        else:
            print("reprobado")
            print("Siga intentando")
    
    run()