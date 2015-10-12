import math

n=10
campos=[]
a=5.0
b=3.0
m=16.0
ser=0.0

def congruencialMixto(entrada):
    Xn = ((a*entrada)+b)%m
    return Xn

lamb=input("Ingrese el valor de lambda: \n")
semilla=input("Ingrese el valor de la semilla: \n")
esp=congruencialMixto(semilla)

for i in range(n):
	ser=(1.0/lamb+0.0)*math.log1p(esp/m)
	print (1.0/lamb+0.0)
	campos.append(ser)
	esp=congruencialMixto(esp)

print campos