# Text-T0-Speech
 3 ways to convert text to speech in Python with screenshots of the steps-output
AIM: Explain any 3 ways to convert text to speech in Python with screenshots of the steps-output
-------------------------------------------------------------------------------------------------------
1) Please refer ttos.py

With the use of gTTS we make Text to speech convertor

For this first make sure that you have installed python3 
Then we need to install gTTS
Run the command #pip install gTTS

The other requirement for run the speech is OS
So install OS module which interacting with operating system
Run the command # pip install os-win

Run the command # pip install os-sys

After that we need to start any editor for code, here I use gedit because I use linux and it is comfortable for me.

I give my python file name as ttos, where .py means it is a python file.

Now let’s start the coding part.
First import the module which we used before in the code.

I make an if else loop/Switch case for, in which language I want to get speech.



Here, I make a user choice option which helps users choose the language I already make 3 different files which this code fetch and read that, with the use of replace() it makes in tokens. Tell is the variable for language and text is the variable for file.



I take speech as a variable and pass the text file and language to the engine, here I make it slow = false, which tells the module to convert audio should have high speed.

Then by speech i just save it in a file which is voice.mp3

After that by inbuilt command (“Play”) i just play it, where I use os.system for using linux command in python.
(NOTE: First I install the mp3 player in my system, for use that mp3 player I have to type command (#play <filename.mp3>))
I install this on my linux. If you are a windows user then you can you (“start”) instead of play.

----------------------------------------------------------------------------------------------------------------------------------
2) Please refer ttos2.py



With the use of pyttsx3 we make Text to speech convertor

First we have to install pyttsx3 
Run command #pip install pyttsx3

We already downloaded the OS module so let’s start Coding part.
First import the module which we used before in the code.

Now, we have a english.txt file, so let’s code for read that file and convert it into tokens.

Then we initialize the Text-to-speech engine.

To convert Text into speech.

First we have to save that file in .mp3 format and play it by inbuilt linux command.

------------------------------------------------------------------------------------------------------------

3) Please refer ttos3.py

With the use of API we make Text to speech convertor
First get a API Key for text to speech from any resource, I my case I get my free API for Text To Speech from http://www.voicerss.org/api/
Then we need to install packages
Run command #pip install urllib3

Run command #pip install requests 

We already downloaded the OS module, and we use a webbrowser module. We already have this module so we need to install it. Let's start Coding part.

We use requests module for get/post the request. Then we use module urllib for open or download a file over HTTP. we have to pass two arguments to the urlretrieve method, first argument is the URL of the resource that you want to retrieve, and second argument is the local file. In last we use Webbrowser module for high-level interface to allow displaying web-based documents.

We are using speech variable to store and give speech in .mp3 
Then we use urlreteriere that help to retrieve the URL.
In that I put my API link accordingly, which my API website already given to me and parameters you can find from http://www.voicerss.org/api/.
(NOTE: if you use other website for API you will get different parame-
 
---------------------------------------------------------------------------------------------------------------------------
You can use my text file to verify the code. Please put all the thing in same file
 
 
 

