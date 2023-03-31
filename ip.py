from outils import *

def verify(trame):
    return (trame[0][12] == "08" and trame[0][13] == "00")

def source(trame):
    ip = str(to_decimal(trame[1][10])) + "." + str(to_decimal(trame[1][11])) + "." + str(to_decimal(trame[1][12])) + "." + str(to_decimal(trame[1][13]))
    return ip

def destination(trame):
    ip = str(to_decimal(trame[1][14])) + "." + str(to_decimal(trame[1][15])) + "." + str(to_decimal(trame[2][0])) + "." + str(to_decimal(trame[2][1]))
    return ip
