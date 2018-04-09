from random import random
import math

def cabecera():
    print("set terminal epslatex size 3.5,2.62 color colortext")
    print('set xrange [-0.1:1.1]')
    print('set yrange [-0.1:1.1]')
    print('set size square')
    print('set key off')
    print('unset colorbox')
    
def inf(destino, tipo):
    if tipo == 0:
        print("plot '{:s}' using 1:2:0 with points pt 7 lc 'black'".format(destino))
    else:
        print("plot '{:s}' using 1:2:(rand(0)) with points pt 7 lc palette".format(destino))

class Grafo:
 
    def __init__(self):
        self.N = 0;
        self.coord = dict()
        self.V = set() # un conjunto
        self.E = dict() # un mapeo de pesos de aristas
        self.vecinos = dict() # un mapeo
        self.c = dict()
 
    def agrega(self, v):
        self.V.add(v)
        if not v in self.vecinos: # vecindad de v
            self.vecinos[v] = set() # inicialmente no tiene nada
 
    def conecta(self, v, u, peso=1):
        self.agrega(v)
        self.agrega(u)
        self.E[(v, u)] = self.E[(u, v)] = peso # en ambos sentidos
        self.vecinos[v].add(u)
        self.vecinos[u].add(v)
 
    def complemento(self):
        comp= Grafo()
        for v in self.V:
            for w in self.V:
                if v != w and (v, w) not in self.E:
                    comp.conecta(v, w, 1)
        return comp

    def camino(s, t, c, f): # construcción de un camino aumentante
        cola = [s]
        usados = set()
        camino = dict()
        while len(cola) > 0:
            u = cola.pop(0)
            usados.add(u)
            for (w, v) in c:
                if w == u and v not in cola and v not in usados:
                    actual = f.get((u, v), 0)
                    dif = c[(u, v)] - actual
                    if dif > 0:
                        cola.append(v)
                        camino[v] = (u, dif)
        if t in usados:
            return camino
        else: # no se alcanzó
            return None
 
 
 
    def ford_fulkerson(self, s, t): # algoritmo de Ford y Fulkerson
        if s == t:
            return 0
        maximo = 0
        f = dict()
        while True:
            aum = Grafo.camino(s, t, c, f)
            if aum is None:
                break # ya no hay
            incr = min(aum.values(), key = (lambda k: k[1]))[1]
            u = t
            while u in aum:
                v = aum[u][0]
                actual = f.get((v, u), 0) # cero si no hay
                inverso = f.get((u, v), 0)
                f[(v, u)] = actual + incr
                f[(u, v)] = inverso - incr
                u = v
            maximo += incr
        return maximo

    def floyd_warshall(G): 
        d = {}
        for v in G.V:
            d[(v, v)] = 0 # distancia reflexiva es cero
            for u in G.vecinos[v]: # para vecinos, la distancia es el peso
               d[(v, u)] = G.E[(v, u)]
        for intermedio in G.V:
            for desde in G.V:
                for hasta in G.V:
                    di = None
                    if (desde, intermedio) in d:
                        di = d[(desde, intermedio)]
                    ih = None
                    if (intermedio, hasta) in d:
                        ih = d[(intermedio, hasta)]
                    if di is not None and ih is not None:
                        c = di + ih # largo del camino via "i"
                        if (desde, hasta) not in d or c < d[(desde, hasta)]:
                            d[(desde, hasta)] = c # mejora al camino actual
        return d

c = dict();
c = {(0, 1): 16, (0, 2): 13, (1, 2): 10, (2, 1): 4, (3, 2): 9, \
(1, 3): 12, (2, 4): 14, (4, 3): 7, (3, 5): 20, (4, 5): 4}



print(Grafo.ford_fulkerson(c, 0, 5))

