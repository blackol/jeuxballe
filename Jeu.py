import pygame
import random
from random import *
from pygame.locals import*
from ElementGraphique import ElementGraphique
from ElementGraphiqueAnimee import ElementGraphiqueAnimee
from Balle import Balle
from BalleAnimee import BalleAnimee
from Bonus import Bonus
from BonusAnimee import BonusAnimee
from Mallus import Mallus
from Joueur import Joueur
from JoueurAnimee import JoueurAnimee

def supprimerElement(tab):
    newtab=[]
    for e in tab:
        if e.isAlive():
            newtab.append(e)
    return newtab

def creerBalle(tour,largeur,hauteur):
    if (tour%100) == 0:
        balles.append(BalleAnimee(images["balle"],randint(0,largeur),randint(0,hauteur)))

def creerBonus(tour,largeur,hauteur):
    #Creer un bonus tour les 300 tours
    if (tour%300) == 0:
        bonus.append(BonusAnimee(images["vie"],randint(0,largeur),randint(0,hauteur),"Vie"))
    if (tour%400) == 0:
        bonus.append(BonusAnimee(images["boost"],randint(0,largeur),randint(0,hauteur),"Boost"))

def creerMallus(tour,largeur,hauteur):
    if (tour%400) == 0:
        mallus.append(Mallus(images["monstre"],randint(0,largeur),randint(0,hauteur)))

