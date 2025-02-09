# 📌 Fusionneur de fichiers JSON

## 📖 Présentation
Ce script Python permet de **fusionner plusieurs fichiers JSON** en un seul fichier unique nommé `data.json`. Il est utile lorsque vous avez plusieurs fichiers contenant des données au **même format** et que vous souhaitez les regrouper en une seule structure sans perdre d'informations.

---

## 🚀 Comment utiliser ce script ?

### 🔹 1. Pré-requis
- **Python** doit être installé sur votre machine (version 3.x recommandée).
- Avoir des fichiers JSON à fusionner dans le même répertoire que le script.

### 🔹 2. Installation
1. **Téléchargez ou créez le script** Python (`fusion_json.py`).
2. **Ajoutez vos fichiers JSON** dans le même dossier que le script.
3. **Modifiez la liste** `fichiers_json` pour inclure les noms de vos fichiers.

### 🔹 3. Exécution du script
Ouvrez un terminal (cmd, PowerShell ou terminal Mac/Linux) et exécutez la commande :

```sh
python fusion_json.py
```

Après l'exécution, un fichier `data.json` contenant toutes les données fusionnées sera créé dans le même répertoire.

---

## 📜 Explication du code

### 🔹 1. Importation des modules nécessaires
```python
import json
import glob
```
- `json` : Permet de lire et écrire des fichiers JSON.
- `glob` (non utilisé ici, mais utile pour une recherche automatique de fichiers JSON).

### 🔹 2. Définition des fichiers à fusionner
```python
fichiers_json = [
    "fichier1.json",
    "fichier2.json",
    "fichier3.json",
    "fichier4.json",
]
```
Cette liste contient les noms des fichiers JSON à fusionner. **Vous devez modifier cette liste** en fonction des fichiers que vous souhaitez traiter.

### 🔹 3. Initialisation d'une liste pour stocker toutes les données
```python
toutes_les_donnees = []
```
Une liste vide est créée pour stocker l'ensemble des données provenant de tous les fichiers JSON.

### 🔹 4. Lecture et fusion des fichiers JSON
```python
for fichier in fichiers_json:
    with open(fichier, "r", encoding="utf-8") as f:
        donnees = json.load(f)
        toutes_les_donnees.extend(donnees)  # Ajouter les données à la liste principale
```
- Ouvre chaque fichier JSON **en lecture (`r`) avec l'encodage UTF-8**.
- Charge son contenu en mémoire (`json.load(f)`).
- **Ajoute son contenu** à la liste `toutes_les_donnees`.

### 🔹 5. Sauvegarde des données fusionnées dans un fichier `data.json`
```python
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(toutes_les_donnees, f, indent=4, ensure_ascii=False)
```
- Crée ou écrase le fichier `data.json` en **mode écriture (`w`)**.
- Écrit toutes les données **avec une indentation de 4 espaces** pour rendre le fichier lisible.
- `ensure_ascii=False` permet de garder les caractères spéciaux (accents, etc.).

### 🔹 6. Message de confirmation
```python
print("Fichier fusionné sauvegardé sous 'data.json'")
```
Une fois le script exécuté avec succès, un message de confirmation s'affiche.

---

## 🔧 Améliorations possibles
✅ Ajouter une **vérification d'existence des fichiers** pour éviter les erreurs.
✅ **Fusion automatique** de tous les fichiers JSON du dossier sans avoir à les lister manuellement (`glob.glob("*.json")`).
✅ Gérer les **doublons** et éviter d'ajouter plusieurs fois les mêmes données.

---

## ✉️ Support
Si vous avez des questions ou des problèmes, n'hésitez pas à me contacter ou à proposer des améliorations. 😊

---

🚀 **Bon fusionnage de JSON !**

