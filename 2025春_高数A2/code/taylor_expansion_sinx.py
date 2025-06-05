import math
import numpy as np
import matplotlib.pyplot as plt

# Use matplotlib's math text rendering
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'STIXGeneral'

def sin_taylor(x, n):
    """
    Calculate the n-th order Taylor series expansion of sin(x)
    """
    result = 0
    for i in range(n):
        result += (-1)**i * x**(2*i+1) / math.factorial(2*i+1)
    return result

def taylor_expression(n):
    """
    Generate the math expression for the n-th order Taylor series of sin(x)
    """
    terms = []
    for i in range(n):
        if i == 0:
            terms.append("x")
        else:
            sign = "-" if i % 2 == 1 else "+"
            terms.append(f"{sign}\\frac{{x^{{{2*i+1}}}}}{{{(2*i+1)}!}}")
    return " ".join(terms)

# Create an array of x values
x = np.linspace(-1.5*np.pi, 1.5*np.pi, 200)

# Calculate the true sin(x) values
y_true = np.sin(x)

# Create the figure
plt.figure(figsize=(16, 10))

# Plot the true sin(x) function
plt.plot(x, y_true, label=r'$\sin(x)$', color='black', linewidth=2)

# Plot different orders of Taylor series expansion
colors = ['red', 'green', 'blue', 'purple', 'orange']
orders = [1, 3, 5, 7, 9]
for n, color in zip(orders, colors):
    y_approx = sin_taylor(x, n)
    expression = taylor_expression(n)
    plt.plot(x, y_approx, label=fr'${n}\mathrm{{th}}\,\mathrm{{order}}:$ ${expression}$', color=color, linestyle='--')

# Set figure properties
plt.title(r'$\sin(x)$ Function and Its Taylor Series Expansions')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0., fontsize=10)
plt.grid(True)
plt.tight_layout()

# Show the figure
plt.show()
