number_of_employees = int(input("Enter number of Employees!!\n"))
x = input("Enter Values\n")
x = x.split(' ')
start = input("Enter Starting Pos\n")
end = input("Enter Starting Pos\n")
output =[i for i in x if i>start and i < end]
print(output)