def lireImages():

    images = {}
    images["perso"] = pygame.image.load("images/kara.png").convert_alpha()
    images["fond"] = pygame.image.load("images/fond2.jpg").convert_alpha()
    images["couteau"] = pygame.image.load("images/couteau.png").convert_alpha()
    images["coeur"] = pygame.image.load("images/coeur.png").convert_alpha()
    images["fondnoir"] = pygame.image.load("images/carre-noir.jpg").convert_alpha()
    images["noir"] = pygame.image.load("images/noir.jpg").convert_alpha()
    images["fin"] = pygame.image.load("images/fin.jpg").convert_alpha()

    images["balle"]=[]
    images["balle"].append(pygame.image.load("images/ennemi/ennemi1.png").convert_alpha())
    images["balle"].append(pygame.image.load("images/ennemi/ennemi2.png").convert_alpha())
    images["balle"].append(pygame.image.load("images/ennemi/ennemi3.png").convert_alpha())
    images["balle"].append(pygame.image.load("images/ennemi/ennemi4.png").convert_alpha())
    images["balle"].append(pygame.image.load("images/ennemi/ennemi5.png").convert_alpha())
    images["balle"].append(pygame.image.load("images/ennemi/ennemi6.png").convert_alpha())
    images["balle"].append(pygame.image.load("images/ennemi/ennemi7.png").convert_alpha())
    images["balle"].append(pygame.image.load("images/ennemi/ennemi8.png").convert_alpha())
    images["balle"].append(pygame.image.load("images/ennemi/ennemi9.png").convert_alpha())
    images["balle"].append(pygame.image.load("images/ennemi/ennemi10.png").convert_alpha())
    images["balle"].append(pygame.image.load("images/ennemi/ennemi11.png").convert_alpha())
    images["balle"].append(pygame.image.load("images/ennemi/ennemi12.png").convert_alpha())
    images["balle"].append(pygame.image.load("images/ennemi/ennemi13.png").convert_alpha())
    images["balle"].append(pygame.image.load("images/ennemi/ennemi14.png").convert_alpha())
    images["balle"].append(pygame.image.load("images/ennemi/ennemi15.png").convert_alpha())
    images["balle"].append(pygame.image.load("images/ennemi/ennemi16.png").convert_alpha())
    images["balle"].append(pygame.image.load("images/ennemi/ennemi17.png").convert_alpha())
    images["balle"].append(pygame.image.load("images/ennemi/ennemi18.png").convert_alpha())
    images["balle"].append(pygame.image.load("images/ennemi/ennemi19.png").convert_alpha())
    images["balle"].append(pygame.image.load("images/ennemi/ennemi20.png").convert_alpha())
    images["balle"].append(pygame.image.load("images/ennemi/ennemi21.png").convert_alpha())
    images["balle"].append(pygame.image.load("images/ennemi/ennemi22.png").convert_alpha())
    images["balle"].append(pygame.image.load("images/ennemi/ennemi23.png").convert_alpha())


    images["monstre"] = []
    images["monstre"].append(pygame.image.load("images/monster/monsterParts-00.png").convert_alpha())
    images["monstre"].append(pygame.image.load("images/monster/monsterParts-01.png").convert_alpha())
    images["monstre"].append(pygame.image.load("images/monster/monsterParts-02.png").convert_alpha())
    images["monstre"].append(pygame.image.load("images/monster/monsterParts-03.png").convert_alpha())
    images["monstre"].append(pygame.image.load("images/monster/monsterParts-04.png").convert_alpha())
    images["monstre"].append(pygame.image.load("images/monster/monsterParts-05.png").convert_alpha())
    images["monstre"].append(pygame.image.load("images/monster/monsterParts-06.png").convert_alpha())
    images["monstre"].append(pygame.image.load("images/monster/monsterParts-07.png").convert_alpha())

    images["vie"] = []
    images["vie"].append(pygame.image.load("images/Vie/Vie_1.png").convert_alpha())
    images["vie"].append(pygame.image.load("images/Vie/Vie_2.png").convert_alpha())
    images["vie"].append(pygame.image.load("images/Vie/Vie_3.png").convert_alpha())
    images["vie"].append(pygame.image.load("images/Vie/Vie_4.png").convert_alpha())
    images["vie"].append(pygame.image.load("images/Vie/Vie_5.png").convert_alpha())
    images["vie"].append(pygame.image.load("images/Vie/Vie_6.png").convert_alpha())
    images["vie"].append(pygame.image.load("images/Vie/Vie_7.png").convert_alpha())
    images["vie"].append(pygame.image.load("images/Vie/Vie_8.png").convert_alpha())

    images["boost"] = []
    images["boost"].append(pygame.image.load("images/Boost/Boost_1.png").convert_alpha())
    images["boost"].append(pygame.image.load("images/Boost/Boost_2.png").convert_alpha())
    images["boost"].append(pygame.image.load("images/Boost/Boost_3.png").convert_alpha())
    images["boost"].append(pygame.image.load("images/Boost/Boost_4.png").convert_alpha())
    images["boost"].append(pygame.image.load("images/Boost/Boost_5.png").convert_alpha())
    images["boost"].append(pygame.image.load("images/Boost/Boost_6.png").convert_alpha())
    images["boost"].append(pygame.image.load("images/Boost/Boost_7.png").convert_alpha())
    images["boost"].append(pygame.image.load("images/Boost/Boost_8.png").convert_alpha())



    images["piece"] = []
    images["piece"].append(pygame.image.load("images/piece/star coin rotate 1.png").convert_alpha())
    images["piece"].append(pygame.image.load("images/piece/star coin rotate 2.png").convert_alpha())
    images["piece"].append(pygame.image.load("images/piece/star coin rotate 3.png").convert_alpha())
    images["piece"].append(pygame.image.load("images/piece/star coin rotate 4.png").convert_alpha())
    images["piece"].append(pygame.image.load("images/piece/star coin rotate 5.png").convert_alpha())
    images["piece"].append(pygame.image.load("images/piece/star coin rotate 6.png").convert_alpha())

    images["sans"] = {}
    images["sans"]["debout"] =  [pygame.image.load("images/sans animation/Sans animation1.png").convert_alpha()]
    images["sans"]["face"] = []
    images["sans"]["face"].append(pygame.image.load("images/sans animation/Sans animation1.png").convert_alpha())
    images["sans"]["face"].append(pygame.image.load("images/sans animation/Sans animation2.png").convert_alpha())
    images["sans"]["face"].append(pygame.image.load("images/sans animation/Sans animation3.png").convert_alpha())

    images["sans"]["droite"] = []
    images["sans"]["droite"].append(pygame.image.load("images/sans animation/Sans animation4.png").convert_alpha())
    images["sans"]["droite"].append(pygame.image.load("images/sans animation/Sans animation5.png").convert_alpha())
    images["sans"]["droite"].append(pygame.image.load("images/sans animation/Sans animation6.png").convert_alpha())

    images["sans"]["gauche"] = []
    images["sans"]["gauche"].append(pygame.image.load("images/sans animation/Sans animation7.png").convert_alpha())
    images["sans"]["gauche"].append(pygame.image.load("images/sans animation/Sans animation8.png").convert_alpha())
    images["sans"]["gauche"].append(pygame.image.load("images/sans animation/Sans animation9.png").convert_alpha())

    images["sans"]["dos"] = []
    images["sans"]["dos"].append(pygame.image.load("images/sans animation/Sans animation10.png").convert_alpha())
    images["sans"]["dos"].append(pygame.image.load("images/sans animation/Sans animation11.png").convert_alpha())
    images["sans"]["dos"].append(pygame.image.load("images/sans animation/Sans animation12.png").convert_alpha())

    images["kara"] = {}
    images["kara"]["debout"] = [pygame.image.load("images/kara animation/kara animation1.png").convert_alpha()]
    images["kara"]["face"] = []
    images["kara"]["face"].append(pygame.image.load("images/kara animation/kara animation1.png").convert_alpha())
    images["kara"]["face"].append(pygame.image.load("images/kara animation/kara animation2.png").convert_alpha())
    images["kara"]["face"].append(pygame.image.load("images/kara animation/kara animation3.png").convert_alpha())

    images["kara"]["droite"] = []
    images["kara"]["droite"].append(pygame.image.load("images/kara animation/kara animation4.png").convert_alpha())
    images["kara"]["droite"].append(pygame.image.load("images/kara animation/kara animation5.png").convert_alpha())
    images["kara"]["droite"].append(pygame.image.load("images/kara animation/kara animation6.png").convert_alpha())

    images["kara"]["gauche"] = []
    images["kara"]["gauche"].append(pygame.image.load("images/kara animation/kara animation7.png").convert_alpha())
    images["kara"]["gauche"].append(pygame.image.load("images/kara animation/kara animation8.png").convert_alpha())
    images["kara"]["gauche"].append(pygame.image.load("images/kara animation/kara animation9.png").convert_alpha())

    images["kara"]["dos"] = []
    images["kara"]["dos"].append(pygame.image.load("images/kara animation/kara animation10.png").convert_alpha())
    images["kara"]["dos"].append(pygame.image.load("images/kara animation/kara animation11.png").convert_alpha())
    images["kara"]["dos"].append(pygame.image.load("images/kara animation/kara animation12.png").convert_alpha())

    return images

