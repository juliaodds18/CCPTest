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

	# Check if point is within dist of rectangle's x-coordinates
	dist_left = Point(rect.bottom_left.x - dist, rect.bottom_left.y)
	dist_right = Point(rect.bottom_left.x + rect.width + dist, rect.bottom_left.y)

	if (point.x >= dist_left.x and point.x <= dist_right.x):
		# Point is definitely within the x-coordinate bound, need edge cases to check distance for corner points
		# First, check point outside left x-boundary 
		if (point.x <= rect.bottom_left.x): 
			# Need to find the point with the minimum and maximum y-values possible 
			# Using a variant of the formula to find distance between points: Sqrt((x2 - x1)^2 + (y2 - y1)^2)
			x_dist = rect.bottom_left.x - point.x 
			min_y = rect.bottom_left.y - math.sqrt(dist**2 - x_dist**2)
			max_y = rect.bottom_left.y + rect.height + math.sqrt(dist**2 - x_dist**2)
			
			if (point.y >= min_y and point.y <= max_y): 
				return True
			else:
				return False

		# Next, check point outside right x-boundary
		elif (point.x >= rect.bottom_left.x + rect.width):
			# Again, find points with maximum and minimum y-values possible
			x_dist = rect.bottom_left.x + rect.width + point.x
			min_y = rect.bottom_left.y - math.sqrt(x_dist**2 - dist**2)
			max_y = rect.bottom_left.y + rect.height + math.sqrt(x_dist**2 - dist**2)

			if (point.y >= min_y and point.y <= max_y): 
				return True
			else:
				return False

		# Lastly, check if the point is within x-boundaries
		else: 
			x_dist = rect.bottom_left.x + rect.width - point.x
			min_y = rect.bottom_left.y - dist
			max_y = rect.bottom_left.y + dist

			if (point.y >= min_y and point.y <= max_y): 
				return True
			else:
				return False	


rect = Rectangle(0.0, 0.0, 1.0, 1.0)
point = Point(1.7, -0.7)
print(is_point_within_dist_of_rect(rect, point, 1.0))

