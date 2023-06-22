# Password Package

This project is part of my thesis within the Python programming course at Macromedia University.
The implementation of classes allows generating passwords of any lenght and from different character sets.


#two examples of use

##################################################################################################
#Short description		
##################################################################################################	

import password_module

# eine Instanz der PasswordManagement-Klasse erstellen
password_manager = password_module.PasswordManagement('Daten\character_pool.json')

# Verwendung der Methoden der PasswordManagement-Klasse
generated_password =password_manager.generate_password(10, password_manager.selection_character())
password_manager.save_password('Website', 'Benutzername', generated_password)
password_manager.view_password()

			
##################################################################################################
#Long description		
##################################################################################################	

import password_module			

# Instanziieren Sie die PasswordManagement-Klasse mit dem Dateinamen der JSON-Datei
password_manager = PasswordManagement("Daten\character_pool.json")
#-------------------------------------------------------------

#-------------------------------------------------------------
#Anwendungen/Dienste, mit denen das Passwort genutzt werden soll.
#label="email@gmx.de"
label = input('Anwendung: (z.B. Banking)')
#-------------------------------------------------------------

#-------------------------------------------------------------
#Benutzername
#User="Victoria"
User = input('Benutzername: ')
#-------------------------------------------------------------

#-------------------------------------------------------------
# Definiert die gewünschte Länge des Passworts
password_length = 10
try:
    password_length = int(input('Zeichenanzahl: '))
    if password_length < 8:
        print('!!! Empfohlene Mindsetläge beträgt 8 Zeichen !!!')
        
except:
    print('Sie haben keine Zahl eingegeben!')
#-------------------------------------------------------------  

#-------------------------------------------------------------
#Vorauswahl für Umfang des Zeichenvorrats treffen
lowercase_bool=True
uppercase_bool=True
number_bool=True
special_bool=True

#Abfrage für Kleinbuchstaben starten
Switch=True     #Steuerschalter zum Ausstieg aus der while -Schleife
while Switch:   #Solange Schalter an ist, läuft auch die Schleife
   answer = input('Kleinbuchstaben benutzen?:')
   if answer=="n":
      lowercase_bool=False
      Switch=False            #Bei der korrekten Eingabe, über den Schalter unterbrechen
   elif answer=="j":
      Lowercase_bool=True      
      Switch=False            #Bei der korrekten Eingabe, über den Schalter unterbrechen
    
   else:
      print('Nur j oder n eingeben!') 

#Abfrage für Großbuchstaben starten
Switch=True     #Steuerschalter zum Ausstieg aus der while -Schleife
while Switch:   #Solange Schalter an ist, läuft auch die Schleife
   answer = input('Großbuchstaben benutzen?:')
   if answer=="n":
      uppercase_bool=False
      Switch=False            #Bei der korrekten Eingabe, über den Schalter unterbrechen
   elif answer=="j":
      Uppercase_bool=True      
      Switch=False            #Bei der korrekten Eingabe, über den Schalter unterbrechen
    
   else:
      print('Nur j oder n eingeben!') 

#Abfrage für Zahlen starten
Switch=True     #Steuerschalter zum Ausstieg aus der while -Schleife
while Switch:   #Solange Schalter an ist, läuft auch die Schleife
   answer = input('Zahlen benutzen?:')
   if answer=="n":
      number_bool=False
      Switch=False            #Bei der korrekten Eingabe, über den Schalter unterbrechen
   elif answer=="j":
      Number_bool=True      
      Switch=False            #Bei der korrekten Eingabe, über den Schalter unterbrechen
    
   else:
      print('Nur j oder n eingeben!') 

#Abfrage für Sonderzeichen starten
Switch=True     #Steuerschalter zum Ausstieg aus der while -Schleife
while Switch:   #Solange Schalter aktiv ist, läuft auch die Schleife
   answer = input('Sonderzeichen benutzen?:')
   if answer=="n":
      special_bool=False
      Switch=False            #Bei der korrekten Eingabe, über den Schalter unterbrechen
   elif answer=="j":
      Special_bool=True      
      Switch=False            #Bei der korrekten Eingabe, über den Schalter unterbrechen
    
   else:
      print('Nur j oder n eingeben!') 

# Ruft die Methode selection_character auf, um den Zeichensatz basierend auf den gewünschten Optionen zu erhalten
character_pool = password_manager.selection_character(lowercase_bool, uppercase_bool, number_bool, special_bool)
#-------------------------------------------------------------

#-------------------------------------------------------------
# Generiert das Passwort
generated_password = password_manager.generate_password(password_length, character_pool)
#-------------------------------------------------------------

#-------------------------------------------------------------
# Öffnet das generierte Passwort
print("Generiertes Passwort:", ''.join(generated_password))
#-------------------------------------------------------------


###################################################################################################
# Speichern des Passworts
password_manager.save_password('Email', 'test@example.com', generated_password)

###################################################################################################

# Anzeigen der Passwortliste
password_manager.view_password()

##################################################################################################


