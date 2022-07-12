list_a = ["Safan", 21, "Engineer", 9.2,"Engineer"]

#list_a[2] = "Doctor"

print(list_a)

#list is an ordered collection different data type objects, 
# which can be mutable and can have duplicate values

# for xxxxxxxxxxxxx in list_a:
# 	print(xxxxxxxxxxxxx)

print(len(list_a))
print(list_a[4])
print(list_a[-2])
print(list_a[0:3])


list_a.append(30)
print(list_a)
list_a.pop()
print(list_a)
list_a.insert(2,"Hello")
print(list_a)
list_b = ["ok", "not ok"]
list_a =  list_a + list_b
print(list_a)
list_a.pop(2)
print(list_a)
del list_a[2]
print(list_a)
list_a.clear()
print(list_a)













