import numpy as np

def cross_product(a, b):
    n = len(a)

    return [
        a[(i + 1) % n]*b[(i + 2) % n] - a[(i+2) % n]*b[(i+1) % n]
        for i in range(n)
    ]