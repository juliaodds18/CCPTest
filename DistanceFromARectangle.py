class Point(object):
	def __init__(self, init_x=0.0, init_y=0.0):
		self.x = init_x
		self.y = init_y

class Rectangle(object):
	def __init__(self, bottom_left_x=0.0, bottom_left_y=0.0, init_width=0.0, init_height=0.0):
		self.bottom_left = Point(bottom_left_x, bottom_left_y)
		self.width = init_width
		self.height = init_height

def is_point_within_dist_of_rect(rect=Rectangle(), point=Point(), dist=0.0):
	# TO DO: implement
	# Return value should be True or False.
	
	# TO DO: Check if point falls within dist of rec 
	# First iteration: Check if point is within the area of rect 

	

	pass