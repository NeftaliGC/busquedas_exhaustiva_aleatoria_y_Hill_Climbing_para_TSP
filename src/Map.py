import random
import math
import matplotlib.pyplot as plt

class Map:
    ubications = []
    matx_dist = []
    def __init__(self, n, r = 1):
        self.n = n
        self.cities = list(range(n))
        self.generate_angles()
        self.r = r
        self.generate_matrix()

    def generate_angles(self, method=1):
        if method == 1:
            # Genera n ángulos aleatorios en el rango [0, 360)
            self.ubications = random.sample(range(360), self.n)
        elif method == 2:
            # Genera n ángulos equidistantes en el rango [0, 360)
            step = 360 / self.n
            self.ubications = [i * step for i in range(self.n)]
            # Baraja las ubicaciones para asignar aleatoriamente a las ciudades
            random.shuffle(self.ubications)


    def distance_between_points(self, angle1, angle2):
        # Convert angles to radians
        theta1 = math.radians(angle1)
        theta2 = math.radians(angle2)
        # Calculate Euclidean distance between two points on a circle
        return self.r * math.sqrt(2 * (1 - math.cos(theta2 - theta1)))

    def generate_matrix(self):
        matx = []
        for i in range(self.n):
            row = []
            for j in range(self.n):
                row.append(self.distance_between_points(self.ubications[i], self.ubications[j]))
            matx.append(row)
        self.matx_dist = matx.copy()

    def showPlot(self, route):
        # Convert angles to radians for plotting
        route_radians = []
        for city in route:
            route_radians.append(math.radians(self.ubications[city - 1]))
        
        x = [self.r * math.cos(angle) for angle in route_radians]
        y = [self.r * math.sin(angle) for angle in route_radians]
        
        # Close the loop
        x.append(x[0])
        y.append(y[0])
        
        plt.figure(figsize=(8, 8))
        plt.plot(x, y, 'o-', markersize=10)
        plt.title('Optimal TSP Route on a Circle')
        plt.xlabel('X')
        plt.ylabel('Y')
        
        for i, txt in enumerate(route):
            plt.annotate(txt, (x[i], y[i]), textcoords="offset points", xytext=(0,10), ha='center')
        
        plt.grid(True)
        plt.axis('equal')
        plt.show()

    def getUbications(self):
        return self.ubications

    def getDistance(self, city1, city2):
        return self.matx_dist[city1][city2]

    def getTotalDistance(self, route):
        distance = 0
        for i in range(len(route)):
            city1 = route[i] - 1  # Ajustamos para índice base 0
            city2 = route[(i + 1) % len(route)] - 1  # Conectar al primer ciudad al final
            distance += self.getDistance(city1, city2)

        return distance

    def getQuality(self, route):
        total_distance = self.getTotalDistance(route)
        # Calcula el perímetro del círculo
        perimeter = 2 * math.pi * self.r
        
        # Calcula la calidad como la razón entre el perímetro y la distancia total
        quality = perimeter / total_distance if total_distance != 0 else 0

        return quality