import Game

class Plugin():
	def __init__(self):
		self._game = None
	# end __init__
	
	def setGame(self, game):
		# Check if it's an instance of Game
		if isinstance(game, Game.Game):
			self._game = game
		else:
			raise Exception, "Must be an instance of Game."
	# end setGame
	
	def game(self):
		'''
		I would normally check that the _game variable is an instance of Game()
		here but it would be unneccessary overhead 99.9999% of the time.
		'''
	
		return self._game
	#end game

	def startUp(self):
		# Optional plugin method
		return True
	# end startUp

	def preStep(self):
		# Optional plugin method
		return True
	# end preStep
		
	def postStep(self):
		# Optional plugin method
		return True
	# end postStep
		
	def step(self):
		# Optional plugin method
		return True
	# end step
		
	def shutDown(self):
		# Optional plugin method
		return True
	# end shutDown
# end Plugin