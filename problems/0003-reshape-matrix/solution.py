import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method
    array = np.array(a)
    m_a, n_a = array.shape
    m_b, n_b = new_shape
    if m_a * n_a != m_b * n_b:
        return []
    return array.reshape(new_shape).tolist()