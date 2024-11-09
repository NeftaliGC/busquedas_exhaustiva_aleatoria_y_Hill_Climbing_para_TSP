import json
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = self._cargar_datos()
    
    def _cargar_datos(self):
        # Cargar datos del archivo JSON
        with open(self.filepath, 'r') as file:
            contenido = json.load(file)
        
        # Extraer los resultados (primera clave del JSON)
        metodo = list(contenido.keys())[0]
        return contenido[metodo]

    def graficar_calidad(self):
        # Extraer las calidades de cada iteración
        calidades = [result["Calidad"] for result in self.data]
        plt.plot(calidades, marker='o')
        plt.title("Calidad por iteración")
        plt.xlabel("Iteración")
        plt.ylabel("Calidad")
        plt.show()

    def graficar_distancia_total(self):
        # Extraer las distancias totales de cada iteración
        distancias = [result["Distancia total"] for result in self.data]
        plt.plot(distancias, marker='o', color='orange')
        plt.title("Distancia Total por iteración")
        plt.xlabel("Iteración")
        plt.ylabel("Distancia Total")
        plt.show()

    def graficar_tiempo_ejecucion(self):
        # Extraer el tiempo de ejecución de cada iteración
        tiempos = [result["Tiempo de ejecucion"] for result in self.data]
        plt.plot(tiempos, marker='o', color='green')
        plt.title("Tiempo de Ejecución por iteración")
        plt.xlabel("Iteración")
        plt.ylabel("Tiempo de Ejecución (s)")
        plt.show()

    def graficar_todas(self):
        # Subgráficos para mostrar todas las métricas juntas
        fig, axs = plt.subplots(3, 1, figsize=(8, 12))

        # Graficar calidad
        calidades = [result["Calidad"] for result in self.data]
        axs[0].plot(calidades, marker='o')
        axs[0].set_title("Calidad por iteración")
        axs[0].set_xlabel("Iteración")
        axs[0].set_ylabel("Calidad")

        # Graficar distancia total
        distancias = [result["Distancia total"] for result in self.data]
        axs[1].plot(distancias, marker='o', color='orange')
        axs[1].set_title("Distancia Total por iteración")
        axs[1].set_xlabel("Iteración")
        axs[1].set_ylabel("Distancia Total")

        # Graficar tiempo de ejecución
        tiempos = [result["Tiempo de ejecucion"] for result in self.data]
        axs[2].plot(tiempos, marker='o', color='green')
        axs[2].set_title("Tiempo de Ejecución por iteración")
        axs[2].set_xlabel("Iteración")
        axs[2].set_ylabel("Tiempo de Ejecución (s)")

        plt.tight_layout()
        plt.show()

    def numero_de_resultados(self):
        # Devolver el número de resultados en el JSON
        return len(self.data)
