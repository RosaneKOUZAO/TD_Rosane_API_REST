from health.patient import Patient


def test_patient_creation():
    p = Patient("Dupont", "Jean", "199051275123456")
    assert p.nom == "Dupont"


def test_sexe():
    p = Patient("Dupont", "Jean", "199051275123456")
    assert p.get_sexe() == "Homme"


def test_ssn_invalide():
    p = Patient("Dupont", "Jean", "123")
    assert p.is_valid() == False