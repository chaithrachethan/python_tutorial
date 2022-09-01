name = "Sachin "
age = 40

sentence1 = "My name is "+ name +" my age is "+ str(age)
# sentence2 = "My name is {} my age is {}"

# print(sentence1)
# print(sentence2.format(name, str(age)))



#Uppercase, Lowercase
#name = "Sachin "

name = "123"
name = name.upper()
#name2 = sentence1.lower()
#name3 = sentence1.capitalize()


# print(name)
# print("my string contains only characters = " , name.isalpha())
# print("my string contains only numbers = " , name.isdecimal())
# print("my string contains both numbers and charecters = " , 
# 	name.isalnum())# is decimal or is alphabet

sentence1 = "28-08-2022 20:50"
date, time = sentence1.split()
print(sentence1.lstrip())
print( "2022" not in sentence1)
print(sentence1.find("2024"))
x = ["today", "is" , "a" , "good", "day"]
x_str = ' '.join(x)
#string to list ==> split()
#list to string ==> join










#x_str = "ABBAC"

RegisterNumber = '999999999'
print(RegisterNumber.zfill(5))














