import json
import glob

# Liste des fichiers à fusionner
fichiers_json = [
    "fichier1.json",
    "fichier2.json",
    "fichier3.json",
    "fichier4.json",
]

# Liste pour stocker toutes les données
toutes_les_donnees = []

# Charger et fusionner les fichiers
for fichier in fichiers_json:
    with open(fichier, "r", encoding="utf-8") as f:
        donnees = json.load(f)
        toutes_les_donnees.extend(donnees)  # Ajouter les données à la liste principale

# Sauvegarde du fichier combiné
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(toutes_les_donnees, f, indent=4, ensure_ascii=False)

print("Fichier fusionné sauvegardé sous 'data.json'")
