from State import State
from Map import Map
from search_algoritms import Search_Algoritms
import random

if __name__ == "__main__":
    nCitys = int(input("Ingrese el numero de ciudades: "))

    initial_state = [i for i in range(1, nCitys + 1)]

    stados = State(initial_state)
    Search_Algoritms(nCitys)


