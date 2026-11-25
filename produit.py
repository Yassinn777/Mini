import api
import donnees

while True:
    print("\n--- LOCALISATION DE VILLES ---")
    print("1. Chercher et enregistrer une ville")
    print("2. Voir les villes enregistrées")
    print("3. Quitter")
    choix = input("Votre choix : ")

    if choix == "1":
        nom = input("Nom de la ville : ").strip()
        if not nom:
            continue
        infos = api.chercher_ville(nom)
        if infos:
            print(f"Trouvée : {infos['nom']} ({infos['pays']}) -> Lat: {infos['latitude']}, Lon: {infos['longitude']}")
            elements = donnees.charger()
            deja_present = any(
                e["nom"].lower() == infos["nom"].lower() and e["pays"] == infos["pays"]
                for e in elements
            )
            if not deja_present:
                elements.append(infos)
                donnees.sauvegarder(elements)
                print("Ville ajoutée à l'historique.")
            else:
                print("Cette ville est déjà enregistrée.")

    elif choix == "2":
        elements = donnees.charger()
        if not elements:
            print("Aucune ville enregistrée.")
        else:
            for i, v in enumerate(elements, 1):
                print(f"{i}. {v['nom']} - {v['pays']} (Lat: {v['latitude']}, Lon: {v['longitude']})")

    elif choix == "3":
        print("Au revoir !")
        break
    else:
        print("Choix invalide.")