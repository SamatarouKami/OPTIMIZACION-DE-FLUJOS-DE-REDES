import math

c = set()
n = 100
theta = 2*math.pi/n


for nodo in range(n):
    x = math.cos(theta*nodo)
    y = math.sin(theta*nodo)
    c.add((x,y))
    print(str(nodo+1)+ " " + str(x) +" " +str(y))
