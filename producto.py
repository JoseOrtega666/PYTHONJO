#nombre cliente
#producto (5 productos a elegir)
#precio producto
#cantidad del producto
#total a pagar del cliente (cuanto vale el producto x su cantidad)

print("")
print("PAMPILLA INSUCO")
print("")

def mostrar_menu():
    print("Menú productos:")
    print("1 - Choripan: 800")
    print("2 - Anticucho: 1000")
    print("3 - Terremoto: 900")
    print("4 - Completo: 1200")
    print("5 - Sandwich de Potito: 2500")

def elegir_producto():
    precios = [800, 1000, 900, 1200, 2500]
    while True:
        producto = int(input("Ingrese el numero del producto (1-Choripan, 2-Anticucho, 3-Terremoto, 4-Completo, 5-Sandwich de Potito): "))
        if producto >= 1 and producto <= 5:
            print("Precio del producto elegido:", precios[producto - 1])
            return precios[producto - 1]
        else:
            print("Producto no valido, ingrese un numero entre 1 y 5.")

def cantidad_productos():
    while True:
        cantidad = int(input("Ingrese la cantidad (1 a 7): "))
        if cantidad >= 1 and cantidad <= 7:
            return cantidad
        else:
            print("Cantidad no valida, ingrese un numero entre 1 y 7.")

def procesar_cliente():
    input("Ingrese el nombre del cliente: ")
    mostrar_menu()
    precio_producto = elegir_producto()
    cantidad_producto = cantidad_productos()

    total_pagar = precio_producto * cantidad_producto

    print("RESULTADOS")
    print("Precio del producto elegido:", precio_producto)
    print("Cantidad:", cantidad_producto)
    print("Total a pagar:", total_pagar)

procesar_cliente()
