def operate(power):
	return lambda number : number ** power

cube    = operate(3)
sqluare = operate(2)


print(cube(20))