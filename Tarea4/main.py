from Grafo import Grafo
from time import time


#nodos = 16
conexiones = 8 
probabilidad = 0.2
radio = 1
x0 = 0
y0 = 0

TPromAvg = 0
TPromCC = 0
PromedioMedio = 0
PromClusterC = 0

with open("Tarea4.dat", "w") as archivo:
    for nodos in range(2,78,5):
        for conex in range (1,27,5):
            G = Grafo()
            G.generaCirculo("circulo.dat",conex, nodos, probabilidad, radio, x0, y0)
            G.graficaCirculo("circulo.gnuplot","circulo.dat")
            G.graficar("aristas.gnuplot")
            iTAvg = time()
            promedio = G.avgdist()
            fTAvg = time() - iTAvg
            TPromAvg += fTAvg
            iTCC = time()
            clusterCoef = G.clustcoef()
            fTCC = time() - iTCC
            TPromAvg += fTAvg
            TPromCC += fTCC
            PromedioMedio += promedio
            PromClusterC += clusterCoef
        print(nodos, PromedioMedio/6,TPromAvg/6,PromClusterC/6,TPromCC/6, file=archivo)
        TPromAvg = 0
        TPromCC = 0
        PromedioMedio = 0
        PromClusterC = 0         
#        print(str(nodos) + "|" + str(conex) +"|"+ str(promedio) +"|"+ str(fTAvg) +"|"+ str(clusterCoef) +"|"+ str(fTCC))
    
    



#for grafico in range(NPruebas):
#    tiempo_inicio = time()

#G = Grafo()
#G.generaCirculo("circulo.dat",conexiones, nodos, probabilidad, radio, x0, y0)
#G.graficaCirculo("circulo.gnuplot","circulo.dat")
#G.graficar("aristas.gnuplot")
#print(G.avgdist())
#print(G.clustcoef())






