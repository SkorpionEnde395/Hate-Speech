import pandas as pd

import nltk
nltk.data.path.append("C:\\Users\\sonny\\nltk_data")
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

import spacy # für deutsche Lemmatisierung 

#from sklearn.naive_bayes import MultinomialNB


daten=None
#Stopwordliste Herunterladen und in Variable abspeichern

#nltk.download('stopwords')
#nltk.download('punkt')
#nltk.download('wordnet') 

stop_words = set(stopwords.words('german'))

# Laden des deutschen Sprachmodells
nlpde = spacy.load("de_core_news_sm")

def dateneinlesen(pfad):
    try :
        #einlesen der trainingsdaten csv datei
        daten=pd.read_csv(pfad)
        df = pd.DataFrame(daten)
        #Festlegen der Spaltennamen des Datensatzes 
        daten.columns = ["id","Count", "hate_Spech", "offensive_Language", "neither", "class", "tweet"]
        #count,hate_speech,offensive_language,neither,class,tweet
        return df
    except FileNotFoundError:
        print("Fehler: Die Datei wurde nicht gefunden. Bitte prüfen Sie den Pfad.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

    datenkopf= df.head
    print(datenkopf)


def datenvorverarbeitung(text):

    #in Kleinschreibung Konvertieren 
    text = text.lower()
    print(text)

    # Verarbeite den Text
    doc = nlpde(text)
    # Tokens extrahieren 
    text_tokens = [token.text for token in doc]

    #Lemmatisierung der Tweets
    lemmatized_tokens = lemmatize_text(text)
    print(lemmatized_tokens)

    #wenn Tweet URL True
    #dann
    #URL_zerlegen()
    #sonst keine weitere verarbeitung 

    #Stopwörter entfernten 
    
    text_tokens_ohne_stoppwörter=[word for word in text if word not in stop_words]
    #zerlegt den TExt in einzelne Buchstaben --> Warum?

    print(text_tokens_ohne_stoppwörter)

def URL_zerlegen():
    print("TEst")

def lemmatize_text(text):
    # Den Text mit SpaCy verarbeiten
    doc = nlpde(text)
    # Lemmatisierte Tokens extrahieren
    lemmatized_tokens = [token.lemma_ for token in doc]
    return lemmatized_tokens


dateneinlesen("C:\\Users\\sonny\\PythonProjekte\\Softwareprojekt\\labeled_data.csv")
#datenvorverarbeitung("DAS IST EIN TEST")


