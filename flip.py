import numpy as np
import random

def flip_right(front_face, right_face, back_face, left_face, up_face, down_face):
	up_face = np.rot90(up_face, 1)
	down_face = np.rot90(down_face, -1)
	temp_face[:] = front_face[:]
	front_face[:], left_face[:], back_face[:], right_face[:] = left_face[:], back_face[:], right_face[:], temp_face[:]
	return(front_face, right_face, back_face, left_face, up_face, rotated_down_face)

def flip_left(front_face, right_face, back_face, left_face, up_face, down_face):
	up_face = np.rot90(up_face, -1)
	down_face = np.rot90(down_face, 1)
	temp_face[:] = front_face[:]
	front_face[:], right_face[:], back_face[:], left_face[:] = right_face[:], back_face[:], left_face[:], temp_face[:]
	return(front_face, right_face, back_face, left_face, up_face, rotated_down_face)

def flip_up(front_face, right_face, back_face, left_face, up_face, down_face):
	right_face = np.rot90(right_face, -1)
	left_face = np.rot90(left_face, 1)
	temp_face[:] = up_face[:]
	front_face[:], down_face[:], back_face[:], up_face[:] = down_face[:], back_face[:],up_face[:], temp_face[:]
	return(front_face, right_face, back_face, left_face, up_face, rotated_down_face)

if __name__ == '__main__':
	rubix_array = np.zeros([6,9], dtype = str)
	rubix_array = [
		['G','Y','W','B','W','Y','B','R','W'],
		['B','G','W','R','R','B','R','R','R'],
		['R','G','O','W','Y','Y','B','O','Y'],
		['G','R','Y','G','O','Y','G','W','Y'],
		['W','O','B','G','B','W','O','O','O'],
		['O','B','G','O','G','W','R','B','Y']
	]
	print("Orgial Scrambled Cube")
	print(np.reshape(rubix_array, (6,9)))
	front_face = np.reshape(rubix_array[0], (3, 3))
	right_face = np.reshape(rubix_array[1], (3, 3))
	back_face = np.reshape(rubix_array[2], (3, 3))
	left_face = np.reshape(rubix_array[3], (3, 3))
	up_face = np.reshape(rubix_array[4], (3, 3))
	down_face = np.reshape(rubix_array[5], (3, 3))

	print("Flip right ")
	print(np.reshape(flip_right(front_face, right_face, back_face, left_face, up_face, down_face),(6, 9)))