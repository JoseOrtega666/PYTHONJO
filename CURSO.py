# Crear un programa que ingrese 3 notas para cada alumno
# Ingresar la cantidad de alumnos del curso
# Para cada alumno debe ingresar:
# nombre
# genero
# notas (nota1, nota2, nota3)
# Calcular promedio para cada alumno
# Calcular cuantas mujeres hay en el curso
# Calcular el promedio de los hombres

cantidad_mujeres = 0
suma_promedio_hombres = 0
cantidad_hombres = 0

cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))

for i in range(cantidad_alumnos):
    nombre = input("Ingrese el nombre del alumno: ")
    genero = input("Ingrese el genero del alumno (m para hombre, f para mujer): ").lower()
    nota1 = float(input("Ingrese la NOTA 1: "))
    nota2 = float(input("Ingrese la NOTA 2: "))
    nota3 = float(input("Ingrese la NOTA 3: "))

    promedio = (nota1 + nota2 + nota3) / 3
    print("El promedio de", nombre, "es:", round(promedio, 2))

    if genero == "f":
        cantidad_mujeres += 1
    elif genero == "m":
        suma_promedio_hombres += promedio
        cantidad_hombres += 1

print("")
print("Resultados")
print("")
print("Cantidad de mujeres en el curso:", cantidad_mujeres)

if cantidad_hombres > 0:
    promedio_hombres = suma_promedio_hombres / cantidad_hombres
    print("El promedio de los hombres es:", round(promedio_hombres, 2))
else:
    print("No hay hombres en el curso.")
