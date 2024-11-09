from Map import Map
from State import State
import random

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
        
        return s, self.mapa.getQuality(s), self.mapa.getTotalDistance(s)

    def randomSearch(self, n):
        s = self.estado.generate_random_route(self.n)

        i = 1
        while i < n:
            r = self.estado.generate_random_route(self.n)
            if self.mapa.getQuality(r) > self.mapa.getQuality(s):
                s = r

            i += 1

        return s, self.mapa.getQuality(s), self.mapa.getTotalDistance(s)

    def hillClimbing(self, n, method=1):
        s = self.estado.generate_random_route(self.n)

        i = 1
        while i < n:
            r = self.estado.tweak(s.copy(), method)
            if self.mapa.getQuality(r) > self.mapa.getQuality(s):
                s = r

            i += 1

        return s, self.mapa.getQuality(s), self.mapa.getTotalDistance(s)


    def mapRute(self, route):
        self.mapa.showPlot(route)

    