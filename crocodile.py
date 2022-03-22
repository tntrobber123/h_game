# Crocodile char

import pygame
import random

class Crocodile(pygame.sprite.Sprite):
    def __init__(self):
        self.def_loc = 1
        self.loc = 1
        self.timer = 0
        self.counter = 0
        self.need = random.randint(3, 15)