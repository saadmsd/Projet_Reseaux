def lecture(file):
    #ouverture du fichier texte contenant les trames
    with open(file, 'r') as file:
        lines = [l for l in (line.strip() for line in file) if l]  # on retire les lignes vides
        trames = []
        trame = []
        first = True
        for l in lines:
            #on retire les espace au debut et a la fin de la ligne
            l = l.strip()
            #on separe l'offset et les octets
            split = l.split("  ")
            offset = split[0]
            if (offset == "0000"):
                # ajout des octets de la trame passée dans la liste des trames
                if not first:
                    trames.append(trame)
                    trame = []
                first = False
            #on split par des espaces
            ltrame = split[1].split(" ")
            #on retire les espaces vides
            ltrame = [x for x in ltrame if x]
            print(ltrame)
            trame.append(ltrame)
        trames.append(trame)
        return trames
