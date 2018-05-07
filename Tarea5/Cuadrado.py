x = dict()
y = dict()

k = 5
P = 0.01
l = 1


with open("nodos.dat","w") as matriz:
    for i in range(1,k+1,1):
        for j in range(1,k+1,1):
            x[i] = i
            y[j] = j
            print(x[i],y[j],file=matriz)

print("set term postscript color eps")
print("set output 'matriz.eps'")
print("set xrange [0:"+str(k+1)+"]")
print("set yrange [0:"+str(k+1)+"]")
print ("plot \"nodos.dat\" with points pt 7")

