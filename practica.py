print("Bienvenido al aniversario INSUSCO")
print("")

# Contadores para cada color
cont_rojo = 0
cont_azul = 0
cont_amarillo = 0

# Función para mostrar el menú y validar la selección de color
def elegir_color():
    print("Elija un color:")
    print("1. Rojo")
    print("2. Azul")
    print("3. Amarillo")
    while True:
        try:
            opcion = int(input("Ingrese el número correspondiente al color: "))
            if opcion == 1:
                return "rojo"
            elif opcion == 2:
                return "azul"
            elif opcion == 3:
                return "amarillo"
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

# Registro de 5 usuarios
for i in range(1, 6):
    print(f"\nUsuario {i}:")
    user = input("Ingrese nombre del usuario: ")
    color = elegir_color()
    
    if color == "rojo":
        cont_rojo += 1
    elif color == "azul":
        cont_azul += 1
    elif color == "amarillo":
        cont_amarillo += 1

# Resultados finales
print("\nResultados finales:")
print("La cantidad de usuarios que son rojos es:", cont_rojo)
print("La cantidad de usuarios que son azules es:", cont_azul)
print("La cantidad de usuarios que son amarillos es:", cont_amarillo)





