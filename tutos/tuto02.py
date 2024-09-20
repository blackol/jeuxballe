#-*- coding:utf-8 -*-
import pygame
from pygame.locals import *

## Initialisation de la fenetre et crÃ©ation
pygame.init()
#creation de la fenetre

largeur = 640
hauteur = 480
fenetre=pygame.display.set_mode((largeur,hauteur))

i=0;

continuer=1
while continuer:
    i=i+1;
    print i

    # on recupere l'etat du clavier
    touches = pygame.key.get_pressed();


    if touches[K_ESCAPE] :
        continuer=0

    # On vide la pile d'evenements et on verifie certains evenements
    for event in pygame.event.get():   # parcours de la liste des evenements recus
        if event.type == QUIT:     #Si un de ces evenements est de type QUIT
            continuer = 0	   # On arrete la boucle


# fin du programme principal...
pygame.quit()
