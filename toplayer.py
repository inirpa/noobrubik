import numpy as np
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

def solve_corners(front_face, right_face, back_face, left_face, up_face, down_face):
	print(front_face, right_face, back_face, left_face, up_face, down_face)
	#flip cube make front face as up face
	#check if corners are already solved
	#check if corners has right color pieces
	#if not look for white corner pieces
	#bring them to bottom at right place (may be wrong orientation)
	#apply algorithm
	front_center_piece = front_face[1,1]
	right_center_piece = right_face[1,1]
	back_center_piece = back_face[1,1]
	left_center_piece = left_face[1,1]
	up_center_piece = up_face[1,1]
	down_center_piece = down_face[1,1]

	top_left_corner_adjacent = [back_face[0,2], left_face[0,0]]
	top_right_corner_adjacent = [right_face[0,2], back_face[0,0]]
	bottom_left_corner_adjacent = [left_face[0,2], front_face[0,0]]
	bottom_right_corner_adjacent = [front_face[0,2], right_face[0,0]]
	# corner_adjacent_face = [top_left_corner_adjacent, top_right_corner_adjacent, bottom_left_corner_adjacent, bottom_right_corner_adjacent]	
	# for rows in range(0,3):
	# 	for cols in range(0,3):
	# 		if(up_face[rows, cols] == up_center_piece):
	# 			print("Top layer solved")
	# 		else:
	# 			print("Top layer needs workout")

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
	print("Flip up ")
	print(flip_up(front_face, right_face, back_face, left_face, up_face, down_face))
<<<<<<< HEAD
	print(right_face)
	# solve_corners(front_face, right_face, back_face, left_face, up_face, down_face)
=======
	solve_corners(front_face, right_face, back_face, left_face, up_face, down_face)
>>>>>>> 7d8340c33d707a28410f0efa2dfd4cdcfd805563
