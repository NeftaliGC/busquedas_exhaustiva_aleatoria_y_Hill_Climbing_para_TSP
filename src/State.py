import random

class State:
    def __init__(self, initial_state):
        self.n = len(initial_state)
        self.initial_state = initial_state


    def heap(self):
        c = [0] * self.n

        perms = [list(self.initial_state)]
        state = list(self.initial_state)

        i = 1
        while i < self.n:
            if c[i] < i:
                if i % 2 == 0:
                    state[0], state[i] = state[i], state[0]
                else:
                    state[c[i]], state[i] = state[i], state[c[i]]
                
                perms.append(list(state))

                c[i] += 1
                i = 1
            else:
                c[i] = 0
                i += 1 

        return perms

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

