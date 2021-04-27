#Importations : 
import pygame
from game import Game
from piece import *

import socket
import threading
import sys
import time
pygame.mixer.init()

''' A Faire :

        - liste des pieces mortes
        - minuteur peut etre
        - refaire déplacement fou
        - loïc = créer png des coords
        - Transformer cases disponible en vert
        - Roulette souris probléme = Equivalent à un clic
        - Problème pions 2 puis 1 quand on se déplace
'''

''' 
Pattern pieces : (68)
        - Tour : nombre commencant par 6 et terminant par 8
        - Fou : regarde si c'est la bonne couleur de l'échiquier

'''

tab_deplacement = [
    21, 22, 23, 24, 25, 26, 27, 28,
    31, 32, 33, 34, 35, 36, 37, 38,
    41, 42, 43, 44, 45, 46, 47, 48,
    51, 52, 53, 54, 55, 56, 57, 58,
    61, 62, 63, 64, 65, 66, 67, 68,
    71, 72, 73, 74, 75, 76, 77, 78,
    81, 82, 83, 84, 85, 86, 87, 88,
    91, 92, 93, 94, 95, 96, 97, 98
]

#Initialisation
pygame.init()

#Musique :
musique = "assets/musique.mp3"
pygame.mixer.music.load(musique)
pygame.mixer.music.play(-1)

#Timer :
color_timer = (255, 255 ,255)
timer_blanc = 600
timer_noir = 600
pygame.time.set_timer(pygame.USEREVENT, 1000)
timer_font = pygame.font.SysFont("arial", 50, True, False)
texte_timer_blanc = timer_font.render(str(timer_blanc), True, color_timer)
texte_timer_noir = timer_font.render(str(timer_noir), True, color_timer)
pendule = pygame.image.load("assets/PenduleDroite.png")
pendule = pygame.transform.scale(pendule, (800, 210))

#Bouton_exit :
width_bouton_exit = 200
height_bouton_exit = 100
bouton_exit = pygame.image.load("assets/Bouton_Exit.png")
bouton_exit = pygame.transform.scale(bouton_exit, (width_bouton_exit, height_bouton_exit))

#Variables :
cases_dispo_version_0 = []
image_echiquier = pygame.image.load("assets/échiquier.png")
historique_case_piece_touche = []
ancienne_coord_piece = 0

#Bruitage:

pygame.mixer.init()
son_1 = pygame.mixer.Sound("assets/mouvement_piece.wav")

#Cases disponible :
image_case_dispo = pygame.image.load("assets/vert.jpeg")
image_case_dispo = pygame.transform.scale(image_case_dispo, (100, 100))
image_case_dispo_ennemi = pygame.image.load("assets/rouge.png")
image_case_dispo_ennemi = pygame.transform.scale(image_case_dispo_ennemi, (100, 100))

#Création de la fenêtre :
pygame.display.set_caption("Jeux Echecs by Rémi")
fenetre = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
icon = pygame.image.load("assets/icon.png")
icon = pygame.transform.scale(icon, (32, 32))
pygame.display.set_icon(icon)
longueur, hauteur = fenetre.get_size()
print("longueur : ", longueur, "hauteur : ", hauteur)

#Tchat : (enregistre dans une file les messages puis quand c plein on defile)
width_tchat_box = longueur - 870
height_tchat_box = 800
chat_box = pygame.image.load("assets/TchatBox.png")
chat_box = pygame.transform.scale(chat_box, (width_tchat_box, height_tchat_box))
chat_color = ( 10, 41, 64 )
width_text_chat = 70
chat_font = pygame.font.SysFont("arial", width_text_chat, True, False)
text_chat = chat_font.render("Chat", True, chat_color)
x_text_chat = 870 + width_tchat_box / 2 - width_text_chat
fenetre.blit(chat_box, (870, 0))
fenetre.blit(text_chat, (x_text_chat, 25))


#Echiquier :
clair = pygame.image.load("assets/clair.png") 
clair = pygame.transform.scale(clair, (100, 100))
fonce = pygame.image.load("assets/fonce.png") 
fonce = pygame.transform.scale(fonce, (100, 100))

position_x= 0
position_y = 0


for loop in range(4) :

    for loop in range(4) :
        fenetre.blit(clair, (position_x , position_y))
        fenetre.blit(fonce, (position_x + 100, position_y))
        position_x += 200

    position_x = 0

    for loop in range(4) :
        fenetre.blit(fonce, (position_x, position_y + 100))
        fenetre.blit(clair, (position_x + 100, position_y + 100))
        position_x += 200

    position_x = 0
    position_y += 200

