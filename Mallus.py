import pygame
import random
import math
from BonusAnimee import BonusAnimee
from random import randint
from math import *

class Mallus(BonusAnimee):
    def __init__(self,img,x=1,y=-50,effect=0):
            BonusAnimee.__init__(self,img,x)
            self.img = img
            self.alive = True
            self.rect.y = y
            self.rect.x = x
            self.effect = effect
            self.depart = randint(0,650)
            self.k = 0

    def Deplacer(self,hauteur):
            self.k += 1
            self.rect.x = 300*sin(0.075*self.k) + self.depart
            self.rect.y += 10
            if self.rect.y >= hauteur +10:
                    self.alive = False


    def existe(self):
            if self.rect.y <= 0 or self.rect.y >= 510 or self.rect.x <= -10 or self.rect.x >= 650 :
                    return False
            return True