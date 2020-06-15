import données
import fonctions

print("Bienvenue au zPendu !!!! Appuyez sur 0 à tout moment pour quitter.")
essai = ''

print("Un mot incroyable va être choisi...")
motChoisi = fonctions.choisirMot(données.listeMots)
motCache = fonctions.cacherMot(motChoisi)

while essai != '0':
    print("Le mot à trouver est :", motCache)
    essai = input("Saisissez une lettre :\n")
    if fonctions.verifierEssai(essai,motChoisi):
        motCache = fonctions.actualiserMotCache(motChoisi, motCache, essai)
        if motCache == motChoisi:
            print("Bravo vous avez gagné !!!!!")
            essai = '0'
    elif données.nombreDeChances == 0:
        print("Vous avez perdu. Nooooooooooooooooooooon! :'(\nLe mot cherché était :", motChoisi)
        essai = '0'



