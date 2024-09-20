import pygame
from ElementGraphique import ElementGraphique

class Joueur(ElementGraphique):
        def __init__(self,img,x=0,y=0):
                ElementGraphique.__init__(self,img,x,y)
                self.vies = 100
                self.alive = True
                self.boost = 1
                self.cheat = False
                self.trigger = 0
                self.time = 0

        def Deplacer(self,touches,largeur,hauteur):# Rajoute longueur et largeur
                if touches [pygame.K_UP]:
                        self.rect.y -= 10 * self.boost
                        if self.rect.y <= -10 :
                                self.rect.y += 10 * self.boost
                if touches [pygame.K_DOWN]:
                        self.rect.y += 10 * self.boost
                        if self.rect.y >= hauteur + 10 : #Bas de l'écran
                                self.rect.y -= 10 * self.boost
                if touches [pygame.K_RIGHT]:
                        self.rect.x += 10 * self.boost
                        if self.rect.x >= largeur + 10: #Côté droit
                                self.rect.x -= 10 * self.boost
                if touches [pygame.K_LEFT]:
                        self.rect.x -= 10 * self.boost
                        if self.rect.x <= -10 :
                                self.rect.x += 10 * self.boost

        def recevoirDegats(self):
                self.vies -= 1
                if self.vies <= 0:
                        self.alive = False

        def isAlive(self):
                return self.alive

        def recevoirVie(self):
                self.vies += 1

        def Boost(self,tour=0):
                if self.trigger == 1:
                        if tour < self.time:
                                self.boost = 2
                        else:
                               self.trigger = 0
                else:
                        self.boost = 1

        def setTime(self,tour,time,num):
                self.time = tour + time #modifier le 100 en variable
                self.trigger = num
                return self.time
