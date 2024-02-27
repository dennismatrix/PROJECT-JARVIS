import speech_recognition as sr
import pyttsx3
import requests

def listen():
    """Listens for user input and returns the transcribed text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Adjust for ambient noise
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

def speak(text):
    """Speaks the given text aloud."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def googlesearch(query):
    """Performs a Google search for the given query and speaks the top result."""
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url)

    # Extract the top result snippet
    try:
        results = response.json()
        top_result = results["organic_results"][0]["snippet"]
        speak(f"Here's what I found on the web: {top_result}")
    except:
        speak("Sorry, I couldn't retrieve any results from Google.")

if __name__ == "__main__":
    while True:
        query = listen()
        if query:
            googlesearch(query)
