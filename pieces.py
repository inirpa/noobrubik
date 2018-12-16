import numpy as np
class Pieces:
	def corner_pieces(rubix_array):
		# print("Orgial Scrambled Cube")
		# print(np.reshape(rubix_array, (6,9)))
		front_face = np.reshape(rubix_array[0], (3, 3))
		right_face = np.reshape(rubix_array[1], (3, 3))
		back_face = np.reshape(rubix_array[2], (3, 3))
		left_face = np.reshape(rubix_array[3], (3, 3))
		up_face = np.reshape(rubix_array[4], (3, 3))
		down_face = np.reshape(rubix_array[5], (3, 3))
		corner_faces = [front_face, right_face, back_face, left_face, up_face, down_face]
		corner_face_names = ['front_face', 'right_face', 'back_face', 'left_face', 'up_face', 'down_face']
		# front_corner = [front_face[0,0], front_face[0,2], front_face[2,0], front_face[2,2]]
		# print(front_corner)
		corners = {}
		for cf,cfn in zip(corner_faces,corner_face_names):
			corners[cfn] = [cf[0,0], cf[0,2], cf[2,0], cf[2,2]]
		
		corner_triplets_1 = [front_face[0,0], left_face[0,2], up_face[2,0] ]
		corner_triplets_2 = [front_face[0,2], right_face[0,0], up_face[2,2]]
		corner_triplets_3 = [front_face[2,2], right_face[2,0], down_face[0,2]]
		corner_triplets_4 = [front_face[2,0], left_face[2,2], down_face[0,0]]
		
		corner_triplets_5 = [right_face[0,2], back_face[0,0], up_face[0,2]]
		corner_triplets_6 = [back_face[0,2], left_face[0,0], up_face[0,0]]
		corner_triplets_7 = [back_face[2,2], left_face[2,0], down_face[2,0]]
		corner_triplets_8 = [right_face[2,2], back_face[2,0], down_face[2,2]]
		corner_triplets = [corner_triplets_1, corner_triplets_2, corner_triplets_3, corner_triplets_4, corner_triplets_5, corner_triplets_6, corner_triplets_7, corner_triplets_8]
		return corner_triplets

	# if __name__ == '__main__':
	# 	# rubix_array = np.zeros([6,9], dtype = str)
	# 	# rubix_array = [
	# 	# 	['G','Y','W','B','W','Y','B','R','W'],
	# 	# 	['B','G','W','R','R','B','R','R','R'],
	# 	# 	['R','G','O','W','Y','Y','B','O','Y'],
	# 	# 	['G','R','Y','G','O','Y','G','W','Y'],
	# 	# 	['W','O','B','G','B','W','O','O','O'],
	# 	# 	['O','B','G','O','G','W','R','B','Y']
	# 	# ]
	# 	print("Orgial Scrambled Cube")
	# 	print(np.reshape(rubix_array, (6,9)))
	# 	front_face = np.reshape(rubix_array[0], (3, 3))
	# 	right_face = np.reshape(rubix_array[1], (3, 3))
	# 	back_face = np.reshape(rubix_array[2], (3, 3))
	# 	left_face = np.reshape(rubix_array[3], (3, 3))
	# 	up_face = np.reshape(rubix_array[4], (3, 3))
	# 	down_face = np.reshape(rubix_array[5], (3, 3))
	# 	corner_pieces(front_face, right_face, back_face, left_face, up_face, down_face)