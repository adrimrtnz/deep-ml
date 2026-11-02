def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	a_rows = len(a)
	a_cols = len(a[0])
	b_rows = len(b)

	is_compatible = (a_cols == b_rows)
	if not is_compatible:
		return -1
	result = []

	for i in range(a_rows):
		num = 0
		for j in range(b_rows):
			num += a[i][j] * b[j]
		result.append(num)
	return result
	