
def addition(x, y, z, p):
    """Retourne la somme de x et y et z et p"""
    return x + y + z + p


def soustraction(x, y):
    """Retourne la différence de x et y"""
    return x-y


def noms_binome():
    """
    Affiche les noms des membres du binôme
    Attention, chacun écrit la ligne pour afficher son nom
    """
    print("Mohamed")
    print("Noah")

a = 2
b = 1

print(f"La somme de {a} et {b} vaut {addition(a, b)}")
print(f"La différence de {a} et {b} vaut {soustraction(a, b)}")

noms_binome()
