def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    num_set = sorted(list(set(samples)))
    n = len(samples)
    return [(item, samples.count(item) / n) for item in num_set]