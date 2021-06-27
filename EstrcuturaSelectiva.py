# _Ejercicio 1:ESTRCUTURAS SELECTIVAS SIMPLES_
class Tarea:
    def aprobar(self):

        calf = float(input("Ingrese la calificacion : "))

        if calf >= 7 :
            print("Felicidades usted ha aprobado con una calificacion de {}".format(calf))


        #_ Ejercicio 2: ESTRUCTURAS SELECTIVAS DOBLES_
        calf = float(input("Ingrese la calificacion : "))

        if calf >= 7 :
            print("Felicidades usted ha aprobado con una calificacion de {}".format(calf))
        else:
            print("Usted ha reprobado")

    # _Ejercicio 3_

    def aumento(self):

        sueldo_b = float(input("Ingrese el sueldo del trabajador : "))

        if sueldo_b <= 600:
            aumento = sueldo_b * 0.10
            n_sueldo = sueldo_b + aumento
        else:
            n_sueldo=sueldo_b
        print("El sueldo final que el trabajador recibira es : {} USD".format(n_sueldo))


    # _Ejercicio 4: ESTRUCTURAS SELECTIVAS COMPLEJAS_

    def pago_hora(self):
        horas = int(input("Ingrese las de horas trabajadas : "))
        pago_h= float(input("Ingrese el valor a pagar por hora trabajada : "))

        if horas > 40:
            h_ext = horas - 40
            if h_ext > 8:
                sobrepasan_extras = h_ext -8
                pago_h_ext = ((pago_h * 2) *8)+((pago_h * 3)*h_ext)
            else:
                pago_h_ext = pago_h*(h_ext*2)
            pago_t = (pago_h*40)+pago_h_ext
        else:
            pago_t=pago_h * horas
        print("Usted a trabajado {} horas , por tanto recibira el total de  {}".format(horas,pago_t))

    # _Ejercicio 5_
    def mayor(self):
        n1 = float(input("Ingrese el primer numero : "))
        n2 = float(input("Ingrese el segundo numero : "))
        n3 = float(input("Ingrese el tercer numero : "))

        if n1 > n2 and n1 > n3:
            may = n1
        elif  n2 > n3:
            may = n2
        else:
            may = n3
        print("De los 3 numeros ingresados {} , {} , {} el numero mayor es  {}".format(n1,n2,n3,may))

# _Ejercicio 6: ESTRUCTURAS SELECTIVAS MULTIPLES_
    def seleccion(self):

        val= int(input("Ingrese un valor cualquiera: "))
        num =int(input("Ingrese un numero del 1 al 3: "))

        if num == 1:
            resp = 100 * val
        if num == 2:
            resp = 100 ** val
        if num == 3:
            resp = 100 / val
        if num > 3 or num < 1:
            resp = "error"
        print(resp)

# _Ejercicio 7: EXPRESIONES LOGICAS_
    def comprobar_calif(self):
        calf1 = float(input("Ingrese la calificacion del primer examen: "))
        calf2 = float(input("Ingrese la calificacion del segundo examen: "))

        if calf1 >= 80 and calf2 >=80:
            print("Usted ha aprobado")
        else:
            print("Usted ha reprobado")

    # _Ejercicio 8_

        calf1 = float(input("Ingrese la calificacion del primer examen: "))
        calf2 = float(input("Ingrese la calificacion del segundo examen: "))

        if calf1 >= 90 or calf2 >=90:
            print("Usted ha aprobado")
        else:
            print("Usted ha reprobado")

ejercicios=Tarea()
# ejercicios.aprobar()
# ejercicios.aumento()
# ejercicios.pago_hora()
# ejercicios.mayor()
# ejercicios.seleccion()
# ejercicios.comprobar_calif