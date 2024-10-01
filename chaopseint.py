print(" *** Bienvenido a Python *** ")
print("   - Calculadora Insuco -    ")
def suma (a, b):
    return a + b

def resta (a, b):
    return a - b

def multiplicacion (a, b):
    return a * b

def division (a, b):
    return a / b

def promedio (a, b, c):
    return (a + b + c)/3

def mayor (a, b, c):
    if(a>b) and (a>c) : numeromayor=a
    if(b>a) and (b>c) : numeromayor=b
    if(c>a) and (c>b) : numeromayor=c


    
    

# Ingreso de datos:

print("    -*.-|SUMAS|-.*-    ")

# Primera ronda
num1 = float(input("Ingrese el primer número:"))
num2 = float(input("Ingrese el segundo número:"))

print("Suma 1 = ", suma(num1, num2))
print ("")

# Segunda ronda
num3 = float(input("Ingrese un número:"))
num4 = float(input("Ingrese otro número:"))

print("Suma 2 = ", suma(num3, num4))
print ("")

# Tercera ronda
num5 = float(input("Ingrese nuevamente un número:"))
num6 = float(input("Ingrese nuevamente otro número:"))

print("Suma 3 = ", suma(num5, num6))
print ("")

print("    -*.-|RESTAS|-.*-    ")

# Primera ronda
resta1 = float(input("Ingrese el primer número:"))
resta2 = float(input("Ingrese el segundo número:"))

print("Resta 1 = ", resta(resta1, resta2))
print ("")

# Segunda ronda
resta3 = float(input("Ingrese un número:"))
resta4 = float(input("Ingrese otro número:"))

print("Resta 2 = ", resta(resta3, resta4))
print ("")

# Tercera ronda
resta5 = float(input("Ingrese nuevamente un número:"))
resta6 = float(input("Ingrese nuevamente otro número:"))

print("Resta 3 = ", resta(resta5, resta6))
print ("")

print("   -*.-|MULTIPLICACION|-.*-    ")

# Primera ronda
mul1 = float(input("Ingrese el primer número:"))
mul2 = float(input("Ingrese el segundo número:"))

print("Multiplicacion 1 = ", multiplicacion(mul1, mul2))
print ("")

# Segunda ronda
mul3 = float(input("Ingrese un número:"))
mul4 = float(input("Ingrese otro número:"))

print("Multiplicacion 2 = ", multiplicacion(mul3, mul4))
print ("")

# Tercera ronda
mul5 = float(input("Ingrese nuevamente un número:"))
mul6 = float(input("Ingrese nuevamente otro número:"))

print("Multiplicacion 3 = ", multiplicacion(mul5, mul6))
print ("")

print("     -*.-|DIVISION|-.*-    ")

# Primera ronda
div1 = float(input("Ingrese el primer número:"))
div2 = float(input("Ingrese el segundo número:"))

print("Division 1 = ", division(div1, div2))
print ("")

# Segunda ronda
div3 = float(input("Ingrese un número:"))
div4 = float(input("Ingrese otro número:"))

print("Division 2 = ", division(div3, div4))
print ("")

# Tercera ronda
div5 = float(input("Ingrese nuevamente un número:"))
div6 = float(input("Ingrese nuevamente otro número:"))

print("Division 3 = ", division(div5, div6))
print ("")

print("     -*.-|PROMEDIO|-.*-     ")

# Cuarta ronda
prom1 = float(input("Ingrese un número:"))
prom2 = float(input("Ingrese otro número:"))
prom3 = float(input("Ingrese un ultimo número:"))

print("Promedio = ", promedio(prom1 , prom2, prom3))
print("Numero mayor ingresado = ", mayor (prom1, prom2, prom3))

print ("Hasta la proximaaa")
