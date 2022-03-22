import pygame
import time
import random
import math

from wolf import Wolf
wlf = Wolf()

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

crshair = pygame.image.load("sprites/crosshair.png")
crshair_using = pygame.image.load("sprites/crosshair_using.png")
planefix = pygame.image.load("sprites/fixplane.png")
foodimg = pygame.image.load("sprites/food.png")
soundimg = pygame.image.load("sprites/sound.png")

food = False

progbar = pygame.image.load("sprites/progressbar.png")
greenbar = pygame.image.load("sprites/greenbar.png")

wlf_img = pygame.image.load("sprites/chars/wlf.png")

screen.blit(testbkgrnd, (-500, 0))
pygame.display.flip()

view = 0
move = 0
cam = 0

tooluse = False
foodlure = False
soundlure = False

plane = 0
inv = False

w_dif = 1

def vision():
    global view
    screen.blit(testbkgrnd, ((-500 - (view * 10)), 0))
    
    screen.blit(foodimg, ((300 - (view * 10)), 500))
    screen.blit(planefix, ((600 - (view * 10)), 500))
    screen.blit(soundimg, ((900 - (view * 10)), 500))

def crosshair():
    screen.blit(crshair, (650, 500))

def progress_bar():
    screen.blit(progbar, (0, 460))
    
def green_bar():
    global view
    screen.blit(greenbar, ((-490 + (plane * 5)), 460))
    
def cams():
    global cam
    if cam == 0:
        screen.blit(cam_0, (85, 120))
        if wlf.loc == 0:
            screen.blit(wlf_img, (85, 120))
    if cam == 1:
        screen.blit(cam_1, (85, 120))
        if wlf.loc == 1:
            screen.blit(wlf_img, (85, 120))
    if cam == 2:
        screen.blit(cam_2, (85, 120))
        if wlf.loc == 2:
            screen.blit(wlf_img, (85, 120))
    if cam == 3:
        screen.blit(cam_3, (85, 120))
        if wlf.loc == 3:
            screen.blit(wlf_img, (85, 120))
    if cam == 4:
        screen.blit(cam_4, (85, 120))
        if wlf.loc == 4:
            screen.blit(wlf_img, (85, 120))
    if cam == 5:
        screen.blit(cam_5, (85, 120))
        if wlf.loc == 5:
            screen.blit(wlf_img, (85, 120))
    if cam == 6:
        screen.blit(cam_6, (85, 120))
        if wlf.loc == 6:
            screen.blit(wlf_img, (85, 120))
    if cam == 7:
        screen.blit(cam_7, (85, 120))
        if wlf.loc == 7:
            screen.blit(wlf_img, (85, 120))

def wlf_move(): 
    global wlf
    if food == False:
        if wlf.counter == wlf.need:
            # Jumpscare
            wlf.need = random.randint(3, 10)
            pass
        else:
            wlf.counter += 1
            wlf.loc = random.randint(0, 7)
            
    
def main():
    global inv
    global move
    global view
    global tooluse
    global plane
    
    # Event loop
        
    while True:
        
        """AI loop:"""
        
        wlf.timer += 1
        if wlf.timer == (500 / w_dif):
            wlf_move()
            wlf.timer = 0
            
        
        global cam
        if inv == True:
            cams()
            pygame.display.flip()
            
        if inv == False:
            vision()
            green_bar()
            progress_bar()
            crosshair()
            pygame.display.flip()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                
            if event.type == pygame.KEYUP:
                move = 0
                tooluse = False
                   
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
                    if inv == False:
                        view = 0
                    
                if event.key == pygame.K_SPACE:
                    
                    if view < 10 and view > -10:
                        tooluse = True
                        
                    if view < -20 and view > -40:
                        foodlure = True
                        print("foodlure")
                        
                    if view < 40 and view > 20:
                        soundlure = True
                        print("soundlure")
                
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
                
        # Cam range = 0-7
        if cam == 8:
            cam = 0
        if cam == -1:
            cam = 7
        
        if tooluse == True:
            plane += .2
        if plane >= 100:
            print("you win")
            pygame.quit()
            quit()
main()
