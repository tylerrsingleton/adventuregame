### Adventure Game Project ###
#By Friday, 2/16/18, create a window and charcter
#that can move side to side with the arrow keys.

#import and initialize pygame
import pygame
pygame.init()

#Create window
w = pygame.display.set_mode([1000,500])

#Create character
character = pygame.Rect(900,450,0,10,10)

#Create main loop
drawing = True
while drawing:
    #Create event loop
    for event in pygame.event.get():
        if event.type == pyamge.QUIT:
            drawing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character.x -= 5
            elif event.key == pygame.K_RIGHT:
                character.x += 5
            elif event.key == pygame.K_UP:
                character.y -= 5
            elif event.key == pygame.K_DOWN:
                character.y += 5
                

    #Draw the character
    pygame.draw.ellipse(0, (0,255,255), character)
    
    pygame.display.flip()
    w.fill((255,255,255))
