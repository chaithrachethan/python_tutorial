def greetings(fn, mn="0000", ln="ok"):	#defajult parameter passing	
    print("Hello {} {} {}".format(fn, mn, ln))


# 1. def <function_name>():
# 2. def <function_name>(argument):
# 3. def <function_name>(argument_name=<value>): #default parameter passing
# function_name(argument_name=<value>)
# 4. if u have multiple parmeters, 
# 	if one argument has default value, 
# 	rest all should have default vaues


# def find_greatest_of_3(a,b,c):
# 	if a > b and a > c:
# 	    print("A {} is greatest".format(a))
# 	elif b > a and b > c:
# 	    print("B {} is greatest".format(b))
# 	else:
# 	    print("C {} is greatest".format(c))


# find_greatest_of_3(10, 20, 30)
# find_greatest_of_3(100, 20, 30)
# find_greatest_of_3(100, 20, 300)


def add(a, b):
	sum_of_numbers = a + b
	return a, 100, sum_of_numbers

inp1, inp2, ouput = add(10, 20)


print(inp1, inp2, ouput)