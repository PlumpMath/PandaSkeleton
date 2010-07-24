class Plugin():
	def startUp(self):
		return True
	# end startUp

	def preStep(self):
		return True
	# end preStep
		
	def postStep(self):
		return True
	# end postStep
		
	def step(self):
		return True
	# end step
		
	def shutDown(self):
		return True
	# end shutDown
# end Plugin