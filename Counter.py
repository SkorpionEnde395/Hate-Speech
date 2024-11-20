import csv
from collections import Counter
import re

def load_text_from_csv(file_path):
    text = ""
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # Überprüft, ob die Zeile nicht leer ist
                text += " ".join(row) + " "  # Kombiniere den Text aus allen Spalten
    return text

def hate_speech_count(text, hate_speech_words):
    # Bereinige den Text von Zahlen, @-User-Tags und Sonderzeichen
    text = re.sub(r'\d+', '', text)  # Entfernt alle Zahlen
    text = re.sub(r'@\w+', '', text)  # Entfernt alle User-Tags
    words = re.findall(r'\b\w+\b', text.lower())  # Finde alle Wörter in Kleinbuchstaben

    # Filtere und zähle nur die Wörter, die in der Hate Speech-Liste sind
    hate_speech_counts = Counter(word for word in words if word in hate_speech_words)
    return hate_speech_counts

# Beispielhafte Liste von frauenfeindlichen Begriffen
hate_speech_words = {
    'Hallo', 
    #file_path = 'labeled_data2.csv'
    #Blacklist 'Wort', 'Wort', 

    # Weitere frauenfeindliche Begriffe hinzufügen
}

# Beispielpfad zur CSV-Datei
file_path = "C:\\Users\\sonny\\PythonProjekte\\Softwareprojekt\\labeled_data.csv"

# Text aus der CSV-Datei laden und Hate Speech-Wörter zählen
text = load_text_from_csv(file_path)
counts = hate_speech_count(text, hate_speech_words)

# Ergebnis anzeigen
print("Häufigkeit der Hate Speech-Wörter:")
for word, count in counts.items():
    print(f"{word}: {count}")


#labeled_data.csv
#
#Bert testen #navebase

