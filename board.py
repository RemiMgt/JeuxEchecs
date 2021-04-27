import pygame
from piece import *

coord=[
    'a8','b8','c8','d8','e8','f8','g8','h8',
    'a7','b7','c7','d7','e7','f7','g7','h7',
    'a6','b6','c6','d6','e6','f6','g6','h6',
    'a5','b5','c5','d5','e5','f5','g5','h5',
    'a4','b4','c4','d4','e4','f4','g4','h4',
    'a3','b3','c3','d3','e3','f3','g3','h3',
    'a2','b2','c2','d2','e2','f2','g2','h2',
    'a1','b1','c1','d1','e1','f1','g1','h1',
    ]


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

class Board() :

    def __init__(self) :
        super().__init__()

        #Création des pièces :
        self.pion = Pion
        self.cavalier = Cavalier
        self.fou = Fou
        self.dame = Dame
        self.roi = Roi
        self.tour = Tour

        #Positionnement des pièces :

        '''Blanc : '''
        #Pions
        self.posx_pion1_blanc = 12
        self.posy_pion1_blanc = 615
        self.posx_pion2_blanc = 112
        self.posy_pion2_blanc = 615
        self.posx_pion3_blanc = 212
        self.posy_pion3_blanc = 615
        self.posx_pion4_blanc = 312
        self.posy_pion4_blanc = 615
        self.posx_pion5_blanc = 412
        self.posy_pion5_blanc = 615
        self.posx_pion6_blanc = 512
        self.posy_pion6_blanc = 615
        self.posx_pion7_blanc = 612
        self.posy_pion7_blanc = 615
        self.posx_pion8_blanc = 712
        self.posy_pion8_blanc = 615
        #Tour
        self.posx_tour1_blanc = 12
        self.posy_tour1_blanc = 720
        self.posx_tour2_blanc = 712
        self.posy_tour2_blanc = 720
        #Cavalier
        self.posx_cavalier1_blanc = 112
        self.posy_cavalier1_blanc = 720
        self.posx_cavalier2_blanc = 612
        self.posy_cavalier2_blanc = 720
        #Fou
        self.posx_fou1_blanc = 212
        self.posy_fou1_blanc = 720
        self.posx_fou2_blanc = 512
        self.posy_fou2_blanc = 720
        #Roi
        self.posx_roi_blanc = 412
        self.posy_roi_blanc = 720
        #Dame
        self.posx_dame_blanc = 312
        self.posy_dame_blanc = 720

        '''noir : '''
        #Pions
        self.posx_pion1_noir = 12
        self.posy_pion1_noir = 118
        self.posx_pion2_noir = 112
        self.posy_pion2_noir = 118
        self.posx_pion3_noir = 212
        self.posy_pion3_noir = 118
        self.posx_pion4_noir = 312
        self.posy_pion4_noir = 118
        self.posx_pion5_noir = 412
        self.posy_pion5_noir = 118
        self.posx_pion6_noir = 512
        self.posy_pion6_noir = 118
        self.posx_pion7_noir = 612
        self.posy_pion7_noir = 118
        self.posx_pion8_noir = 712
        self.posy_pion8_noir = 118
        #Tour
        self.posx_tour1_noir = 12
        self.posy_tour1_noir = 18
        self.posx_tour2_noir = 712
        self.posy_tour2_noir = 18
        #Cavalier
        self.posx_cavalier1_noir = 112
        self.posy_cavalier1_noir = 18
        self.posx_cavalier2_noir = 612
        self.posy_cavalier2_noir = 18
        #Fou
        self.posx_fou1_noir = 212
        self.posy_fou1_noir = 18
        self.posx_fou2_noir = 512
        self.posy_fou2_noir = 18
        #Roi
        self.posx_roi_noir = 412
        self.posy_roi_noir = 18
        #Dame
        self.posx_dame_noir = 312
        self.posy_dame_noir = 18


        self.cases = [ #A modifier(pour les déplacements ...)

    self.tour("noir", self.posx_tour1_noir, self.posy_tour1_noir, "tour"),self.cavalier("noir", self.posx_cavalier1_noir, self.posy_cavalier1_noir, "cavalier"),self.fou("noir", self.posx_fou1_noir, self.posy_fou1_noir, "fou", "clair"),self.dame("noir", self.posx_dame_noir, self.posy_dame_noir, "dame"),self.roi("noir", self.posx_roi_noir, self.posy_roi_noir, "roi"),self.fou("noir", self.posx_fou2_noir, self.posy_fou2_noir, "fou", "fonce"),self.cavalier("noir", self.posx_cavalier2_noir, self.posy_cavalier2_noir, "cavalier"),self.tour("noir", self.posx_tour2_noir, self.posy_tour2_noir, "tour"),
    self.pion("noir", self.posx_pion1_noir, self.posy_pion1_noir, "pion"),self.pion("noir", self.posx_pion2_noir, self.posy_pion2_noir, "pion"),    self.pion("noir", self.posx_pion3_noir, self.posy_pion3_noir, "pion"),self.pion("noir", self.posx_pion4_noir, self.posy_pion4_noir, "pion"),self.pion("noir", self.posx_pion5_noir, self.posy_pion5_noir, "pion"),self.pion("noir", self.posx_pion6_noir, self.posy_pion6_noir, "pion"),self.pion("noir", self.posx_pion7_noir, self.posy_pion7_noir, "pion"),self.pion("noir", self.posx_pion8_noir, self.posy_pion8_noir, "pion"),
    "vide",          "vide",                "vide",           "vide",           "vide",           "vide",           "vide",           "vide",
    "vide",          "vide",                "vide",           "vide",           "vide",           "vide",           "vide",           "vide",
    "vide",          "vide",                "vide",           "vide",           "vide",           "vide",           "vide",           "vide",
    "vide",          "vide",                "vide",           "vide",           "vide",           "vide",           "vide",           "vide",
    self.pion("blanc", self.posx_pion1_blanc, self.posy_pion1_blanc, "pion"),self.pion("blanc", self.posx_pion2_blanc, self.posy_pion2_blanc, "pion"),    self.pion("blanc", self.posx_pion3_blanc, self.posy_pion3_blanc, "pion"),self.pion("blanc", self.posx_pion4_blanc, self.posy_pion4_blanc, "pion"),self.pion("blanc", self.posx_pion5_blanc, self.posy_pion5_blanc, "pion"),self.pion("blanc", self.posx_pion6_blanc, self.posy_pion6_blanc, "pion"),self.pion("blanc", self.posx_pion7_blanc, self.posy_pion7_blanc, "pion"),self.pion("blanc", self.posx_pion8_blanc, self.posy_pion8_blanc, "pion"),
    self.tour("blanc", self.posx_tour1_blanc, self.posy_tour1_blanc, "tour"),self.cavalier("blanc", self.posx_cavalier1_blanc, self.posy_cavalier1_blanc, "cavalier"),self.fou("blanc", self.posx_fou1_blanc, self.posy_fou1_blanc, "fou", "fonce"),self.dame("blanc", self.posx_dame_blanc, self.posy_dame_blanc, "dame"),self.roi("blanc", self.posx_roi_blanc, self.posy_roi_blanc, "roi"),self.fou("blanc", self.posx_fou2_blanc, self.posy_fou2_blanc, "fou", "clair"),self.cavalier("blanc", self.posx_cavalier2_blanc, self.posy_cavalier2_blanc, "cavalier"),self.tour("blanc", self.posx_tour2_blanc, self.posy_tour2_blanc, "tour")

                    ]

    def coord_num_lettre(self, coordonne) : #Coordonne --> 2 / 4 / 5 ...
        return coord[coordonne] #Return a8 / c3 ...

    def coord_num_nombre(self, coordonne) : #Coordonnee --> 2 / 4 / 5
        return tab_deplacement[coordonne] #Return 65 30 ..


    def cases_disponible(self, piece, coordonne) : #Coord(a9...)
        result = []
        coord_tab_deplacement = coordonne #(65 13 ...)
        deplacements_tour = [-10, -20, -30, -40, -50, -60, -70, -80, 10, 20, 30, 40, 50, 60, 70, 80,-1, -2, -3, -4, -5, -6, -7, -8, 1, 2, 3, 4, 5, 6, 7, 8]
        deplacements_fou = [-11, -22, -33, -44, -55, -66, -77, -88,-9, -18, -27, -36, -45, -54, -63, -72,11, 22, 33, 44, 55, 66, 77, 88,9, 18, 27, 36, 45, 54, 63, 72]
        deplacements_cavalier = [-12,-21,-19,-8,12,21,19,8]
        deplacements_roi = [-11, -10, -9, -1, 1, 9, 10, 11]
        deplacements_dame = deplacements_fou + deplacements_tour
        deplacements_pion = [-10, -20]

        if piece.nom == "tour" :
            tab_piece = list(str(coordonne))
            for elt in deplacements_tour :
                for nombre in tab_deplacement :
                    tab_nombre = list(str(nombre))
                    if nombre == coordonne + elt and self.cases[tab_deplacement.index(nombre)] == "vide":
                        if tab_nombre[0] == tab_piece[0] or tab_nombre[1] == tab_piece[1]:
                            result.append(nombre)

        elif piece.nom == "cavalier" :
            for elt in deplacements_cavalier :
                for nombre in tab_deplacement :
                    if nombre == coordonne + elt and self.cases[tab_deplacement.index(nombre)] == "vide" :
                        result.append(nombre)

        elif piece.nom == "fou" :
            couleur_casee = piece.couleur_case
            for elt in deplacements_fou :
                for nombre in tab_deplacement :
                    if nombre == coordonne + elt  and self.cases[tab_deplacement.index(nombre)] == "vide" :
                        result.append(nombre)

        elif piece.nom == "roi" :
            for elt in deplacements_roi :
                for nombre in tab_deplacement :
                    if nombre == coordonne + elt  and self.cases[tab_deplacement.index(nombre)] == "vide" :
                        result.append(nombre)

        elif piece.nom == "dame" :
            for elt in deplacements_dame :
                for nombre in tab_deplacement :
                    if nombre == coordonne + elt and self.cases[tab_deplacement.index(nombre)] == "vide" :
                        result.append(nombre)

        elif piece.nom == "pion" :
            for elt in deplacements_pion :
                for nombre in tab_deplacement :
                    if nombre == coordonne + elt  and self.cases[tab_deplacement.index(nombre)] == "vide" :
                        result.append(nombre)

        return result