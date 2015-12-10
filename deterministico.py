import math
from scipy.integrate import quad

k=50
a=5.0
b=3.0
m=16.0
fac=0.0
valor=0.0
acum_sum=0.0
integral=0.0
nor=0.0
pois=0.0
ser=0.0
pux=[]
px=[]
acumulada=[]
servidor=[]
llegada=[]

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

lamb=input("Ingrese el valor de lambda: \n")
miu=input("Ingrese el valor de miu: \n")
sigma=input("Ingrese el valor de sigma: \n")

for i in range(k):
    valor=(math.exp((-1)*(lamb))*(lamb**i))/(factorial(1,i)+0.0)
    pux.append(i)
    px.append(valor)
    acum_sum+=valor
    acumulada.append(acum_sum)

nor=congruencialMixto(123456789)
pois=congruencialMixto(987654321)

for i in range(21):
	inte,err=quad(integrand,0.0,((2.0*((nor+0.0)/(m+0.0)))-1.0))
	integral=((2.0/((math.pi+0.0)**(1.0/2.0)))+0.0)*inte
	ser=miu+(sigma*math.sqrt(2.0))*integral
	servidor.append(ser)
	pois=congruencialMixto(pois)
	llegada.append(comparar_valores(pois/m))
	nor=congruencialMixto(nor)

for i in xrange(21):
    print "Tiempo: "+str(i)+", pila: "+str(llegada[i])+", servidor: "+str(servidor[i])