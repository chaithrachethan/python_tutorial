#assignment
a = 10

#arithmatic
a = a+ 10
a = a- 10
a = a* 10
a = a/ 10
a = a// 10
a = a % 10
a = a ** 10

#comparisions
a = 10
b = 20
output = a > b
output = a >= b
output = a < b
output = a <= b
output = a == b
output = a != b


#logical
output =  a or b
		  # T    T   > T
		  # T    F   > T
		  # F    T   > T
		  # F    F   > F
output =  a and b
		  # T    T   > T
		  # T    F   > F
		  # F    T   > F
		  # F    F   > F

output =  not a
# is ==> Identity
# in ==> membership

#bitwise operators
a = a & b
a = a | b
a = a >> 3
a = a << 3
a = a ^ b
	# T    T   > F
	# F    T   > T
	# T    F   > T
	# F    F   > F
a = ~a