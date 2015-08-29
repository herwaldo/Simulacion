import time
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import math
a=48.0
control=0
datosX=[]
datosY=[]
radio=0.0
b=34.0
m=123456789.0
k=6.0
Xn=0.0
delta=0.0
rando_x=0.0
rando_y=0.0
gerX=0.0
gerY=0.0
x=0.0
y=0.0
i=0.0
limite=0.0

def congruencialMixto(entrada):
	Xn = ((a*entrada)+b)%m
	return Xn/m

def congruencialMixtoXn(entrada):
	Xn = ((a*entrada)+b)%m
	return Xn

def dentro(rando_x,rando_y):
	valor=rando_x**2+rando_y**2
	if valor<=(radio**2):
		print "Este valor esta dentro del circulo."
	else:
		print "Este valor no esta dentro del circulo."

def convertir(numero):
	val=((2*k)*numero)-k
	return val

x0 = input("Ingrese el valor de la semilla: \n")
limite = input ("Ingrese el numero de valores aleatorios a generar: \n")+0.0
radio = input("Ingrese el radio del circulo: \n")+0.0
rando_x=congruencialMixto(x0)
gerX=congruencialMixtoXn(x0)
while i<limite:
	rando_y=congruencialMixto(gerX)
	gerY=congruencialMixtoXn(gerX)
	rando_x=congruencialMixto(gerY)
	gerX=congruencialMixtoXn(gerY)
	x=convertir(rando_x)
	y=convertir(rando_y)
	datosX.append(x)
	datosY.append(y)
	#dentro(x,y)
	#print "Esta es la cordenada: "+str(x)+", "+str(y)
	i+=1
	valor=rando_x**2+rando_y**2
	if valor<=(radio**2):
		delta+=(1/(limite*((2*radio)**2)))
		print delta
	'''if (control==100):
		control=0
		plt.ion()
		ax=plt.gca()
		for z in range(int(i)):
			if valor<=(radio**2):
				ax.plot(datosX[z],datosY[z],"b*")
			else:
				ax.plot(datosX[z],datosY[z],"r*")
		plt.draw()'''
	plt.ion()
	ax=plt.gca()
	if valor<=(radio**2):
		ax.plot(datosX[control],datosY[control],"b*")
	else:
		ax.plot(datosX[control],datosY[control],"r*")
	plt.draw()
	control+=1
	#print "Este es el radio generado: "+str(delta)+", este es el radio teorico: "+str(math.pi*(radio**2))
