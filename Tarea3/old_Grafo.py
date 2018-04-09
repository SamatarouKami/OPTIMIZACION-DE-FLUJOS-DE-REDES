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
        self.n = None
        self.x = dict()
        self.y = dict()
        self.peso = dict()
        self.E = []
        self.nodos = []
        self.destino = None       
	

    
    def generar(self, orden):
        self.n = orden 
        for nodo in range(self.n):
            self.x[nodo] = random() 
            self.y[nodo] = random()
            self.nodos.append((self.x[nodo],self.y[nodo]))

 
    def imprimir(self, direccion):
        self.destino = direccion
        with open(self.destino, "w") as archivo:
            for nodo in range(self.n):
                print(self.x[nodo], self.y[nodo], file=archivo)
        
    def conectar(self, dist): 
        for nodo in range(self.n - 1):
            for nodo2 in range(nodo + 1, self.n):
                distancia = math.sqrt(pow(self.x[nodo2]-self.x[nodo],2)+pow(self.y[nodo2]-self.y[nodo],2))
                if distancia < dist:
                    self.E.append( ( (nodo,nodo2) , int(random()*5 + 1) ) )
                if distancia > (1-(dist/10)):
                    self.E.append( ( (nodo2,nodo) , int(random()*5 + 1) ) )
    

    def camino(self, s, t, f): # construcción de un camino aumentante
        cola = [s]
        usados = set()
        camino = dict()
        while len(cola) > 0:
            u = cola.pop(0)
            usados.add(u)
            for (w, v) in self.E:
                if w == u and v not in cola and v not in usados:
                    actual = f.get((u, v), 0)
                    dif = self.E[(u, v)] - actual
                    if dif > 0:
                        cola.append(v)
                        camino[v] = (u, dif)
        if t in usados:
            return camino
        else: # no se alcanzó
            return None
 
    def ford_fulkerson(self, s, t): # algoritmo de Ford y Fulkerson
        if self.nodos[s] == self.nodos[t]:
            return 0
        maximo = 0
        f = dict()
        while True:
            aum = self.camino(s, t, f)
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

        
    def graficar (self, tipo,nombreArchivo): 
        cabecera()
        print("set output '"+nombreArchivo+"'")
        numArrow = 1
        nodoidx = 0
        for(v, w) in self.E:
            x1 = self.x[v[0]]
            x2 = self.x[v[1]]
            y1 = self.y[v[0]]
            y2 = self.y[v[1]]
            pesoArrow = w
            if tipo == 0:
                print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} nohead lw 1 lc rgb 'black'".format(numArrow,x1,y1,x2,y2))
            if tipo == 1:
                print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} head filled lw 1 lc rgb 'black'".format(numArrow,x1,y1,x2,y2))
            if tipo == 2:
                print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} head filled lw {:d} lc rgb 'black'".format(numArrow,x1,y1,x2,y2,pesoArrow))
            numArrow+=1
            nodoidx+=1
        inf(self.destino,tipo)




                
