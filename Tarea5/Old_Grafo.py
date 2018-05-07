from random import random, uniform, randint, gauss, expovariate
from math import sqrt, ceil, floor, factorial, cos, sin, pi
#from random import random, choice
#import math

colores = ["black", "blue", "pink", "orange", "red"]
pesos = [1,1,1]

def cabecera(aristas, k,  eps=True):
    if eps:
        print("set term postscript color eps", file = aristas)
        print("set output 'circulo12.eps'", file = aristas)
    else:
        print("set term png", file = aristas)
        print("set output 'circulo12.png'", file = aristas)
    print("set xrange [0:"+str(k+1)+"]", file = aristas)
    print("set yrange [0:"+str(k+1)+"]", file = aristas)
    print('set size square', file = aristas) 
    print('set key off', file = aristas)

def pie(destino, aristas):
    print("plot '{:s}' using 1:2 with points pt 5  ps 1".format(destino), file = aristas)

class Grafo:
    
    def __init__(self):
        self.n = None # se crean las variables pero aun no se inicializan
        self.x = dict()
        self.y = dict()
        self.E = []
        self.nodos = dict()
        self.destino = None
        self.vecinos = dict()
        self.vecinos2 = dict()
        self.posicion = dict()
        self.tamano = dict()
        self.i = None
        self.aristas = []
        self.d = None
        self.sumatoria = None
        

    def generar(self, orden): # creando los nodos
        self.n = orden        
        for nodo in range(self.n):
            self.x[nodo] = random()
            self.y[nodo] = random() 

    def imprimir(self, dest): # guardando los pares X y Y en un archivo
        self.destino = dest
        with open(self.destino , "w") as archivo:
            for nodo in range(self.n):
               print(self.x[nodo], self.y[nodo], file=archivo)
        print(self.destino)


    def factorial(self, *n):
        for x in n:
            fac = 1
            for y in range(1,x + 1):
                fac = fac * y
                
        return fac

    def conectar(self, v, u):
        peso = choice(pesos)
        color = "red"
               
        if not v in self.nodos:
            self.agrega(v)
        if not u in self.nodos:
            self.agrega(u)
        
        self.E.append((self.i, v, u, peso, color))      
        self.vecinos[u].add((int(v), peso))
        self.vecinos2[u].add(int(v))
        self.vecinos[v].add((int(u), peso))
        self.vecinos2[v].add(int(u))
            
    def agrega(self, v, posicion = (0,0)):
        self.nodos.add(v)
        
        self.posicion[v] = posicion
        if not v in self.vecinos:
            self.vecinos[v] = set()
            self.vecinos2[v] = set()

    def generaCirculo(self, dest, k, N, prob, r, x0, y0): #Para crear vertices que formen un circulo y guardarlos en un .txt
        self.destino = dest
        self.i = 1
        size = random()
        self.n = N
        with open(self.destino , "w") as circulo:
            for n in range(N):
                xn = x0 + r *(math.cos(2*math.pi * (n/N)))
                yn = y0 + r *(math.sin(2*math.pi * (n/N)))
                print(xn, yn, file = circulo)
                self.x[n] = xn
                self.y[n] = yn
                self.agrega(size, (xn, yn))                        
                           
            for a in range(N):
                for j in range(k):
                    
                    jj = (a+j+1)%n            
                    self.conectar(str(a),str(jj))
                    self.i += 1                  

            for i in range(n-1):
                for j in range(n-2*k-1):
                    jj = (i+j+k+1)%n
                    if random() > prob:   
                        self.conectar(str(a),str(jj))
                        
        return self.E

    
    def graficaCirculo(self, plot, circulo): #Para plotear un circulo en gnuplot 
        with open(plot, "w") as circulo:
            cabecera(circulo)                        
            circulos = "plot 'circulo.dat' with points pt 5"
            print(circulos, file=circulo)
            
    def graficar(self, plot,k): # imprimiendo el grafo con aristas
        assert self.destino is not None
        with open(plot, "w") as aristas:
            cabecera(aristas,k)
            
            for (num, v, w, p, c) in self.E:
                x1 = self.x[int(v)]
                x2 = self.x[int(w)]
                y1 = self.y[int(v)]
                y2 = self.y[int(w)]                 
                flecha = "set arrow {:d} from {:f}, {:f} to {:f}, {:f} lt 2 lw {:f} lc rgb '{:s}' nohead".format(num,x1,y1,x2,y2,p,c)
                print(flecha, file=aristas)
            pie(self.destino, aristas)
        
    def FloydWarshall(self):
        d = {}
        for nod in range(self.n-1):
            d[(nod,nod)] = 0 # distancia reflexiva es cero
            for (vecino,peso) in self.vecinos[str(nod)]: # para vecinos, la distancia es el peso               
                d[(nod,vecino)] = peso
        for intermedio in self.vecinos:
            for desde in self.vecinos:
                for hasta in self.vecinos:
                    di = None
                    if (desde,intermedio) in d:
                        di = d[(desde, intermedio)]
                    ih = None
                    if (intermedio,hasta) in d:
                        ih = d[(intermedio,hasta)]
                    if di is not None and ih is not None:
                        c = di + ih # largo del camino via "i"
                        if (desde, hasta) not in d or c < d[(desde, hasta)]:
                            d[(desde, hasta)] = c # mejora al camino actual

           
        return d


    def avgdist(self): #Promedio de las distancias
        self.d = self.FloydWarshall()
        self.sumatoria = sum(self.d.values())/ len(self.d)
        return self.sumatoria

  
    def clustcoef(self):
        g = len(self.vecinos2) - 1
        valor = 0
        for v in range(1, g):
            m = 0
            for u in self.vecinos2[str(v)]:
                for w in self.vecinos2[str(v)]:
                    if u in self.vecinos2[str(w)]:
                        m+= 1
            n = len(self.vecinos2[str(v)])
            if n > 1: 
                valor += m/(n*(n-1))                
        return(valor/g)

