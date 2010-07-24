import direct.directbase.DirectStart
from direct.showbase import DirectObject

import Plugin
 
class Game(DirectObject.DirectObject):
    def __init__(self):
    	self.quit = False
    	self.paused = False
    	
    	self._plugins = dict()
    # end __init__
    	
    def registerPlugin(self, name, plugin):
    	if isinstance(plugin, Plugin.Plugin):
    		self._plugins[name] = plugin
    	else:
    		raise Exception, "Plugin must be an instance of Plugin class."
    #end registerPlugin
    
    def getPlugin(self, name)
    	return self._plugins[name]
    # end getPlugin
    	
    def run(self):
    	'''Our main run loop.'''
    	self._startUp()
    
    	while(self.quit == False):
    		if(self.paused):
    			# Call our pause handler
    			print "Paused."
    		else:
    			self._preStep()
    			taskMgr.step()
    			self._postStep()
    			
    	self._shutDown()
    # end run
    			
    def _startUp(self):
    	for name, plugin in self._plugins.iteritems():
    		plugin.startUp()
    # end _startUp
    
    def _preStep(self):
    	'''Process pre-render tasks.'''
    	for name, plugin in self._plugins.iteritems():
	    	plugin.preStep()
    # end _preStep
    	
    def _postStep(self):
    	'''Process post-render tasks.'''
    	for name, plugin in self._plugins.iteritems():
	    	plugin.postStep()
    # end _postStep	
    
    def _shutDown(self):
	    for name, plugin in self._plugins.iteritems():
	    	plugin.startUp()
	# end _shutDown
# end Game