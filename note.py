from Speak import speak
import time
import subprocess
from Listen import listen
def note():
    # Speak instructions to the user
    speak("I will record a note for you. Please start speaking, and I will save the note silently. When you're done, just pause, and I'll let you know the note has been recorded.")

    # Listen for the user's note
    note_content = ""
    while True:
        user_input = listen()

        # Check for a pause or a stop command
        if not user_input.strip():
            break

        note_content += user_input + " "

    # Save the note content to a file
    with open("note.txt", "w") as file:
        file.write(note_content)

    # Open Notepad to silently save the note
    subprocess.Popen(["notepad.exe", "note.txt"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

    # Wait for a moment before notifying the user
    time.sleep(2)

    # Speak confirmation
    speak("Note recorded. You can access it later.")

note()