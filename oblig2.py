import numpy as np
import matplotlib.pyplot as plt

# Definer f(x)
def f(x):
    return np.exp(-x/4) * np.arctan(x)

# Likninga fra den analytiske utregningen
# arctan(x) - 4/x^2+1 = 0
def g(x):
    return np.arctan(x) - 4/(x**2 + 1)
