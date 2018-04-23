set term postscript color eps
set output 'circulo.eps'
set size square
set key off
plot 'circulo.dat' with points pt 5
