import pygame
import time
import random
import math

from wolf import Wolf
wlf = Wolf()

from crocodile import Crocodile
croc = Crocodile()

from ghost import Ghost
gst = Ghost()

black = (0, 0, 0)
white = (255, 255, 255)
size = [1400, 1000]
screen = pygame.display.set_mode(size)

# Sprites and Backgrounds
testbkgrnd = pygame.image.load("backdrops/test_background.png")
inv_img = pygame.image.load("backdrops/inv.png")

# Camreas
cam_0 = pygame.image.load("backdrops/cams/cam_0.png")
cam_1 = pygame.image.load("backdrops/cams/cam_1.png")
cam_2 = pygame.image.load("backdrops/cams/cam_2.png")
cam_3 = pygame.image.load("backdrops/cams/cam_3.png")
cam_4 = pygame.image.load("backdrops/cams/cam_4.png")
cam_5 = pygame.image.load("backdrops/cams/cam_5.png")
cam_6 = pygame.image.load("backdrops/cams/cam_6.png")
cam_7 = pygame.image.load("backdrops/cams/cam_7.png")

# Sprites
crshair = pygame.image.load("sprites/crosshair.png")
crshair_using = pygame.image.load("sprites/crosshair_using.png")
planefix = pygame.image.load("sprites/fixplane.png")
foodimg = pygame.image.load("sprites/food.png")
minifood = pygame.image.load("sprites/minifood.png")
soundimg = pygame.image.load("sprites/sound.png")
minisound = pygame.image.load("sprites/minisound.png")
progbar = pygame.image.load("sprites/progressbar.png")
greenbar = pygame.image.load("sprites/greenbar.png")

# Characters
wlf_img = pygame.image.load("sprites/chars/wlf.png")
croc_img = pygame.image.load("sprites/chars/croc.png")
gst_img = pygame.image.load("sprites/chars/ghost.png")

food = False
foodcount = 0
has_food = False
foodroom = False

sound = False
soundcount = 0
has_sound = False
soundroom = False

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
c_dif = 1
g_dif = 1

w_disable = False
c_disable = False
g_disable = False

def vision():
    screen.blit(testbkgrnd, ((-500 - (view * 10)), 0))
    if g_disable == True:
        screen.blit(gst_img, ((-500 - (view * 10)), 0))
    screen.blit(foodimg, ((300 - (view * 10)), 500))
    screen.blit(planefix, ((600 - (view * 10)), 500))
    screen.blit(soundimg, ((900 - (view * 10)), 500))

def draw_ent():
    screen.blit(crshair, (650, 500))
    screen.blit(progbar, (0, 460))
    
def green_bar():
    plane_int = int(plane)
    global view
    screen.blit(greenbar, ((-490 + (plane_int * 5)), 460))

def cams():
    global cam
    if cam == 0:
        screen.blit(cam_0, (85, 120))
        if wlf.loc == 0:
            screen.blit(wlf_img, (85, 120))
        if croc.loc == 0:
            screen.blit(croc_img, (185, 120))
        if gst.loc == 0:
            screen.blit(gst_img, (250, 120))
            
    if cam == 1:
        screen.blit(cam_1, (85, 120))
        if wlf.loc == 1:
            screen.blit(wlf_img, (85, 120))
        if croc.loc == 1:
            screen.blit(croc_img, (185, 120))
        if gst.loc == 1:
            screen.blit(gst_img, (250, 120))
        
    if cam == 2:
        screen.blit(cam_2, (85, 120))
        if wlf.loc == 2:
            screen.blit(wlf_img, (85, 120))
        if croc.loc == 2:
            screen.blit(croc_img, (185, 120))
        if gst.loc == 2:
            screen.blit(gst_img, (250, 120))
        
    if cam == 3:
        screen.blit(cam_3, (85, 120))
        if wlf.loc == 3:
            screen.blit(wlf_img, (85, 120))
        if croc.loc == 3:
            screen.blit(croc_img, (185, 120))
        if gst.loc == 3:
            screen.blit(gst_img, (250, 120))
        
    if cam == 4:
        screen.blit(cam_4, (85, 120))
        if wlf.loc == 4:
            screen.blit(wlf_img, (85, 120))
        if croc.loc == 4:
            screen.blit(croc_img, (185, 120))
        if gst.loc == 4:
            screen.blit(gst_img, (250, 120))
        
    if cam == 5:
        screen.blit(cam_5, (85, 120))
        if wlf.loc == 5:
            screen.blit(wlf_img, (85, 120))
        if croc.loc == 5:
            screen.blit(croc_img, (185, 120))
        if gst.loc == 5:
            screen.blit(gst_img, (250, 120))
        
    if cam == 6:
        screen.blit(cam_1, (85, 120))
        if wlf.loc == 6:
            screen.blit(wlf_img, (85, 120))
        if croc.loc == 6:
            screen.blit(croc_img, (185, 120))
        if gst.loc == 6:
            screen.blit(gst_img, (250, 120))
        
    if cam == 7:
        screen.blit(cam_7, (85, 120))
        if wlf.loc == 7:
            screen.blit(wlf_img, (85, 120))
        if croc.loc == 7:
            screen.blit(croc_img, (185, 120))
        if gst.loc == 7:
            screen.blit(gst_img, (250, 120))
        
