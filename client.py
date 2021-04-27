import socket
import pygame

''' #Le client a une addresse et un port(le meme que le serveur donc) : '''
host = 'localhost' 
port = 5567  

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Création d'une comminication en utilisant les 2 familles les plus courantes que l'on va utilisées ( c comme un téléphone)
