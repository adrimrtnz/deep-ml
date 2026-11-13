def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode == 'row':
        n_cols = len(matrix[0])
        return [
            sum(row) / n_cols for row in matrix
        ]
    
    if mode == 'column':
        n_rows = len(matrix)
        return [
            sum(col) / n_rows for col in zip(*matrix)
        ]
    return ValueError('mode should be either "row" or "column"')