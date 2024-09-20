
#-*- coding:utf-8 -*-
import pygame
import random
import math
import tkinter
from random import randint
from pygame.locals import*

#on creer la fenetre pour nôtre jeux qui sera en plein écran.
pygame.init()
largeur = 960
hauteur = 672
fenetre = pygame.display.set_mode((largeur,hauteur))
font = pygame.font.Font(None, 34)






class ElementGraphique():
    # Le constructeur basique
    def __init__(self, img):
        self.image = img
        self.rect = self.image.get_rect()

    # Constructeur qui positionne
    def position(self, img, x=0 , y=0):
        # tout d'abord on appelle le constructeur précédent.
        ElementGraphique.__init__(self,img)

        # puis on positionne l'element.
        self.rect.x = x
        self.rect.y = y

    def collide(self,other):
        if self.rect.colliderect(other.rect):
            return True
        return False

    def afficher(self, window) :
        window.blit(self.image, self.rect)







def deplacerperso(self):
    if touches[K_RIGHT] :
        self.rect.x = self.rect.x  + 30

    if touches[K_LEFT] :
        self.rect.x = self.rect.x  -30

    if touches[K_UP] :
        self.rect.y = self.rect.y - 30

    if touches[K_DOWN] :
        self.rect.y = self.rect.y +30
  # limite du personnage dans la map      

    if self.rect.y>hauteur-80 :
        self.rect.y=hauteur-80

    if self.rect.x>largeur-60 :
         self.rect.x=largeur-60

    if self.rect.x<0:
        self.rect.x= 0

    if self.rect.y<0:
        self.rect.y=0








#ajout balles tout les 100 tours
def ajoutballes(balles,i):
    if i ==100:
        balles.append(Balle(image))


class Balle (ElementGraphique):
    def __init__(self,img):
        ElementGraphique.__init__(self, img)
        self.deltaX = 7
        self.deltaY = 9

    def deplacer(self):
        self.rect.x += self.deltaX
        self.rect.y += self.deltaY
        #rebond bord
        if self.rect.x >= largeur-40 :
            self.deltaX = random.randint(5,40)
            self.deltaX = self.deltaX*(-1)
            
        if self.rect.x<=0:
            self.deltaX = random.randint(5,40)
            
        if self.rect.y>= hauteur-40:
            self.deltaY = random.randint(5,20)
            self.deltaY= self.deltaY*(-1)

        if self.rect.y <= 0:
            self.deltaY = random.randint(5,40)


def ajoutbonus(bonus,i):
    if i ==100:
        bonu.append(Balle(image))

# deplacer bonus
class Bonus (ElementGraphique):
    def __init__(self,img):
        ElementGraphique.__init__(self, img)
        self.rect.x=largeur
        self.deltaY = 5
        self.deltaX = 1

    def deplacerbonus(self):
        self.rect.y += self.deltaY
        #rebond bord
        if self.rect.y >=hauteur:
            self.rect.y=-150

        if self.rect.x>=hauteur:
            self.rect.x=random.randint(50,500)
            
       

            
def GameOver():
    font = pygame.font.Font(None, 34)
    
    gameover=2
    while gameover>1:

            touches = pygame.key.get_pressed();

            if touches[K_a]:
                gameover = 0
            imageFond = pygame.image.load("background2.jpg").convert()
            rectFond = imageFond.get_rect()

            #Création de la surface correspondant au texte
            imageTextpause = font.render('game over ( a pour recommencer)', True, (0, 255, 0))
            imageTextpause2 = font.render('je suis deçue là', True, (0, 0, 255))
            #recuperation du rectangle du texte
            rectTextpause = imageTextpause.get_rect()
            rectTextpause2 = imageTextpause2.get_rect()
            #positionnement du rectangle
            rectTextpause.x = largeur / 3
            rectTextpause.y = hauteur / 3

            rectTextpause2.x = largeur / 3
            rectTextpause2.y = hauteur / 3 + 90

            imageTextescore = font.render(('sCore:')+(str(score)), True, (0, 255,0))
            rectTextescore = imageTextescore.get_rect()
            rectTextescore.x = 450
            rectTextescore.y = 450
            fenetre.blit(imageFond, rectFond)
            fenetre.blit(imageTextescore,rectTextescore)

            fenetre.blit(imageTextpause, rectTextpause)
            fenetre.blit(imageTextpause2, rectTextpause2)

            
            for event in pygame.event.get():  # parcours de la liste des evenements recus
                if event.type == QUIT:# Si un de ces evenements est de type QUIT
                    gameover = 0

            #raffraichissement
            pygame.display.flip()










    
