import math

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
	# First check if point is within the area of rect 
	ret_value = is_point_within_rectangle(rect, point)

	# If the point is not within the rect, then check if it falls within dist of rect
	if (ret_value == False):
		is_point_within_dist(rect, point, dist)
		
		
	return False 
	

def is_point_within_rectangle(rect, point): 
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


def is_point_within_dist(rect, point, dist):
	retVal = dist_between_points(point, Point(2.0, 2.0))
	print(retVal)



def dist_between_points(point1, point2): 
	# Formula: Sqrt((x2 - x1)^2 + (y2 - y1)^2)
	x_point = math.pow(point2.x - point1.x, 2)
	y_point = math.pow(point2.y - point1.y, 2)
	return math.sqrt(x_point + y_point)


rect = Rectangle(0.0, 0.0, 1.0, 1.0)
point = Point(2.0, 0.5)
is_point_within_dist_of_rect(rect, point)
