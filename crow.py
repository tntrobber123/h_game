# Scarecrow char

import pygame
import random

class Crow(pygame.sprite.Sprite):
    def __init__(self):
        self.loc = 4
        self.timer = 0
        self.counter = 0
        self.need = random.randint(1, 2)
        self.img = pygame.image.load("sprites/chars/crow.png")
        self.crowjs = (
"sprites/chars/JS/0.png",
"sprites/chars/JS/1.png",
"sprites/chars/JS/2.png",
"sprites/chars/JS/3.png",
"sprites/chars/JS/4.png",
"sprites/chars/JS/5.png",
"sprites/chars/JS/6.png",
"sprites/chars/JS/7.png",
"sprites/chars/JS/8.png",
"sprites/chars/JS/9.png",
"sprites/chars/JS/10.png",
"sprites/chars/JS/11.png",
"sprites/chars/JS/12.png",
"sprites/chars/JS/13.png",
"sprites/chars/JS/14.png",
"sprites/chars/JS/15.png",
"sprites/chars/JS/16.png",
"sprites/chars/JS/17.png",
"sprites/chars/JS/18.png",
"sprites/chars/JS/19.png",
"sprites/chars/JS/20.png",
)