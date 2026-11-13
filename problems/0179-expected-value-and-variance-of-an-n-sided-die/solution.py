def dice_statistics(n: int) -> tuple[float, float]:
    """
    Compute the expected value and variance of a fair n-sided die roll.

    Args:
        n (int): Number of sides of the die

    Returns:
        tuple: (expected_value, variance)
    """
    expected_value = (n+1) / 2
    variance = expected_value * (2*n + 1) / 3 - expected_value*expected_value
    return expected_value, variance