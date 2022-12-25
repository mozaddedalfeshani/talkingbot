import pyttsx3


def talk(text):
    m = pyttsx3.init()
    m.say(text)
    m.runAndWait()
