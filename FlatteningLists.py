# TODO: Write a function to flatten nested lists of arbitrary depth 
# Write a recursive function that accepts a list

def flatten_lists(input_list=[]):
	for sublist in input_list: 
		# If the type of the sublist is a list, then call the function again recursively
		if type(sublist) == list:
			flatten_lists(sublist)
		# If the type is not a list, it is an item that should be appended to the final list
		else:
			final_list.append(sublist)


# Test cases
final_list = []
flatten_lists([1, 2, 3, 4, 5])
print(final_list)


final_list = []
flatten_lists([1, [2,3,4, [5,6], [7,8]]])
print(final_list)

final_list = []
flatten_lists([])
print(final_list)

final_list = []
flatten_lists([1, [2,3,4, [5,6], [7,8], 9, [10, [11, 12], 13]]])
print(final_list)

final_list = []
flatten_lists(['item1', 'item2', ['item3', ['item4'], 'item5']])
print(final_list)
