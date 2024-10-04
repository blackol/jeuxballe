import pygame
import random
from ElementGraphiqueAnimee import ElementGraphiqueAnimee
from random import randint

class BalleAnimee(ElementGraphiqueAnimee):
        def __init__(self,img,x=0,y=0):
                ElementGraphiqueAnimee.__init__(self,img)
                self.deltaX = randint(-2,2)
                self.deltaY = randint(-2,2)
                self.rect.x = randint(0,650)
                self.rect.y = randint(0,510)


        def Deplacer(self):
                self.rect.x += self.deltaX
                if self.rect.x <= -10 or self.rect.x >= 1000 :
                        self.deltaX = - self.deltaX
                        self.rect.x = self.rect.x

                self.rect.y += self.deltaY
                if self.rect.y <= 0 or self.rect.y >= 550 :
                        self.deltaY = - self.deltaY
                        self.rect.y = self.rect.y

        def rebond(self,other):
                if self.rect.colliderect(other.rect):
                        self.deltaX *= -1
                        self.deltaY *= -1