def Playlist():

    playlist = {}
    playlist["mort"] = "music/deadson.mp3"
    playlist["jeu"] = "music/undertale megalovania.mp3"

    return playlist

def lireTexteIntro():
    textes = {}

    font = pygame.font.Font(None,34)
    textes["bonjour"] = font.render("Bonjour, joueur vous venez essayer mon jeu ?",True,(255, 255, 255))
    textes["choix"] = font.render("<Espace> pour jouer ou <Escape> pour quitter",True,(255, 255, 255))
    return textes

def lireTextes():
    textes = {}

    font = pygame.font.Font(None,34)
    textes["score"] = font.render("Score : " + str(score),True,(255, 255, 255))
    textes["vie"] = font.render("Vie: " + str(perso.vies) ,True,(255, 255, 255))
    textes["choix"] = font.render("<Espace> pour continuer ou <Echap> pour quitter",True,(255, 255, 255))
    return textes

def Intro():
    intro = True

    textes = lireTexteIntro()
    fond = ElementGraphique(images["noir"],0,0)
    message = ElementGraphique(images["fondnoir"],largeur/2 - 100,hauteur/2 -120) ################################### Modifier quand on aurale massage
    sans = JoueurAnimee(images["sans"],100,288)
    tour = 0

    framerate = pygame.time.Clock()

    while intro:
        Fps = framerate.tick(30)
        touches = pygame.key.get_pressed()
        fond.afficher((fenetre))
        sans.afficher((fenetre))

        sans.Intro(largeur,message,fenetre)
        fenetre.blit(textes["bonjour"],(262,440))
        fenetre.blit(textes["choix"],(262,480))

        for event in pygame.event.get():
            if event.type == pygame.QUIT or touches[K_ESCAPE]:
                quit()
            if touches[K_SPACE]:
                intro = False

        pygame.display.update()

