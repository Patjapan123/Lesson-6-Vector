from code import Vector

vector1 = Vector(9.81, 270)
vector2 = Vector(19.62, 30)
vector3 = vector2.strip_x()

if vector3.get_scalar() == 16.99142 and vector3.get_angle() == 0:
	print("Test Case 1 Passed!")
else:
	print("Test Case 1 Failed, vector3.get_scalar() expected 16.99142 and got", vector3.get_scalar(), "vector3.get_angle() expected 0 and got", vector3.get_angle())

added_vector = vector1.plus(vector2)

if added_vector.get_scalar() == 16.99142 and added_vector.get_angle() == 0:
	print("Test Case 2 Passed!")
else:
	print("Test Case 2 Failed, added_vector.get_scalar() expected 16.99142 and got", added_vector.get_scalar()), "added_vector.get_angle() expected 0 and got", added_vector.get_angle()

subtracted_vector = vector1
subtracted_vector.subtract_with(vector2)

if subtracted_vector.get_dy() == -19.62:
	print("Test Case 3 Passed!")
else:
	print("Test Case 3 Failed, subtracted_vector.get_dy() expected -19.62 and got", subtracted_vector.get_dy())