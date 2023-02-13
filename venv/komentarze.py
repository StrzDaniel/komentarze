import pandas as pd
import plotly.express as px
import streamlit as st
import json #pip intall json
from streamlit_lottie import st_lottie  #pip install streamlit-lottie
import datetime
import numpy as np

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lista = []

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