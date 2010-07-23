import direct.directbase.DirectStart
from direct.showbase import DirectObject

import Plugin
 
class Game(DirectObject.DirectObject):
    def __init__(self):
    	self.quit = False
    	self.paused = False
    	
    	self._plugins = list()
    	
    def registerPlugin(self, plugin):
    	if isinstance(plugin, Plugin.Plugin):
    		self._plugins.append(plugin)
    	else:
    		raise Exception, "Plugin must be an instance of Plugin class."
    	
    def run(self):
    	'''Our main run loop.'''
    	while(self.quit == False):
    		if(self.paused):
    			# Call our pause handler
    			print "Paused."
    		else:
    			self.preStep()
    			taskMgr.step()
    			self.postStep()
    			
    def preStep(self):
    	'''Process pre-render tasks.'''
    	
    def postStep(self):
    	'''Process post-render tasks.'''