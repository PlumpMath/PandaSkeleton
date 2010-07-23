class Plugin():
	def preStep(self):
		return True
		
	def postStep(self):
		return True
		
	def step(self):
		raise Exception, "step() must be implemented in a Plugin class."