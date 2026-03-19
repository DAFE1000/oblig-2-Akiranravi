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

# Plot funksjonen
x_plot = np.linspace(-10, 15, 1000)

plt.figure(figsize=(10, 6))
plt.plot(x_plot, f(x_plot), color='blue', label='f(x)')

# Markerer toppunktet med rød prikk
plt.plot(x_topp, y_topp, 'ro', markersize=10,
         label=f'Toppunkt ({x_topp:.4f}, {y_topp:.4f})')

plt.title('f(x) = e^(-x/4) * arctan(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

plt.savefig('oblig2_plot.png')
plt.show()