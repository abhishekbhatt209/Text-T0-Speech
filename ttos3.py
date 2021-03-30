import requests,os
from urllib.request import urlretrieve
import webbrowser
Speech = 'voice.mp3'
urlretrieve("http://api.voicerss.org/?key=c17efb821e2a4c4889353736d098ab03""&hl=en-us&c=wav&""src=thank+you+so+much ", Speech)
os.system("play voice.mp3")
