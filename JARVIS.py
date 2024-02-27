from Speak import speak
from key import authentication
import random
import json
from GreetMe import greet
from Task import InputExecution, NonInputExecution
from Listen import listen
from Brain import NeuralNet
from NeuralNetwork import bag_of_words, tokenize
import torch

# _____________________________________________JARVIS AI_______________________________________

name = "JARVIS"





device = torch.device('cpu')

try:
    with open(r"D:\project prime-20240122T115552Z-001\project prime\intents.json", 'r') as json_data:
        intents = json.load(json_data)
except Exception as e:
    print(f"Error loading intents: {e}")
    intents = {}

greet()
FILE = r'D:\project prime-20240122T115552Z-001\project prime\TrainData.pth'

try:
    data = torch.load(FILE)
except Exception as e:
    print(f"Error loading model data: {e}")
    data = {}

if not all(key in data for key in ["input_size", "hidden_size", "output_size", "all_words", "tags", "model_state"]):
    print("Incomplete data loaded from the model file.")

input_size = data.get("input_size", 0)
hidden_size = data.get("hidden_size", 0)
output_size = data.get("output_size", 0)
all_words = data.get("all_words", [])
tags = data.get("tags", [])
model_state = data.get("model_state", {})

model = NeuralNet(input_size, hidden_size, output_size).to(device)

try:
    model.load_state_dict(model_state)
except Exception as e:
    print(f"Error loading model state: {e}")

def main():
    while True:
        sentence = listen()

        sentence = tokenize(sentence)
        x = bag_of_words(sentence, all_words)
        x = x.reshape(1, x.shape[0])
        x = torch.from_numpy(x).to(device)

        output = model(x)

        _, predicted = torch.max(output, dim=1)

        if 0 <= predicted.item() < len(tags):
            tag = tags[predicted.item()]
        else:
            print(f"Error: Predicted item index {predicted.item()} is out of bounds.")
            continue

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        if prob.item() > 0.8:
            for intent in intents['intents']:
                if tag == intent['tags']:
                    reply = random.choice(intent["responses"])

                    if "time" in reply:
                        NonInputExecution(reply)

                    elif "date" in reply:
                        NonInputExecution(reply)

                    elif "meet my friend" in reply:
                        NonInputExecution(reply)    

                    elif "day" in reply:
                        NonInputExecution(reply)

                    elif "google" in reply:
                        speak("Just a moment boss")
                        from information import searchGoogle
                        searchGoogle(reply)


                    elif "wikipedia" in reply:
                        InputExecution(tag, reply)
                    else:
                        speak(reply)

if __name__ == "__main__":
    authentication()
    main()
