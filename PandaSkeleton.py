import sys

# Load the config
from pandac.PandaModules import loadPrcFile 
loadPrcFile("appconfig.prc")

appName = sys.argv[1]
app = __import__('examples.' + appName)