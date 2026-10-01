
def addition(x, y):
    """Retourne la somme de x et y"""
    return x + y # retourne la somme de x et y


def soustraction(x, y):
    """Retourne la différence de x et y"""
    return x-y #retourne la différence entre x et y


def noms_binome():
    """
    Affiche les noms des membres du binôme
    Attention, chacun écrit la ligne pour afficher son nom
    """
    print("Clémentine")
    print("Noah")

a = 2
b = 1

print(f"La somme de {a} et {b} vaut {addition(a, b)}")
print(f"La différence de {a} et {b} vaut {soustraction(a, b)}")

noms_binome()
