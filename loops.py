# Loops can be applied on sequences
# string, set, list, touple, dictionary and range

sentence = "today is a good day"

#for loop

# for index, charecter in enumerate(sentence.split(' ')):
# 	print('At index {} we have value {}'.format(index, charecter))


# student = {
# 	"Name": "Safan",
# 	"Branch":"EEE",
# 	"Batch":2020
# }

# for key, value in student.items():
# 	print(student.get(key))

# print(student.values())

# for i in range(1,10):
# 	print(i)


output = [i for i in range(1,10) if i%2==0]
print(output)


output2 = ["even" if i%2==0 else "odd" for i in range(1,10)]
print(output2)

x = 200
while (x>10):
	print(x)
	x -= 50

