# _Ejercicio 1: Estructura FOR_
class Tarea:
    def suma_cuadrados(self):
        sum = 0
        for i in range(1, 101):
            sum = sum + (i * i)
        print("La suma de los cuadrados de los primeros 100 enteros es : {}".format(sum))

        # _Ejercicio 2: ESTRUCTURA WHILE_

    def primeros_primos(self):
        i = 1
        while i <= 100:
            print("presentacion de los 100 primeros numeros: ", i)
            i += 1

    # _Ejercicio 3_
    def suma_multiplicacion(self):
        sum = 0
        producto = 1
        respuesta = input("Desea continuar? (Pulse X para salir) ")

        while respuesta.lower() != "n":
            num = int(input("Ingrese un numero entero : "))
            sum = sum + num
            producto = producto * num
            respuesta = input("Desea continuar? (Pulse X para salir) ")

        print("El total de la suma es : {} y el total de la multiplicacion : {}".format(sum, producto))

    # _Ejercicio 4_
    def suma_multi(self):
        sum = 0
        producto = 1
        num = int(input("Ingrese un numero entero (Digite -1 para salir): "))

        while num != -1:
            sum = sum + num
            producto = producto * num
            num = int(input("Ingrese un numero entero (Digite -1 para salir): "))

        print("El total de la suma es : {} y el total de la multiplicacion : {}".format(sum, producto))

    # _Ejercicio 5_
    def num_primo(self):

        num = int(input("Ingrese un numero entero : "))
        primo = True
        divisor = 2

        while (divisor < num) and primo == True:
            residuo = num % divisor
            if residuo == 0:
                primo = False
            divisor += 1
        if primo == True:
            print("El numero {} es un numero primo".format(num))
        else:
            print("El numero {} no es un numero primo".format(num))

    # _Ejercicio 6_
    def factorial(self):
        num = int(input("Ingrese el numero de veces que desea repetir el bucle : "))

        i = 1
        for i in range(num):
            n = int(input("Ingrese el numero que desea calcular el factorial : "))
            fact = 1
            for j in range(n):
                fact = fact * (j + 1)
            print("El factorial del numero {} , es : {}".format(n, fact))


ejercicio = Tarea()
# ejercicio.suma_cuadrados()
# ejercicio.primeros_primos()
# ejercicio.suma_multiplicacion()
# ejercicio.suma_multi()
# ejercicio.num_primo()
# ejercicio.factorial()