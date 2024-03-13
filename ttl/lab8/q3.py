import numpy as np
from scipy.linalg import solve
from scipy import integrate
from scipy.optimize import minimize
from scipy.misc import derivative  

# Integration
def f1(x):
    return x**2

result, error = integrate.quad(f1, 0, 1)
print("Result of integration:", result)

# Differentiation
def f2(x):
    return x**2

result = derivative(f2, 1.0)
print("Result of differentiation:", result)

# Optimization
def f3(x):
    return (x - 2)**2

init = 0  # Initial guess for the minimum
result = minimize(f3, init)
print("Minimum value found:", result.fun)
print("Value of x at minimum:", result.x)

# Linear algebra
coeff = np.array([[2, 1], [1, 1]])
consts = np.array([1, 3])

solution = solve(coeff, consts)
print("Solution of the system:", solution)
