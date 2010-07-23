# Load the config
from pandac.PandaModules import loadPrcFile 
loadPrcFile("appconfig.prc")

# Import our application class
from libs.Game import Game, Plugin
        
# Instantiate and run the game
game = Game()
game.registerPlugin(Plugin.Plugin())

game.run()