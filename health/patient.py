class Patient:

    def __init__(self, nom, prenom, ssn):
        self.nom = nom
        self.prenom = prenom
        self.ssn = ssn

    def get_sexe(self):
        if self.ssn[0] == "1":
            return "Homme"
        elif self.ssn[0] == "2":
            return "Femme"
        return "Invalide"

    def is_valid(self):
        return len(self.ssn) == 15 and self.ssn.isdigit()