print("Bienvenido a python")
print("Calculadora insuco")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida"

# Menú de selección
print("\nSeleccione la operación que desea realizar:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = int(input("Ingrese el número de la operación: "))

if opcion == 1:
    # Suma
    print("\nOperación: Suma")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print("Resultado de la suma:", suma(num1, num2))

elif opcion == 2:
    # Resta
    print("\nOperación: Resta")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print("Resultado de la resta:", resta(num1, num2))

elif opcion == 3:
    # Multiplicación
    print("\nOperación: Multiplicación")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print("Resultado de la multiplicación:", multiplicacion(num1, num2))

elif opcion == 4:
    # División
    print("\nOperación: División")
    num1 = float(input("Ingrese el primer número: ")) 
    num2 = float(input("Ingrese el segundo número: "))
    print("Resultado de la división:", division(num1, num2))

else:
    print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
