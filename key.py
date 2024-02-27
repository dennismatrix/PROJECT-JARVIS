from Speak import speak

import getpass
import hashlib


def encrypt_password(password):
    # Hash the password using MD5 (you can use a stronger hashing algorithm if needed)
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    return hashed_password

def save_encrypted_password(filename, encrypted_password):
    with open(filename, 'w') as file:
        file.write(encrypted_password)

def authentication(max_attempts=3):
    # Set your desired password
    password = "ACCESS"
    hashed_password = encrypt_password(password)

    attempts = 0
    while attempts < max_attempts:
        entered_password = getpass.getpass("Enter the password: ")

        # Hash the entered password
        hashed_entered_password = hashlib.md5(entered_password.encode()).hexdigest()

        # Compare the hashed entered password with the stored hashed password
        if hashed_entered_password == hashed_password:
            speak("Authentication was successful. Welcome, Mr. Dennis.")
            return True
        else:
            speak("Authentication failed. Please enter the correct password.")
            attempts += 1

    # After max_attempts unsuccessful attempts
    speak("Security concern detected. Initiating security protocol.")
    speak("I am calling Mr. Dennis and recording this security event.")
    speak("I am terminating the program immediately")
    exit()

    
    