#menu jeux
def menu():
    a=3
    if a>2:
         intro = 1

         while intro:
             imageFond = pygame.image.load("background2.jpg").convert()
             rectFond = imageFond.get_rect()
             touches = pygame.key.get_pressed();

             if touches[K_j]:
                  intro = 0

             # Création de la surface correspondant au texte

             imageTextmenu = font.render('<bienvenue dans le menu démarrer', True, (255, 0, 255))
             imageTextmenu2 = font.render('<appuyer sur J pour jouer', True, (0, 255, 255))
              # recuperation du rectangle du texte
             rectTextmenu = imageTextmenu.get_rect()
             rectTextmenu2 = imageTextmenu2.get_rect()
              # positionnement du rectangle
             rectTextmenu.x = largeur / 3
             rectTextmenu.y = hauteur / 3

             rectTextmenu2.x = largeur / 3
             rectTextmenu2.y = hauteur / 3 + 90

             fenetre.blit(imageFond, rectFond)
             fenetre.blit(imageTextmenu, rectTextmenu)
             fenetre.blit(imageTextmenu2, rectTextmenu2)
             for event in pygame.event.get():  # parcours de la liste des evenements recus
                 if event.type == QUIT:  # Si un de ces evenements est de type QUIT
                    intro = 0

             # raffraichissement
             pygame.display.flip()












            
# on definit les images
#image fond
image = pygame.image.load("background2.jpg").convert()
fond = ElementGraphique(image)
#imageperso
print(fond.rect.x)
image = pygame.image.load("perso.png").convert_alpha()
perso = ElementGraphique(image)
perso.rect.x = 300
perso.rect.y = 250
# initilisation balle infini
#image balle
image = pygame.image.load("balle.png").convert_alpha()
bi=  Balle(image)
balles =[bi]
# On definit l'image bonus
bonus = pygame.image.load("images-2.png").convert_alpha()
     #on redimensionne
bonus = pygame.transform.scale(bonus,(25,25))
bonus =Bonus(bonus)
bonu=[bonus]






# vie joueur
vie=100

d=0
horloge = pygame.time.Clock()
fps = 120
i=0
x=1
y=15
score=100
intro = 1
menu()
while intro:
    x+=1
    if i==100:
        d=1
    

    

    #affichage score + vie
    imageTextescore = font.render(('score:')+(str(score)), True, (0, 255,0))
    rectTextescore = imageTextescore.get_rect()
    rectTextescore.x = largeur-130
    rectTextescore.y = 0
    imageTextevie = font.render(('vie:')+(str(vie)), True, (0, 255,0))
    rectTextevie = imageTextevie.get_rect()
    rectTextevie.x = 0
    rectTextevie.y = 0
    
    
    horloge.tick(fps)
# Pour prendre en compte le clavier
    touches =pygame.key.get_pressed();
    print(vie)
    i=i+1
# Permet de quitter le jeux
    if touches[K_SPACE]:
        intro=0
# On ajoute les balles tts 5s
    ajoutballes(balles,i)
    if i>100:
        i=0
        score+=100

# ici nous avons les deplacement
    deplacerperso(perso)
    bonus.deplacerbonus()
    
    

    for bi in balles :
        bi.deplacer()
#colition perso balles
    for b in balles:
        if perso.collide(b):
            score -=2
            vie-=1
            # on initialise le game over et on initialise tt le jeux
    if vie<=0:
        GameOver()
        vie=100
        score=100
        balles=[]
        image = pygame.image.load("balle.png").convert_alpha()
        bi=  Balle(image)
        balles =[bi]
        
#affichons les elements graphique

    fond.afficher((fenetre))
    fenetre.blit(imageTextescore,rectTextescore)
    fenetre.blit(imageTextevie,rectTextevie)
    perso.afficher((fenetre))
    bonus.afficher((fenetre))
    for b in balles :
        b.afficher((fenetre))

    
    for event in pygame.event.get():   # parcours de la liste des evenements recus
        if event.type == QUIT:     #Si un de ces evenements est de type QUIT
            intro = 0	   # On arrete la boucle
   



    # raffraichissement
    pygame.display.flip()


# fin du programme principal...
pygame.quit()



    

