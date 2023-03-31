# Visualisateur de trafic réseau
Projet d'un visualisateur de trafic réseau dans le cadre d'une UE - Sorbonne Université  

Nous avons choisi de coder notre projet en Python pour sa simplicité et ses nombreux modules prédéfinis. 
# Structure 
Le projet est consitué de huits fichiers .py pour le code et deux fichiers .txt.

  - trame.txt : fichier .txt contenant plusieurs trames écrit en hexadécimal (copié depuis WireShark)


  - outils.py : fichier contenant des fonctions outils pour notre projet

  - lecture.py : 
    Le fichier est composé d'une fonction lecture(file) qui va lire le fichier trame.txt et analyser toute les trames qui s'y trouvent.
    

  - ethernet.py :
       
    Le fichier est composé de deux fonctions et son rôle principal est de capturer les informations importante de la couche ethernet.
        
    destination(trame) : prend en argument une trame et retourne l'adresses MAC destination d'une trame 

    source(trame) : prend en argument une trame et retourne l'adresses MAC source d'une trame 
 
  - ip.py :
     
    Le fichier est composé de trois fonctions et son rôle principal est de capturer les informations importante de la couche IP.

    verify(trame) : prend en argument un trame et verifie si la trame utilise bien IP
        
    destination(trame) : prend en argument une trame et retourne l'adresses IP destination d'une trame 

    source(trame) : prend en argument une trame et retourne l'adresses IP source d'une trame 

  - tcp.py :
       
    Le fichier est composé de huits fonctions et son rôle principal est de capturer les informations importante de la couche TCP.

    verify(trame) : prend en argument une trame et verifie si la trame utilise bien le protocole TCP
       
    portdest(trame) : prend en argument une trame et retourne le port destination d'une trame 

    portsource(trame) : prend en argument une trame et retourne le port source d'une trame 

    flags(trame) : prend en argument une trame et retourne les drapeaux capturés d'une trame

    ainsi que 4 autres fonctions qui prennent en argument une trame et retournent des informations pertinantes (ack, seq, win, len)

  - http.py :
       
    Le fichier est composé de deux fonctions et son rôle principal est de capturer les informations importante de la couche HTTP.
        
    verify(trame) : prend en argument une trame et verifie si la trame est une requete HTTP

    methodhttp(trame) : prend en argument une trame et retourne la requete HTTP

  - run.py :

    Ce fichier permet l'execution du projet.
    
    flow(trames, filtre_http, filtre_tcp, filtre_ip, filtre_ip_addr, filtre_port) : 
        Cette fonction prend en arguement la liste des trames renvoyé par la fonction lecture(file) du fichier lecture.py ainsi que les filtres choisis, et affiche le visualiseur du flux de trafic
    
    table_flux(trames, filtre_http, filtre_tcp, filtre_ip, filtre_ip_addr, filtre_port) : 
        Cette fonction prend en arguement la liste des trames renvoyé par la fonction lecture(file) du fichier lecture.py ainsi que les filtres choisis, et affiche un tableau avec toutes les informations qui concernent les trames flitrés. 
    
      
      
      
     
      
      