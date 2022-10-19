import math
from re import S
class Vector:
	def __init__(self,scalar,angle):
		self.scalar=scalar
		self.angle=angle
	def set_scalar(self,newscalar):
		self.scalar=newscalar
	def set_angle(self,newangle):
		self.angle=newangle
	def get_angle(self):
		return self.angle
	def get_scalar(self):
		return self.scalar
	def get_dx(self):
		return round(self.scalar * math.cos(self.angle* math.pi/180),5)
	def get_dy(self):
		return round(self.scalar * math.sin(self.angle * math.pi/180),5)
	def strip_x(self):
		return Vector(self.get_dx(),0)
	def strip_y(self):
		return Vector(self.get_dy(),90)
	def add_with(self,another) -> None:
		x=self.get_dx()+another.get_dx()
		y=self.get_dy()+another.get_dy()
		s=math.sqrt(x**2+y**2)
		theta=math.atan2(y,x) * 180/math.pi
		self.scalar=round(s,5)
		self.angle=round(theta,5)
	def subtract_with(self,another) -> None:
		x=self.get_dx()-another.get_dx()
		y=self.get_dy()-another.get_dy()
		s=math.sqrt(x**2+y**2)
		theta=math.atan2(y,x) * 180/math.pi
		self.scalar=round(s,5)
		self.angle=round(theta,5)
	def plus(self,another):
		copy = self
		copy.add_with(another)
		return copy
	def minus(self,another):
		copy = self
		copy.subtract_with(another)
		return copy 
