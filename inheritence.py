class Parent:
	drive = True
	def __init__(self, Car, House):
		self.House = House
		self.Car = Car
		self.Villa = 20

	def prints(self):
		print("House: "+str(self.House), "Car: "+str(self.Car))


class Child(Parent):
	def __init__(self, Car, House, Bike):
		super().__init__(Car, House)

	def prints(self):
		print("Hello")

	def printout(self):
		super().prints()

Child1 = Child(1,2,3)
Child1.printout()
