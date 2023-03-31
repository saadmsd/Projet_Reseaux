import ethernet as eth
import ip
import tcp
import Http
from outils import *
from lecture import lecture
import sys
import os
# module qui permet de mettre des couleurs à un texte en mode console 
from rich.console import Console
console = Console()
# module qui permet de visualiser des tables sur un terminal 
from rich.table import Table
# module qui permet de facilité les communication entre l'utilisateur et le programme
from rich.prompt import Prompt


def flow(trames, filtre_http, filtre_tcp, filtre_ip, filtre_ip_addr, filtre_port):
    console.print("\n[u]Flow graph[/u]", style = "bold yellow")
    i = 0
    sources = []
    ips = dict()
    for trame in trames:
        i+=1
       # les ips passées dans la liste des trames
        if ip.source(trame) not in sources:
            ips[ip.source(trame)] = i
        
        #HTTP
        if(filtre_http and ip.verify(trame) and tcp.verify(trame) and Http.verify(trame)):
            if filtre_ip_addr == "" or filtre_ip_addr == ip.source(trame) or filtre_ip_addr == ip.destination(trame):
                if filtre_port == "" or filtre_port == str(tcp.portsource(trame)) or filtre_port == str(tcp.portdest(trame)):

                    if (ip.destination(trame) in sources and ip.source(trame) not in sources) or ip.destination(trame) in sources and ip.source(trame) in sources and ips[ip.source(trame)] > ips[ip.destination(trame)]:
                        print("\n")
                        console.print(ip.destination(trame)+"\t"*12+ip.source(trame))
                        console.print("\t"*6+Http.methodhttp(trame))
                        console.print("   "+str(tcp.portdest(trame))+"[b][red]<<[/b][/red]"+"[bold red]-[/bold red]"*100 + str(tcp.portsource(trame)))
                    else :
                        print("\n")
                        console.print(ip.source(trame),"\t"*12, ip.destination(trame))
                        console.print("\t"*6,Http.methodhttp(trame))
                        console.print("   "+str(tcp.portsource(trame))+"[bold magenta]-[/bold magenta]"*100+"[bold magenta]>>[/bold magenta]"+str(tcp.portdest(trame)))
                        #print(eth.source(trame),"\t"*11, eth.destination(trame))
       #TCP
        elif(filtre_tcp and ip.verify(trame) and tcp.verify(trame)):
            if filtre_ip_addr == "" or filtre_ip_addr == ip.source(trame) or filtre_ip_addr == ip.destination(trame):
                if filtre_port == "" or filtre_port == str(tcp.portsource(trame)) or filtre_port == str(tcp.portdest(trame)):

                    if (ip.destination(trame) in sources and ip.source(trame) not in sources) or ip.destination(trame) in sources and ip.source(trame) in sources and ips[ip.source(trame)] > ips[ip.destination(trame)]:
                        print("\n")
                        console.print(ip.destination(trame)+"\t"*12+ip.source(trame))
                        console.print("\t\t"+str(tcp.flags(trame))+" Seq = "+str(tcp.seq(trame))+" Ack = "+str(tcp.ack(trame))+" Win = "+str(tcp.window(trame))+" Len = "+str(tcp.lenght(trame)))
                        console.print("   "+str(tcp.portdest(trame))+"[bold red]<<[/bold red]"+"[bold red]-[/bold red]"*100+str(tcp.portsource(trame)))
                    else :
                        print("\n")
                        console.print(ip.source(trame)+"\t"*12+ip.destination(trame))
                        console.print("\t\t"+str(tcp.flags(trame))+" Seq = "+str(tcp.seq(trame))+" Ack = "+str(tcp.ack(trame))+" Win = "+str(tcp.window(trame))+" Len = "+str(tcp.lenght(trame)))
                        console.print("   "+str(tcp.portsource(trame))+"[bold magenta]-[/bold magenta]"*100+"[bold magenta]>>[/bold magenta]"+str(tcp.portdest(trame)))
                        #print(eth.source(trame),"\t"*11, eth.destination(trame))
        
        
        elif(filtre_ip and ip.verify(trame)):
            if filtre_ip_addr == "" or filtre_ip_addr == ip.source(trame) or filtre_ip_addr == ip.destination(trame):

                if (ip.destination(trame) in sources and ip.source(trame) not in sources) or ip.destination(trame) in sources and ip.source(trame) in sources and ips[ip.source(trame)] > ips[ip.destination(trame)]:
                    print("\n")
                    print("IP source"+ip.source(trame)+"[bold red]<--------[/bold red] IP destination"+ip.destination(trame))
                else :
                    print("\n")
                    print("IP source"+ip.source(trame)+"[bold magenta]-------->[/bold magenta] IP destination"+ip.destination(trame))
                    #print("MAC source", eth.source(trame), "--------> MAC destination", eth.destination(trame))
        
        sources.append(ip.source(trame))
        
        
    return


