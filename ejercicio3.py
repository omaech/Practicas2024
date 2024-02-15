#Same exercise as 2 but Schunk is not divisible by the total number of elements

import numpy as np
import numexpr as ne
from time import time
from numpy import floating, ndarray, dtype
from numpy._typing import _64Bit

dtype = np.float64
a = np.linspace(0, 10, num=12500000, dtype=dtype)  ##I create an array that will have a number of elements with a value between 0 and 10
b = np.linspace(0, 10, num=12500000, dtype=dtype)
c = np.linspace(0, 10, num=12500000, dtype=dtype)
t0 = time()
d1 = ne.evaluate("a+b*c")
t1 = time() - t0 #0.044
print(f"{t1=:.3f}")

#Each Schunk is 3 MB = (3*10^6)%8 = 375,000
nelem = 12500000
d2 = np.empty(nelem, dtype=np.float64)
pi = 0
i = 375000
entradas = ["aa", "bb", "cc"]
contador = 0
t00 = time()

#12.500.000 % 375.000 = 33,3333 It is not divisible
while i < nelem:   #I have to create a dictionary with three entries a,b,c.I am updating
    vistas = [a[pi:i], b[pi:i], c[pi:i]]
    dicc = dict(zip(entradas, vistas))
    expr = "aa + bb * cc"  #Expressions do not accept operands, I have to tell it to access the dicc
    d2[pi: i] = ne.evaluate(expr,local_dict=dicc)
    pi = i
    i += 375000
    contador += 1

print(f"{contador}")
i = nelem
pi = nelem - 125000  #The loop is done 33 times, 375,000 * 33 = 12,375,000, up to 12,500,000, 125,000 are missing
vistas = [a[pi:i], b[pi:i], c[pi:i]]
dicc = dict(zip(entradas, vistas))
expr = "aa + bb * cc"  #Expressions do not accept operands, I have to tell it to access the dicc
d2[pi: i] = ne.evaluate(expr,local_dict=dicc)



# Testing
print("Valores en dicc ")
for key, value in dicc.items():
    print(f"{key}: {value}")

t2 = time() - t00
tolerancia = 1e-15
sol = np.testing.assert_allclose(d1, d2, atol=tolerancia, rtol=tolerancia)

print(f"{sol}")
print(f"{t2=:.3f}") #f-string

