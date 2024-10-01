#ingresar datos de tres alumnos:
#nombre
#edad
#nota
#mesada
#promediar edad, nota y mesada


print("Bienvenido a septiembre")
print("")

def promedio(a, b, c):
    return (a + b + c) / 3

def edad():
    while True:
        edad = int(input("Ingrese edad del alumno (10 a 20): "))
        if 10 <= edad <= 20:
            return edad
        else:
            print("Edad no valida, ingrese una edad entre 10 y 20.")

def nota():
    while True:
        nota = float(input("Ingrese nota del alumno (1 a 7): "))
        if 1 <= nota <= 7:
            return nota
        else:
            print("Nota no valida, ingrese una nota entre 1 y 7.")

def mesada():
    while True:
        mesada = int(input("Ingrese mesada del alumno (100 a 50000): "))
        if 100 <= mesada <= 50000:
            return mesada
        else:
            print("Mesada no valida, ingrese un valor entre 100 y 50000.")

def especialidad():
    while True:
        especialidad = int(input("Ingrese especialidad (1 para programacion, 2 para administracion, 3 para contabilidad): "))
        if especialidad in [1, 2, 3]:
            return especialidad
        else:
            print("Especialidad no valida, ingrese 1 para programacion, 2 para administracion, 3 para contabilidad")

nombres = [0, 0, 0]
edades = [0, 0, 0]
notas = [0, 0, 0]
mesadas = [0, 0, 0]
especialidades = [0, 0, 0]

for i in range(3): 
    print("")
    print("DATOS ALUMNO", i + 1)
    print("")
    nombres[i] = input("Ingrese nombre del alumno: ")
    edades[i] = edad()
    notas[i] = nota()
    mesadas[i] = mesada()
    especialidades[i] = especialidad()

promedio_edad = promedio(edades[0], edades[1], edades[2])
promedio_notas = promedio(notas[0], notas[1], notas[2])
promedio_mesada = promedio(mesadas[0], mesadas[1], mesadas[2])

mejor_nota = notas.index(max(notas))
especialidades_str = {1: "Programacion", 2: "Administracion", 3: "Contabilidad"}

print("")
print("Respuestas")
print("")
print("El promedio de edad de los alumnos es:", round(promedio_edad))
print("El promedio de las notas de los alumnos es:", round(promedio_notas, 2))
print("El promedio de las mesadas de los alumnos es:", round(promedio_mesada))
print("El alumno con la mejor nota es:", nombres[mejor_nota])
print("Especialidad del alumno con la mejor nota es:", especialidades_str[especialidades[mejor_nota]])
