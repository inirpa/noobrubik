import numpy as np
import Rotate
import random

if __name__ == '__main__':
	rubix_array = np.zeros([6,9], dtype = str)
	# color_array = ['W','G','Y','R','B','O']
	# for faces in range(0,6):
	# 	for pieces in range(0,9):
	# 		rubix_array[faces][pieces] = color_array[random.randrange(1,6)]
	rubix_array = [
		['G','Y','W','B','W','Y','B','R','W'],
		['B','G','W','R','R','B','R','R','R'],
		['R','G','O','W','Y','Y','B','O','Y'],
		['G','R','Y','G','O','Y','G','W','Y'],
		['W','O','B','G','B','W','O','O','O'],
		['O','B','G','O','G','W','R','B','Y']
	]
	print("Orgial Scrambled Cube")
	print(rubix_array)
	front_face = np.reshape(rubix_array[0], (3, 3))
	right_face = np.reshape(rubix_array[1], (3, 3))
	back_face = np.reshape(rubix_array[2], (3, 3))
	left_face = np.reshape(rubix_array[3], (3, 3))
	up_face = np.reshape(rubix_array[4], (3, 3))
	down_face = np.reshape(rubix_array[5], (3, 3))
	# print("Face rotate anti-clockwise F'")
	# print(np.reshape(Rotate.front_anti_clockwise(front_face, right_face, back_face, left_face, up_face, down_face), (6, 9)))
	print("Face rotate clockwise F")
	print(np.reshape(Rotate.front_clockwise(front_face, right_face, back_face, left_face, up_face, down_face),(6, 9)))