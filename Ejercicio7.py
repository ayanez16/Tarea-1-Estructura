#Determinar la cantidad de dinero que recibira un trabajador por concepto de las horas extras trabajadas en una empresa, sabiendo que cuando
#las horas de trabajo exceden de 40, el resto se consideran horas extras y que estas se pagan el doble de una hora normal cuando no exceden
#de 8; si las horas extran exceden de 8 se pagan las primeras 8 al doble de lo que se paga por una hora normal y esl resto al triple
class Ejercicio7:
    def __init__(self):
        pass
    def calcularJornada(self):
        h,hex,hext=0,0,0
        p,phex,ptr,p8=0,0,0,0
        h = int(input("Ingrese las horas trabajadas: "))
        p = float(input("Ingrese el valor hora: "))
        if h > 40:
            hex = h-40
            if hex > 8:
                hext = hex-8
                p8 = 8*p*2
                p8 = hext*p*3
            else:
                p8 = h*p*2
            ptr = 40*p*phex+p8
        else:
            ptr = h*p
        print("Sobretiempo<8:{} Sobretiempo>8:{} Jornada:{} ".format(p8,phex,ptr))
ejercicio = Ejercicio7()
ejercicio.calcularJornada()
            