#crear un algoritmo que resuelva lo siguiente:
#estacionamiento
#ingresar clientes hasta que el estacionamiento este completo
#ingresar cantidad total de estacionamientos
#ingresar el nombre del cliente
#ingresar patente del auto
#ingresar hora de ingreso al estacionamiento
#ingresar hora de salida
#ingresr valor por hora
#calcular total a pagar

def calcular_total(hora_ingreso, hora_salida, valor_por_hora):
    horas_estacionado = hora_salida - hora_ingreso
    if horas_estacionado < 0:
        horas_estacionado = 0 
    return horas_estacionado * valor_por_hora

def obtener_hora(mensaje):
    while True:
        try:
            hora = int(input(mensaje))
            if 7 <= hora <= 12:
                return hora
            else:
                print("La hora debe estar entre 7 y 12. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")

def estacionamiento():
    print("")
    total_estacionamientos = int(input("Ingrese la cantidad total de estacionamientos: "))
    espacios_disponibles = total_estacionamientos
    print("")

    for i in range(total_estacionamientos):

        if espacios_disponibles > 0:
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            print("")
            patente = input("Ingrese la patente del auto: ")
            print("")

            hora_ingreso = obtener_hora("Ingrese la hora de ingreso al estacionamiento (entre 7 y 12): ")
            print("")
            hora_salida = obtener_hora("Ingrese la hora de salida (entre 7 y 12): ")
            print("")

            valor_por_hora = 1000

            total_a_pagar = calcular_total(hora_ingreso, hora_salida, valor_por_hora)
            print("")
            print(f"Total a pagar por {nombre_cliente} es: ${total_a_pagar}")
            print("")

            espacios_disponibles -= 1
        else:
            print("")
            print("El estacionamiento está completo.")
            break

estacionamiento()
