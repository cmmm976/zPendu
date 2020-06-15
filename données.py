with open("listeMots.txt","r") as f_listeMots:
    str_listeMots = f_listeMots.read()
    listeMots = str_listeMots.split(sep="\n")

nbreDeMots = listeMots.__len__()
nombreDeChances = 10

