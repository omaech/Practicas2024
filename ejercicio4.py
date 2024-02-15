import blosc2
import numpy as np
from time import time

#Numpy

dtype = np.float64
a1 = np.linspace(0,10,num=12500000,dtype=dtype)  ##I create an array that will have a number of elements with a value between 0 and 10
b1 = np.linspace(0,10,num=12500000,dtype=dtype)
c1 = np.linspace(0,10,num=12500000,dtype=dtype)
t0 = time()
d1 = a1+b1*c1
t1 = time() - t0
print(f"{t1=:.3f}") #f-string, with 3 decimals and brings it closer

#We define in Blosc2

a2 = blosc2.zeros(12500000, dtype=dtype)
b2 = blosc2.zeros(12500000, dtype=dtype)
c2 = blosc2.zeros(12500000, dtype=dtype)
a2[:] = a1
b2[:] = b1
c2[:] = c1
nelem = 12500000
d2 = blosc2.empty(nelem, dtype=np.float64)
pi = 0
i = 125000
t00 = time()
while i <= 12500000:   #SLICE = a sight
    d2[pi:i] = a2[pi:i] + b2[pi:i] * c2[pi:i]
    pi = i
    i += 125000

t2 = time() - t00
print(f"{t2=:.3f}") #f-string

#WeCompare
tolerancia = 1e-14
#d2[:] to convert to array and compare
sol = np.testing.assert_allclose(d1, d2[:], atol=tolerancia, rtol=tolerancia)
print(f"{sol}")