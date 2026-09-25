import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	if len(a)*len(a[0])!=new_shape[0]*new_shape[1]:
		return []
	flat=[x for row in a for x in row]
	reshaped_matrix=[
		[x for x in flat[i*new_shape[1]:i*new_shape[1]+new_shape[1]]] for i in range(new_shape[0]) 
	]
	return reshaped_matrix