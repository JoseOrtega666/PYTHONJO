#ingresar n personajes para un show en la pampilla (N ingresado por teclado)
#ingresar por personaje lo siguiente:
#nombre
#apellido
#sueldo (rango de 1.000.000 y 17.000.000 (validar))
#fecha de su especaculo (las opciones son: 17 septiembre, 18septiembre, 19septiembre, 20septiembre(validar las opciones))
#calcular promedio y nombre completo (funciones) 
#cacular mostrar el artista que mas se le pago

def validar_sueldo():
    while True:
        sueldo = float(input("Ingrese el sueldo del artista: "))
        if 1000000 <= sueldo <= 17000000:
            return sueldo
        else:
            print("Sueldo fuera de rango, ingrselo de nuevo.")

def validar_fecha():
    while True:
        print("Ingrese la fecha del espectaculo:")
        print("1: 17 septiembre")
        print("2: 18 septiembre")
        print("3: 19 septiembre")
        print("4: 20 septiembre")
        fecha_opcion = input("Seleccione una opcion de 1 a 4: ")
        
        if fecha_opcion == "1":
            return "17 septiembre"
        elif fecha_opcion == "2":
            return "18 septiembre"
        elif fecha_opcion == "3":
            return "19 septiembre"
        elif fecha_opcion == "4":
            return "20 septiembre"
        else:
            print("Opcion invalida, ingresela de nuevo")

def calcular_promedio_sueldos(sueldos):
    return sum(sueldos) / len(sueldos)

def nombre_completo(nombre, apellido):
    return f"{nombre} {apellido}"

def artista_mas_pagado(nombres_completos, sueldos):
    max_sueldo = max(sueldos)
    indice = sueldos.index(max_sueldo)
    return nombres_completos[indice], max_sueldo

PRESUPUESTO = 17000000

while True:
    n = int(input("Ingrese el numero de artistas: "))
    if n > 0:
        break
    else:
        print("La cantidad de artistas ingresados debe ser positiva")

artistas = []
sueldos = []
total_sueldos = 0

for i in range(n):
    nombre = input("Ingrese el nombre del artista: ")
    apellido = input("Ingrese el apellido del artista: ")

    while True:
        sueldo = validar_sueldo()
        if total_sueldos + sueldo <= PRESUPUESTO:
            total_sueldos += sueldo
            break
        else:
            print("El sueldo supera el presupuesto, ingrese un sueldo mas chico")

    fecha = validar_fecha()
    nombre_completo_artista = nombre_completo(nombre, apellido)
    artistas.append(nombre_completo_artista)
    sueldos.append(sueldo)

if total_sueldos <= PRESUPUESTO:
    promedio_sueldo = calcular_promedio_sueldos(sueldos)
    artista_max_pagado, max_sueldo = artista_mas_pagado(artistas, sueldos)

    print("\nResultados:")
    print(f"Promedio de sueldos: {promedio_sueldo:.2f}")
    print(f"Artista al que mas se le pago: {artista_max_pagado} con sueldo de {max_sueldo:.2f}")
