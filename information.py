from Speak import speak
import pywhatkit
from Listen import listen

query = listen().lower()


def searchGoogle(query):
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google","")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query, 1)
            speak("Boss. This is what i found on google.")

            speak(result)
        except:
            speak("Boss, it appears there is a problem. I will notify when i diagonise the system as soon as possible.")



searchGoogle(query)