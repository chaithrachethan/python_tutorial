class Vehicle:
	drive = True
	def __init__(self, w, s, x, u, t, r):
		self.wheels = w
		self.seat = 200

	def prints(self):
		self.road = 40
		print(self.road, self.wheels, self.seat)

	def something(self):
		print("ok", self.road)


Car = Vehicle(20, 4,0,0,0,0)
Car.road = 100
Car.prints()