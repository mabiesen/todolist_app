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

	while rowctr < numrows:

		while colctr < numcols:
			item = initialarray(masterctr)
			# Now on each iteration, we append accordingly
			masterarray[rowctr].append(item)
			colctr = colctr + 1
			masterctr = masterctr + 1
		colctr = 0
		rowctr = rowctr + 1

	return masterarray
