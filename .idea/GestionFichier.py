class GestionFichier:
    FICHIER = "bibliotheque.json"

    @staticmethod
    def sauvegarder(livres):
        try:
            with open(GestionFichier.FICHIER, "w") as fichier:
                json.dump([livre.to_dict() for livre in livres], fichier, indent=4)
            print("💾 Données sauvegardées !")
        except Exception as e:
            print("❌ Erreur lors de la sauvegarde :", e)

    @staticmethod
    def charger():
        try:
            with open(GestionFichier.FICHIER, "r") as fichier:
                data = json.load(fichier)
                return [Livre.from_dict(livre) for livre in data]
        except FileNotFoundError:
            print("🔄 Aucune donnée trouvée.")
            return []
        except Exception as e:
            print("❌ Erreur lors du chargement :", e)
            return []
        except FileNotFoundError:
            print("🔄 Aucune donnée trouvée.")
            return []
        except Exception as e:
            print("❌ Erreur lors du chargement :", e)
            return []
