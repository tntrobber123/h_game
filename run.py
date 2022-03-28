import pygame
import time
import random
import math

x = 0

from wolf import Wolf
wlf = Wolf()

from crocodile import Crocodile
croc = Crocodile()

from crow import Crow
s = Crow()

size = [1400, 1000]
screen = pygame.display.set_mode(size)

# Sprites and Backgrounds
testbkgrnd = pygame.image.load("backdrops/test_background.png")
inv_img = pygame.image.load("backdrops/inv.png")

# Cameras
cam_0 = pygame.image.load("backdrops/cams/cam_0.png")
cam_1 = pygame.image.load("backdrops/cams/cam_1.png")
cam_2 = pygame.image.load("backdrops/cams/cam_2.png")
cam_3 = pygame.image.load("backdrops/cams/cam_3.png")
cam_4 = pygame.image.load("backdrops/cams/cam_4.png")
cam_5 = pygame.image.load("backdrops/cams/cam_5.png")
cam_6 = pygame.image.load("backdrops/cams/cam_6.png")
cam_7 = pygame.image.load("backdrops/cams/cam_7.png")

nonv_0 = pygame.image.load("backdrops/cams/nonv/nonv_1.png")
nonv_1 = pygame.image.load("backdrops/cams/nonv/nonv_1.png")
nonv_2 = pygame.image.load("backdrops/cams/nonv/nonv_1.png")
nonv_3 = pygame.image.load("backdrops/cams/nonv/nonv_3.png")
nonv_4 = pygame.image.load("backdrops/cams/nonv/nonv_1.png")
nonv_5 = pygame.image.load("backdrops/cams/nonv/nonv_3.png")
nonv_6 = pygame.image.load("backdrops/cams/nonv/nonv_3.png")
nonv_7 = pygame.image.load("backdrops/cams/nonv/nonv_3.png")

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

night = 1

w_dif = 1
c_dif = 1
s_dif = 1

sjs = False

w_disable = False
wlf_countdown = -1
c_disable = False
croc_countdown = -1
s_disable = False
s_countdown = -1

nightvision = False
battery = 10000

def vision():
    screen.blit(testbkgrnd, ((-500 - (view * 10)), 0))
    screen.blit(foodimg, ((300 - (view * 10)), 500))
    screen.blit(planefix, ((600 - (view * 10)), 500))
    screen.blit(soundimg, ((900 - (view * 10)), 500))

def draw_ent():
    screen.blit(crshair, (650, 500))
    screen.blit(progbar, (0, 460))
    
def green_bar():
    screen.blit(greenbar, ((-490 + (int(plane) * 5)), 460))

def cams():
    global cam
    global nightvision
    
    if nightvision == False:
    
        if cam == 0:
            screen.blit(nonv_0, (85, 120))
            if wlf.loc == 0:
                screen.blit(wlf.img, (85, 120))
            if croc.loc == 0:
                screen.blit(croc.img, (185, 120))
            if s.loc == 0:
                screen.blit(s.img, (400, 220))
            
        if cam == 1:
            screen.blit(nonv_1, (85, 120))
            if wlf.loc == 1:
                screen.blit(wlf.img, (85, 120))
            if croc.loc == 1:
                screen.blit(croc.img, (185, 120))
            if s.loc == 1:
                screen.blit(s.img, (400, 220))
        
        if cam == 2:
            screen.blit(nonv_2, (85, 120))
            if wlf.loc == 2:
                screen.blit(wlf.img, (85, 120))
            if croc.loc == 2:
                screen.blit(croc.img, (185, 120))
            if s.loc == 2:
                screen.blit(s.img, (400, 220))
        
        if cam == 3:
            screen.blit(nonv_3, (85, 120))
            if wlf.loc == 3:
                screen.blit(wlf.img, (85, 120))
            if croc.loc == 3:
                screen.blit(croc.img, (185, 120))
            if s.loc == 3:
                screen.blit(s.img, (400, 220))
        
        if cam == 4:
            screen.blit(nonv_4, (85, 120))
            if wlf.loc == 4:
                screen.blit(wlf.img, (85, 120))
            if croc.loc == 4:
                screen.blit(croc.img, (185, 120))
            if s.loc == 4:
                screen.blit(s.img, (400, 220))
        
        if cam == 5:
            screen.blit(nonv_5, (85, 120))
            if wlf.loc == 5:
                screen.blit(wlf.img, (85, 120))
            if croc.loc == 5:
                screen.blit(croc.img, (400, 220))
            if s.loc == 5:
                screen.blit(s.img, (400, 220))
        
        if cam == 6:
            screen.blit(nonv_6, (85, 120))
            if wlf.loc == 6:
                screen.blit(wlf.img, (85, 120))
            if croc.loc == 6:
                screen.blit(croc.img, (185, 120))
            if s.loc == 6:
                screen.blit(s.img, (400, 220))
        
        if cam == 7:
            screen.blit(nonv_7, (85, 120))
            if wlf.loc == 7:
                screen.blit(wlf.img, (85, 120))
            if croc.loc == 7:
                screen.blit(croc.img, (185, 120))
            if s.loc == 7:
                screen.blit(s.img, (400, 220))
                
    if nightvision == True:
        
        if cam == 0:
            screen.blit(cam_0, (85, 120))
            if wlf.loc == 0:
                screen.blit(wlf.img, (85, 120))
            if croc.loc == 0:
                screen.blit(croc.img, (185, 120))
            if s.loc == 0:
                screen.blit(s.img, (400, 220))
            
        if cam == 1:
            screen.blit(cam_1, (85, 120))
            if wlf.loc == 1:
                screen.blit(wlf.img, (85, 120))
            if croc.loc == 1:
                screen.blit(croc.img, (185, 120))
            if s.loc == 1:
                screen.blit(s.img, (400, 220))
        
        if cam == 2:
            screen.blit(cam_2, (85, 120))
            if wlf.loc == 2:
                screen.blit(wlf.img, (85, 120))
            if croc.loc == 2:
                screen.blit(croc.img, (185, 120))
            if s.loc == 2:
                screen.blit(s.img, (400, 220))
        
        if cam == 3:
            screen.blit(cam_3, (85, 120))
            if wlf.loc == 3:
                screen.blit(wlf.img, (85, 120))
            if croc.loc == 3:
                screen.blit(croc.img, (185, 120))
            if s.loc == 3:
                screen.blit(s.img, (400, 220))
        
        if cam == 4:
            screen.blit(cam_4, (85, 120))
            if wlf.loc == 4:
                screen.blit(wlf.img, (85, 120))
            if croc.loc == 4:
                screen.blit(croc.img, (185, 120))
            if s.loc == 4:
                screen.blit(s.img, (400, 220))
        
        if cam == 5:
            screen.blit(cam_5, (85, 120))
            if wlf.loc == 5:
                screen.blit(wlf.img, (85, 120))
            if croc.loc == 5:
                screen.blit(croc.img, (400, 220))
            if s.loc == 5:
                screen.blit(s.img, (400, 220))
        
        if cam == 6:
            screen.blit(cam_6, (85, 120))
            if wlf.loc == 6:
                screen.blit(wlf.img, (85, 120))
            if croc.loc == 6:
                screen.blit(croc.img, (185, 120))
            if s.loc == 6:
                screen.blit(s.img, (400, 220))
        
        if cam == 7:
            screen.blit(cam_7, (85, 120))
            if wlf.loc == 7:
                screen.blit(wlf.img, (85, 120))
            if croc.loc == 7:
                screen.blit(croc.img, (185, 120))
            if s.loc == 7:
                screen.blit(s.img, (400, 220))
        
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
            
