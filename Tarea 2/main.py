
from Grafo import Grafo

nodos = 15

GrafoNDir = Grafo()
GrafoNDir.generar(nodos)
GrafoNDir.imprimir("nodosNoDirigido.txt")
GrafoNDir.conectar(0.25)
GrafoNDir.graficar(0,"NoDirigido.tex")
print("unset arrow")

GrafoDir = Grafo()
GrafoDir.generar(nodos)
GrafoDir.imprimir("nodosDirigido.txt")
GrafoDir.conectar(0.25)
GrafoDir.graficar(1,"Dirigido.tex")
print("unset arrow")


GrafoPond = Grafo()
GrafoPond.generar(nodos)
GrafoPond.imprimir("nodosPonderado.txt")
GrafoPond.conectar(0.25)
GrafoPond.graficar(2,"Ponderado.tex")
print("unset arrow")
