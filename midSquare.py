import math
i=0
Xn=0.0
Un=0.0
x0=input("Ingrese el valor de la semilla \n")
if (len(str(x0))%2) == 0:
<<<<<<< HEAD
	limite = input ("ingrese el numero de valores aletaorios \n")
=======
	limite = input ("ingrese el numero de iteraciones \n")
>>>>>>> 9248fc74e2ce22c4fac558913476bb1a29d609a4
	while i<limite:
		valor=x0*x0
		convertir=""+str(valor)
		if (len(str(valor))%2) == (len(str(x0))%2):
			m=len(str(x0))/2
			print "cumple para hacer el valor aletaorio Un es: 0."+convertir[m:(len(str(convertir))-m)]
			x0=int(convertir[m:(len(str(convertir))-m)])
			i+=1
		else:
			convertir="0"+str(valor)
			m=len(str(x0))/2
			print "cumple para hacer el valor aletaorio Un es: 0."+convertir[m:(len(str(convertir))-m)]
			x0=int(convertir[m:(len(str(convertir))-m)])
			i+=1
else:
	print "intente con otro numero"