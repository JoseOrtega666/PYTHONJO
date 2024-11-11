#ordenar un arreglo mediante metodo burbuja

def edad():
    while True:
        try:
            edad = int(input("Ingrese una edad: "))
            if 1 <= edad <= 100:
                return edad
            else:
                print("Edad invalida, ingrese una edad entre 1 y 100:")
        except ValueError:
            print("Entrada invalida, ingrese un numero entero")

def burbuja(edades):
    n = len(edades)
    for i in range(n):
        for j in range(0, n - i - 1):
            if edades[j] > edades[j + 1]:
                edades[j], edades[j + 1] = edades[j + 1], edades[j]

print("Bienvenido al metodo burbuja")
print("")

n = int(input("Ingrese dimension del arreglo: "))
edades = [0] * n

for x in range(n):
    edades[x] = edad()

print("Edades ingresadas:", edades)

burbuja(edades)

print("Edades ingresadas ordenadas:", edades)




