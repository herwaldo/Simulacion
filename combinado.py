from matplotlib.pylab import *
Un=0.0
Xn=0.0
Yn=0.0
Zn=0.0
mx=30269.0
my=30307.0
mz=30323.0
ax=171
ay=172
az=170
i=0
x0=input("Ingrese el valor de la semilla X0: \n")
y0=input("Ingrese el valor de la semilla Y0: \n")
z0=input("Ingrese el valor de la semilla Z0: \n")
limite = input ("ingrese el numero de valores aleatorios: \n")
datos=[]
while i<limite:
	Xn = (ax*x0)%mx
	Yn = (ay*y0)%my
	Zn = (az*z0)%mz
	Un=((Xn/mx)+(Yn/my)+(Zn/mz))%1
	i+=1
	x0=Xn
	y0=Yn
	z0=Zn
	print "El valor de X"+str(i+1)+" es: "+str(Xn)
	print "El valor de Y"+str(i+1)+" es: "+str(Yn)
	print "El valor de Z"+str(i+1)+" es: "+str(Zn)
	print "El valor de Un"+str(i+1)+" es: "+str(Un)
	datos.append(Un)

#print datos[100]

hist(datos,100,(0,1))
show()
'''pos = arange(len(datos))
bar(pos,datos)
#xticks(pos,array2,rotation=30, size='small')
savefig("NumCanal.jpg")


fig,l = plt.subplots()
n,bins = np.histogram([1,2,3,4,2],10)
plt.show()'''