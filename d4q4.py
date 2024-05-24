﻿
# Auteur : Sophie Séguin
# Numero d'étudiant : 300225009
# et 
# Auteur : Christine Peters
# Numéro d'étudiant : 300072385

###########################################################


# Jeu de cartes.

# L'ordinateur est le donneur des cartes.

# Une carte est une chaine de 2 caractères. 
# Le premier caractère représente une valeur et le deuxième une couleur.
# Les valeurs sont des caractères comme '2','3','4','5','6','7','8','9','10','J','Q','K', et 'A'.
# Les couleurs sont des caractères comme : ♠, ♡, ♣, et ♢.
# On utilise 4 symboles Unicode pour représenter les 4 couleurs: pique, coeur, trèfle et carreau.
# Pour les cartes de 10 on utilise 3 caractères, parce que la valeur '10' utilise deux caractères.

import random

#ces premieres fonctions sont deja completees pour vous, ne les changez pas

def attend_le_joueur():
    '''()->None
    Pause le programme jusqu'a ce que l'usager appuie Enter
    '''
    try:
         input("Appuyez Enter pour continuer. ")
    except SyntaxError:
         pass


def prepare_paquet():
    '''()->list of str
        Retourne une liste des chaines de caractères qui représente toutes les cartes,
        sauf le valet noir.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') # élimine le valet noir (le valet de trèfle)
    return paquet

def melange_paquet(p):
    '''(list of str)->None
       Melange la liste des chaines des caractères qui représente le paquet des cartes    
    '''
    random.shuffle(p)
    
#######################################################################################
#Les fonctions precedentes sont deja completees
#Completez les fonctions apres ce commentaire
#######################################################################################
    
def donne_cartes(p):
     '''(list of str)-> tuple of (list of str,list of str)

     Retournes deux listes qui représentent les deux mains des cartes.  
     Le donneur donne une carte à l'autre joueur, une à lui-même,
     et ça continue jusqu'à la fin du paquet p.
     '''
     
     donneur=[]
     autre=[]
     for i in range(len(p)):
        if i%2==0:
            autre.append(p[i])
        else:
            donneur.append(p[i])

     return (donneur, autre)


def elimine_paires(l):
    '''
     (list of str)->list of str

     Retourne une copie de la liste l avec toutes les paires éliminées 
     et mélange les éléments qui restent.

     Test:
     (Notez que l’ordre des éléments dans le résultat pourrait être différent)
     
     >>> elimine_paires(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> elimine_paires(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    resultat=[]
    l.sort()

    for e in range(len(l)):
        paire=e
        count=0
        i=0
        while count==0 and i<len(l):
            # l[i] nous donne le ième élément et len(l[i]) nous donne sa longueur
            # ainsi,  l[i][0:len(l[i])] nous retourne le premier caractere de l[i] jusqu'à l'avant dernier
            # comme les symboles se trouvent à la dernière position de chaque élément
            # ceci teste si les nombres sont égaux
            if i!= e and l[i][0:len(l[i])-1] == l[e][0:len(l[e])-1]:
                count += 1
                paire = i
            else:
                i +=1
        if count == 0:
            resultat.append(l[e])
        else:
            #on supprime les paires et insère une entrée vide pour ne pas changer la longueur de la liste
            # on les élimine pour qu'ils ne soient pas considérer comme candidats d'autres paires dans la liste
            del(l[paire])
            l.insert(paire,'')
            del(l[e])
            l.insert(e,'')
    random.shuffle(resultat)
    return resultat


def affiche_cartes(p):
    '''
    (list)-None
    Affiche les éléments de la liste p séparées par d'espaces
    '''
    for e in p:
        print(e, end = ' ')
    print('') # pour qu'une nouvelle ligne commence
    

def entrez_position_valide(n):
     '''
     (int)->int
     Retourne un entier lu au clavier, de 1 à n (1 et n inclus).
     Continue à demander si l'usager entre un entier qui n'est pas entre 1 et n

     Précondition: n>=1
     '''
     # on commence en initialisant k, la variable pour la position, à 0.
     # Après la premier entrée au clavier, on vérifie d'abord si l'entrée est un entier; si oui, on affecte sa valeur à k
     # on ajoute cette partie avant la boucle pour qu'on ait un message d'erreur dans la boucle
     k = 0
     k = int(input("J'ai "+str(n)+" cartes. Si 1 est la position de ma première carte et \n"+str(n)+" est la position de ma dernière carte, laquelle de mes cartes vous voulez? "))
     # dans la boucle, on veut s'en sortir si k>=1 et k <=n. Le complément est si k<1 ou k >n
     # dans ce cas, on reste dans la boucle
     while k<1 or k > n:
         print("Mauvaise entrée. Réessayez.")
         k = int(input("J'ai "+str(n)+" cartes. Si 1 est la position de ma première carte et \n"+str(n)+" est la position de ma dernière carte, laquelle de mes cartes vous voulez? "))
         
    # pour afficher quelle carte est choisie
     if k == 1:
         print("Vous avez demande ma 1ère carte.")
     else:
         print("Vous avez demande ma "+str(k)+"ème carte.")
    # comme la ième carte correspond à la i-1 ième position, on retourne k-1
     return k-1

def joue():
     '''()->None
     Cette fonction joue le jeu'''
     # préparation du jeu
     p=prepare_paquet()
     melange_paquet(p)
     tmp=donne_cartes(p)
     donneur=tmp[0]
     humain=tmp[1]

     # tour 0
     print("Bonjour. Je m'appelle Robot et je distribue les cartes.")
     print("Votre main est:")
     affiche_cartes(humain)
     print("Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.")
     print("Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.")
     attend_le_joueur()
     
     donneur=elimine_paires(donneur)
     humain=elimine_paires(humain)

     # pour représenter à qui jouer, on va utiliser une variable tour qui est 1 lorsque c'est au humain à joueur
     # et 0 si c'est le tour du robot
     # l'humain commence toujours en premier

     tour = 1

     # tour humain
     while tour == 1 and (len(humain)>0 and len(donneur)>0):
         if tour == 1:
             # tour humain
             print("Votre tour.")
             print("Votre main est:")
             affiche_cartes(humain)
             carte = entrez_position_valide(len(donneur))
             print("La voila. C'est un", donneur[carte])
             humain.append(donneur[carte])
             print("Avec", donneur[carte], "ajouté, votre main est:")
             affiche_cartes(humain)
             del(donneur[carte])
             
             humain=elimine_paires(humain)
             print("Après avoir défaussé toutes les paires et mélangé les cartes, votre main est:")
             affiche_cartes(humain)
             attend_le_joueur()
             tour = 0
             
         if tour ==0 and (len(humain)>0 and len(donneur)>0):
            # tour robot
            print("Mon tour.")
            carte = random.randint(0,len(humain)-1)
            if carte == 0:
                 print("J'ai pris votre 1ère carte.")
            else:
                 print("J'ai pris votre "+str(carte+1)+"ème carte.")
            donneur.append(humain[carte])
            del(humain[carte])
            donneur=elimine_paires(donneur)
            attend_le_joueur()
            tour = 1

     if len(humain)==0:
         print("Vous avez terminé toutes les cartes. \n Félicitations! Vous, Humain, vous avez gagné.")
     if len(donneur)==0:
         print("J'ai terminé toutes les cartes. \n Vous avez perdu! Moi, Robot, j'ai gagné.")
	 
# programme principale deja completé
joue()


##################################################################################################################
'''
Un exemple de partie gagnee par Humain:
---------------------------------------

Bonjour. Je m'appelle Robot et je distribue les cartes.
Votre main est:
7♡ 4♠ 9♣ 5♣ 9♠ Q♡ A♠ 10♢ J♠ 5♡ 7♢ 6♢ 10♠ Q♢ 4♡ Q♣ J♡ 7♠ 6♡ 6♠ 3♠ 3♢ 8♠ 10♣ K♢ 6♣ 
Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.
Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.
Appuyez Enter pour continuer. 
***********************************************************
Votre tour.
Votre main est:
A♠ 7♢ Q♣ K♢ 10♣ 8♠ 
J'ai 7 cartes. Si 1 est la position de ma première carte et
7 est la position de ma dernière carte, laquelle de mes cartes vous voulez?
SVP entrer un entier de 1 à 7: 6
Vous avez demande ma 6ème carte.
La voila. C'est un A♣
Avec A♣ ajouté, votre main est:
A♠ 7♢ Q♣ K♢ 10♣ 8♠ A♣ 
Après défaussé toutes les paires et mélanger les cartes, votre main est:
8♠ Q♣ 10♣ 7♢ K♢ 
Appuyez Enter pour continuer. 
***********************************************************
Mon tour.
J'ai pris votre 2ème carte.
Appuyez Enter pour continuer. 
***********************************************************
Votre tour.
Votre main est:
8♠ 10♣ 7♢ K♢ 
J'ai 5 cartes. Si 1 est la position de ma première carte et
5 est la position de ma dernière carte, laquelle de mes cartes vous voulez?
SVP entrer un entier de 1 à 5: 3
Vous avez demande ma 3ème carte.
La voila. C'est un 10♡
Avec 10♡ ajouté, votre main est:
8♠ 10♣ 7♢ K♢ 10♡ 
Après défaussé toutes les paires et mélanger les cartes, votre main est:
7♢ 8♠ K♢ 
Appuyez Enter pour continuer. 
***********************************************************
Mon tour.
J'ai pris votre 1ère carte.
Appuyez Enter pour continuer. 
***********************************************************
Votre tour.
Votre main est:
8♠ K♢ 
J'ai 3 cartes. Si 1 est la position de ma première carte et
3 est la position de ma dernière carte, laquelle de mes cartes vous voulez?
SVP entrer un entier de 1 à 3: 1
Vous avez demande ma 1ère carte.
La voila. C'est un K♣
Avec K♣ ajouté, votre main est:
8♠ K♢ K♣ 
Après défaussé toutes les paires et mélanger les cartes, votre main est:
8♠ 
Appuyez Enter pour continuer. 
***********************************************************
Mon tour.
J'ai pris votre 1ère carte.
Appuyez Enter pour continuer. 
***********************************************************
J'ai terminé toutes les cartes.
Felicitations! Vous, Humain, vous avez gagné.
>>> 
'''

##################################################################################################################
'''
Un exemple de partie gagnee par Robot:
---------------------------------------

Bonjour. Je m'appele Robot et je donne les cartes.
Votre main de cartes est:
3♣ 6♣ 2♢ 10♡ 10♠ 8♢ 5♣ Q♣ 4♡ 8♠ 5♠ J♢ 3♢ A♠ 7♡ 3♠ A♣ 9♡ 3♡ 9♣ 8♣ 6♠ 7♣ 6♢ K♠ Q♠ 
Ne vous inquitez pas, je ne peux pas voir votres cartes ou leur ordre.
Maintenant defaussez toutes les paires de votre main. Je vais faire ca aussi.
Appuyez Enter pour continuer. 
***********************************************************
Votre tour.
Votre main est:
4♡ 2♢ J♢ 6♣ 8♣ K♠ 
J'ai 5 cartes. Si 1 est la position de ma premiere carte et
5 est la position de ma derniere carte, laquelle de mes cartes vous voulez?
SVP entrer un entier de 1 a 5: 5
Vous avez demande ma 5-eme carte.
La voila. C'est un K♣
Avec K♣ ajoute, votre main est:
4♡ 2♢ J♢ 6♣ 8♣ K♠ K♣ 
Apres defausser toutes les paires et melanger les cartes, votre main est:
J♢ 6♣ 8♣ 4♡ 2♢ 
Appuyez Enter pour continuer. 
***********************************************************
Mon tour.
J'ai pris votre 2-eme carte.
Appuyez Enter pour continuer. 
***********************************************************
Votre tour.
Votre main est:
J♢ 8♣ 4♡ 2♢ 
J'ai 3 cartes. Si 1 est la position de ma premiere carte et
3 est la position de ma derniere carte, laquelle de mes cartes vous voulez?
SVP entrer un entier de 1 a 3: 3
Vous avez demande ma 3-eme carte.
La voila. C'est un 8♡
Avec 8♡ ajoute, votre main est:
J♢ 8♣ 4♡ 2♢ 8♡ 
Apres defausser toutes les paires et melanger les cartes, votre main est:
4♡ 2♢ J♢ 
Appuyez Enter pour continuer. 
***********************************************************
Mon tour.
J'ai pris votre 2-eme carte.
Appuyez Enter pour continuer. 
***********************************************************
Votre tour.
Votre main est:
4♡ J♢ 
J'ai 1 cartes. Si 1 est la position de ma premiere carte et
1 est la position de ma derniere carte, laquelle de mes cartes vous voulez?
SVP entrer un entier de 1 a 1: 1
Vous avez demande ma 1-ere carte.
La voila. C'est un 4♣
Avec 4♣ ajoute, votre main est:
4♡ J♢ 4♣ 
Apres defausser toutes les paires et melanger les cartes, votre main est:
J♢ 
Appuyez Enter pour continuer. 
J'ai terminé toutes les cartes.
Vous avez perdu! Moi, Robot, j'ai gagné.
>>> 
'''
##################################################################################################################