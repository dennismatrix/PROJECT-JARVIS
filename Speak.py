# this is a speak module

import pyttsx3

engine = pyttsx3.init("sapi5")

voices  = engine.getProperty("voices")

engine.setProperty("voices",voices[2].id)

engine.setProperty("rate",210)

engine.setProperty("volume",200)

def speak(Text):
    print(f"J.A.R.V.I.S: {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print(" ")