def Fin(continuer):
    LoadMusic(playlist["mort"])
    LireMusic()

    fond = ElementGraphique(images["fin"],0,0)
    while continuer == 0:
        fond.afficher((fenetre))
        fenetre.blit(textes["score"],(largeur/2-100,100))

        touches = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or touches[K_ESCAPE]:
                quit()
            if touches[K_SPACE]:
                return 1


        pygame.display.update()

def LireMusic():
    pygame.mixer.music.play()

def LireSound(nom):
    pygame.mixer.Sound.play(nom)

def LoadMusic(nom):
    pygame.mixer.music.load(nom)

def LoadSound(nom):
    pygame.mixer.Sound(nom)

def Restart(rep):
    if rep == 1:
        return 1
    else:
        quit()

pygame.init()

largeur = 1024
hauteur = 572
fenetre = pygame.display.set_mode((largeur,hauteur))
restart = 1
images = lireImages()
playlist = Playlist()
framerate = pygame.time.Clock()


Intro()

while Restart(restart) != 0:
    #Variable de temps
    tour = 0
    score = 0

    fond = ElementGraphique(images["fond"],0,0)
    perso = JoueurAnimee(images["kara"],500,400)
    #Tableaux de balles et de bonus
    balles = []
    bonus = []
    mallus = []

    continuer = 1
    font = pygame.font.Font(None, 34)

    LoadMusic(playlist["jeu"])
    LireMusic()

    while continuer:

        tour += 1
        score += 1
        Fps = framerate.tick(60)
        textes = lireTextes()

        fond.afficher((fenetre))
        perso.afficher((fenetre))


        fenetre.blit((textes["vie"]),(0,0))
        fenetre.blit(textes["score"],(550,0))

        #Afficher et deplacer toutes les balles....
        for b in balles:
            b.afficher((fenetre))
            b.Deplacer()
            if b.collide(perso):
                perso.recevoirDegats()

        #Et les bonus
        for b in bonus:
            b.afficher((fenetre))
            b.Deplacer(hauteur)
            if b.collide(perso) and b.effect == "Vie":
                 perso.recevoirVie()
            if b.collide(perso) and b.effect == "Boost":
                perso.setTime(tour,100,1)

        for m in mallus:
            m.afficher((fenetre))
            m.Deplacer(hauteur)
            if m.collide(perso):
                perso.recevoirDegats()
                perso.setTime(tour,200,2)

        perso.Boost(tour)
        perso.Mallus(tour)

        #Creation des balles infinis
        creerBalle(tour,largeur,hauteur)
        creerBonus(tour,largeur,hauteur)
        creerMallus(tour,largeur,hauteur)

        #Deplacement du perso
        touches = pygame.key.get_pressed()
        perso.Deplacer(touches,largeur,hauteur)

        #Verifie si le personnage est en vie
        if perso.isAlive() == False:
             continuer = 0

        #Supprimer les balles et bonus quand tu les touches
        balles = supprimerElement(balles)
        bonus = supprimerElement(bonus)
        mallus = supprimerElement(mallus)

        for event in pygame.event.get():   # parcours de la liste des evenements recus
            if event.type == pygame.QUIT or touches[K_ESCAPE]:     #Si un de ces evenements est de type QUIT
                continuer = 0
        pygame.display.update()

    while continuer == 0:
        if Fin(continuer) == 1:
            continuer = 1

pygame.quit()
quit()
