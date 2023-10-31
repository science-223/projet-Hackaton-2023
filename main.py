import json


# Charger les données JSON depuis le fichier
with open('Data_Ressource/DataBase.JSON', 'r', encoding='UTF-8') as DATA:
    data = json.load(DATA)

note_eco_valeur = []
# ------------------------------------------------------------------------------------------------------------------

# choix du Véhicule

# Récupérer les données de l'utilisateur
Car_choice = input("Avec quelle type de voiture parmis les choix suivants :\n"
                   "Citadine\n"
                   "Cabriolet\n"
                   "Berline\n"
                   "SUV\n"
                   "4x4\n")

for index, Car in enumerate(data["intents"][0]["Voiture"]):
    if Car_choice == Car:
        note_eco_valeur.append(data["intents"][0]["note eco"][index])
        break
else:
    print("Choix de voiture non valide.")

# ------------------------------------------------------------------------------------------------------------------

# choix d'énergie

Energie_choice = input("Avec quelle type d'énergie parmis les choix suivants :\n"
                       "Essence\n"
                       "Electrique\n"
                       "gaze\n"
                       "Diesel\n"
                       "Hybride\n")

for index, energie in enumerate(data["intents"][1]["energie"]):
    if Energie_choice == energie:
        note_eco_valeur.append(data["intents"][1]["note eco"][index])
        break
else:
    print("Choix d'énergie non valide.")

# ------------------------------------------------------------------------------------------------------------------

# choix du Kilométrage

Km_choice = input("Avec quelle type de kilométrage parmis les choix suivants :\n"
                  "5-10K/km\n"
                  "10-15K/km\n"
                  "15-20K/km\n"
                  "20-25K/km\n"
                  "25-30K/km\n")

for index, kilometrage in enumerate(data["intents"][2]["Distance"]):
    if Km_choice == kilometrage:
        note_eco_valeur.append(data["intents"][2]["note eco"][index])
        break
else:
    print("Choix de kilométrage non valide.")

# ------------------------------------------------------------------------------------------------------------------

# choix de l'année

AN_choice = input("de quelle année parmis les choix suivants :\n"
                  "1960-1970\n"
                  "1970-1980\n"
                  "1990-2000\n"
                  "2000-2010\n"
                  "Après 2010\n")

for index, Anner in enumerate(data["intents"][3]["Anner"]):
    if AN_choice == Anner:
        note_eco_valeur.append(data["intents"][3]["note eco"][index])
        break
else:
    print("Choix de lannée non valide.")

# ------------------------------------------------------------------------------------------------------------------

# Calculer la somme des valeurs 'note eco'

sum_note_eco = sum(note_eco_valeur)
print(str(int(sum_note_eco)) + " / 40")

if 0 <= sum_note_eco <= 10:
    eco_percent = 3.0

if 11 <= sum_note_eco <= 15:
    eco_percent = 2.74

if 16 <= sum_note_eco <= 25:
    eco_percent = 2.52

if 26 <= sum_note_eco <= 33:
    eco_percent = 2.10

if 34 <= sum_note_eco <= 40:
    eco_percent = 1.85

Passenger_nb = input("combien de passager seront présent dans ce véhicule ?\n"
                     "veuiller saisir un nombre : ")

if Passenger_nb == '1':
    print(str(float(eco_percent) + (float(0.11))) + '%')

if Passenger_nb == '2':
    print(str(float(eco_percent) - (float(0.17))) + '%')

if Passenger_nb == '3':
    print(str(float(eco_percent) - (float(0.29))) + '%')

if Passenger_nb == '4':
    print(str(float(eco_percent) - (float(0.53))) + '%')
