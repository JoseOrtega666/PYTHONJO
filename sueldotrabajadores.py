#crear un programa en python que:
#ingresar sueldo de los trabajadores mientras el sueldo sea distinto de cero
#ingresar nombre, y sueldo
#ordenar del mayor sueldo hasta el menor sueldo

def burbuja(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-1-i):
            if lista[j][1] < lista[j+1][1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

trabajadores = []

while True:
    nombre = input("Ingresa el nombre del trabajador: ")
    
    while True:
        sueldo = input(f"Ingresa el sueldo de {nombre} (entre 500.000 y 5.000.000): ")
        if sueldo.isdigit():
            sueldo = int(sueldo)
            if sueldo == 0:
                break
            elif sueldo >= 500000 and sueldo <= 5000000:
                trabajadores.append((nombre, sueldo))
                break
            else:
                print("El sueldo debe estar entre 400.000 y 50.000.000")
        else:
            print("Ingresa un numero entero")
    
    if sueldo == 0:
        break

trabajadores_ordenados = burbuja(trabajadores)

if trabajadores_ordenados:
    print("\nTrabajadores ordenados:")
    for nombre, sueldo in trabajadores_ordenados:
        print(f"Nombre: {nombre}, Sueldo: {sueldo}")