def wlf_move(): 
    if food == False:
        if wlf.counter == wlf.need:
            # Jumpscare
            pass
        else:
            wlf.counter += 1
            wlf.loc = random.randint(0, 7)
            
def croc_move():
    if sound == False:
        if croc.counter == croc.need:
            # Jumpscare
            pass
        else:
            croc.counter += 1
            croc.loc = random.randint(0, 7)
            
def gst_move():
    global inv
    global g_disable
    if gst.counter == gst.need:
        inv = False
        gst.loc = 10
        g_disable = True
        # Timer
        # Jumpscare
    else:
        gst.counter += 1
        gst.loc = random.randint(0, 7)
            
            
    
def main():
    global inv
    global cam
    global move
    global view
    global tooluse
    global plane
    global foodlure
    global foodcount
    global foodroom
    global soundlure
    global soundcount
    global soundroom
    global has_food
    global has_sound
    
    # Event loop
        
    while True:
            
        if inv == True:
            cams()
            
        if inv == False:
            vision()
            green_bar()
            draw_ent()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                
            if event.type == pygame.KEYUP:
                move = 0
                tooluse = False
                foodlure = False
                soundlure = False
                   
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
                        
                if event.key == pygame.K_DOWN:
                    if inv == True:
                        inv = False
                    if inv == False:
                        view = 0
                    
                if event.key == pygame.K_SPACE:
                    if inv == True:
                        
                        if has_food == True:
                            foodroom = cam
                            has_food = False
                            
                        if has_sound == True:
                            soundroom = cam
                            has_sound = False
                            
                    if inv == False:
                    
                        if view < 10 and view > -10:
                            tooluse = True
                        
                        if view < -20 and view > -40:
                            foodlure = True
                        
                        if view < 40 and view > 20:
                            soundlure = True
                
        """Code for num resets"""
        if not foodlure:
            foodcount = 0
            
        if not soundlure:
            soundcount = 0
        
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
            # Advance the level
            pygame.quit()
            quit()
            
        if foodlure == True:
            foodcount += 1
            
        if foodcount >= 50:
            has_food = True
            has_sound = False
            foodcount = 0
        
        if soundlure == True:
            soundcount += 1
            
        if soundcount >= 50:
            has_sound = True
            has_food = False
            soundcount = 0
        
        if has_food == True:
            screen.blit(minifood, (0, 590))
             
        if has_sound == True:
            screen.blit(minisound, (0, 590))
            
        """AI loop:"""
        
        if not w_disable:
            wlf.timer += 1
            if wlf.timer == (500 // w_dif):
                wlf_move()
                wlf.timer = 0
            
        if not c_disable:
            croc.timer += 1
            if croc.timer == (800 // c_dif):
                croc_move()
                croc.timer = 0
        
        if not g_disable:
            gst.timer += 1
            if gst.timer == (100 // g_dif):
                gst_move()
                gst.timer = 0
            
        pygame.display.flip()
main()
