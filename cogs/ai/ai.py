import random

import nltk
import json
import os
import pandas
from keras.layers import Input, Embedding, LSTM, Dense, Flatten
from keras.models import Model
from keras_preprocessing.sequence import pad_sequences
from keras_preprocessing.text import Tokenizer
from sklearn.preprocessing import LabelEncoder

nltk.download('punkt')

with open(os.getcwd() + "/cogs/ai/intents.json") as file:
    data = json.load(file)

tags = []
patterns = []
responses = {}

for intent in data["intents"]:
    responses[intent['tag']] = intent['responses']
    for lines in intent["patterns"]:
        patterns.append(lines.lower())
        tags.append(intent['tag'])

data = pandas.DataFrame({"patterns": patterns, "tags": tags})

# Tokenizing the data
tokenizer = Tokenizer(num_words=2000)
tokenizer.fit_on_texts(data['patterns'])
train = tokenizer.texts_to_sequences(data['patterns'])
x_train = pad_sequences(train)

# Encode the outputs
label_encoder = LabelEncoder()
y_train = label_encoder.fit_transform(data['tags'])

input_shape = x_train.shape[1]
# print(input_shape)

# Define vocabulary
vocabulary = len(tokenizer.word_index)
# print("Number of unique words: ", vocabulary)
output_length = label_encoder.classes_.shape[0]
# print("Output length: ", output_length)

# Creating the model
i = Input(shape=(input_shape,))
x = Embedding(vocabulary + 1, 10)(i)
x = LSTM(10, return_sequences=True)(x)
x = Flatten()(x)
x = Dense(output_length, activation="softmax")(x)
model = Model(i, x)

# Compiling the model
model.compile(loss="sparse_categorical_crossentropy", optimizer='adam', metrics=['accuracy'])

# Train the model
train = model.fit(x_train, y_train, epochs=200)


def get_response(self, message: str):
    message = message.lower()

    prediction = tokenizer.texts_to_sequences([message])
    prediction = pad_sequences(prediction, maxlen=input_shape)

    output = model.predict(prediction)
    predicted_index = max(range(len(output[0])), key=output[0].__getitem__)
    response_tag = label_encoder.inverse_transform([predicted_index])[0]
    response = random.choice(responses[response_tag])

    return response
