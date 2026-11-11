def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    if mode == 'row':
        return [
            sum(r)/len(r) for r in matrix
        ]
    return [
        sum([r[i] for r in matrix ]) / n_rows  for i in range(n_cols)
    ]