#Coord échiquier :
coord_color = (255, 255, 255)
coord_bas = ["a", "b", "c", "d", "e", "f", "g", "h"]
coord_droite = ["8", "7", "6", "5", "4", "3", "2", "1"]

coord_font = pygame.font.SysFont("arial", 30, True, False)
text_coord_bas = coord_font.render(coord_bas[0], True, coord_color)
text_coord_droite = coord_font.render(coord_droite[0], True, coord_color)

coord_bas_num = 40
coord_droite_num = 40

for loop in range(8) :
    text_coord_bas = coord_font.render(coord_bas[loop], True, coord_color)
    fenetre.blit(text_coord_bas, (coord_bas_num, 820))
    coord_bas_num += 100

for loop in range(8) :
    text_coord_droite = coord_font.render(coord_droite[loop], True, coord_color)
    fenetre.blit(text_coord_droite, (825, coord_droite_num))
    coord_droite_num += 100

#Fonctions :
def case_cliquee(mouse_x, mouse_y) :
    abscisse, ordonnee = int(mouse_x / 100), int(mouse_y / 100)
    numero_case = abscisse + 8*ordonnee 
    return numero_case

def return_coord(num) :
    position_x = 0
    position_y = 0

    #Position_y :
    if num >= 0 and num <= 7 :
        position_y = 0
    elif num >= 8 and num <= 15 :
        position_y = 100
    elif num >= 16 and num <= 23 :
        position_y = 200
    elif num >= 24 and num <= 31 :
        position_y = 300
    elif num >= 32 and num <= 39 :
        position_y = 400
    elif num >= 40 and num <= 47 :
        position_y = 500
    elif num >= 48 and num <= 55 :
        position_y = 600
    elif num >= 56 and num <= 63 :
        position_y = 700

    #Position_x :
    colonne1 =[0, 8, 16, 24, 32, 40, 48, 56]
    colonne2 =[1, 9, 17, 25, 33, 41, 49, 57]
    colonne3 =[2, 10, 18, 26, 34, 42, 50, 58]
    colonne4 =[3, 11, 19, 27, 35, 43, 51, 59]
    colonne5 =[4, 12, 20, 28, 36, 44, 52, 60]
    colonne6 =[5, 13, 21, 29, 37, 45, 53, 61]
    colonne7 =[6, 14, 22, 30, 38, 46, 54, 62]
    colonne8 =[7, 15, 23, 31, 39, 47, 55, 63]

    if num in colonne1 :
        position_x = 0
    elif num in colonne2 :
        position_x = 100
    elif num in colonne3 :
        position_x = 200
    elif num in colonne4 :
        position_x = 300
    elif num in colonne5 :
        position_x = 400
    elif num in colonne6 :
        position_x = 500
    elif num in colonne7 :
        position_x = 600
    elif num in colonne8 :
        position_x = 700

    return (position_x, position_y)

def converti_num_coord(tab_coord_dispo) :
    #Position_x :
    colonne1_x =[0, 8, 16, 24, 32, 40, 48, 56]
    colonne2_x =[1, 9, 17, 25, 33, 41, 49, 57]
    colonne3_x =[2, 10, 18, 26, 34, 42, 50, 58]
    colonne4_x =[3, 11, 19, 27, 35, 43, 51, 59]
    colonne5_x =[4, 12, 20, 28, 36, 44, 52, 60]
    colonne6_x =[5, 13, 21, 29, 37, 45, 53, 61]
    colonne7_x =[6, 14, 22, 30, 38, 46, 54, 62]
    colonne8_x =[7, 15, 23, 31, 39, 47, 55, 63]
    #Position_y :
    colonne1_y =[0, 1, 2, 3, 4, 5, 6, 7]
    colonne2_y =[8, 9, 10, 11, 12, 13, 14, 15]
    colonne3_y =[16, 17, 18, 19, 20, 21, 22, 23]
    colonne4_y =[24, 25, 26, 27, 28, 29, 30, 31]
    colonne5_y =[32, 33, 34, 35, 36, 37, 38, 39]
    colonne6_y =[40, 41, 42, 43, 44, 45, 46, 47]
    colonne7_y =[48, 49, 50, 51, 52, 53, 54, 55]
    colonne8_y =[56, 57, 58, 59, 60, 61, 62, 63]

    result = []
    index_abscisse = 0
    index_ordonne = 0
    coordonnee = ()
    for elt in tab_coord_dispo :
        x = 0
        y = 0
        if elt in colonne1_x :
            x = 0
        elif elt in colonne2_x :
            x = 100
        elif elt in colonne3_x :
            x = 200
        elif elt in colonne4_x :
            x = 300
        elif elt in colonne5_x :
            x = 400
        elif elt in colonne6_x :
            x = 500
        elif elt in colonne7_x :
            x = 600
        elif elt in colonne8_x :
            x = 700

        if elt in colonne1_y :
            y = 0
        elif elt in colonne2_y :
            y = 100
        elif elt in colonne3_y :
            y = 200
        elif elt in colonne4_y :
            y = 300
        elif elt in colonne5_y :
            y = 400
        elif elt in colonne6_y :
            y = 500
        elif elt in colonne7_y :
            y = 600
        elif elt in colonne8_y :
            y = 700
        coordonnee = (x, y)
        result.append(coordonnee)
    return result


