# Este código ofue generado por ChatGPT-4o (chatgpt.com) utilizando el siguiente
# prompt: "Write a python program that implements the traveling salesman problem 
#          placing the cities to visit on a circle"
#
# Además del código mostrado abajo, la respuesta incluyó la siguiente información:
#
# Explanation: 
#   1. distance_between_points: Calculates the Euclidean distance between two 
#      points on a circle given their angles.
#   2. total_distance: Computes the total distance of a route by summing the 
#      distances between consecutive cities.
#   3. solve_tsp: Generates all permutations of the cities and finds the one  
#      with the minimum total distance.
#   4. plot_route: Plots the best route on a circle using matplotlib.
#
# Usage:
#   * The number of cities is set to 6.
#   * The radius of the circle is set to 10.
#   * Cities are placed evenly around the circle.
#   * The optimal route and its distance are calculated and printed.
#   * The route is visualized using matplotlib.
#
# This program uses brute-force, which is computationally expensive. For larger 
# numbers of cities, more efficient algorithms like dynamic programming or 
# genetic algorithms should be used.

import itertools
import math
import matplotlib.pyplot as plt

def distance_between_points(angle1, angle2, radius):
    # Convert angles to radians
    theta1 = math.radians(angle1)
    theta2 = math.radians(angle2)
    # Calculate Euclidean distance between two points on a circle
    return radius * math.sqrt(2 * (1 - math.cos(theta2 - theta1)))

def total_distance(cities, radius):
    total_dist = 0
    n = len(cities)
    for i in range(n):
        total_dist += distance_between_points(cities[i], cities[(i + 1) % n], radius)
    return total_dist

def solve_tsp(cities, radius):
    # Generate all permutations of cities
    permutations = itertools.permutations(cities)
    min_distance = float('inf')
    best_route = None
    
    for perm in permutations:
        current_distance = total_distance(perm, radius)
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = perm
    
    return best_route, min_distance

def plot_route(cities, route, radius):
    # Convert angles to radians for plotting
    route_radians = [math.radians(angle) for angle in route]
    
    x = [radius * math.cos(angle) for angle in route_radians]
    y = [radius * math.sin(angle) for angle in route_radians]
    
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

# Example usage
num_cities = 3
radius = 1
cities = [i * (360 / num_cities) for i in range(num_cities)]

best_route, min_distance = solve_tsp(cities, radius)
print("Best route:", best_route)
print("Minimum distance:", min_distance)

plot_route(cities, best_route, radius)
