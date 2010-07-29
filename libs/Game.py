import direct.directbase.DirectStart
from direct.showbase import DirectObject
import sys

import Plugin, Scene
 
class Game(DirectObject.DirectObject):
    def __init__(self):
    	self.VERSION = 'PandaSkeleton v0.0.1';
    
    	# Game states
    	self._quit = False
    	self._paused = False
    	
    	# Plugins
    	self._plugins = dict()
    	
    	# Scenes
    	self._scenes = list()
    	self._currentScene = None
    	
    	print self.VERSION
    # end __init__
    	
    def registerPlugin(self, name, plugin):
    	if isinstance(plugin, Plugin.Plugin):
    		plugin.setGame(self)
    		self._plugins[name] = plugin
    	else:
    		raise Exception, "Plugin must be an instance of Plugin class."
    #end registerPlugin
    
    def getPlugin(self, name):
    	return self._plugins[name]
    # end getPlugin
    
    def pushScene(self, scene):
    	if self._currentScene != None:
    		self._currentScene.hideScene()
    		self._scenes.append(self._currentScene)
    		
    	self._currentScene = scene
    	if self._currentScene.loadScene():
    		self._currentScene.showScene()
    # end pushScene
    
    def popScene(self):
    	if self._currentScene != None:
    		self._currentScene.hideScene()
    		self._currentScene.unloadScene()
    		self._currentScene = None
    		
    	if self._scenes.len() > 0:
    		self._currentScene = self._scenes.pop()
    		self._currentScene.showScene()
    # end popScene
    	
    def run(self):
    	'''Our main run loop.'''
    	self._startUp()
    
    	while(self._quit == False):
    		if(self._paused):
    			# TODO Call our pause handler?
    			print "Paused."
    		else:
    			self._preStep()
    			taskMgr.step()
    			self._postStep()
    			
    	self._shutDown()
    # end run
    
    def quit(self):
    	self._quit = True
    # end quit
    			
    def _startUp(self):
    	self._quit = False
    	
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
	    	plugin.shutDown()
	    
	    # exit the application
	    print "Goodbye!"
	    sys.exit()
	# end _shutDown
# end Game