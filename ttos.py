from gtts import gTTS
import os

print("choose your language")
print("1: for Hindi")
print("2: for English")
print("3: for Spanish")
l=int(input("Enter your choice :"))

if l == 1:
	tell = "hi"
	text = open("hindi.txt","r").read().replace("\n","")
elif l == 2:
	tell = "en"
	text = open("english.txt","r").read().replace("\n","")
elif l == 3:
	tell = "es"
	text = open("spanish.txt","r").read().replace("\n","")
else:
	print("Wrong input")
speech = gTTS(text = str(text), lang =tell, slow = False)
speech.save("voice.mp3")
os.system("play voice.mp3")
