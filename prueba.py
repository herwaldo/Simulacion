import math
a=3.0
b=7.0
m=29.0
x0 = input(" Ingrese el valor de la semilla \n")
limite = input ("ingrese el numero de iteraciones \n")
i=0
Xn=0.0
Un=0.0
acumula=0.0
dat=[]
while i<limite:
    Xn = ((a*x0)+b)%m
    Un = Xn/m
    print "El valor de X"+str(i+1)+" es: "+str(Xn)+" el valor de U"+str(i+1)+" es: "+str(Un)
    x0=Xn
    dat.append(Un)
    acumula+=Un
    i+=1

segundo=0.0
acumula=acumula/limite
for x in xrange(limite):
    segundo+=(dat[x]-acumula)**2
    print segundo

segundo=(segundo/limite)**0.5
print "desviacion estandar: "+str(segundo)