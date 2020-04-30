#Python 2.x program to transcribe an Audio file 
import speech_recognition as sr 

A = ("example.wav") 

# use the audio file as the audio source 

r = sr.Recognizer() 

with sr.AudioFile(A) as source: 
	#reads the audio file. Here we use record instead of 
	#listen 
	audio = r.record(source) 

try: 
	print("The audio file contains: " + r.recognize_google(audio,language="ru-RU")) 

except sr.UnknownValueError: 
	print("Google Speech Recognition could not understand audio") 

except sr.RequestError as e: 
	print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
