set term postscript color eps
set output 'resultados.eps'
set logscale x 2
set xrange [2e-3:1.1]
set xlabel "Tiempo de Ejecucion(s)"
set yrange [-0.1:1.1]
set ylabel "Distancia promedio(d/s)"
set y2label "Coeficiente de cluster(c)"
set key off
plot "Tarea4.dat" using 3:2 title "Distancia promedio (d/s)" , "Tarea4.dat" using 5:4 title "Coeficiente del Cluster (c)"


