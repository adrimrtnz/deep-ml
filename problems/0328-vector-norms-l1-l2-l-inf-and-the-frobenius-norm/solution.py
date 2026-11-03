import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    # Your code here
    match norm_type:
        case 'l1':
            return np.abs(arr).sum().astype(dtype=np.float32)
        case 'l2':
            return np.linalg.norm(arr).astype(dtype=np.float32)
        case 'linf':
            return np.abs(arr).max().astype(dtype=np.float32)
        case 'frobenius':
            return np.linalg.norm(arr, 'fro')

