from random import random
from math import sqrt, ceil, sin, cos, pi, floor
from random import randint, uniform, normalvariate, expovariate, random
import time


def dist(s, t):
     return (abs(t[0]-s[0])+ abs(t[1]-s[1]))
    

class Grafo:

    def __init__(self,k,prob):
        self.dis = dict()
        self.vecinos = dict()
        self.aristas = dict()
        self.nodos = []
        self.k = 0;

        
    def agrega(self, i):
        self.k = i
        with open("Fulk.dat", "w") as archivo:
            for m in range (1,i+1):
                for n in range(1, i+1):
                    x = m
                    y = n
                    self.nodos.append((x,y))
                    print(x, y, 0, file = archivo)
                    if not (x, y) in self.vecinos:
                        self.vecinos[(x,y)] = []
            print(self.nodos[0][0],self.nodos[0][1],4, file=archivo)
            print(self.nodos[len(self.nodos)-1][0],self.nodos[len(self.nodos)-1][1],7, file=archivo)
            
                        

    def nuevosNodos(self):
        with open ("NodFulk.dat", "w") as archivo:
            print(self.nodos[0][0],self.nodos[0][1],4, file=archivo)
            print(self.nodos[len(self.nodos)-1][0],self.nodos[len(self.nodos)-1][1],7, file=archivo)
            t = randint(1,len(self.nodos)-2)
            if t not in self.auxNodo:
                self.auxIndice.append(t)
                self.auxNodo.append(self.nodos[t])
                del self.nodos[t]
     
            else:
               t = randint(1,len(self.nodos)-2)
               if t not in self.auxIndice:
                    self.auxNodo.append(t)
                    self.auxNodo.append(self.nodos[t])
                    del self.nodos[t]
                    
            for n in self.auxNodo:
                 for m in self.nodos:
                     if (n,m) in self.aristas:
                         del self.aristas[(n,m)]
                     if (m,n) in self.aristas:
                          del self.aristas[(m,n)]
            
            for w in self.nodos:
                if w is not self.nodos[0] and w is not self.nodos[len(self.nodos)-1]:
                    print(w[0],w[1],0, file=archivo)

                        

    def conexiones(self, umbral):
        for n in self.nodos:
            for m in self.nodos: 
                if n is not m:
                    if dist (n,m) < umbral+1:
                        self.aristas[n,m] = self.aristas[m,n] = floor(normalvariate(4,0.5))+1


    def conexionesAleatorias(self,prob):
        self.cuentaAristas = 0
        for n in self.nodos:
            if n is not self.nodos[self.k**2 - 1]:
                for m in self.nodos:
                    if m is not self.nodos[0]:
                        if n is not m:
                            aleatorio = random()
                            if aleatorio < prob and (n,m) not in self.aristas:
                                self.aristas[n,m] = ceil(expovariate(1/10))
                                self.cuentaAristas += 1


    def NuevasAristas(self):
        for qa in range(0,20):
            s = randint(0,k**2-1)
            t = randint(0,k**2-1)
            arista = (self.nodos[s],self.nodos[t])
            while arista not in self.aristas:
                s = randint(0,k**2-1)
                t = randint(0,k**2-1)
                arista = (self.nodos[s],self.nodos[t])
            if arista not in self.lqq:
                self.lqq.append(arista)
                del self.aristas[arista]
                
                   
    def camino(self):
        cola = [self.s]
        usados = set()
        camino = dict()
        while len(cola) > 0:
            u = cola.pop(0)
            usados.add(u)
            for (w, v) in self.aristas:
                if w == u and v not in cola and v not in usados:
                    actual = self.f.get((u, v), 0)
                    dif = self.aristas[(u, v)] - actual
                    if dif > 0:
                        cola.append(v)
                        camino[v] = (u, dif)
        if self.t in usados:
           return camino
        else:
            return None
        

    def ford_fulk(self): 
        self.s = self.nodos[0]
        self.t = self.nodos[len(self.nodos) - 1]
        if self.s == self.t:
            return 0
        maximo = 0
        self.f = dict()
        while True:
            aum = self.camino()
            if aum is None:
                break 
            incr = min(aum.values(), key = (lambda k: k[1]))[1]
            u = self.t
            while u in aum:
                v = aum[u][0]
                actual = self.f.get((v, u), 0) 
                inverso = self.f.get((u, v), 0)
                self.f[(v, u)] = actual + incr
                self.f[(u, v)] = inverso - incr
                u = v
            maximo += incr
        print(maximo)
        return maximo


    def percNod(self):
        self.auxIndice = []
        for pn in range(2*self.k+5):
            self.auxNodo = []
            self.nuevosNodos()
            self.ford_fulk()


    def percolaAri(self):
        self.lqq = []
        for pn in range(1,8):
            self.NuevasAristas()
            self.ford_fulk()


    def graficar(self):
        with open("NoPercola.plot","w") as archivo:
             print("set term postscript color eps", file=archivo)
             print("set output 'NoPercola.eps'", file=archivo)
             print("set xrange [0: {:d}]".format(self.k+1), file=archivo)
             print("set yrange [0: {:d}]".format(self.k+1), file=archivo)
             print("unset xtics", file=archivo)
             print("unset ytics", file=archivo)
             print("set pointsize .5", file=archivo)
             print("set size square", file=archivo)
             print("set key off", file=archivo)
             num = 0
             conteo = 0
             for key in self.aristas:
                 x1 = key[0][0] 
                 y1 = key[0][1] 
                 x2 = key[1][0] 
                 y2 = key[1][1]
                 s = self.aristas[key]
                 conteo += 1
                 if conteo < len(self.aristas)-(self.cuentaAristas - 1):
                     print("set arrow {:d} from {:f},{:f} to {:f}, {:f} nohead lw 1 lc 0".format(num+1,x1,y1,x2,y2),file=archivo)
                 else:
                     print("set arrow {:d} from {:f},{:f} to {:f}, {:f} head filled size screen 0.02,15,45 lw 1.5 lc 6".format(num+1,x1,y1,x2,y2),file=archivo)
                 num+=1
             print("plot 'Fulk.dat' using 1:2:3 with points pt 7 lc var", file=archivo)
             print("show arrow", file=archivo)
             print("quit()",file=archivo)


    def graficarP(self):
        with open("PercolaNodo.plot","w") as archivo:
             print("set term postscript color eps", file=archivo)
             print("set output 'PercolaNodo.eps'", file=archivo)
             print("set xrange [0: {:d}]".format(self.k+1), file=archivo)
             print("set yrange [0: {:d}]".format(self.k+1), file=archivo)
             print("unset xtics", file=archivo)
             print("unset ytics", file=archivo)
             print("set pointsize .5", file=archivo)
             print("set size square", file=archivo)
             print("set key off", file=archivo)
             num = 0
             conteo = 0
             for key in self.aristas:
                 x1 = key[0][0] 
                 y1 = key[0][1] 
                 x2 = key[1][0] 
                 y2 = key[1][1]
                 s = self.aristas[key]
                 conteo += 1
                 if conteo < len(self.aristas)-(self.cuentaAristas - 3):
                     print("set arrow {:d} from {:f},{:f} to {:f}, {:f} nohead lw 1 lc 0".format(num+1,x1,y1,x2,y2),file=archivo)
                 else:
                     print("set arrow {:d} from {:f},{:f} to {:f}, {:f} head filled size screen 0.02,15,45 lw 1.5 lc 6".format(num+1,x1,y1,x2,y2),file=archivo)
                 num+=1
             print("plot 'NodFulk.dat' using 1:2:3 with points pt 7 lc var", file=archivo)
             print("show arrow", file=archivo)
             print("quit()",file=archivo)


    def graficarA(self):
        with open("PercolaArista.plot","w") as archivo:
             print("set term postscript color eps", file=archivo)
             print("set output 'PercolaArista.eps'", file=archivo)
             print("set xrange [0: {:d}]".format(self.k+1), file=archivo)
             print("set yrange [0: {:d}]".format(self.k+1), file=archivo)
             print("unset xtics", file=archivo)
             print("unset ytics", file=archivo)
             print("set pointsize .5", file=archivo)
             print("set size square", file=archivo)
             print("set key off", file=archivo)
             num = 0
             conteo = 0
             for key in self.aristas:
                 x1 = key[0][0] 
                 y1 = key[0][1] 
                 x2 = key[1][0] 
                 y2 = key[1][1]
                 p = self.aristas[key]
                 conteo += 1
                 if conteo < len(self.aristas)-(self.cuentaAristas - 2):
                     print("set arrow {:d} from {:f},{:f} to {:f}, {:f} nohead lw 1 lc 0".format(num+1,x1,y1,x2,y2),file=archivo)
                 else:
                     print("set arrow {:d} from {:f},{:f} to {:f}, {:f} head filled size screen 0.02,15,45 lw 1.5 lc 6".format(num+1,x1,y1,x2,y2),file=archivo)
                 num+=1
             print("plot 'Fulk.dat' using 1:2:3 with points pt 7 lc var", file=archivo)
             print("show arrow", file=archivo)
             print("quit()",file=archivo)


    def graficar1(self):
        with open("NoPercola1.plot","w") as archivo:
             print("set term postscript color eps", file=archivo)
             print("set output 'NoPercola1.eps'", file=archivo)
             print("set xrange [0: {:d}]".format(self.k+1), file=archivo)
             print("set yrange [0: {:d}]".format(self.k+1), file=archivo)
             print("unset xtics", file=archivo)
             print("unset ytics", file=archivo)
             print("set pointsize .5", file=archivo)
             print("set size square", file=archivo)
             print("set key off", file=archivo)
             num = 0
             conteo = 0
             for key in self.aristas:
                 x1 = key[0][0] 
                 y1 = key[0][1] 
                 x2 = key[1][0] 
                 y2 = key[1][1]
                 p = self.aristas[key]
                 conteo += 1
                 if conteo < len(self.aristas)-(self.cuentaAristas - 1):
                     print("set arrow {:d} from {:f},{:f} to {:f}, {:f} nohead lw 1 lc 0".format(num+1,x1,y1,x2,y2),file=archivo)
                 else:
                     print("set arrow {:d} from {:f},{:f} to {:f}, {:f} head filled size screen 0.02,15,45 lw 1.5 lc 6".format(num+1,x1,y1,x2,y2),file=archivo)
                 num+=1
             print("plot 'Fulk.dat' using 1:2:3 with points pt 7 lc var", file=archivo)
             print("show arrow", file=archivo)
             print("quit()",file=archivo)



