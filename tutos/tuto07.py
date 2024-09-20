#-*- coding:utf-8 -*-
import pygame
from pygame.locals import *

## Initialisation de la fenetre et crÃ©ation
pygame.init()
#creation de la fenetre

largeur = 640
hauteur = 480
fenetre=pygame.display.set_mode((largeur,hauteur))

## Lecture des differentes images.
# lecture de l'image du fond
imageFond = pygame.image.load("background.jpg").convert()
# lecture de l'image du perso
imagePerso = pygame.image.load("perso.png").convert_alpha()

# Choix de la police pour le texte
font = pygame.font.Font(None, 34)

# Creation de la surface correspondant au texte
imageText = font.render('<Escape> pour quitter', True, (255, 255, 255))

# recuperation du rectangle du texte
rectText = imageText.get_rect()
# positionnement du rectangle
rectText.x = 10
rectText.y = 10


# rectangle du personnage
rectPerso = imagePerso.get_rect()
rectPerso.x = 60
rectPerso.y = 80

# rectangle du fond
rectFond = imageFond.get_rect()


# servira a regler l'horloge du jeu
framerate = pygame.time.Clock()
continuer=1
while continuer:

    # fixons le nombre max de frames / secondes
    framerate.tick(20)

    # on recupere l'etat du clavier
    touches = pygame.key.get_pressed();

    if touches[K_SPACE] :
        print ("toto")

    if touches[K_ESCAPE] :
        continuer=0

    # Affichage du fond
    fenetre.blit(imageFond, rectFond)	

    # Affichage Perso
    fenetre.blit(imagePerso, rectPerso)

    # Affichage du Texte
    fenetre.blit(imageText, rectText)

    # On vide la pile d'evenements et on verifie certains evenements
    for event in pygame.event.get():   # parcours de la liste des evenements recus
        if event.type == QUIT:     #Si un de ces evenements est de type QUIT
            continuer = 0	   # On arrete la boucle


    # raffraichissement
    pygame.display.flip()


# fin du programme principal...
pygame.quit()


