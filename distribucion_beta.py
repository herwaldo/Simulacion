import math

n=50
campos=[]
a=5.0
b=3.0
m=16.0
ser=0.0

def congruencialMixto(entrada):
    Xn = ((a*entrada)+b)%m
    return Xn

semilla=input("Ingrese el valor de la semilla: \n")
esp=congruencialMixto(semilla)

for i in range(n):
	ser=1.0-(((esp+0.0)/(m+0.0))**(1.0/(n+0.0)))
	campos.append(ser)
	esp=congruencialMixto(esp)

print campos