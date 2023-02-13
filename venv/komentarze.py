# run from teminal :  streamlit run ./venv/komentarze.py

import pandas as pd
import plotly.express as px
import streamlit as st
import json #pip intall json
from streamlit_lottie import st_lottie  #pip install streamlit-lottie
import datetime
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
#from keras.keras_preprocessing.text import glorot_uniform
from keras.models import model_from_json
from tensorflow.keras.preprocessing.text import tokenizer_from_json

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

from tensorflow import keras
model = keras.models.load_model('./venv/Model')

maxlen = 20   # skracamy recenzje do 20 słów

#---------- wczytuje przygotowany przy trenowaniu modelu tokenizer z json ------------------------
with open('./venv/tokenizer_json.json') as f:
    #data = json.load(f)
    #tokenizer = tokenizer_from_json(data)
    json_save = f.read()
tokenizer = tokenizer_from_json(json_save)
#--------------------------------------------------------------------------------------------------

lista = []
wynik = []

ikonka = load_lottiefile("./venv/call-center.json")


st.set_page_config(page_title="Analiza opinii klientow ",
                   page_icon=":satisfied:",
                   layout="wide"
                   )

df = pd.read_excel(
    io = './venv/komentarze.xlsx',
    engine = 'openpyxl',
    sheet_name='Lsum',
    skiprows=0,
    usecols='A:B',
    nrows = 221,
)

# print(df)
#st.dataframe(df)

# -------- SIEDEBAR ----------------
st.sidebar.header("Wybierz filtry")
temat = st.sidebar.multiselect(
    "Wybierz temat opinii :",
    options=["Produkty","Obsluga","Dostawa"],
    default=["Produkty","Obsluga","Dostawa"]
)

rodzaj = st.sidebar.multiselect(
    "Wybierz rodzaj opinii :",
    options=["Pozytywne","Negatywne"],
    default=["Pozytywne","Negatywne"]
)

# ------------- Filtr wyswietlania lista ---------------
if  "Produkty" in temat and 1 not in  lista:
    lista.append(1)
if "Obsluga" in temat and 2 not in lista:
    lista.append(2)
if "Dostawa" in temat and 3 not in lista:
    lista.append(3)
if  "Produkty" not in temat and 1 in lista:
    lista.remove(1)
if  "Obsluga" not in temat and 2 in lista:
    lista.remove(2)
if  "Dostawa" not in temat and 3 in lista:
    lista.remove(3)
lista.sort()


#lista = [1,2]

df_selection = df.query(
   "label == @lista"
)

import datetime

#------------ wybor czasu na sidebarze----------
data_start = st.sidebar.date_input(
    "Wybierz date rozpoczecia analizy ",
    datetime.date(2023, 1, 1))
data_end = st.sidebar.date_input(
    "Wybierz date zakonczenia analizy ",
    datetime.date(2023, 1, 31))

# ------------------Okno glowne-------------------------------
st.title('Analiza i klasyfikacja komentarzy klientow :sunglasses:')
st.write('Analiza wykonana od :', data_start, ' do : ',data_end)

#------------------ dwie kolumny na layoucie------------------------
col1, col2 = st.columns([1, 3])

col1.subheader("Dana po klasyfikacji")
col1.dataframe(df_selection)


col2.subheader("Wykresy czasowy i zbiorczy")
data = np.random.randn(10, 1)
col2.line_chart(data)

#chart_data = pd.DataFrame(
#    np.random.randn(20, 3),
#    columns=["a", "b", "c"])

#chart_data = dataframe(df_selection)
#col2.bar_chart(df_selection[1:])
#st.dataframe(df_selection)


#st.text(temat[2])
st.text(temat)
st.text('Labele :')
st.text('0 - komentarz negatywny dostawa, 1-komentarz pozytywny obsługa, 2- komenatrz pozytywny towar')
st.text('3- komenatrz pozytywny dostwa, 4- komenatrz negatywny obsługa, 5- komenatrz negatwyny towar')
col3, col4 = st.columns([3, 1])
test_texts = col3.text_input('Wpisz komenatrz', 'moj komenatrz')
#col3.write('Przewidywanie dla komenatrza : ', title)

if col4.button('Sprawdz'):
    st.write(test_texts)
    #st.write(list(tokenizer.index_word.items()))
    #tokenizer = Tokenizer(num_words=num_words)
    #tokenizer.fit_on_texts(train_texts)
    #tokeny = list(tokenizer.index_word.items())
    #print(tokeny[:10])
    # ---- przekodowanie komenatrzy na tokeny
    testowa_seq = tokenizer.texts_to_sequences(test_texts)
    X_test = pad_sequences(testowa_seq, maxlen=maxlen)
    result = model.predict(X_test)

#--------wyswietlane przewidywania, sortowanie ------------------
    opis = ['negatywna ocena dostawy','pozytywna ocena osbługi','pozytywna ocena towaru', 'pozytywna ocena dostawy', 'negatywna ocena obsługi', 'negatywna ocena towaru']
    wynik[0:5] = [0,0,0,0,0,0]
    for y in range(6):
        for x in range(result.shape[1]):
            wynik[y] = wynik[y] + result[x,y]
        wynik[y] = wynik[y]/result.shape[1]
    st.table(wynik)
    wynik1 = wynik.copy()
    wynik1.sort(reverse=True)
    for x1 in range(6) :
        label1 = wynik.index(wynik1[x1])
        st.write(label1, '  :  ', round(wynik1[x1],3),'  :     ',opis[label1])
    #st.write(result)
    #st.write(result.shape)
else:
    st.write('B')

st_lottie(
   ikonka,
    speed=1,
    reverse=False,
    loop=True,
    quality="low",
    #renderer="svg",
    height=300,
    width=None,
    key=None,
)