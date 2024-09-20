import pygame
import random
import math
from Balle import Balle
from random import randint
from math import *

class Bonus(Balle):
        
        def __init__(self,img,x,y=-50):
                Balle.__init__(self,img)
                self.img = img
                self.alive = True
                self.rect.y = y
                self.rect.x = x
                self.depart = randint(0,650)
                self.k = 0
                        

                
        def existe(self):
                if self.rect.y <= 0 or self.rect.y >= 510 or self.rect.x <= -10 or self.rect.x >= 650 :
                        return False
                return True


""" k * sin ( a *x ) 
k == amplitude
a == fluidité/vitesse"""
