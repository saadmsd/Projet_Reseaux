from outils import *

def verify(trame):
    return ((trame[1][7]) == "06")

def portdest(trame):
    port = to_decimal(trame[2][4] + trame[2][5])
    return port

def portsource(trame):
    port = to_decimal(trame[2][2] + trame[2][3])
    return port

def flags(trame):
    #return the flags if they are set in a table
    flags = to_decimal(trame[2][14][1]+trame[2][15])
    flags = bin(flags)[2:].zfill(12)
    res = []
    if (flags[6] == '1'):
        res.append("URG")
    if (flags[7] == '1'):
        res.append("ACK")
    if (flags[8] == '1'):
        res.append("PSH")
    if (flags[9] == '1'):
        res.append("RST")
    if (flags[10] == '1'):
        res.append("SYN")
    if (flags[11] == '1'):
        res.append("FIN")
    return res


def lenght(trame):
    total_lenght = to_decimal(trame[1][0] + trame[1][1]) - to_decimal(trame[0][14][1])*4
    tcplen = total_lenght - to_decimal(trame[2][14][0])*4
    return tcplen

def ack(trame):
    ack = to_decimal(trame[2][10] + trame[2][11] + trame[2][12] + trame[2][13])
    return ack

def seq(trame):
    seq = to_decimal(trame[2][6] + trame[2][7] + trame[2][8] + trame[2][9])
    return seq

def window(trame):
    window = to_decimal(trame[3][0] + trame[3][1])
    return window
