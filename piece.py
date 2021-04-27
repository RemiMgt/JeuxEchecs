import pygame

longueur, hauteur = 75, 75 

class Pion(pygame.sprite.Sprite) :

    def __init__(self, couleur, posx, posy, nom) :
        super().__init__()
        self.couleur = couleur
        self.base = True
        self.nom = nom
        self.a_une_image = True
        if self.couleur == "blanc" :
            self.image = pygame.image.load("assets/piece/pion_blanc.png")
            self.image = pygame.transform.scale(self.image, (longueur, hauteur))
            self.rect = self.image.get_rect()
        else :
            self.image = pygame.image.load("assets/piece/pion_noir.png")
            self.image = pygame.transform.scale(self.image, (longueur, hauteur))
            self.rect = self.image.get_rect()

        self.rect.x = posx 
        self.rect.y = posy 

    

class Cavalier(pygame.sprite.Sprite) :

    def __init__(self, couleur, posx, posy, nom) :
        super().__init__()
        self.couleur = couleur
        self.base = True
        self.nom = nom
        self.a_une_image = True
        if self.couleur == "blanc" :
            self.image = pygame.image.load("assets/piece/cavalier_blanc.png")
            self.image = pygame.transform.scale(self.image, (longueur, hauteur))
            self.rect = self.image.get_rect()
        else :
            self.image = pygame.image.load("assets/piece/cavalier_noir.png")
            self.image = pygame.transform.scale(self.image, (longueur, hauteur))
            self.rect = self.image.get_rect()

        self.rect.x = posx 
        self.rect.y = posy 

class Fou(pygame.sprite.Sprite) :

    def __init__(self, couleur, posx, posy, nom, couleur_case) :
        super().__init__()
        self.couleur = couleur
        self.base = True
        self.nom = nom
        self.a_une_image = True
        self.couleur_case = couleur_case
        if self.couleur == "blanc" :
            self.image = pygame.image.load("assets/piece/fou_blanc.png")
            self.image = pygame.transform.scale(self.image, (longueur, hauteur))
            self.rect = self.image.get_rect()
        else :
            self.image = pygame.image.load("assets/piece/fou_noir.png")
            self.image = pygame.transform.scale(self.image, (longueur, hauteur))
            self.rect = self.image.get_rect()

        self.rect.x = posx 
        self.rect.y = posy 

class Dame(pygame.sprite.Sprite) :

    def __init__(self, couleur, posx, posy, nom) :
        super().__init__()
        self.couleur = couleur
        self.base = True
        self.nom = nom
        self.a_une_image = True
        if self.couleur == "blanc" :
            self.image = pygame.image.load("assets/piece/dame_blanc.png")
            self.image = pygame.transform.scale(self.image, (longueur, hauteur))
            self.rect = self.image.get_rect()
        else :
            self.image = pygame.image.load("assets/piece/dame_noir.png")
            self.image = pygame.transform.scale(self.image, (longueur, hauteur))
            self.rect = self.image.get_rect()

        self.rect.x = posx 
        self.rect.y = posy 


class Roi(pygame.sprite.Sprite) :

    def __init__(self, couleur, posx, posy, nom) :
        super().__init__()
        self.couleur = couleur
        self.base = True
        self.nom = nom
        self.a_une_image = True
        if self.couleur == "blanc" :
            self.image = pygame.image.load("assets/piece/roi_blanc.png")
            self.image = pygame.transform.scale(self.image, (longueur, hauteur))
            self.rect = self.image.get_rect()
        else :
            self.image = pygame.image.load("assets/piece/roi_noir.png")
            self.image = pygame.transform.scale(self.image, (longueur, hauteur))
            self.rect = self.image.get_rect()

        self.rect.x = posx 
        self.rect.y = posy 

class Tour(pygame.sprite.Sprite) :

    def __init__(self, couleur, posx, posy, nom) :
        super().__init__()
        self.couleur = couleur
        self.base = True
        self.nom = nom
        self.a_une_image = True
        if self.couleur == "blanc" :
            self.image = pygame.image.load("assets/piece/tour_blanc.png")
            self.image = pygame.transform.scale(self.image, (longueur, hauteur))
            self.rect = self.image.get_rect()
        else :
            self.image = pygame.image.load("assets/piece/tour_noir.png")
            self.image = pygame.transform.scale(self.image, (longueur, hauteur))
            self.rect = self.image.get_rect()

        self.rect.x = posx 
        self.rect.y = posy 
