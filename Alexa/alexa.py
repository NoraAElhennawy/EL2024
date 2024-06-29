# Python program to translate
# speech to text and text to speech

import os
import speech_recognition as sr
import pyttsx3 
#from gtts import gTTS
#import vlc
import time

# Initialize the recognizer 
r = sr.Recognizer() 

# Function to convert text to
# speech
def change_voice(engine, gender):
    for voice in engine.getProperty('voices'):
        if gender == voice.gender:
            engine.setProperty('voice', voice.id)
            return True
def SpeakText(command):
	
	# Initialize the engine
    #tts = gTTS(command,lang='ar')
    #tts.save('hello.mp3')
    #record=vlc.MediaPlayer('hello.mp3')
    #record.play()
    #time.sleep(5)
	engine = pyttsx3.init()
	#voice_status=change_voice(engine,'VoiceGenderFemale')
	#print(voice_status)
	
	engine.setProperty('rate', 110)
	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[1].id)
	engine.say(command) 
	engine.runAndWait()

def ProcessText(command):
	if(command=="alexa"):
		SpeakText("AsslamAlykom How can i help you")
	elif(command==("vs code")):
		SpeakText("opening VS code")	
		os.system("code &")
	elif((command==("exit"))or(command=="shutdown")):
		SpeakText("GoodBye")
		exit()
	else:
		SpeakText("Sorry did not understand your command")	
# Loop infinitely for user to
# speak

while(1): 
	
	# Exception handling to handle
	# exceptions at the runtime
	try:
		
		# use the microphone as source for input.
		with sr.Microphone() as source2:
			
			# wait for a second to let the recognizer
			# adjust the energy threshold based on
			# the surrounding noise level 
			r.adjust_for_ambient_noise(source2, duration=0.2)
			
			#listens for the user's input 
			audio2 = r.listen(source2)
			
			# Using google to recognize audio
#			MyText = r.recognize_google(audio2,language='ar-EGY')
			MyText = r.recognize_google(audio2)
			MyText = MyText.lower()

			print("Did you say ",MyText)
#			SpeakText("مرحبا نورا كيف يمكن أن أساعدك")
			
			ProcessText(MyText)
			
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	except sr.UnknownValueError:
		print("unknown error occurred")
