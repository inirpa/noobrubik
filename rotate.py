import numpy as np
def front_rotate_clockwise(rubix_array):
	# print(rubix_array[0])
	rotated_face = np.roll(rubix_array, 3)
	print(rotated_face)

if __name__ == '__main__':
	rubix_array = np.zeros([6,9], dtype = str)
	color_array = ['W','G','Y','R','B','O']
	for faces in range(0,6):
		for pieces in range(0,9):
			rubix_array[faces][pieces] = color_array[faces]
	front_rotate_clockwise(rubix_array)
	