from time import time
from typing import Type, Any

import numpy as np
import numexpr as ne
from numpy import floating, ndarray, dtype
from numpy._typing import _64Bit

#Same as exercise 1 but with NumExpr

dtype = np.float64
a = np.linspace(0, 10, num=12500000, dtype=dtype)  ##I create an array that will have a number of elements with a value between 0 and 10
b = np.linspace(0, 10, num=12500000, dtype=dtype)
c = np.linspace(0, 10, num=12500000, dtype=dtype)
t0 = time()
d1 = ne.evaluate("a+b*c")
t1 = time() - t0 #0.044
print(f"{t1=:.3f}")


a1 = a[2]
b1 = b[2]
c1 = c[2]
dd = d1[2]
print(f"{a1=:.3e}") #f-string
print(f"{b1=:3e}") #f-string
print(f"{c1=:3e}") #f-string
print(f"{dd=:3e}") #f-string

nelem = 12500000
d2 = np.empty(nelem, dtype=np.float64)
pi = 0
i = 125000
entradas = ["aa", "bb", "cc"]
t00 = time()
while i <= nelem:   #I have to create a dictionary with three entries a,b,c.I am updating
    vistas = [a[pi:i], b[pi:i], c[pi:i]]
    dicc = dict(zip(entradas, vistas))
    expr = "aa + bb * cc"  #Expressions do not accept operands, I have to tell it to access the dicc
    d2[pi: i] = ne.evaluate(expr,local_dict=dicc)
    pi = i
    i += 125000


# Testing
print("Valores en dicc ")
for key, value in dicc.items():
    print(f"{key}: {value}")

t2 = time() - t00
tolerancia = 1e-15
sol = np.testing.assert_allclose(d1, d2, atol=tolerancia, rtol=tolerancia)

print(f"{sol}")
print(f"{t2=:.3f}") #f-string

