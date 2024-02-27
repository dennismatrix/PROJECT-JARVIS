import wikipedia
import logging
from Speak import speak
def WikipediaSearch(query, num_sentences=3, language='en'):
    try:
        # Set the language for the Wikipedia search
        wikipedia.set_lang(language)

        # Attempt to fetch information
        result = wikipedia.summary(query, sentences=num_sentences)
        page_url = wikipedia.page(query).url

        # Log the successful search
        logging.info(f"Successful Wikipedia search for '{query}' in {language}.")

        # Speak the information to the user
        speak(f"Sure, Boss. Here's some information about {query}: {result}")
        speak(f"For more details, you can visit {page_url}")

    except wikipedia.exceptions.DisambiguationError as e:
        # Handle disambiguation by asking the user for clarification
        options = e.options[:3]
        speak(f"Boss, there are multiple results for {query}. Did you mean {', '.join(options)} or something else?")

    except wikipedia.exceptions.PageError:
        # Handle page not found error
        speak(f"Sorry, Boss, I couldn't find any information on {query}. Make sure the topic is spelled correctly.")

    except Exception as ex:
        # Log the error for debugging purposes
        logging.error(f"Error in Wikipedia search for '{query}': {ex}")

        # Speak a generic error message to the user
        speak(f"Sorry, Boss, there was an error while searching on Wikipedia. Please try again later.")

# Usage Example:
WikipediaSearch("Artificial intelligence", num_sentences=5, language='en')
