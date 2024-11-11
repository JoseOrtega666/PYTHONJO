#hacer un algoritmo en python para insuco streaming:
#ingresar n peliculas
#cada pelicula tiene: nombre de la pelicula, protagonista, antagonista, director, genero, año de estreno, cantidad de visualizaciones
#crear una funcion para validar genero de la pelicula
#crear otra funcion para validar año de estreno (2000-2024)
#mostrar pelicula mas vista
#mostrar pelicula menos vista
#calcular promedio de visualizaciones o visitas
#se deve implementar array o arreglo
#sumar cantidad de peliculas de accion y almacenarlas en un nuevo arreglo

def validar_gen(genero):
    return genero in [1, 2, 3, 4, 5]

def validar_año(año):
    return 2000 <= año <= 2024

def ingresar_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if (minimo is not None and valor < minimo) or (maximo is not None and valor > maximo):
                print(f"Ingrese un numero entre {minimo} y {maximo}")
            else:
                return valor
        except ValueError:
            print("Ingrese un numero entero")

def main():
    print("")
    n = ingresar_entero("Ingrese la cantidad de peliculas: ", minimo=1, maximo=30)
    
    nombres = [""] * n
    protagonistas = [""] * n
    antagonistas = [""] * n
    directores = [""] * n
    generos = [0] * n
    años = [0] * n
    visualizaciones = [0] * n
    peliculas_accion = [0] * n
    contador_accion = 0

    for i in range(n):
        print("")
        nombres[i] = input("Ingrese el nombre de la pelicula: ")
        print("")
        protagonistas[i] = input("Ingrese el protagonista: ")
        print("")
        antagonistas[i] = input("Ingrese el antagonista: ")
        print("")
        directores[i] = input("Ingrese el director: ")
        print("")
        
        while True:
            genero = ingresar_entero("Ingrese el genero (1: Accion, 2: Terror, 3: Comedia, 4: Romance, 5: Infantil): ")
            if validar_gen(genero):
                generos[i] = genero
                break
            else:
                print("Genero invalido ingreselo denuevo")
        
        while True:
            print("")
            año = ingresar_entero("Ingrese el año de estreno (2000-2024): ")
            if validar_año(año):
                años[i] = año
                break
            else:
                print("Año invalido ingreselo denuevo")
        
        print("")
        visualizaciones[i] = ingresar_entero("Ingrese la cantidad de visualizaciones: ", minimo=1, maximo=1000000)
        print("")
        
        if generos[i] == 1:
            peliculas_accion[contador_accion] = nombres[i]
            contador_accion += 1

    peliculas_accion = peliculas_accion[:contador_accion]

    max_visualizaciones = max(visualizaciones)
    min_visualizaciones = min(visualizaciones)
    
    pelicula_mas_vista = nombres[visualizaciones.index(max_visualizaciones)]
    pelicula_menos_vista = nombres[visualizaciones.index(min_visualizaciones)]

    print(f"La pelicula mas vista es: {pelicula_mas_vista}")
    print(f"La pelicula menos vista es: {pelicula_menos_vista}")

    promedio_visualizaciones = sum(visualizaciones) / n
    print(f"El promedio de visualizaciones es: {promedio_visualizaciones:.2f}")

    cantidad_accion = len(peliculas_accion)
    
    print(f"Cantidad de peliculas de accion: {cantidad_accion}")
    print("Peliculas de accion:", peliculas_accion)

if __name__ == "__main__":
    main()


