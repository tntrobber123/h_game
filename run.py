import pygame
import time
import random
import math

black = (0, 0, 0)
white = (255, 255, 255)
size = [1400, 1000]
screen = pygame.display.set_mode(size)

# Sprites and Backgrounds
testbkgrnd = pygame.image.load("backdrops/test_background.png")
inv_img = pygame.image.load("backdrops/inv.png")

cam_0 = pygame.image.load("backdrops/cams/cam_0.png")
cam_1 = pygame.image.load("backdrops/cams/cam_1.png")
cam_2 = pygame.image.load("backdrops/cams/cam_2.png")
cam_3 = pygame.image.load("backdrops/cams/cam_3.png")
cam_4 = pygame.image.load("backdrops/cams/cam_4.png")
cam_5 = pygame.image.load("backdrops/cams/cam_5.png")
cam_6 = pygame.image.load("backdrops/cams/cam_6.png")
cam_7 = pygame.image.load("backdrops/cams/cam_7.png")

screen.blit(testbkgrnd, (-500, 0))
pygame.display.flip()

view = 0
move = 0
cam = 0
inv = False

def vision():
    global view
    screen.blit(testbkgrnd, ((-500 - (view * 10)), 0))
    pygame.display.flip()
    
def cams():
    global cam
    if cam == 0:
        screen.blit(cam_0, (100, 100))
        pygame.display.flip()
    if cam == 1:
        screen.blit(cam_1, (100, 100))
        pygame.display.flip()
    if cam == 2:
        screen.blit(cam_2, (100, 100))
        pygame.display.flip()
    if cam == 3:
        screen.blit(cam_3, (100, 100))
        pygame.display.flip()
    if cam == 4:
        screen.blit(cam_4, (100, 100))
        pygame.display.flip()
    if cam == 5:
        screen.blit(cam_5, (100, 100))
        pygame.display.flip()
    if cam == 6:
        screen.blit(cam_6, (100, 100))
        pygame.display.flip()
    if cam == 7:
        screen.blit(cam_7, (100, 100))
        pygame.display.flip()

def main():
    global inv
    global move
    global view
    
    # Event loop
        
    while True:
        global cam
        if inv == True:
            cams()
            
        if inv == False:
            vision()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                
            if event.type == pygame.KEYUP:
                move = 0
                   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                
                # Movement (looking)
                if event.key == pygame.K_RIGHT:
                    if inv == False:
                        move = 1
                    if inv == True:
                        cam += 1
                        
                if event.key == pygame.K_LEFT:
                    if inv == False:
                        move = -1
                    if inv == True:
                        cam -= 1
                        
                if event.key == pygame.K_UP:
                    if inv == False:
                        inv = True
                        screen.blit(inv_img, (0, 0))
                        pygame.display.flip()
                        
                if event.key == pygame.K_DOWN:
                    if inv == True:
                        inv = False
                    
                if event.key == pygame.K_SPACE:
                    # Light or other function?
                    pass
                
        """Code for num resets"""
        if move == 1:
            if view < 50:
                view += 2
            elif view >= 50:
                view = 50
                    
        if move == -1:
            if view > -50:
                view -= 2
            elif view <= -50:
                view = -50
                
        if cam == 8:
            cam = 0
        if cam == -1:
            cam = 7
main()