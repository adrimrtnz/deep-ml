def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    a_rows = len(a)
    a_cols = len(a[0])
    b_rows = len(b)
    b_cols = len(b[0])

    if not a_cols == b_rows:
        return -1

    c = [[0] * b_cols for _ in range(a_rows)]

    for c_i in range(a_rows):
        for c_j in range(b_cols):
            num = 0
            for n in range(a_cols):
                num += a[c_i][n] * b[n][c_j]
            c[c_i][c_j] = num
            
    return c