def s_move():
    global inv
    global s_disable
    global s_countdown
    
    if s.counter == s.need:
        inv = False
        s.loc = 10
        s_disable = True
        s.counter = 0
        s.need = random.randint(10, 15)
        # This puts him in the state where he's off to the side but will JS you in like 5 seconds or so.
        #This \/ is the countdown timer.
        s_countdown = 100
    else:
        s.counter += 1
        s.loc = random.randint(0, 7)

def s_js():
    global plane
    global has_food
    global has_sound
    global s_disable
    global x
    
    plane -= 10
    has_food = False
    has_sound = False

    while x != 20:
        chosenimg = pygame.image.load(s.crowjs[x])
        newimg = pygame.transform.scale(chosenimg, (1400, 750))
        screen.blit(newimg, (0, 0))
        pygame.display.flip()
        time.sleep(.03)
        x += 1
    s.loc = 4
    s_disable = False

def s_reset():
    global x
    global s_disable
    global sjs
    
    s.loc = 4
    s_disable = False
    x = 0
    s.timer = 100
    s.counter = 0
    s.need = random.randint(10, 15)
    sjs = False
    screen.blit(inv_img, (0, 0))

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
    global s_countdown
    global sjs
    global croc_countdown
    global wlf_countdown
    global nightvision
    
    # Event loop
        
    while True:
            
        if s_countdown > 0:
            s_countdown -= 1
        if s_countdown == 0:
            sjs = True
            s_countdown = -1
            
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
                nightvision = False
                   
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
                    if inv == True:
                        nightvision = True
                        
                if event.key == pygame.K_DOWN:
                    if inv == True:
                        inv = False
                    if inv == False:
                        view = 0
                    
                if event.key == pygame.K_SPACE:
                    if inv == True:
                        
                        if has_food == True:
                            wlf.loc = cam
                            wlf.need += 7
                            has_food = False
                            screen.blit(inv_img, (0, 0))
                            
                        if has_sound == True:
                            croc.loc = cam
                            croc.need += 7
                            has_sound = False
                            screen.blit(inv_img, (0, 0))
                            
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
            if wlf.timer >= (500 // w_dif):
                wlf_move()
                wlf.timer = 0
            
        if not c_disable:
            croc.timer += 1
            if croc.timer >= (800 // c_dif):
                croc_move()
                croc.timer = 0
        
        if cam == s.loc:
            s_disable = True
            s.timer -= 5
        if cam != s.loc:
            s_disable = False
            
        if s_disable == False:
            s.timer += 1
            if s.timer >= (50 // s_dif):
                s_move()
                s.timer = 0
                
        if sjs == True:
            s_js()
            s_reset()
            
        pygame.display.flip()
main()