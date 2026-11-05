import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    exp_g = [i for i in range(len(g_coeffs) - 1, -1, -1)]
    exp_h = [i for i in range(len(h_coeffs) - 1, -1, -1)]
    g_x = sum([coeff * x ** exp for coeff, exp in zip(g_coeffs, exp_g)])
    h_x = sum([coeff * x ** exp for coeff, exp in zip(h_coeffs, exp_h)])

    g_prime_x = sum([
        coeff * exp * x ** (exp - 1) for i, (coeff, exp) in enumerate(zip(g_coeffs, exp_g)) \
        if i < len(g_coeffs) and not (x == 0 and (exp - 1) < 0)
        ])
    h_prime_x = sum([
        coeff * exp * x ** (exp - 1) for i, (coeff, exp) in enumerate(zip(h_coeffs, exp_h)) \
        if i < len(h_coeffs) and not (x == 0 and (exp - 1) < 0)
        ])
    numerator   = g_prime_x * h_x - g_x * h_prime_x
    denominator = h_x * h_x
    return numerator / denominator