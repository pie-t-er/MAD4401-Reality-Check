import numpy as np
import matplotlib.pyplot as plt
import scipy
import sympy as sp

L1 = 2
L2 = sp.sqrt(2)
L3 = L2
upsilon = sp.pi/2
p1 = sp.sqrt(5)
p2 = p1
p3 = p1
x1, x2, y2 = sp.symbols('x1 x2 y2', real=True)

def f(theta):
  A2 = L3 * sp.cos(theta) - x1
  A3 = L2 * (sp.cos(theta)*sp.cos(upsilon) - sp.sin(theta)*sp.sin(upsilon)) - x2
  B2 = L3 * sp.sin(theta)
  B3 = L2 * (sp.cos(theta)*sp.sin(upsilon) + sp.sin(theta)*sp.cos(upsilon)) - y2

  N1 = B3*(p2**2 - p1**2 - A2**2 - B2**2) - B2*(p3**2 - p1**2 - A3**2 - B3**2)
  N2 = -A3*(p2**2 - p1**2 - A2**2 - B2**2) + A2*(p3**2 - p1**2 - A3**2 - B3**2)
  D = 2*(A2*B3 - B2*A3)

  out = N1**2 + N2**2 - p1**2 * D**2

  return sp.simplify(out)

print(f(-sp.pi/4))
print(f(sp.pi/4))