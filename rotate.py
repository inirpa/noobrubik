import numpy as np

class Rotate():		
	def front_anti_clockwise(front_face, right_face, back_face, left_face, up_face, down_face):
		anti_rotated_front_face = np.rot90(front_face)

		temp_face = np.zeros([1, 3], dtype = int)

		temp_face = right_face[:, 0]
		right_face[:, 0] = down_face[0, :]
		down_face[0, :] = left_face[:, 2]
		left_face[:, 2] = up_face[2, :]
		up_face[2, :] = temp_face
		return(anti_rotated_front_face, right_face, back_face, left_face, up_face, down_face)

	def front_clockwise(front_face, right_face, back_face, left_face, up_face, down_face):
		rotated_front_face = np.rot90(front_face, -1)

		t_face = np.zeros([1, 3], dtype = int)
		t_face = right_face[:, 0]
		right_face[:, 0], up_face[2, :], left_face[:, 2], down_face[0, :] =  up_face[2, :], left_face[:, 2], down_face[0, :], t_face
		# right_face[:, 0] = up_face[2, :]
		# up_face[2, :] = left_face[:, 2]
		# left_face[:, 2] = down_face[0, :]
		# print(id(t_face))
		# down_face[0, :] = t_face
		return(rotated_front_face, right_face, back_face, left_face, up_face, down_face)