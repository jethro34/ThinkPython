import string
import random


def read_n_strip(file):
    """ Reads a text file and populates a list. """

    fin = open(file)
    for line in fin:
        if line.strip() == "Versos sencillos (J. Martí) José Martí":
            continue
        for pre_word in line.replace("--", " ").replace("¿", "").replace("¡", "").split():
            word = pre_word.strip(string.punctuation + string.whitespace).lower()
            if word.isalpha() and (word == "vil" or word.strip("ivxl") != ""):
                worter_liste.append(word)


def create_markov_dict(liste, pre_worter):
    """ Creates a {tuple: set} Markov dictionary from a given list and a number of pre-words."""

    for i in range(len(liste) - pre_worter):
        markov_dikt.setdefault(tuple(liste[i: i + pre_worter]), set()).add(liste[i + pre_worter])


def generate_markov_text(lista, dicc, pre_palabras, ciclos):
    """ Generates a given number of cycles of a given pre-word length of Markov text
        by reading from a given list and a dictionary. """

    texto = ''
    num_random = random.randint(0, len(lista) - pre_palabras)
    llave = tuple(lista[num_random: num_random + pre_palabras])

    while llave not in dicc:
        num_random = random.randint(0, len(lista) - pre_palabras)
        llave = tuple(lista[num_random: num_random + pre_palabras])

    for i in range(pre_palabras):
        texto += str(llave[i]) + " "

    for _ in range(ciclos):
        valor = random.choice(tuple(dicc[llave]))
        texto += valor + " "
        llave = llave[1:] + (valor,)
        if llave not in dicc:
            break

    print(texto)
    return None


worter_liste = []
markov_dikt = {}

read_n_strip("/Users/hejtor/OneDrive/CS/ThinkPython stuff/revolution.txt")

# print(worter_liste)
create_markov_dict(worter_liste, 1)
for item in markov_dikt:
    print(item, markov_dikt[item])

generate_markov_text(worter_liste, markov_dikt, 1, 300)
