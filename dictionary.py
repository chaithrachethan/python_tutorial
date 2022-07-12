student = {
	"Name":"Safwan",
	"Branch":"ECE",
	"Batch":2020
}


#print(student)
#print(list(student.items())[0])
#print(student["Gender"])
#print(student.get("Gender", "Male"))

#x , y,  z = student.values()
#print(y)

student.update({"Batch2":2030})
student["Gender"] = "Male"
print(student)
student.pop("Batch")
student.popitem()
print(student)


x = [("Country", "India")]
print(dict(x))
