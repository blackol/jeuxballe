import pygame
import random
from ElementGraphique import ElementGraphique
from random import randint

class Balle(ElementGraphique):
        def __init__(self,img,x=0,y=0):
                ElementGraphique.__init__(self,img)
                self.deltaX = randint(-10,10)
                self.deltaY = randint(-10,10)
                self.rect.x = randint(0,650)
                self.rect.y = randint(0,510)
                self.alive = True


        def Deplacer(self,largeur,hauteur):
	        self.rect.x += self.deltaX
	        if self.rect.x <= -10 or self.rect.x >= largeur - 40 :
	            self.deltaX = - self.deltaX
	            self.rect.x = self.rect.x

	        self.rect.y += self.deltaY
	        if self.rect.y <= 0 or self.rect.y >= hauteur - 40 :
	            self.deltaY = - self.deltaY
	            self.rect.y = self.rect.y

        def rebond(self,other):
                if self.rect.colliderect(other.rect):
                        self.deltaX *= -1
                        self.deltaY *= -1
                
