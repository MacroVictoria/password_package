import json
import random

#Die Klasse JsonFile bietet Methoden zum Laden und Speichern von JSON-Daten.
class JsonFile:
     # Daten beim Initialisieren der Klasse laden
    def __init__(self, filename):
        self.filename = filename
        self.data = self.load_data() 

    # JSON-Daten für  __init__ bereitstellen
    def load_data(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except Exception as e:
            print(f"Fehler beim Laden der JSON-Daten für {self.filename}: {str(e)}")
            return None

    # JSON-Daten aus einer anderen Datei laden und zurückgeben
    def load_json(self, file):
        try:
            with open(file, 'r', encoding='utf-8') as file:
                return json.load(file)
        except Exception as e:
            print(f"Fehler beim Laden der JSON-Datei: {file}")
        
    def save_json(self, file, content):
        with open(file, 'w', encoding='utf-8') as file:
            json.dump(content, file, indent=4)  # JSON-Inhalt in die Datei schreiben und formatieren

        print("Daten wurden erfolgreich gespeichert.")  # Erfolgsmeldung ausgeben, wenn die Daten erfolgreich gespeichert wurden

        
#Die  Klasse CharacterSet erbt von der Klasse JsonFile und erweitert sie um die Methode zur Bildung des Zeichenvorrats
class CharacterSet(JsonFile):
    def selection_character(self, lowercase_bool=True, uppercase_bool=True, number_bool=True, special_bool=True):
        character_pool = []
        string_feedback = ""

        # Überprüfen, ob Kleinbuchstaben ausgewählt sind
        if lowercase_bool:
            if "lowercase" in self.data:
                lowercase = self.data["lowercase"]
                character_pool += lowercase
                string_feedback += "Kleinbuchstaben/"

        # Überprüfen, ob Großbuchstaben ausgewählt sind
        if uppercase_bool:
            if "uppercase" in self.data:
                uppercase = self.data["uppercase"]
                character_pool += uppercase
                string_feedback += "Großbuchstaben/"

        # Überprüfen, ob Zahlen ausgewählt sind
        if number_bool:
            if "numbers" in self.data:
                numbers = self.data["numbers"]
                character_pool += numbers
                string_feedback += "Zahlen/"

        # Überprüfen, ob Sonderzeichen ausgewählt sind
        if special_bool:
            if "special" in self.data:
                special = self.data["special"]
                character_pool += special
                string_feedback += "Sonderzeichen/"

        # Überprüfen, ob Zeichen im character_pool vorhanden sind
        if not character_pool:
            print('Keine Zeichen in der JSON-Datei gefunden!')
        
        #Feedback über die ausgewählten Zeichen für die Passwortbildung
        print("Ihr Auswahl: ", string_feedback)

        return character_pool

#Die Klasse erweitert die Klasse CharacterSet und enthält Methoden zur Generierung und Verwaltung von Passwörtern.
class PasswordManagement(CharacterSet):
    def __init__(self, filename):
        super().__init__(filename)   #den Konstruktor der Elternklasse aufzurufen

    #Die Methode generate_password generiert ein Passwort basierend auf der übergebenen Zeichenlänge und dem Zeichensatz.
    def generate_password(self, password_length, character_set):
        password = []
        for e in range(password_length):
            password += random.choice(character_set)
        print("Zeichenlänge:", password_length)
        print("---------------------------------------------")
        return password
    
    #In der Methode wird das Passwort mit dem angegebenen Label und Benutzer in die Passwortdatenbank gespeichert.
    def save_password(self, label, user, password):
        password_string = "".join(password)
        try:
            password_database = self.load_json('password_package\modules\Daten\password_Database.json')
            
            if password_database is None:
                password_database = []

            new_entry = {
                "label": label,
                "user": user,
                "password": password_string
            }

            password_database.append(new_entry)

            self.save_json('password_package\modules\Daten\password_Database.json', password_database)
            print("Passwort wurde erfolgreich gespeichert.")
            
        except Exception as e:
            print(f"Fehler beim Speichern des Passworts: {str(e)}")
    
    #In der Methode view_password werden die in der Passwortdatenbank gespeicherten Passwörter angezeigt.
    def view_password(self):
        try:
            password_database = self.load_json('password_package\modules\Daten\password_Database.json')

            if not password_database:
                print("Die Passwortliste ist leer.")
            else:
                print("Passwortliste:")
                for entry in password_database:
                    print(f"Label: {entry['label']}")
                    print(f"Benutzer: {entry['user']}")
                    print(f"Passwort: {entry['password']}")
                    print("---------------------------------------------")
                    
        except Exception as e:
            print(f"Fehler beim Anzeigen der Passwörter: {str(e)}")   
			