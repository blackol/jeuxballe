import pygame
from ElementGraphiqueAnimee import ElementGraphiqueAnimee
from ElementGraphique import ElementGraphique

class JoueurAnimee(ElementGraphiqueAnimee):
        def __init__(self,img,x=0,y=0):
                ElementGraphiqueAnimee.__init__(self,img["debout"],x,y)
                self.vies = 10
                self.alive = True
                self.boost = 1
                self.cheat = False
                self.time = 0
                self.trigger = 0
                self.image = img
                self.numimage = 0
                self.direction = "debout"

        def Deplacer(self,touches,largeur,hauteur):

                if touches [pygame.K_UP]:
                    self.rect.y -= 12 * self.boost
                    if self.rect.y <= -12 :
                            self.rect.y += 12 * self.boost

                if touches [pygame.K_DOWN]:
                    self.rect.y += 12 * self.boost
                    if self.rect.y >= hauteur - 10  : #Bas de l'écran
                            self.rect.y -= 12 * self.boost
                if touches [pygame.K_RIGHT]:
                    self.rect.x += 12 * self.boost
                    if self.rect.x >= largeur - 10: #Côté droit
                            self.rect.x -= 12 * self.boost

                if touches [pygame.K_LEFT]:
                    self.rect.x -= 12 * self.boost
                    if self.rect.x <= -20 :
                            self.rect.x += 12 * self.boost

                if touches [pygame.K_UP]:
                        self.direction = "dos"
                        self.numimage += 1

                elif touches [pygame.K_DOWN]:
                        self.direction = "face"
                        self.numimage += 1
                elif touches [pygame.K_RIGHT]:
                        self.direction = "droite"
                        self.numimage += 1

                elif touches [pygame.K_LEFT]:
                        self.direction = "gauche"
                        self.numimage += 1

                else:
                        self.direction = "debout"

        def afficher(self, window) :
            if (self.fps % 1 )== 0:
                self.numimage = (self.numimage)%len(self.image[self.direction])
                window.blit(self.image[self.direction][self.numimage],self.rect,)

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

        def Mallus(self,tour=0):
                if self.trigger == 2:
                        if tour < self.time:
                                self.boost = 0.5

                        else:
                                self.boost = 1
                                self.trigger = 0


        def setTime(self,tour,time,num):
                self.time = tour + time
                self.trigger = num
                return self.time

        def Intro(self,largeur,message,fenetre):
            intro = True
            if intro:
                if self.rect.x <= largeur/2:
                    self.direction = "droite"
                    self.numimage += 1
                    self.rect.x += 10
                else:
                    self.direction = "debout"
                    message.afficher((fenetre))
            return 1
