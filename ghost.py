# Ghost char

import pygame
import random

class Ghost(pygame.sprite.Sprite):
    def __init__(self):
        self.def_loc = 4
        self.loc = 4
        self.timer = 0
        self.counter = 0
        self.need = 2