import datetime
import wikipedia
import webbrowser
import json
import os
from Speak import speak
from Listen import listen
from NeuralNetwork import tokenize

MEMORY_FILE = "memory.json"

# Check if the memory file exists and contains data
if os.path.exists(MEMORY_FILE) and os.path.getsize(MEMORY_FILE) > 0:
    # Load existing memory
    with open(MEMORY_FILE, 'r') as file:
        memory = json.load(file)
else:
    # Initialize an empty memory dictionary
    memory = {}


def update_memory(name):
    # Add the introduced friend to memory
    memory[name.lower()] = {"name": name}

    # Save the updated memory to a file
    with open(MEMORY_FILE, 'w') as file:
        json.dump(memory, file)


def introduce_friend(friend_name):
    speak(f"Nice to meet you {friend_name}! I'll remember you.")
    speak("Is is there anything i can help you with?")
    update_memory(friend_name)


def get_time():
    current_time = datetime.datetime.now().strftime("%H:%M")
    speak(f"The current time is {current_time}")


def get_date():
    current_date = datetime.date.today().strftime("%B %d, %Y")
    speak(f"Today's date is {current_date}")


def get_day():
    current_day = datetime.datetime.now().strftime("%A")
    speak(f"Today is {current_day}")


def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=3)
        page_url = wikipedia.page(query).url
        speak(f"Here's some information about {query}: {result}")
        speak(f"For more details, you can visit {page_url}")
    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options[:3]  # Display the first three options in case of disambiguation
        speak(f"There are multiple results for {query}. Did you mean {', '.join(options)} or something else?")
    except wikipedia.exceptions.PageError:
        speak(f"Sorry, I couldn't find any information on {query}.")
    except Exception as ex:
        speak(f"There was an error while searching on Wikipedia: {ex}")


def search_google(query):
    try:
        speak("Searching Google for information.")
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open(search_url)
    except Exception as e:
        speak(f"There was an error while searching on Google: {e}")


def NonInputExecution(query):
    if "time" in query.lower():
        get_time()
    elif "date" in query.lower():
        get_date()
    elif "day" in query.lower():
        get_day()
    elif "meet my friend" in query.lower():
        friend_name = listen().lower().replace("meet my friend", "").strip()
        introduce_friend(friend_name)


def InputExecution(tag, query):
    if "wikipedia" in tag.lower():
        topic = query.lower().replace("wikipedia", "").strip()
        search_wikipedia(topic)
    elif "google" in tag.lower():
        search_query = query.replace("google", "").strip()
        search_google(search_query)
