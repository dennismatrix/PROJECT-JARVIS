
import nltk
nltk.download('punkt')

import numpy as np
import json
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from NeuralNetwork import bag_of_words, tokenize, stem
from Brain import NeuralNet

# Load your intents.json and define ignore_words
with open('intents.json', 'r') as f:

    intents = json.load(f)

ignore_words = [',', '?', '/', '-', '!']

# Process intents and create xy, all_words, and tags
all_words = []
tags = []
xy = []

for intent in intents['intents']:
    tag = intent['tags']
    tags.append(tag)

    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))

all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))
tags = sorted(set(tags))

# Process xy to create x_train and y_train
x_train = []
y_train = []

for (pattern_sentence, tag) in xy:
    bag = bag_of_words(pattern_sentence, all_words)
    x_train.append(bag)

    label = tags.index(tag)
    y_train.append(label)

x_train = np.array(x_train)
y_train = np.array(y_train)

# Define hyperparameters and model architecture
num_epochs = 2500
batch_size = 10
learning_rate = 0.003
input_size = len(x_train[0])
hidden_size = 64  # Increase hidden layer size
output_size = len(tags)

# Create a DataLoader
class ChatDataset(Dataset):
    def __init__(self, x, y):
        self.n_samples = len(x)
        self.x_data = x
        self.y_data = y

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.n_samples

dataset = ChatDataset(x_train, y_train)
train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=0)

# Initialize model, loss function, and optimizer
device = torch.device('cpu')

model = NeuralNet(input_size, hidden_size, output_size).to(device=device)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# Training loop
print("Training in progress sir!......")
for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(dtype=torch.long).to(device)
        outputs = model(words)
        loss = criterion(outputs, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], loss: {loss.item():.4f}')

print(f"Final loss: {loss.item():.4f}")

data = {
    "model_state":model.state_dict(),
    "input_size":input_size,
    "hidden_size":hidden_size,
    "output_size":output_size,
    "all_words":all_words,
    "tags":tags
}
FILE = "TrainData.pth"
torch.save(data,FILE)
print(f"Sir, I just completed updating our database, Data saved to {FILE}")

