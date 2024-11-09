from Map import Map
import random

class Search_Algoritms:
    def __init__(self, n):
        self.n = n
        self.mapa = Map(self.n)

    def bruteForce(self, solutions):
        s = solutions[0]

        i = 1
        while i < len(solutions):
            r = solutions[i]
            if self.mapa.getQuality(r) > self.mapa.getQuality(s):
                s = r

            i += 1
        
        return s, self.mapa.getQuality(s), self.mapa.getTotalDistance(s)

    def randomSearch(self, n):
        s = self.generate_random_route(self.n)

        i = 1
        while i < n:
            r = self.generate_random_route(self.n)
            if self.mapa.getQuality(r) > self.mapa.getQuality(s):
                s = r

            i += 1

        return s, self.mapa.getQuality(s), self.mapa.getTotalDistance(s)

    def hillClimbing(self, n, method=1):
        s = self.generate_random_route(self.n)

        i = 1
        while i < n:
            r = self.tweak(s.copy(), method)
            if self.mapa.getQuality(r) > self.mapa.getQuality(s):
                s = r

            i += 1

        return s, self.mapa.getQuality(s), self.mapa.getTotalDistance(s)


    def mapRute(self, route):
        self.mapa.showPlot(route)

    def generate_random_route(self, n):
        lista = list(range(1, n + 1))
        random.shuffle(lista)
        return lista
    
    def tweak(self, route, method=1):
        if method == 1: # inversion entre dos nodos
            i = random.randint(0, len(route) - 1)
            j = random.randint(0, len(route) - 1)
            if i > j:
                i, j = j, i  # Asegurarse de que i <= j
            if i == j:
                i = 0
                j = len(route) - 1
            route[i:j + 1] = route[i:j + 1][::-1]
            return route

        elif method == 2: # intercambio entre dos nodos
            i = random.randint(0, self.n - 1)
            j = random.randint(0, self.n - 1)
            if i == j: # Asegurarse de que i != j
                i = 0
                j = len(route) - 1 # intercambia el primer y último nodo
            route[i], route[j] = route[j], route[i]
            return route

        elif method == 3: # insercion de un nodo
            i = random.randint(0, self.n - 1)
            j = random.randint(0, self.n - 1)
            if i == j:
                i = 0
                j = len(route) - 1 # inserta el nodo en la primera posición
            # inserta el nodo j en la posición i
            route.insert(i, route.pop(j))
            return route
