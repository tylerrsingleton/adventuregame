### Adventure Game Project ###
#By Friday, 2/16/18, create a window and charcter
#that can move side to side with the arrow keys.
#By Friday, 3/9/18, fix program and add characteristics to background and character.

#import random
import random

#import and initialize pygame
import pygame
pygame.init()

#Create window and fill
w = pygame.display.set_mode([1000,500])
w.fill((0,0,0))

#Create clock
c = pygame.time.Clock()

#Create characteristics of character
character_color = (0, 255, 255)
x = 0
y = 0

#Bomb characteristics
bomb_color = (239,73,40)
bx = 1000
by = random.randint(0,255)

#Create main loop
drawing = True
while drawing:
    #Create event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 5
            elif event.key == pygame.K_RIGHT:
                x += 5
            elif event.key == pygame.K_UP:
                y -= 5
            elif event.key == pygame.K_DOWN:
               y += 5
               
    #Draw the character, eyes, and mouth
    pygame.draw.circle(w, character_color, (x,y), 25)
    pygame.draw.circle(w, (0,0,0), (x-8, y), 5)
    pygame.draw.circle(w, (0,0,0), (x+8, y), 5)
    pygame.draw.line(w, (0,0,0), (x-8, y+8), (x+8, y+8))
    
    #Draw bomb
    pygame.draw.circle(w, bomb_color, (bx,by), 30)
    bx -= 10
    if bx == 0:
        bx = 1000
        by = random.randint(0, 255)
        
    #Draw exit
    exit_color = (255,255,255)
    game_exit = pygame.Rect(980, 400, 20, 80)
    pygame.draw.rect(w, exit_color, game_exit)
    
    #Set tick
    c.tick(30)
    
    #Flip display and fill window
    pygame.display.flip()
    w.fill((0,0,0))
