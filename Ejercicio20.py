#Se tiene información sobre las calificaciones de 6 exámenes de un grupo de 30 alumnos. 
#Los datos sobre estos exámenes se proporcionan de la siguiente manera:
class arreglos:
    def __init__(self) -> None:
        pass
    def arreglo3(self):
        notas_listas = []
        alumnos_lista = []
        ALUMNOS = 30
        CASILLAS_NOTAS = 6
        promedio_examenes = []
        for alumno in range(1, 31):
            """lectura de los 30 alumnos."""
            alum_temporal=input("nombre del alumno {}: ".format(alumno))
            alumnos_lista.append(alum_temporal)
            for nota in range(1, 7):
                print("escriba la calificacion del alumno en el examen """.format(alum_temporal, nota))
                """lectura de las 6 calificaciones de los 30 alumnos."""
                notas_temporal= round(float(input("nota #{}: ".format(nota))),2)
                if nota ==1:
                    notas_listas.append/([notas_temporal])
                else:
                    notas_listas[alumno-1].append(notas_temporal)
            print("")
            """calculo promedio de calificaciones de cada uno de los examenes"""
            for numero_examen in range(6):
                suma_notas = 0
                for notas in notas_listas:
                    suma_notas += nota[numero_examen]
                    promedio = round((suma_notas/ALUMNOS),2)
                    if prom_mayor < promedio:
                        prom_mayor = promedio
                    promedio_examenes.append(promedio)
            print("")
            print("el examen", promedio_examenes.index(prom_mayor)+1,"obtuvo el mayor promedio:",prom_mayor)
class1= arreglos()
class1.arreglo3()
