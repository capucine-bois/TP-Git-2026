
def addition(x, y):
    """Retourne la somme de x et y"""
    res = x + y
    return res


def soustraction(x, y):
    """Retourne la différence de x et y"""
    print("**** La super soustraction ****")
    return x-y


def noms_binome():
    """
    Affiche les noms des membres du binôme
    Attention, chacun écrit la ligne pour afficher son nom
    """

    print("A")
    print("B")


a = 2
b = 1

print(f"La somme de {a} et {b} vaut {addition(a, b)}")
print(f"La différence de {a} et {b} vaut {soustraction(a, b)}")

noms_binome()
