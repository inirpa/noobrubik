import numpy as np
import random

def front_anti_clockwise(front_face, right_face, back_face, left_face, up_face, down_face):
	anti_rotated_front_face = np.rot90(front_face)

	temp_face = np.zeros([1, 3], dtype = int)

	temp_face = right_face[:, 0]
	right_face[:, 0] = down_face[0, :]
	down_face[0, :] = left_face[:, 2]
	left_face[:, 2] = up_face[2, :]
	up_face[2, :] = temp_face

	rotated_cube = [
					anti_rotated_front_face,
					right_face,
					back_face,
					left_face,
					up_face,
					down_face
					]
	return np.reshape(rotated_cube, (6,9))


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
	print("Orgial Scrambled Cube")
	print(rubix_array)
	print("Face rotate clockwise F'")
	front_face = np.reshape(rubix_array[0], (3, 3))
	right_face = np.reshape(rubix_array[1], (3, 3))
	back_face = np.reshape(rubix_array[2], (3, 3))
	left_face = np.reshape(rubix_array[3], (3, 3))
	up_face = np.reshape(rubix_array[4], (3, 3))
	down_face = np.reshape(rubix_array[5], (3, 3))
	print(front_anti_clockwise(front_face, right_face, back_face, left_face, up_face, down_face))