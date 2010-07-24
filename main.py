# Load the config
from pandac.PandaModules import loadPrcFile 
loadPrcFile("appconfig.prc")

# Import our application class
from libs.Game import Game
from libs.Input import Input
        
# Instantiate and run the game
game = Game()
game.registerPlugin('input', Input())

game.run()