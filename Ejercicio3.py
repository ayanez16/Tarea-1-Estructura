#Un vendedor recibe u sueldo base mas un 10% extra por comision de sus ventas.
#El vendedor desea saber cuanto dinero obtendra por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibira
#en el mes tomando en cuenta su sueldo base y sus comosiones.
class Ejercicio3:
    def run():
        S=float(input("Ingrese el salario base: "))
        V1=float(input("Ingrese el valor de la primera venta: "))
        V2=float(input("Ingrese el valor de la segunda venta: "))
        V3=float(input("Ingrese el valor de la tercera venta: "))
        T=V1+V2+V3
        B=T*0.10
        R=S+B
        print("El total del salario a recibir es: $")
        print(R,"El sueldo a recibir: $")
    run()
    