import math
a=3.0
b=7.0
m=29.0
x0 = input(" Ingrese el valor de la semilla \n")
limite = input ("ingrese el numero de iteraciones \n")
i=0
Xn=0.0
Un=0.0
while i<limite:
	Xn = ((a*x0)+b)%m
	Un = Xn/m
	print "El valor de X"+str(i+1)+" es: "+str(Xn)+" el valor de U"+str(i+1)+" es: "+str(Un)
	x0=Xn
	i+=1
