set terminal eps
set output "tiempos.eps"
set yrange[0:60]
set xrange[0:2700]
set ylabel "Segundos(s)"
set xlabel "Instancia(n)"
l(x) = 0.000008*x**2
plot "tiempos.dat" u 1:2:3:4 t "Tiempos" w yerr, l(x) t "f(x)= 8x10^-^6x^2" w lines

