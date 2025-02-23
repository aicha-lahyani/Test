def afficher_menu():
    print("\n --- Menu Bibliothèque ---")
    print(" Ajouter un livre")
    print(" Afficher les livres")
    print(" Rechercher un livre")
    print(" Emprunter un livre")
    print(" Retourner un livre")
    print(" Supprimer un livre")
    print(" Quitter et sauvegarder")

def main():
    biblio = Bibliotheque()
    biblio.charger()

    while True:
        afficher_menu()
        choix = input(" Votre choix : ")

        if choix == "1":
            titre = input(" Titre : ")
            auteur = input(" Auteur : ")
            annee = input(" Année de publication : ")
            biblio.ajouter_livre(titre, auteur, annee)

        elif choix == "2":
            biblio.afficher_livres()

        elif choix == "3":
            titre = input(" Titre à rechercher : ")
            biblio.rechercher_livre(titre)

        elif choix == "4":
            id_livre = int(input(" ID du livre à emprunter : "))
            biblio.emprunter_livre(id_livre)

        elif choix == "5":
            id_livre = int(input(" ID du livre à retourner : "))
            biblio.retourner_livre(id_livre)

        elif choix == "6":
            id_livre = int(input(" ID du livre à supprimer : "))
            biblio.supprimer_livre(id_livre)

        elif choix == "7":
            biblio.sauvegarder()
            print(" Fin du programme.")
            break

        else:
            print(" Choix invalide, réessayez.")

if name == "main":
    main()
    