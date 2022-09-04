
#print(student)
#print(list(student.items())[0])
#print(student["Gender"])
#print(student.get("Gender", "Male"))

#x , y,  z = student.values()
#print(y)
# student.update({"Batch2":2030})
# student["Gender"] = "Male"
# print(student)
# student.pop("Batch")
# student.popitem()
# print(student)


# x = [("Country", "India")]
# print(dict(x))



student = {
	"Name":{
			"First_Name":"Mahindra",
			"Last_Name":"Dhoni"
		},
	"Branch":"ECE",
	"Batch":2020
	}

college = {
	"College Name":"SIT",
	}


#print(student["Age"])
#print(student.get("Name", "Sachin"))
#print(len(student))

# student.update(college) 
# print(student)


# student.pop("Branch") 
# print(student)
# student.clear()
print(student["Name"]["First_Name"])











