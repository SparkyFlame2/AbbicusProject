
import math
import cmath
import random

def fibonacci(n):
    a, b = 0, 1
    for _ in range(max(int(n), 1)):
        a, b = b, a + b
    return a

def catalan(n):
    from math import comb
    n = int(n)
    return comb(2*n, n) // (n + 1) or 1

def triangular(n):
    n = int(n)
    return (n * (n + 1)) // 2 or 1

def harmonic(n):
    n = int(n)
    return sum(1 / k for k in range(1, n + 1)) or 1

def safe_gamma_imaginary_plus_one():
    try:
        return abs(cmath.gamma(1j + 1))
    except Exception:
        return 1

def golden_phi_power(z):
    phi = (1 + math.sqrt(5)) / 2
    return phi ** z

def abbicus_core(inf_energy=None, entropy_rate=None, z=None, n=None, mode="auto"):
    h = 6.62607015e-34  # Planck constant

    if inf_energy is None:
        from enforcement_module import enforcers
        inf_energy = 1.0 + (enforcers * 0.25) + random.uniform(-0.5, 0.5)
    if entropy_rate is None:
        entropy_rate = 0.5 + random.uniform(-0.25, 0.25)
    if z is None:
        z = random.randint(1, 9)
    if n is None:
        n = random.randint(1, 20)

    numerator = (inf_energy - entropy_rate) / h
    scalar = (10 ** 3) * math.pi * safe_gamma_imaginary_plus_one()
    phi_scale = golden_phi_power(z)

    if mode == "auto":
        if n == 0:
            denominator = 1
        elif n < 0:
            mode = "catalan"
        elif n > 10**5:
            mode = "triangular"
        else:
            mode = "fibonacci"

    if mode == "catalan":
        denominator = catalan(n)
    elif mode == "triangular":
        denominator = triangular(n)
    elif mode == "harmonic":
        denominator = harmonic(n)
    elif mode == "null":
        denominator = 1
    else:  # default to Fibonacci
        denominator = fibonacci(n)

    result = numerator - (scalar * phi_scale / denominator)
    return result
