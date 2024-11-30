from Map import Map
from State import State
import random
import math

class Search_Algoritms:
    def __init__(self, n):
        self.n = n
        self.mapa = Map(self.n)
        self.estado = State(list(range(1, self.n + 1)))

    def bruteForce(self, solutions):
        s = solutions[0]

        i = 1
        while i < len(solutions):
            r = solutions[i]
            if self.mapa.getQuality(r) > self.mapa.getQuality(s):
                s = r

            i += 1
        
        return s, self.mapa.getQuality(s), self.mapa.getTotalDistance(s), self.mapa

    def randomSearch(self, n):
        s = self.estado.generate_random_route(self.n)

        i = 1
        while i < n:
            r = self.estado.generate_random_route(self.n)
            if self.mapa.getQuality(r) > self.mapa.getQuality(s):
                s = r

            i += 1

        return s, self.mapa.getQuality(s), self.mapa.getTotalDistance(s), self.mapa

    def hillClimbing(self, n, method=1):
        s = self.estado.generate_random_route(self.n)

        i = 1
        while i < n:
            r = self.estado.tweak(s.copy(), method)
            if self.mapa.getQuality(r) > self.mapa.getQuality(s):
                s = r

            i += 1

            print(self.mapa.getQuality(s))

        return s, self.mapa.getQuality(s), self.mapa.getTotalDistance(s), self.mapa

    def simulatedAnnealing(self, n, method=1, alpha=0.95, e=0.000000000001, temp=1000):
        t = 1
        i = 0
        change = 0
        temperature = temp
        xtreme_stop_condition = 10000
        s = self.estado.generate_random_route(self.n)

        solutions = []
        changes = {}

        while (temperature > e):
            if t == xtreme_stop_condition:
                break

            change = 0
            while i < n:
                r = self.estado.tweak(s.copy(), method)
                r_quality = self.mapa.getQuality(r, normalize=True)
                s_quality = self.mapa.getQuality(s, normalize=True)
                rand = random.random()
                dif = r_quality - s_quality
                cost = - dif / temperature
                criterio = math.exp(cost)
                if dif < 0:
                    s = r
                elif rand < criterio:
                    change += 1
                    s = r
                
                i += 1

            changes[f"iteracion_{t}"] = change
            solutions.append(self.mapa.getQuality(s))
            i = 0
            temperature = self.G(temperature, t)
            t += 1

        return s, self.mapa.getQuality(s), self.mapa.getTotalDistance(s), self.mapa, solutions, changes

    def mapRute(self, route):
        self.mapa.showPlot(route)

    def G(self, T0, t, alpha=0.01):
        return T0 * (1 / math.log(1 + t))
        #return T0 / (1 + alpha * t)
        
    def calculate_initial_temperature(self, Paccept = 0.8):
        rango = (2 * math.pi * self.mapa.r)
        n = self.n
        if self.n > 150:
            n = 150

        deltaQ = math.factorial(n) / rango 
        log = math.log(Paccept, math.e)
        t0 = - deltaQ / log

        return t0