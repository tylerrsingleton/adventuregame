### Adventure Game Project ###
#By Friday, 2/16/18, create a window and charcter
#that can move side to side with the arrow keys.
#By Friday, 3/9/18, fix program and add characteristics to background and character.

#import and initialize pygame
import pygame
pygame.init()

#Create window
w = pygame.display.set_mode([1000,500])

#Create characteristics of character
character_color = (0, 255, 255)
x = 0
y = 0

#Create main loop
drawing = True
while drawing:
    #Create event loop
    for event in pygame.event.get():
        if event.type == pyamge.QUIT:
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
               
    #Draw the character
    pygame.draw.circle(w, character_color, (x,y), 25)
    
    pygame.display.flip()
    w.fill((255,255,255))
