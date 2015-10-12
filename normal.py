import math
from scipy.integrate import quad

a=5.0
b=3.0
m=16.0
valor=0.0
acum_sum=0.0
integral=0.0
nor=0.0
ser=0.0
campos=[]

def factorial(x,n):
    if (n>0):
        x=factorial(x,n-1)
        x=x*n
    else:
        x=1
    return x

def congruencialMixto(entrada):
    Xn = ((a*entrada)+b)%m
    return Xn

def comparar_valores(valor):
    numero=0.0
    for i in range(len(px)):
        if (valor>=acumulada[i]):
            numero=pux[i]
    return numero

def integrand(x):
    return math.exp(-x**2)

miu=input("Ingrese el valor de miu: \n")
sigma=input("Ingrese el valor de sigma: \n")
semilla=input("Ingrese el valor de la semilla: \n")
nor=congruencialMixto(semilla)

for i in range(21):
	inte,err=quad(integrand,0.0,((2.0*((nor+0.0)/(m+0.0)))-1.0))
	integral=((2.0/((math.pi+0.0)**(1.0/2.0)))+0.0)*inte
	ser=miu+(sigma*math.sqrt(2.0))*integral
	campos.append(ser)
	nor=congruencialMixto(nor)

print campos