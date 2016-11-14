'''
This module provides code supporting  the paper,


"Applications of Conformal Geometric Algebra to Transmission Line Theory", by Alex Arsenovic
'''

# imports basis blades and up/down funcs
from clifford.g2c import * 
from math import e,pi,sqrt

# complex <-> vector 
c2v = lambda x: (x.real*e1) + (x.imag*e2) # complex2vector
v2c = lambda x: float(x|e1)+ float(x|e2)*1j

## basis transforms
Rzy = e**(pi/2*(e2^e3))
Ryz = ~Rzy
Rsz = e**(pi/4*(e1^e3))
Rzs = ~Rsz
Rsy = e**(-pi/(sqrt(2)*2)*(e2*e3+e2*e1))
Rys = ~Rsy

## Transsmission lines
Ls = lambda theta: e**(theta *(e1^e2))
Lz = lambda theta: e**(-theta *(e2^e3))

## Distributed Element Group

# bivector algebra 
R =  e3*e4-e1*e3
X = -e2*e4+e1*e2
G =  e3*e4+e1*e3
B =  e2*e4+e1*e2
N =  e1*e4
Q =  e3*e2
L =  e1*e2
A =  e3*e4

half=.5

# Rotors
Rr = lambda x: e**(half*x*R)
Rx = lambda x: e**(half*x*X)
Rg = lambda x: e**(half*x*G)
Rb = lambda x: e**(half*x*B)
Rn = lambda x: e**(-half*log(x)*N)
Rq = lambda x: e**(half*x*Q)
Rl = lambda x: e**(half*x*L)
Ra = lambda x: e**(-half*log(x)*A)


#stubs
cot = lambda x: 1./tan(x)
Rss = lambda theta: e**(-cot(theta)/2*B)
Rss = lambda theta: e**(tan(theta)/2*B)
