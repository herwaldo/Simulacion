import math
a=5.0
b=3.0
m=16.0
suma=0.0
x=[]
px=[]
acum_sum=0.0
acumulada=[]

def congruencialMixto(entrada):
	Xn = ((a*entrada)+b)%m
	return Xn

def comparar_valores(valor):
	numero=0.0
	for i in range(len(px)):
		if (valor>=acumulada[i]):
			numero=x[i]
	return numero

valor = input("Ingrese el numero de variables de aleatorias \n")
for i in range(valor):
	dato=input("Ingrese el valor de la variable X "+str(i+1)+": \n")
	x.append(dato)
	porba=input("Ingrese el valor de la Provabilidad de X: \n")
	px.append(porba+0.0)
	acum_sum+=porba
	acumulada.append(acum_sum)

dados=input("ingrese el numero de veces a tirar los dados: \n")
semilla=input("Ingrese la semilla por favor \n")
envio=congruencialMixto(semilla)

for i in range(dados):
	envio=congruencialMixto(envio)
	suma+=comparar_valores(envio/m)

print suma