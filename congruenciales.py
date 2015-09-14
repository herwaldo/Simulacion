import math
a=5.0
b=3.0
m=16.0
x0 = input(" Ingrese el valor de la semilla \n")
<<<<<<< HEAD
limite = input ("ingrese el numero de valores aleatorios \n")
=======
limite = input ("ingrese el numero de iteraciones \n")
>>>>>>> 9248fc74e2ce22c4fac558913476bb1a29d609a4
i=0
Xn=0.0
Un=0.0
while i<limite:
	Xn = ((a*x0)+b)%m
	Un = Xn/m
	print "El valor de X"+str(i+1)+" es: "+str(Xn)+" el valor de U"+str(i+1)+" es: "+str(Un)
	x0=Xn
	i+=1
