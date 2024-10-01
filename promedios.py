def promedio_curso(notas):
    return sum(notas) / len(notas)

def promedio_notas(n1, n2, n3, p1, p2, p3):
    return (p1 * n1 + p2 * n2 + p3 * n3) / 100

notas = [0,0,0]
alumnos = [0,0,0,0,0]
p = [20,30,50]

p1 = 20
p2 = 30
p3 = 50

print("")
print("WELCOME TO THE INSUCO SCHOOL")
print("")

for i in range(0,5,1):
    
    notas[0] = float(input("Ingrese la nota 1: "))
    notas[1] = float(input("Ingrese la nota 2: "))
    notas[2] = float(input("Ingrese la nota 3: "))

    prom = promedio_notas(notas[0], notas[1], notas[2], p1, p2, p3)
    print(f"El promedio del alumno es: {prom:.2f}")




