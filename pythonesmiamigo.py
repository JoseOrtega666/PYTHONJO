#ingresar datos de tres alumnos:
#nombre
#edad
#nota
#mesada
#promediar edad, nota y mesada

print("Bienvenido a septiembre")
print("")

def promedio(a, b, c):
    prom = (a + b + c) / 3
    return prom

def edad():
    while True:
        edad = int(input())
        if 10 <= edad <= 20:
            return edad
        else:
            print("Edad no valida, ingrese una edad entre 10 y 20:")

def nota():
    while True:
        nota = float(input())
        if 1 <= nota <= 7:
            return nota
        else:
            print("Nota no valida, ingrese una nota entre 1 y 7:")

def mesada():
    while True:
        mesada = input("Ingrese mesada (numero entero entre 100 y 50000): ")
        if mesada.isdigit():
            mesada = int(mesada)
            if 100 <= mesada <= 50000:
                return mesada
            else:
                print("Mesada no valida, ingrese un valor entre 100 y 50000.")
        else:
            print("Ingrese un numero entero para la mesada: ")

def alianza():
    while True:
        print("Ingrese alianza (1 para Colombia, 2 para Mexico): ")
        opcion = input()
        if opcion == '1' or opcion == '2':
            return int(opcion)
        else:
            print("Alianza no valida, Ingrese 1 para Colombia o 2 para Mexico.")

print("")
print("DATOS ALUMNO 1")
print("")
print("Ingrese nombre del alumno")
nombre1 = input()
print("Ingrese edad del alumno 1:")
edad1 = edad()
print("Ingrese nota del alumno 1:")
nota1 = nota()
print("Ingrese mesada del alumno 1:")
mesada1 = mesada()
print("Ingresa alianza del alumno")
alianza1 = alianza()

print("")
print("DATOS ALUMNO 2")
print("")
print("Ingrese nombre del alumno")
nombre2 = input()
print("Ingrese edad del alumno 2:")
edad2 = edad()
print("Ingrese nota del alumno 2:")
nota2 = nota()
print("Ingrese mesada del alumno 2:")
mesada2 = mesada()
print("Ingresa alianza del alumno")
alianza2 = alianza()

print("")
print("DATOS ALUMNO 3")
print("")
print("Ingrese nombre del alumno")
nombre3 = input()
print("Ingrese edad del alumno 3:")
edad3 = edad()
print("Ingrese nota del alumno 3:")
nota3 = nota()
print("Ingrese mesada del alumno 3:")
mesada3 = mesada()
print("Ingresa alianza del alumno")
alianza3 = alianza()

print("")
print("Respuestas")
print("")

promedio_edad = promedio(edad1, edad2, edad3)
print("El promedio de edad de los alumnos es:", round(promedio_edad))

promedio_notas = promedio(nota1, nota2, nota3)
print("El promedio de las notas de los alumnos es:", round(promedio_notas))

promedio_mesada = promedio(mesada1, mesada2, mesada3)
print("El promedio de las mesadas de los alumnos es:", round(promedio_mesada))
