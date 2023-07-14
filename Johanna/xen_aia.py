import speech_recognition as sr
import pyttsx3
import os
import time

from dotenv import load_dotenv
load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_KEY')

import openai
openai.api_key = OPENAI_KEY

# Function to convert Text to Speech
def SpeakText(command):
    # Initialize the Engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    female_voices = [v for v in voices if v.gender == 'female']
    if female_voices:
        engine.setProperty('voice', female_voices[0].id)
    engine.say(command)
    engine.runAndWait()

# Initialize the Recognizer
r = sr.Recognizer()

def record_text():
    # Loop in case of Errors
    while True:
        try:
            # Microphone is Source of Input
            with sr.Microphone() as source2:
                # Prep Recognizer to receive
                r.adjust_for_ambient_noise(source2, duration=0.1)
                print("Staging For Active Listening")

                # Listens For Users Input - Voice
                audio2 = r.listen(source2)

                # Using Google (Page-Break-Algorithm) to Recognize the Voice
                MyText = r.recognize_google(audio2)

                return MyText

        except sr.RequestError as e:
            print("Could not compute the request result: {0}".format(e))

        except sr.UnknownValueError:
            print("Unknown Quantum Error Occurred")

def send_to_openAI(messages, model="gpt-3.5-turbo"):
    try:
        start_time = time.time()
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        elapsed_time = time.time() - start_time

        message = response.choices[0].message.content
        messages.append(response.choices[0].message)
        return message, elapsed_time

    except openai.OpenAIError as e:
        print("OpenAI API Error:", e)

    except openai.RateLimitError as e:
        print("OpenAI API Rate Limit Error:", e)

    except openai.AuthenticationError as e:
        print("OpenAI API Authentication Error:", e)

    except openai.APIConnectionError as e:
        print("OpenAI API Connection Error:", e)

    except Exception as e:
        print("An error occurred during API request:", e)

messages = []
while True:
    try:
        text = record_text()
        messages.append({"role": "user", "content": text})
        response, elapsed_time = send_to_openAI(messages)
        print(response)  # Print the response
        SpeakText(response)

        # Check the elapsed time and wait if necessary
        remaining_time = max(0, 5 - elapsed_time)
        time.sleep(remaining_time)

    except Exception as e:
        print("An error occurred:", e)
