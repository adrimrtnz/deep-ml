import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	dot_prod = v1.dot(v2)
	v1_norm = np.linalg.norm(v1)
	v2_norm = np.linalg.norm(v2)
	return dot_prod / (v1_norm * v2_norm)