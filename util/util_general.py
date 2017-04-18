# Convert string to list of items
def colon_string_to_list(myinput):
	input_split = myinput.split(":")
	return input_split

# Convert 1d array to 2d array
def one_to_twod_array(initialarray, numcols, numrows):
	colctr = 0
	rowctr = 0
	actr = 0
	masterctr = 0

	# Create a list.
	masterarray = []

	# Append empty lists for the number of rows
	while actr < numrows:
		masterarray.append([])
		actr = actr + 1

	# Iterate number of rows and columns provided in args
	while rowctr < numrows:
		while colctr < numcols:
			item = initialarray[masterctr]
			# Now on each iteration, we append to each row
			masterarray[rowctr].append(item)
			colctr = colctr + 1
			masterctr = masterctr + 1
		colctr = 0
		rowctr = rowctr + 1
	return masterarray

##array test data
##myarray = [1,2,3,4,5,6,7,8,9]
##newarray = one_to_twod_array(myarray, 3,3)
##
##print(newarray[1][0])
