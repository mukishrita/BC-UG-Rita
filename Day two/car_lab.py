class Car():
	
	car_type, car_name, car_model, car_wheels, car_doors, is_saloon, car_speed

	def __init__(self, *args):
		if len(args) => 1:
			self.car_type = args[0]
		if len(args) => 2:
			self.car_model = args[1]
		if len(args) => 3:
			self.car_model = args[2]

	def model(self, model):
		return self.car_model

	def type(self, type):
		return self.car_type

	def name(self, name):
		return self.car_name

	def is_saloon(self):
		return self.is_saloon

	def num_of_wheels(self):
		return self.car_wheels