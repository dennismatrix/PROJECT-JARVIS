import datetime
import wikipedia
import webbrowser
from Speak import speak

def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    speak(f"The time is {time}")

def Date():
    date = datetime.date.today()
    speak(f"Today is {date}")
    
def Day():
    day = datetime.datetime.now().strftime("%A")
    speak(f"Sir, today is on {day} ")

def WikipediaSearch(query):
    try:
        result = wikipedia.summary(query, sentences=3)
        page_url = wikipedia.page(query).url
        speak(f"Sure, Boss. Here's some information about {query}: {result}")
        speak(f"For more details, you can visit {page_url}")

    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options[:3]  # Display the first three options in case of disambiguation
        speak(f"Boss, there are multiple results for {query}. Did you mean {', '.join(options)} or something else?")

    except wikipedia.exceptions.PageError:
        speak(f"Sorry, Boss, I couldn't find any information on {query}. Make sure the topic is spelled correctly.")

    except Exception as ex:
        speak(f"Sorry, Boss, there was an error while searching on Wikipedia. {ex}")

def GoogleSearch(query):
    try:
        speak("Searching Google for information.")
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open(search_url)
    except Exception as e:
        speak(f"Sorry, Boss, there was an error while searching on Google. {e}")

def NonInputExecution(query):
    query = str(query)

    if "time" in query.lower():
        Time()

    elif "date" in query.lower():
        Date()

    elif "day" in query.lower():
        Day()


def InputExecution(tag, query):
    if "wikipedia" in tag.lower():
        # Extract the topic for Wikipedia search
        name = query.lower().replace("wikipedia", "").strip()
        WikipediaSearch(name)

    elif "google" in query.lower():
        search_query = query.replace("google", "").strip()
        GoogleSearch(search_query)


