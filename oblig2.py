import numpy as np
import matplotlib.pyplot as plt

# Definer f(x)
def f(x):
    return np.exp(-x/4) * np.arctan(x)

# Likninga fra den analytiske utregningen
# arctan(x) - 4/x^2+1 = 0
def g(x):
    return np.arctan(x) - 4/(x**2 + 1)

# Prøver 100 000 x-verdier og finner der g(x) er nærmest 0
x_verdier = np.linspace(0, 5,100000)
g_verdier = g(x_verdier)

idx = np.argmin(np.abs(g_verdier)) # finner indeksen til den minste verdien
x_topp = x_verdier[idx]
y_topp = f(x_topp)

print(f"Toppunkt x = {x_topp:.4f}")
print(f"Toppunkt y = {y_topp:.4f}")