import random
import données

#Fonction qui tire au hasard un mot à trouver das le dictionnaire des mots
def choisirMot(listeMots):
    tirage = random.randrange(listeMots.__len__()-1)
    if tirage < 0:
        tirage = 0
    return listeMots[tirage]

#Fonction qui cache le mot à trouver.
# Exemple : "Baleine" devient "*******".
def cacherMot(mot):
    i = 1
    motCache = "*"
    while i < mot.__len__():
        motCache += '*'
        i += 1
    #tant que motCache n'est pas à la même taille que le mot à cacher, on rajoute un '*'
    return motCache

#Fonction qui affiche une réponse en fonction de si une lettre est trouvée ou pas
def verifierEssai(essai, mot):
    succes = False
    if essai in mot:
        print("Bravo ! Il vous reste", données.nombreDeChances, "essais.")
        succes = True
    else:
        données.nombreDeChances -= 1
        print("Quel dommage ! :( Il vous reste", données.nombreDeChances, "essais.")

    return succes

#Fonction remplaçant les astériques par les lettres trouvées.
#Exemple : si un 'e' est trouvé dans '******', '******' devient '**e**e'
def actualiserMotCache(mot, motCache, lettreTrouvee):
    l_mot = (" ".join(mot)).split(" ")
    l_motCache = (" ".join(motCache)).split(" ")

    i = 0
    while i < l_mot.__len__():
        if l_mot[i] == lettreTrouvee:
            l_motCache[i] = l_mot[i]
        i += 1

    return (" ".join(l_motCache)).replace(" ", "")




