#-*- coding:utf-8 -*-
import pygame
from pygame.locals import *

## Initialisation de la fenetre et crÃ©ation
pygame.init()
#creation de la fenetre

largeur = 640
hauteur = 480
fenetre=pygame.display.set_mode((largeur,hauteur))

i=1;


continuer=1
while continuer:
    i= i+1;
    print ('i')

# fin du programme principal...
pygame.quit()


