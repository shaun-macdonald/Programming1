#Ecersise 3.1


def right_justify(a):
	string = a
	length = len(string)
	total =' ' * (70 - length) + string
	print(total)
	print(len(total)) # print to check



right_justify("shaun")	