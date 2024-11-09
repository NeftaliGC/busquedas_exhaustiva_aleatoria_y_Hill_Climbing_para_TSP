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
