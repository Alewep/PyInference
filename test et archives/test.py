import sympy

t = []
x = sympy.Symbol("x")

var = x == []

print(sympy.sympify(var).is_Boolean)
