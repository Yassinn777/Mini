import requests

def chercher_ville(nom):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": nom, "count": 1, "language": "fr"}
    try:
        reponse = requests.get(url, params=params, timeout=10)
    except requests.exceptions.RequestException:
        print(" Pas de connexion au reseau.")
        return None
    if reponse.status_code != 200:
        print(" Erreur serveur.")
        return None
    data = reponse.json()
    if "results" not in data:
        print(" Ville introuvable.")
        return None
    v = data["results"][0]
    return {
        "nom": v["name"],
        "pays": v["country"],
        "latitude": v["latitude"],
        "longitude": v["longitude"],
    }