def tableflux(trames, filtre_http, filtre_tcp, filtre_ip, filtre_ip_addr, filtre_port):
    
    table = Table(title="Table des flux de trafic réseau")

    table.add_column("No", justify="right", no_wrap=True)
    table.add_column("MACsrc  -> MACdst", justify="center", style="bold blue", no_wrap=True)
    table.add_column("IPsrc   -> IPdst ", justify="center", style="bold green")
    table.add_column("Portsrc -> Portdst", justify="center", style="bold cyan")
    table.add_column("Protocol", style="yellow")
    table.add_column("Infos")
    i = 0
    for trame in trames:
        i+=1
        
        #HTTP
        if(filtre_http and ip.verify(trame) and tcp.verify(trame) and Http.verify(trame)):
            if filtre_ip_addr == "" or filtre_ip_addr == ip.source(trame) or filtre_ip_addr == ip.destination(trame):
                if filtre_port == "" or filtre_port == str(tcp.portsource(trame)) or filtre_port == str(tcp.portdest(trame)):
                    table.add_row(str(i), eth.source(trame) + " -> " + eth.destination(trame),ip.source(trame) + " -> " + ip.destination(trame), str(tcp.portsource(trame)) + " -> " + str(tcp.portdest(trame)), "HTTP", Http.methodhttp(trame))

        #TCP
        elif(filtre_tcp and ip.verify(trame) and tcp.verify(trame)):
            if filtre_ip_addr == "" or filtre_ip_addr == ip.source(trame) or filtre_ip_addr == ip.destination(trame):            
                if filtre_port == "" or filtre_port == str(tcp.portsource(trame)) or filtre_port == str(tcp.portdest(trame)):
                    table.add_row(str(i), eth.source(trame) + " -> " + eth.destination(trame),ip.source(trame) + " -> " + ip.destination(trame), str(tcp.portsource(trame)) + " -> " + str(tcp.portdest(trame)), "TCP", str(tcp.flags(trame)) + " Seq = " + str(tcp.seq(trame)) + " Ack = " + str(tcp.ack(trame)) + " Win = " + str(tcp.window(trame)) + " Len = " + str(tcp.lenght(trame)))

        elif(filtre_ip and ip.verify(trame)):
            if filtre_ip_addr == "" or filtre_ip_addr == ip.source(trame) or filtre_ip_addr == ip.destination(trame):
                table.add_row(str(i), eth.source(trame) + " -> " + eth.destination(trame),ip.source(trame)+ " -> " +ip.destination(trame))

        #else :
        #    print("Trame {} non retenu".format(i))
            
    return table

console.print("\n!!!!!!!!!!!!!!!!!!!!!!! [u]Bienvenue sur notre Visualisateur de trafic réseau[/u] !!!!!!!!!!!!!!!!!!!!!!!\n", style = "bold yellow", justify="center")
fichier = console.input("Veuillez entrer le [cyan]nom du fichier text avec les trames[/cyan] : ")

while not os.path.isfile(fichier):
    console.print("Erreur: Fichier introuvable", style = "bold red")
    fichier = console.input("Veuillez entrer le [u][bold cyan]nom du fichier text avec les trames[/u][/bold cyan] : ")

trames = lecture(fichier)
table =tableflux(trames, filtre_http = True, filtre_tcp = True, filtre_ip = True, filtre_ip_addr = "", filtre_port = "")
console.print(table)
choix = ""
while True:
    filtre_http = True
    filtre_tcp = True
    filtre_ip = True
    filtre_ip_addr = ""
    filtre_port = ""
    choix = Prompt.ask("Voulez vous appliquer des filtres ?", choices = ["oui", "non", "quit"])
    if choix == "quit":
        console.print("[u]Merci d'avoir utilisé notre programme ![/u]\n", style = "bold yellow", justify = "center")
        exit()
    if choix == "oui":
        choix = Prompt.ask("Choisissez votre filtre", choices = ["http", "tcp", "ip", "port"])
        if choix == "http":
            os.system('clear')
            filtre_tcp = False
            filtre_ip = False
            table = tableflux(trames, filtre_http, filtre_tcp, filtre_ip, filtre_ip_addr, filtre_port)
            console.print(table)
        if choix == "tcp":
            os.system('clear')
            filtre_http = False
            filtre_ip = False
            table = tableflux(trames, filtre_http, filtre_tcp, filtre_ip, filtre_ip_addr, filtre_port)
            console.print(table)
        if choix == "ip":
            ip_addr = Prompt.ask("Choisissez une addresse ip")
            os.system('clear')
            filtre_ip_addr=ip_addr
            table = tableflux(trames, filtre_http, filtre_tcp, filtre_ip, filtre_ip_addr, filtre_port)
            console.print(table)

        if choix == "port":
            port_addr = Prompt.ask("Choisissez un numero port")
            os.system('clear')
            filtre_port=port_addr
            table = tableflux(trames, filtre_http, filtre_tcp, filtre_ip, filtre_ip_addr, filtre_port)
            console.print(table)
    choix2 = Prompt.ask("Voulez vous afficher le visualiseur ?", choices = ["oui", "non"])
    if choix2 == "oui":
        flow(trames, filtre_http, filtre_tcp, filtre_ip, filtre_ip_addr, filtre_port)
 
