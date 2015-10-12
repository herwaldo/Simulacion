import math
from scipy.integrate import quad

k=50
a=5.0
b=3.0
m=16.0

def congruencialMixto(entrada):
    Xn = ((a*entrada)+b)%m
    return Xn

def integrand(x):
    return math.exp(-x**2)

nor=congruencialMixto(123456789)
var=quad(integrand,0.0,((2.0*((nor+0.0)/(m+0.0)))-1.0))
print var