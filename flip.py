import numpy as np
import random

def flip_right(front_face, right_face, back_face, left_face, up_face, down_face):
	temp_face = np.zeros([3, 3], dtype = str)
	up_face = np.rot90(up_face, 1)
	down_face = np.rot90(down_face, -1)
	temp_face[:] = front_face[:]
	front_face[:], left_face[:], back_face[:], right_face[:] = left_face[:], back_face[:], right_face[:], temp_face[:]
	return(front_face, right_face, back_face, left_face, up_face, down_face)

def flip_left(front_face, right_face, back_face, left_face, up_face, down_face):
	temp_face = np.zeros([3, 3], dtype = str)
	up_face = np.rot90(up_face, -1)
	down_face = np.rot90(down_face, 1)
	temp_face[:] = front_face[:]
	front_face[:], right_face[:], back_face[:], left_face[:] = right_face[:], back_face[:], left_face[:], temp_face[:]
	return(front_face, right_face, back_face, left_face, up_face, down_face)

def flip_up(front_face, right_face, back_face, left_face, up_face, down_face):
	temp_face = np.zeros([3, 3], dtype = str)
	right_face = np.rot90(right_face, -1)
	left_face = np.rot90(left_face, 1)
	back_face = np.rot90(back_face, -1)
	back_face = np.rot90(back_face, -1)
	temp_face[:] = up_face[:]
	temp_face = np.rot90(temp_face, -1)
	temp_face = np.rot90(temp_face, -1)
	up_face[:], front_face[:], down_face[:], back_face[:] = front_face[:], down_face[:], back_face[:], temp_face[:]
	return(front_face, right_face, back_face, left_face, up_face, down_face)

def flip_down(front_face, right_face, back_face, left_face, up_face, down_face):
	temp_face = np.zeros([3, 3], dtype = str)
	right_face = np.rot90(right_face, 1)
	back_face = np.rot90(back_face, -1)
	back_face = np.rot90(back_face, -1)
	down_face = np.rot90(down_face, -1)
	down_face = np.rot90(down_face, -1)
	left_face = np.rot90(left_face, -1)
	temp_face[:] = up_face[:]
	up_face[:], back_face[:], down_face[:], front_face[:] = back_face[:], down_face[:], front_face[:], temp_face[:]
	return(front_face, right_face, back_face, left_face, up_face, down_face)

if __name__ == '__main__':
	rubix_array = np.zeros([6,9], dtype = str)
	rubix_array = [
		['B','W','G','W','W','W','W','W','O'],
		['R','R','G','R','R','R','Y','Y','R'],
		['O','G','G','G','Y','R','Y','O','B'],
		['W','O','R','B','O','O','Y','O','B'],
		['O','Y','Y','G','B','Y','W','B','W'],
		['O','G','B','Y','G','B','R','B','G']
	]
	print("Orgial Cross Scrambled Cube")
	print(np.reshape(rubix_array, (6,9)))
	front_face = np.reshape(rubix_array[0], (3, 3))
	right_face = np.reshape(rubix_array[1], (3, 3))
	back_face = np.reshape(rubix_array[2], (3, 3))
	left_face = np.reshape(rubix_array[3], (3, 3))
	up_face = np.reshape(rubix_array[4], (3, 3))
	down_face = np.reshape(rubix_array[5], (3, 3))

	# print("Flip right ")
	# print(np.reshape(flip_right(front_face, right_face, back_face, left_face, up_face, down_face),(6, 9)))
	# print("Flip left ")
	# print(np.reshape(flip_left(front_face, right_face, back_face, left_face, up_face, down_face),(6, 9)))
	print("Flip up ")
	print(np.reshape(flip_up(front_face, right_face, back_face, left_face, up_face, down_face),(6, 9)))
	# print("Flip down ")
	# print(np.reshape(flip_down(front_face, right_face, back_face, left_face, up_face, down_face),(6, 9)))