# _Ejercicio 1: ARREGLOS EN UNA DIMENSION_
class Tarea:
    def vectores(self):
        A = []
        B = []
        numeros = [3, -7, 2, 1, -6, 1, -3, 8, 1, 2, 3, 9, -2, -1, -10, 3, 4, 6, -4, 10]

        for i in numeros:
            if i > 0:
                B.append(i)
            else:
                A.append(i)

        print("El vector con los numeros negativos es : ",A)
        print("El vector con los numeros positivos es : ",B)



# _Ejercicio 2 Arreglos en dos dimensiones_

    def calif_matriz(self):
        def calif_matriz(self):
            exam = 6
            alum = 30

            matriz = []
            for i in range(alum):
                matriz.append([])
                for j in range(exam):
                    nota = int(input("Ingrese la nota para el alumno {} en el examen {}: ".format(i + 1, j + 1)))
                    matriz[i].append(nota)

            for alu in matriz:
                print("[", end="")
                for elemento in alum:
                    print("{:8.2f}".format(elemento), end="")
                print("]")

            c = 0
            promediosex = []
            for j in range(exam):
                sum = 0
                for i in range(alum):
                    sum = sum + matriz[i][j]
                prom = sum / alum
                c += 1
                print("El examen {} obtuvo un promedio de {}".format(c, round(prom, 3)))
                promediosex.append(prom)

            print()

            cont = 0
            for i in range(alum):
                sum = 0
                for j in range(exam):
                    sum = sum + matriz[i][j]
                cont += 1
                prom = sum / exam
                print("El alumno{} obtuvo un promedio de  {}".format(cont, round(prom, 3)))

            ex = 1
            cont = 1
            promayor = promediosex[0]
            for i in promediosex:
                if i > promayor:
                    promayor = i
                    ex = cont
                cont += 1
            print("El examen con mayor promedio es el {} con un promedio de {}".format(ex, promayor))


ejercicio=Tarea()
# ejercicio.vectores()
# ejercicio.calf_matriz()