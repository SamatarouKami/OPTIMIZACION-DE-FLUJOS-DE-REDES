from Grafo import Grafo
from time import time



umbral = 1
prob = 0.001

with open("Tarea5.dat","w") as archivo:
    for nodos in range (5,21,1):
        iTiempo = time()
        G = Grafo(nodos,prob)
        G.agrega(nodos)
        G.conexiones(umbral)
        G.conexionesAleatorias(prob)
        G.ford_fulk()
        G.graficar()
        G.percNod()
        G.graficarP()
        fTiempo = time() - iTiempo
        print(nodos, fTiempo, file=archivo)
    

