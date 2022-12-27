# import section
import pyttsx3
import speech_recognition as sr


# A function for next work!


def talk(text):
    m = pyttsx3.init()
    m.say(text)
    m.runAndWait()


listener = sr.Recognizer()
while True:

    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)

            command = listener.recognize_google(voice)

            print(command)
            talk(command)

    except:
        talk('please say something! ')
