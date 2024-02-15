#Same exercise as 3 but Schunk is not divisible by the total number of elements and I include everything within the loop.
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
t1 = time() - t0
print(f"{t1=:.3f}")

#12.500.000 % 375.000 = 33,3333 It is not divisible
nelem = 12500000
dimbloque = 375000
d2 = np.empty(nelem, dtype=np.float64)
pi = 0
i = 0
entradas = ["aa", "bb", "cc"]
t00 = time()

while i != nelem:   #I have to create a dictionary with three entries a,b,c.I am updating
    if (i > nelem):
        dif = i - nelem
        i = nelem
        pi = nelem - dif
    else:
        pi = i
        i += dimbloque

    vistas = [a[pi:i], b[pi:i], c[pi:i]]
    dicc = dict(zip(entradas, vistas))
    expr = "aa + bb * cc"  #Expressions do not accept operands, I have to tell it to access the dicc
    d2[pi: i] = ne.evaluate(expr,local_dict=dicc)


# Testing
print("Valores en dicc ")
for key, value in dicc.items():
    print(f"{key}: {value}")

t2 = time() - t00
print(f"{t2=:.3f}") #f-string
tolerancia = 1e-15
sol = np.testing.assert_allclose(d1, d2, atol=tolerancia, rtol=tolerancia)
print(f"{sol}")


