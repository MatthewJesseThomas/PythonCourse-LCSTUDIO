import speech_recognition as sr
import pyttsx3
import os

from dotenv import load_dotenv
load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_KEY')

import openai
openai.api_key = OPENAI_KEY


# Function to convert Text to Speech
def SpeakText(command):
    
    # Initialize the Engine
    engine = pyttsx3.init()  # Initialize Engine
    engine.say(command)  # Text to be Spoken
    engine.runAndWait()  # Run then Speak


# Initialize the Recognizer
r = sr.Recognizer()


def record_text():
    # Loop in case of Errors
    while(1):
        try:
            # Microphone is Source of Input
            with sr.Microphone() as source2:
                
                # Prep Recognizer to receive
                r.adjust_for_ambient_noise(source2, duration=0.2)
                
                print("Staging For Active Listening")
                
                # Listens For Users Input - Voice
                audio2 = r.listen(source2)
                
                # Using Google(Page-Break-Algorithm) to Recognize the Voice
                MyText = r.recognize_google(audio2)
                
                return MyText
            
        except sr.RequestError as e:
            
            print("Could not Compute The Request Result; {0}".format(e))
            
        except sr.UnknownValueError:
            
            print("Unknown Quantum Error Occured")

            
def send_to_openAI(messages, model="gpt-3.5-turbo"):
    
    response = openai.ChatCompletion.create(
        # Variables for Model
        model=model,
        messages=messages,  # The Array of Messages
        max_tokens=100,  # How long the message should be(Upper-Bound)
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].message.content
    messages.append(response.choices[0].message)
    return message


messages = []
while(1):
    text = record_text()
    messages.append({"role": "user", "content": text})
    response = send_to_openAI(messages)
    SpeakText(response)

print(response)