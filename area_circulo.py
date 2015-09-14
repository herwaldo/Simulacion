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
	return Xn

def congruencialMixtoXn(entrada):
	Xn = ((a*entrada)+b)%m
	return Xn

def convertir(numero):
	val=((2*k)*numero)-k
	return val

x0 = input("Ingrese el valor de la semilla: \n")
limite = input ("Ingrese el numero de valores aleatorios a generar: \n")+0.0
radio = input("Ingrese el radio del circulo: \n")+0.0
rando_x=congruencialMixto(x0)
gerX=congruencialMixtoXn(x0)
while i<limite:
	rando_y=congruencialMixto(gerX)/m
	gerY=congruencialMixtoXn(gerX)
	rando_x=congruencialMixto(gerY)/m
	gerX=congruencialMixtoXn(gerY)
	x=convertir(rando_x)
	y=convertir(rando_y)
	datosX.append(x)
	datosY.append(y)
	i+=1
	valor=rando_x**2+rando_y**2
	if valor<=(radio**2):
		delta+=((1/limite)*((2*radio)**2))
	plt.ion()
	ax=plt.gca()
	if valor<=(radio**2):
		ax.plot(datosX[control],datosY[control],"b*")
	else:
		ax.plot(datosX[control],datosY[control],"r*")
	plt.draw()
	control+=1

print "Este es el radio generado: "+str(delta)+",este es el radio teorico: "+str(math.pi*(radio**2))
