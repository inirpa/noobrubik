import numpy as np
import random

def front_anti_clockwise(rubix_array):
	front_face = np.reshape(rubix_array[0], (3, 3))
	anti_rotated_front_face = np.rot90(front_face)
	print(anti_rotated_front_face)

def front_clockwise(rubix_array):
	front_face = np.reshape(rubix_array[0], (3, 3))
	rotated_front_face = np.rot90(front_face, -1)
	print(rotated_front_face)
	
if __name__ == '__main__':
	rubix_array = np.zeros([6,9], dtype = str)
	color_array = ['W','G','Y','R','B','O']
	for faces in xrange(0,6):
		for pieces in range(0,9):
			rubix_array[faces][pieces] = color_array[random.randrange(1,6)]
	print(rubix_array)
	front_anti_clockwise(rubix_array)
	print()
	front_clockwise(rubix_array)	