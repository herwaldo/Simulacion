import math
from itertools import combinations

n=100
pux=[]
px=[]
acumulada=[]
a=5.0
b=3.0
m=16.0
suma=0.0
acum_sum=0.0

def congruencialMixto(entrada):
    Xn = ((a*entrada)+b)%m
    return Xn

def comparar_valores(valor):
    numero=0.0
    for i in range(len(px)):
        if (valor>=acumulada[i]):
            numero=pux[i]
    return numero

def combinations(target,data):
	for i in range(len(data)):
		new_target = copy.copy(target)
		new_data = copy.copy(data)
		new_target.append(data[i])
		new_data = data[i+1:]
		print new_target
		combinations(new_target,new_data)

p=input("Ingrese el valor de las posibilidades de exito: \n")
semilla=input("Ingrese el valor de la semilla: \n")

for i in range(n):
    valor=((1-p)**i)*p
    pux.append(i)
    px.append(valor)
    acum_sum+=valor
    acumulada.append(acum_sum)

envio=congruencialMixto(semilla)
for i in range(n):
	envio=congruencialMixto(envio)
	suma+=comparar_valores(envio/m)

print suma,acumulada