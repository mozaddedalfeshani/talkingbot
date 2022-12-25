# import section
import pyttsx3

# A function for next work!


def talk(text):
    m = pyttsx3.init()
    m.say(text)
    m.runAndWait()
