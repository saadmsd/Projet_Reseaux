from outils import *
import tcp

def verify(trame):
    if (tcp.portdest(trame) == 80 or tcp.portsource(trame) == 80):
        for i in range(len(trame)):
            for j in range(len(trame[i])-3):
                if (trame[i][j] == "48" and trame[i][j+1] == "54" and trame[i][j+2] == "54" and trame[i][j+3] == "50"):
                    return True
    return False

def methodhttp(trame):
    # On récupère la ligne de requete
    msg = ""
    i = 3  # ligne
    j = 6  # col
    while (trame[i][j] != "0d"):
        msg += chr(to_decimal(trame[i][j]))
        if(j==len(trame[i])-1):
            if(i==len(trame)-1):
                return msg
            j=0
            i = i+1
        else:
            j = j+1
    return msg
