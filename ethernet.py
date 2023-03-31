from outils import *

def destination(trame):
    mac = ""
    for i in range(6):
        mac += str((trame[0][i])) + ":"
    return mac[:-1]

def source(trame):
    mac = ""
    for i in range(6, 12):
        mac += str((trame[0][i])) + ":"
    return mac[:-1]
