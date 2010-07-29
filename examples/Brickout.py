# Import our application class
from libs.Game import Game
from libs.Plugins.Input import InputPlugin
from libs.Scenes.Empty import EmptyScene

# Instantiate and run the game
game = Game()
game.registerPlugin('input', InputPlugin())
game.pushScene(EmptyScene())

game.run()