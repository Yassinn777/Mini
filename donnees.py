import json
FICHIER = "data.json"

def charger():
    try:
        with open(FICHIER, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def sauvegarder(elements):
    with open(FICHIER, "w", encoding="utf-8") as f:
        json.dump(elements, f, ensure_ascii=False, indent=2)