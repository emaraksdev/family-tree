# Individual Creation Object

class Individual:
	def __init__(self, name):
		self.name = name
		self.parents = []
		self.children = []

	def introduce(self):
		print(f"My name is {self.name}!")