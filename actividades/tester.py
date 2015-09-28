from scipy.integrate import quad


def integrand(x, a, b):
    return a * x + b

a = 2
b = 1
I = quad(integrand, 0, 1, args=(a,b))
print I
#I = (2.0, 2.220446049250313e-14)