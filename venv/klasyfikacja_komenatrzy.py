import numpy as np
import pandas as pd
import os
import keras
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import io

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, Flatten
from tensorflow.keras.utils import to_categorical
from keras.models import model_from_json
from tensorflow.keras.layers import SimpleRNN, LSTM


def plot_hist(history):
    hist = pd.DataFrame(history.history)
    hist['epoch'] = history.epoch

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=hist['epoch'], y=hist['accuracy'], name='accuracy', mode='markers+lines'))
    fig.add_trace(go.Scatter(x=hist['epoch'], y=hist['val_accuracy'], name='val_accuracy', mode='markers+lines'))
    fig.update_layout(width=1000, height=500, title='accuracy vs. val accuracy', xaxis_title='Epoki', yaxis_title='accuracy', yaxis_type='log')
    fig.show()

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=hist['epoch'], y=hist['loss'], name='loss', mode='markers+lines'))
    fig.add_trace(go.Scatter(x=hist['epoch'], y=hist['val_loss'], name='val_loss', mode='markers+lines'))
    fig.update_layout(width=1000, height=500, title='loss vs. val loss', xaxis_title='Epoki', yaxis_title='loss', yaxis_type='log')
    fig.show()

# ----------- Odczyt danych trenigowych i testowych z pliku ----------------

train_texts = []
train_labels = []

df = pd.read_excel(
    io = 'komentarze.xlsx',
    engine = 'openpyxl',
    sheet_name='Lsum',
    skiprows=0,
    usecols='A:B',
    nrows = 575,)

train_texts = df['opinia'].values.tolist()
train_labels = df['label'].values.tolist()

#print(df[10:])
#print(train_texts[-10:])
#print(train_labels[-10:])

# ----- rozbicie komenatrzy na slowa, wybor 5000 najczesciej uzywanych --------------
maxlen = 20   # skracamy recenzje do 20 słów
num_words = 5000    # 5000 najczęściej pojawiających się słów
embedding_dim = 100

tokenizer = Tokenizer(num_words=num_words)
tokenizer.fit_on_texts(train_texts)

#--------zapis tokenizer do jsona ----------------------------------------------------
tokenizer_json = tokenizer.to_json()
with open('tokenizer_json.json', 'w') as json_file:
    json_file.write(tokenizer_json)
#-----------------------------------------------------------------------------------

tokeny = list(tokenizer.index_word.items())
print(tokeny[:10])

# ---- przekodowanie komenatrzy na tokeny
sequences = tokenizer.texts_to_sequences(train_texts)
print(sequences[:20])
word_index = tokenizer.word_index

print(f'{len(word_index)} unikatowych słów.')

# skracamy recenzje do pierwszych 20 słów
train_data = pad_sequences(sequences, maxlen=maxlen)
print(train_data.shape)

print(train_data[:3])

train_labels = np.asarray(train_labels)
print(train_labels)

# przemieszanie komenatrzy
indices = np.arange(train_data.shape[0])
np.random.shuffle(indices)
train_data = train_data[indices]
train_labels = train_labels[indices]
print(train_data.shape)

# podział na zbiór treningowy i walidacyjny
training_samples = 520
validation_samples = 50
X_train = train_data[:training_samples]
y_train = train_labels[:training_samples]
X_val = train_data[training_samples: training_samples + validation_samples]
y_val = train_labels[training_samples: training_samples + validation_samples]

y_train = to_categorical(y_train)
y_val = to_categorical(y_val)

# budowa sieci neuronowej
# Embedding(input_dim, output_dim)

model = Sequential()
#model.add(Embedding(num_words, embedding_dim, input_length=maxlen))
#model.add(Flatten())
#model.add(Dense(32, activation='softmax'))
#model.add(Dense(6, activation='sigmoid'))
model.add(Embedding(10000, 32))
model.add(LSTM(16))
model.add(Dense(6, activation='sigmoid'))
print(model.summary())

 # kompilacja modelu
#model.compile(optimizer='adam',
#              loss='sparse_categorical_crossentropy',
#              metrics=['accuracy'])
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(X_train, y_train, batch_size=32, epochs=16, validation_data=(X_val, y_val))
print(history.history)

# plot_hist(history)

 #  ----------- wyswietl dokladnosc modelu ----------------
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(acc) + 1)

# ----------------  wyswietl strate modelu --------------------
#plt.plot(epochs, loss, 'bo', label='training loss')
#plt.plot(epochs, val_loss, 'b', label='Validation loss')
#plt.legend()
#plt.show()

plt.plot(epochs, acc, 'bo', label='training acc')
plt.plot(epochs, val_acc, 'b', label='validation acc')
plt.legend()
plt.show()

#---------- zapis przetrenowanej sieci --------------------------------
model.save('./Model')