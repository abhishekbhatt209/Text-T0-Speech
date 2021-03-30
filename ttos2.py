import pyttsx3
import os
file = open("english.txt","r").read().replace("\n","")
engine = pyttsx3.init()
engine.say(file)
engine.save_to_file(file,"voice.mp3")
os.system("play voice.mp3")


