# Wolf char

import pygame
import random

""" Viable Locations:
0-*cabin - forest-y area with a cabin in front
1-*river - not many trees, but a small clearing with a medium sized river
2-*river 2 - more trees, smaller river
3-*forrest 1 - hugly dense forrest
4-*clearing with cross
5-*hill - clearing, with a field a small distance away
6-*field - clearing, not much there. trees in the distance
7-*abandon mine - small clearing that leads to a hill with a mine in it

8-*bunker
Viable Locations """
class Wolf(pygame.sprite.Sprite):
    def __init__(self):
        self.def_loc = 6
        self.loc = 6
        self.timer = 0
        self.counter = 0
        self.need = random.randint(3, 10)
        self.img = pygame.image.load("sprites/chars/croc.png")