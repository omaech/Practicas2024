from time import time
import numpy as np
import numexpr as ne

##Creating an NDArray from a NumPy array
dtype = np.float64
a = np.linspace(0,10,num=12500000,dtype=dtype)  ##I create an array that will have a number of elements with a value between 0 and 10
b = np.linspace(0,10,num=12500000,dtype=dtype)
c = np.linspace(0,10,num=12500000,dtype=dtype)
t0 = time()
d1 = a+b*c
t1 = time() - t0 #0.083
print(f"{t1=:.3f}") #f-string, with 3 decimals and brings it closer

#testing
a1 = a[2]
b1 = b[2]
c1 = c[2]
dd = d1[2]
print(f"{a1=:.3e}") #f-string
print(f"{b1=:3e}") #f-string
print(f"{c1=:3e}") #f-string
print(f"{dd=:3e}") #f-string

##EXERCISE 2: we divide the 1GB array "a" into 1MB blocks (SChunks) --> each block will be 1 MB = (10^6) % 8 = 12500000
nelem = 12500000
d2 = np.empty(nelem, dtype=np.float64)
pi = 0
i = 125000
t00 = time()
while i < 12500000:   #SLICE = a sight
    d2[pi:i] = a[pi:i] + b[pi:i] * c[pi:i]
    pi = i
    i += 125000

t2 = time() - t00
print(f"{t2=:.3f}") #f-string
tolerancia = 1e-14
sol = np.allclose(d1, d2, atol=tolerancia, rtol=tolerancia)
print(f"{sol}")