def deplacement_piece(piece, coord) :

        position_inter = converti_num_coord([coord])

        position_x = position_inter[0][0]
        position_y = position_inter[0][1]

        #Déplacement des piéces dans le tableau self.cases dans board :
        ancienne_piece = game.board.cases[piece]
        game.board.cases[piece] = "vide"
        game.board.cases[coord] = ancienne_piece
        
        #Deplacement des piéces dans la fenêtre : #Problèmes = il faut changer les variables dans board directement
        pygame.mixer.Sound.play(son_1)
        game.board.cases[coord].rect = (position_x + 12, position_y + 12, 75, 75)

def Quit_Pygame() :
    print("Fermeture des echecs !")
    boucle = False
    pygame.quit()
    sys.exit()


#Instance de la classe game :
game = Game()

#Casee cliqué :
case_clique = 0
selection_blanc = False

#Moteur de jeux :
boucle = True
while boucle :

    x, y = pygame.mouse.get_pos() 

    #Tchat :
    fenetre.blit(chat_box, (870, 0))
    fenetre.blit(text_chat, (x_text_chat, 25))

    #Pendule :
    fenetre.blit(pendule, (0, 870))
    fenetre.blit(texte_timer_blanc, (200, 960))
    fenetre.blit(texte_timer_noir, (500, 960))
    texte_timer_blanc = timer_font.render(str(timer_blanc), True, color_timer)
    texte_timer_noir = timer_font.render(str(timer_noir), True, color_timer)

    #Bouton_exit :
    fenetre.blit(bouton_exit, (longueur - width_bouton_exit, 0))
    if x>= longueur - width_bouton_exit and y <= 100 :
        width_bouton_exit = 205
    else :
        width_bouton_exit = 200

    #Pieces :
    for elt in game.board.cases :
        if elt != "vide" :
            fenetre.blit(elt.image, elt.rect)

    #Affichages des cases dispos :
    for elt in cases_dispo_version_0 :
        fenetre.blit(image_case_dispo, (return_coord(elt)))

    #Flip :
    pygame.display.flip()

    #Evenements :
    for event in pygame.event.get() :

        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE :
            Quit_Pygame()

        #Timer :
        if event.type == pygame.USEREVENT :
            timer_blanc -= 1
            timer_noir -= 1

        if event.type == pygame.MOUSEBUTTONDOWN :

            if x>= longueur - width_bouton_exit and y <= 100 :
                Quit_Pygame()

            if x >= 0 and x <= 800 and y >= 0 and y <= 800 :


                #Déplacement de la piéce active :
                if selection_blanc == True :
                    if case_cliquee(x, y) in cases_dispo_version_0 : #Si on clique sur une case verte
                        case_verte_clique = case_cliquee(x, y)
                        ancienne_coord_piece = historique_case_piece_touche[len(historique_case_piece_touche) - 1]
                        deplacement_piece(ancienne_coord_piece, case_verte_clique)
                    cases_dispo_version_0 = []
                    fenetre.blit(image_echiquier, (0, 0))
                    selection_blanc = False
                    break


                #Définir les cases disponibles de la piece cliquée :
                position_case_touche = game.board.coord_num_nombre(case_cliquee(x, y)) 
                cases_dispo_version_0 = []
                cases_disponible = []

                if game.board.cases[case_cliquee(x, y)] != "vide" :
                    historique_case_piece_touche.append(case_cliquee(x, y))
                    selection_blanc = True
                    cases_dispo_version_0 = []
                    cases_disponible = []
                    fenetre.blit(image_echiquier, (0, 0))
                    cases_disponible = game.board.cases_disponible(game.board.cases[case_cliquee(x, y)], position_case_touche)
                else :
                    fenetre.blit(image_echiquier, (0, 0))
                    selection_blanc = False

                for elt in cases_disponible :
                    cases_dispo_version_0.append(tab_deplacement.index(elt))
                    
            
