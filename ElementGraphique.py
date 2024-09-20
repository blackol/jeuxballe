import pygame
import random
from random import randint
class ElementGraphique():
    # Le constructeur basique
    def __init__(self, img,x=randint(0,650),y=randint(10,510)):
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.alive = True

    def afficher(self, window) :
        window.blit(self.image, self.rect)  

    def collide(self,other): 
        if self.rect.colliderect(other.rect): 
                self.alive = False
                return True
        return False

    def isAlive(self):
                return self.alive
                
