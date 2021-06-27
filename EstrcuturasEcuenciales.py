# _Ejercicio #1_
class Tarea:
    def descuento(self):
        T_compra = float(input("Ingrese el total de compra: " ))
        dsct = T_compra * 0.15
        cant_pagar = T_compra - dsct
        print("""El total de la compra es : {} USD , el descuento recibido es : {} USD , 
        la cantidad final a pagar es : {} USD """.format(T_compra,round(dsct,2),round(cant_pagar,2)))


# _Ejercicio #2_
    def comision(self):
        salario_base= float(input("Ingrese el salario base del trabajador : "))
        v1 = float(input("Ingrese el valor de la primera venta : "))
        v2 = float(input("Ingrese el valor de la segunda venta : "))
        v3 = float(input("Ingrese el valor de la tercera venta : "))

        t_venta = v1+v2+v3
        com = t_venta * 0.1
        t_pagar = salario_base + com

        print("La comision generada por el trabajador es de {} , por consecuente el moto que recibira como sueldo sera de {}".format(round(com,2),t_pagar))

ejercicio=Tarea()
# ejercicio.descuento()
# ejercicio.comision()