from State import State
from search_algoritms import Search_Algoritms
from Graph import Graph
import random
import time
import json
import os

def solve(nCitys, option, iter=3000, tweak=1):
    initial_state = [i for i in range(1, nCitys + 1)]
    state = State(initial_state)
    algoritms = Search_Algoritms(len(initial_state))

    if option == 1:
        perm = algoritms.hillClimbing(iter, tweak)
    elif option == 2:
        perm = algoritms.randomSearch(iter)
    elif option == 3:
        perm = algoritms.bruteForce(state.heap())
    elif option == 4:
        perm = algoritms.simulatedAnnealing(iter, tweak)

    return perm

if __name__ == "__main__":
    # Obtener la ruta absoluta para 'resultados.json'
    dir_path = os.path.abspath('./src/data')
    file_path = os.path.join(dir_path, 'resultados.json')

    nCitys = int(input("Ingrese el numero de ciudades: "))
    print("\n------Metodos de busqueda------")
    print("1. Hill Climbing")
    print("2. Random Search")
    print("3. Brute Force")
    print("4. Simulated Annealing")
    option = int(input("\nIngrese el algoritmo a utilizar: "))

    metodo = "Hill Climbing" if option == 1 else "Random Search" if option == 2 else "Brute Force"

    iter = 0
    tweak = 0

    if option in [1, 2, 4]:
        iter = int(input("\nIngrese el numero de iteraciones: "))
        if option in [1, 4]:
            print("\n------Metodos de tweak------")
            print("1. Inversion entre dos nodos")
            print("2. Intercambio entre dos nodos")
            print("3. Insercion de un nodo")
            tweak = int(input("Ingrese el metodo de tweak: "))

    n = int(input("\nIngrese el numero de pruebas a realizar: "))

    # Inicializar una lista para almacenar los resultados de cada iteración
    results = {f"{metodo}": []}

    for i in range(n):
        start = time.time()

        solution = solve(nCitys, option, iter, tweak)

        end = time.time()

        print("\nMejor ruta: ", solution[0])
        print("Calidad: ", solution[1])
        print("Distancia total: ", solution[2])
        print("Tiempo de ejecucion: ", end - start)
        if option == 4:
            print("Cambios: ", solution[5])
        print("\n")

        # Guardar los resultados de esta iteración en un diccionario
        iteration_result = {
            "Mejor ruta": solution[0],
            "Calidad": solution[1],
            "Distancia total": solution[2],
            "Tiempo de ejecucion": end - start
        }
        
        # Agregar el resultado de esta iteración a la lista de resultados
        results[metodo].append(iteration_result)

        # Calcular el progreso y mostrar el porcentaje en consola
        progreso = ((i + 1) / n) * 100
        print(f"Progreso de pruebas: {progreso:.2f}% completado")

    finalMap = [solution[3], solution[0]]

    # Guardar todos los resultados en un archivo JSON
    with open(file_path, 'w') as file:
        json.dump(results, file, indent=4)


    graph = Graph(file_path)
    graph.graficar_calidad()
    graph.graficar_distancia_total()
    graph.graficar_tiempo_ejecucion()
    graph.graficar_todas()
    finalMap[0].showPlot(finalMap[1])
    
    

    print("Fin del programa")

