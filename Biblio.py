import json

class Livre:
    def init(self, id, titre, auteur, annee):
        self.id = id
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.emprunte = False  # Par défaut, le livre est disponible

    def emprunter(self):
        self.emprunte = True

    def retourner(self):
        self.emprunte = False

    def to_dict(self):
        return {
            "id": self.id,
            "titre": self.titre,
            "auteur": self.auteur,
            "annee": self.annee,
            "emprunte": self.emprunte
        }

    @staticmethod
    def from_dict(data):
        livre = Livre(data["id"], data["titre"], data["auteur"], data["annee"])
        livre.emprunte = data["emprunte"]
        return livre

    def str(self):
        statut = "Emprunté" if self.emprunte else "Disponible"
        return f" ID: {self.id} | {self.titre} - {self.auteur} ({self.annee}) | {statut}"