##New code

    def agregaNodos(self,v,x,y):
        self.nodos[v] = (x,y)
        if not v in self.vecinos: # vecindad de v
            self.vecinos[v] = set() # inicialmente no tiene nada
        #with open("GraficaNodos.txt", 'a') as archivo:
        #    print(x,y,v, file = archivo)

            
    def puntos(self, dest, k):
        self.destino = dest        
        
        with open(self.destino, 'w') as puntos:
            it= 0
            for i in range(1,k+1,1):
                for j in range(1,k+1,1):
                    
                    x = i
                    y = j   
                    self.agregaNodos(it,x,y)
                    it += 1
                    print(x,y,it, file = puntos)

    def getManhattan(self, a,b):
        (x1, y1) = self.nodos[a]
        (x2, y2) = self.nodos[b]
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        md = dx + dy
        
        return(md)




    def manhattan(self, k, l, p):
        
        mu = 10
        sigma = 5
        lmbd = 2


        color = 'black'
        cantidad = 0
        peso1 = 0
        peso2 = 0
        #conecciones l
        for i in self.nodos:
            for j in self.nodos:
                if (self.getManhattan(i,j) <= l):
                    peso1 = gauss(mu,sigma)
                    peso1 = abs(int(peso1))+1
                    
                    self.aristas.append((i, j, peso1, color))
                    self.aristas.append((j, i, peso1, color))
                    
                    self.vecinos[i].add(j)
                    
                    self.vecinos[j].add(i)
                    
                    
                elif (random() < p) :
                   color2 = 'blue'
                   cantidad += 1
                   peso2 = expovariate(lmbd)*mu/4
                   peso2 = abs(int(peso2))+1
                   
                   
                   self.aristas.append((i, j, peso2, color2))
                   self.vecinos[i].add(j) 

    def EliminaArista(self, u,v):

        f = self.aristas[u]
        g = self.aristas[v]
        #print(f)
        print(g)
        self.aristas.remove(f)
        self.aristas.remove(g)
        #print(self.vecinos)
        self.vecinos[u].remove(v)
        if not f:        
            self.vecinos[v].remove(u)

        print(len(self.aristas))    

    def EliminaNodo(self, u):
        vecindad = self.vecinos[u].copy()
        for i in vecindad:
            print("quité arista con",i)
            self.EliminaArista(u,i)
        for n in self.nodos:
            if u in self.vecinos[n]:
                print("uy quité arista con",n)
                self.EliminaArista(n,u)
        
        h = self.nodos.pop(u)
        print(self.nodos)
        print(len(self.aristas))
