class Vehicle:
	drive = True
	def __init__(self, wheels, seat):
		self.wheels = wheels
		self.seat = seat

	def prints(self):
		print(self.wheels)
		print(self.seat)

	def something():
		print("ok")



Car = Vehicle(4, 5)
Bus = Vehicle(6, 20)
Bycycle = Vehicle(2, 1)

Car.wheels = 20
# Car.prints()
# Instantiation
# Car is a Instance of Vehicle

Vehicle.something()





