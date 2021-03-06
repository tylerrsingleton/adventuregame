### Adventure Game Project ###
#By Friday, 2/16/18, create a window and charcter
#that can move side to side with the arrow keys.
#By Friday, 3/9/18, fix program and add characteristics to background and character.
#By Friday, 3/23/17, create clock, add exit, add fruit, and add collision

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

#Exit color
b = 0
variation = 5

#food characteristics
food_x = random.randint(0,950)
food_y = random.randint(0,450)
food_location = (food_x, food_y)
food_color = (255,0,255)
food_draw = True

#Character speed
speed = 5

#Create main loop
drawing = True
while drawing:
    #Create event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= speed
            elif event.key == pygame.K_RIGHT:
                x += speed
            elif event.key == pygame.K_UP:
                y -= speed
            elif event.key == pygame.K_DOWN:
               y += speed
               
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
    game_exit = pygame.Rect(980, 400, 20, 100)
    pygame.draw.rect(w, exit_color, game_exit)
    
    #Have the exit color pulse white to yellow:
    b += variation
    if b > 255:
        b = 255
        variation *= -1
    elif b < 0:
        variation *= -1
        b = 0 
        
    #Draw food:
    if food_draw:
        pygame.draw.circle(w, food_color, food_location, 10)
        
    #Check for collision between the exit and the character
    if 980 <= x <= 1000:
        if 400 <= y <= 480:
            drawing = False
            print("Congradulations! You beat the level.")
            
    #Check for collision between the fruit and the character
    if (food_x - 30) <= x <= (food_x + 30):
        if (food_y - 30) <= x <= (food_x + 30):
            speed += 5
            food_draw = False
            
    #Check for collision between the bomb and the character
    if (bx - 30) <= x <= (bx + 30):
        if (by - 30) <= x <= (by + 30):
            print("Game Over")
            drawing = False           

    #Set tick
    c.tick(30)
    
    #Flip display and fill window
    pygame.display.flip()
    w.fill((0,0,0))
