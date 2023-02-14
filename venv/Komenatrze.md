# Komenatrze 
## Przeznacznie i zastosowanie
Aplikajca "**Komenatrze**" jest przeznaczona do klasyfikacji treści komentarzy tekstowych, umieszczanych na stronach sklepów 
internetowych. Aplikacja wykorzystuje przetrenowaną autorską sieć nerunowa RNN. Jako wynik 
uzyskujemy przewidywane możliwe kategorie z odpowiadającym im prawdopodobieństwem należenia 
do nich, posegregowane malejąco. 
> Komenatrze należa do 6 możliwych kategorii :
1. negatywna ocena dostawy
2. pozytywna ocena osbługi
3. pozytywna ocena towaru
4. pozytywna ocena dostawy
5. negatywna ocena obsługi
6. negatywna ocena towaru



Dodatkowo do projektu dołączono drugą aplikację : "**klasyfikacja_komenatarzy**", która tworzy i trenuje 
redurencyjna sieć neuronowa RNN, wykorzystywaną w aplikacjie "**Komentarze**". Aplikacja może zostać 
wykorzystana ponownie, np. gdy ilość danych do trenowania sieci wzrośnie z biegiem upływu czasu pracy sklepu
internetowego wykorzystującego skypt.

> Przeznaczniem głownym przewydywania i kategoryzacji komeantrzy jest ułatwienie pracy
> i dostarczenie raportu analizy zadowolenia klientow i ocen słąbych stron sklepu internetowego
---

## Technologia, wykorzystane narzedzia i biblioteki

Aplikacja została opracowana w postaci skrytów w jezyku **PYTHON**. Wykorzytane zostały nastepujące biblioteki open source :
* Tensorflow/Keras  - https://keras.io/   - wykorzystana do budowy sieci neruonowej
* Numpy - https://numpy.org/  - wykorzystana do przygotowania i przetwarzania danych 
* Pandas - https://pandas.pydata.org/ - wykorzytywana do przetwarzania i analizy danych
* Streamlit - https://streamlit.io/ - wykorzystana do prezentacji danych na stronie web.
* Matplotlib - https://matplotlib.org/ - wykorzystana do stworzenia wykresów funkcji dokładności i straty po wytrenowaniu stworzonej sieci neuronowej
* Json - https://docs.python.org/3/library/json.html - wykorzystana do exportu i importu słownika (tekenizera) wyznaczonego na etapie tworzenia modelu sieci neuronowej
* Datetime - https://docs.python.org/3/library/datetime.html - wykorzystan do wyboru daty komenatrzy z bazy danych sklepu internetowego


---
## Instalacja
Przed uruchomieniem aplikacji należy używając managera bilbiotek **pip** zainstalować następujące pakiety :
```bash
pip install pandas
pip install streamlit
pip install streamlit-lottie
pip install keras
pip install pandas
pip install os
pip install matplotlib
pip install json
pip install datetime
```
---
## Uruchomienie aplikacji oceny komentarzy 
Aplikację  "Komeantrze" uruchamiamy z konsoli (terminala) z katalogu projektu komendą :
> streamlit run ./venv/komentarze.py

Skrypt uruchmia widok strony web do wygodnej obsługi.
Sieć neruonowa przygotowana i wytrenowana zostaje wczytana na początku z folderu ./Models. Plik formatu .json zawierający 
zestaw słów najczęściej pojawiających się w komenatrzach podczas tworzenia/trenowania sieci (Tokenizery) jest odczytany i wykorzystany
do translacji słów analizowanch bieżacych komenatrzy. Tekst komentarzy został ograniczony do 20 słów. Jeżeli będzie dłuższy 
aplikacja odetnie wszystko ponad. 
* komentarz można wpisać ręcznie i wciskając przycisk "sprawdz" wyświetlić kategoryzację komenatrza przez sieć neuronową
* komentarze można wybrać na postawie dat "od" "do" i wciskając przycisk "sprawdz z bazy" wyświetlić kategoryzację wszytkich 
    tekstów znajdujących się w bazie danych sklepu w zakresie wybranych dat
--
## Sieć neuronowa - zapisana, wyniki
Przygotowania sieć neruonowa ma nastepujące parametry

![dokładnosc](https://github.com/StrzDaniel/komentarze/blob/8b0d53b2f17943122e2d71e76b5c69e82e426d5e/venv/accuracy.PNG)
#![Image](http://url/a.png)
---
## Siec neuronowa - ponowne trenowania
Głowna aplikacja wykorzystuje siec neuronową stoworzoną i wytrenowaną w tym skrypcie.
Stworzona sieć neuronowa RNN w oparciu o biliotekę Tensorflow z nakładką Keras. Do trenowania sieci wykorzystano
plik komenatarze.xls, który zawiera 6 opisanych powyżej rodzajów komenatrzy z odpowiednimi labelami.
>Plik z komenatrzami zawiera ograniczoną ilość komenatrzy, a ich zwiększenie i ponowne przetrenowanie 
sieci, poprawiłoby wyniki i  trafności przewidywań i klasyfikacji. W miarę upływu czasu pracy sklepu gdy
> ilośc komenatarzy w sklepie będzie roznać, zaleca się uzupełnienie listy i ponowne przetrenowanie modelu


---
## Autorzy 
* Daniel Strzelecki https://github.com/StrzDaniel?tab=repositories

---
## Copyrights
Aplikacje, skrytpy są stworzone w oparniu o zasoby opnesource i usdostępnione do wolnego stosowania na zasadach opensource.
Możesz aplikację ściagać, dowolnie modyfikować, udostępniać i wykorzystywać. Należy jednak przy ponownym udostępnieniu z lub bez modyfikacji
wymienić autora na liscie twórców. W przypadku komercyjengo wykorzystania należy uzyskać zgodnę autora. 