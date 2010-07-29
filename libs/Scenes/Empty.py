from direct.gui.OnscreenText import OnscreenText
from ..Scene import Scene

class EmptyScene(Scene):
	def showScene(self):
		self.text = OnscreenText(text = 'Empty Scene', pos = (0, 0), scale = 0.2)

		return True
	# end showScene
	
	def hideScene(self):
		self.text.destroy()
	
		return True
	# end hideScene