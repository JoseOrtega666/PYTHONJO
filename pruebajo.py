#crear un programa en python que haga lo siguiente:
#ingresar por teclado la cantidad de ventas a realizar
#cada venta deve registrar:
#nombre del vendedor
#apellido del vendedor
#nombre del cliente
#cantidad que va a coprar el cliente
#fruta que va a comprar el usuario
#precio de la fruta (en pesos chilenos por kilo)
#con cuanto pago el cliente
#funcion: calcular total a pagar
#funcion: calcular vuelto
#funcion: calcular nombre completo

print("")
print("VENTA DE FRUTAS Y VERDURAS")
print("")

def calcular_p(fruta, kilos):
    precios = {1: 400, 2: 450, 3: 700, 4: 500, 5: 900}
    precio_unit = precios[fruta]
    precio_t = precio_unit * (2 * kilos + 2)
    return precio_t

def calcular_tp(fruta, kilos):
    return calcular_p(fruta, kilos)

def calcular_v(pago, total):
    return pago - total

def calcular_nc(nombre, apellido):
    return f"{nombre} {apellido}"

def main():
    cantidad_v = int(input("Ingrese la cantidad de ventas a realizar: "))
    print("")

    for i in range(cantidad_v):
        print("")
        nom_vendedor = input("Ingrese el nombre del vendedor: ")
        ape_vendedor = input("Ingrese el apellido del vendedor: ")
        print("")
        
        nom_cliente = input("Ingrese el nombre del cliente: ")
        ape_cliente = input("Ingrese el apellido del cliente: ")

        print("\nMenu de frutas y verduras:")
        print("")
        print("1. Manzana")
        print("2. Naranja")
        print("3. Platano")
        print("4. Tomate")
        print("5. palta")
        print("")
        
        fruta = int(input("Ingrese el numero de la fruta (1, 2, 3, 4, 5): "))
        while fruta not in [1, 2, 3, 4, 5]:
            fruta = int(input("Opcion invalida. Ingrese el numero de la fruta (1, 2, 3, 4, 5): "))

        print("")   
        kilos = int(input("Ingrese la cantidad de kilos (1 a 5): "))
        while kilos < 1 or kilos > 5:
            kilos = int(input("Cantidad de kilos debe ser entre 1 y 5. Ingrese nuevamente: "))

        print("")
        total_p = calcular_tp(fruta, kilos)
        print(f"El total a pagar es: {total_p}")

        print("")
        p_cliente = float(input("Ingrese cuanto pago el cliente: "))
        vuelto = calcular_v(p_cliente, total_p)

        print("")
        if vuelto < 0:
            print(f"Faltan {-vuelto} para completar el pago.")
        else:
            print(f"El vuelto es: {vuelto}")

        nombre_cc = calcular_nc(nom_cliente, ape_cliente)
        nombre_cv = calcular_nc(nom_vendedor, ape_vendedor)
        print(f"Nombre completo del cliente: {nombre_cc}")
        print(f"Nombre completo del vendedor: {nombre_cv}")

if __name__ == "__main__":
    main()


