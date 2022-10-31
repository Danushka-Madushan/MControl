class Validate():
	def __init__(self, uuid):
		self.uuid = uuid
		self.id = "123456789"

	def check(self):
		if self.uuid == self.id:
			return True
