behavior: Vector should be a class that contains an angle (measured in degrees) and scalar. It should hold the following functions:
	__init__(scalar,angle) initializes the vector (angle is measured in degrees)
	-set_scalar(new_scalar) sets the current scalar to a given different one
	-set_angle(new_angle) sets the current angle to a given different one
	-get_angle() returns the current angle
	-get_scalar() returns the current scalar
	-get_dx() returns the change in x value from the scalar
	-get_dy() returns the change in y value from the scalar
	-strip_x() similar to get_dx(), but returns a Vector. returns a new Vector that contains only the x direction (e.g. the scalar is 6 and the angle is 60 degrees, strip_x returns Vector with scalar 3 and angle 0 degrees)
	-strip_y() returns a new Vector that contains onnlt the y direction
	-add_with(another) adds another Vector to the current one
	-subtract_with(another) subtracts another Vector from the current one
	-plus(another) adds another Vector to the current one without changing the current one and returns the resulting vector
	-minus(another) subtracts another Vector from the current one without changing the current one and returns the resulting vector
library functions: at the top of the code, write "import math" to use the pi constant and trigonometry functions; math.pi, math.sin(), math.cos(), math.tan(), math.atan(). These operate in radians, convert back and forth.
concepts: application of class, application of math, writing useful code, critical thinking, difference between setter functions and expression functions
