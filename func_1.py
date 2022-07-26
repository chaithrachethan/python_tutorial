# x = 10
# def print1():
# 	print(1)

# y = 30
# def print2():
# 	print(2)

# def print3():
# 	print(3)

def print4(n):
	for i in range(n):
		if i < 2:
			print(i)
	else:
		print("Out of range")

print4(2)