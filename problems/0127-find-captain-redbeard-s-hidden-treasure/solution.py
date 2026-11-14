def find_treasure(start_x: float) -> float:
    """
    Find the x-coordinate where f(x) = x^4 - 3x^3 + 2 is minimized.

  Returns:
        float: The x-coordinate of the minimum point.
    """
    lr  = 0.12
    grad = lambda x: 4*x - 9
    x = start_x
    epochs = 1_000
    max_g = 10

    for _ in range(epochs):
        g = grad(x)
        g = max(min(g, max_g), -max_g)
        step = lr * g
        if abs(step) < 1e-10:
            break
        x = x - lr * g
    return x
