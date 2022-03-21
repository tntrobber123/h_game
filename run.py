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

screen.blit(testbkgrnd, (-500, 0))
pygame.display.flip()

view = 0
move = 0
pause = False
inv = True

def vision():
    global view
    screen.blit(testbkgrnd, ((-500 - (view * 10)), 0))
    pygame.display.flip()

def main():
    global pause
    global move
    global view
    
    # Event loop
    while pause == True:
        global inv
        screen.blit(inv_img, (0, 0))
        pygame.display.flip()
        inv = True
        
    if pause == False:
        while True:
            print(pause)
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
                        move = 1
                        
                    if event.key == pygame.K_LEFT:
                        move = -1
                        
                    if event.key == pygame.K_UP:
                        if inv == False:
                            pause = False
                        
                    if event.key == pygame.K_DOWN:
                        if inv == False:
                            pause = True
                    
                    if event.key == pygame.K_SPACE:
                        # Light or other function?
                        pass
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
main()