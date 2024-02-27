import speech_recognition as sr

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening... (Speak now)")
        r.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = r.listen(source, timeout=4, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            print("No speech detected. Please try again.")
            return "None"

    try:
        print("Processing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "None"
    except Exception as e:
        print(f"Error during speech recognition: {e}")
        return "None"

    return query
