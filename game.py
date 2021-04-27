import pygame
from board import Board
from piece import *

class Game() :
    def __init__(self) :
        self.board = Board()

        self.au_tour_de = "Blanc"
        self.score = 0
        self.gagnant = "None"
        self.FIN = False

        self.list_pieces_dead_white = []
        self.list_pieces_dead_black = []