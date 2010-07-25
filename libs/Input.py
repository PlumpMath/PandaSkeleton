from direct.showbase.DirectObject import DirectObject
import Plugin

class Input(Plugin.Plugin, DirectObject):
	def startUp(self):
		# Disable default input
		base.disableMouse()
		
		# accept the following input
		self.accept("escape", self.quit)
		
		return True
	# end startUp
	
	def quit(self):
		self.game().quit()
	# end quit
# end Input