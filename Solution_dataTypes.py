def data_type(x):
	"""Takes one input and returns a value in respect to data type of the input  """
	my_data_type =type(x)
	if my_data_type == str:
		return len(x)
	elif my_data_type ==bool:
		return x
	elif my_data_type ==int:
		if x > 100:
			return 'more to 100'
		elif x < 100:
			return 'less than 100'

		else:
			return 'equal than 100'

	elif my_data_type ==list:
		if len(X) > 2:
			return [2]
		else:
			return "None"
		
	else:
return 'no value'
