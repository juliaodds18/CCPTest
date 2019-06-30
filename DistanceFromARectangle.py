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

	# Find the location of the bottom right point 
	bottom_right = Point(rect.bottom_left.x + rect.width, rect.bottom_left.y)
	# Find the location of the top left point 
	top_left = Point(rect.bottom_left.x, rect.bottom_left.y + rect.height)

	
	# Check if the point falls within the rectangle's x-scale
	if (point.x >= rect.bottom_left.x and point.x <= bottom_right.x):
		# Check if the point falls within the rectangle's y-scale
		if (point.y >= rect.bottom_left.y and point.y <= top_left.y):
			# The point falls within the area of the rectangle, return true
			return True	
	

	return False



rect = Rectangle(0.0, 0.0, 1.0, 1.0)
point = Point(1.0, 1.0)
is_point_within_dist_of_rect(rect, point)
