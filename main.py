# import section
import pyttsx3
import speech_recognition as sr
import pywhatkit
import wikipedia


def wiki(command):
    command = wikipedia.summary(command, sentences=2)
    talk(command)


# A function for next work!
def talk(text):
    m = pyttsx3.init()
    m.say(text)
    m.runAndWait()


listener = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source)

        command = listener.recognize_google(voice)
        if 'play' in command:
            command = command.replace('play', '')
            print('opening youtube and play ' + command)
            pywhatkit.playonyt(command)
        elif 'tell' in command:
            print('telling about ' + command)
            command = command.replace('tell', '')
            wiki(command)


except:
    talk('please say something!')
