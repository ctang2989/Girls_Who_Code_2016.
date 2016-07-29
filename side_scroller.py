import pygame
import random
#import the Scroller to use as background
#from scroller import Scroller
#import building_while.py  
from block import *


pygame.init()
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])
    
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)


clock = pygame.time.Clock()
score = 0
lives = 5

## The scroller object is created here
#any_scroller = building.Building(screen_width, 300, screen_height, (255, 100, 100), 2)

## Font to allow for 
font = pygame.font.SysFont("Gill Sans", 25, True, False)

# Blocks for first run of game, stores them in all the lists
make_blocks()
keys = pygame.key.get_pressed() 
#check that game is not done
done = False

#Start game loop

while not done:
    for event in pygame.event.get():

#        if keys[pygame.K_LEFT]:
 #           self.rect.x -= 5
  #      if keys[pygame.K_RIGHT]:
   #         self.rect.x += 5
    #    if keys[pygame.K_UP]:       
     #       self.rect.y -= 5
      #  if keys[pygame.K_DOWN]:
       #     self.rect.y += 5 
       
   
        if event.type == pygame.QUIT: 
            done = True

                
    # Clear the screen
    screen.fill(WHITE)

    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()
 
    # Fetch the x and y out of the list,
    # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location
    player.rect.x = pos[0]
    player.rect.y = pos[1]

    # See if the player block has collided with anything.
    black_blocks_hit_list = pygame.sprite.spritecollide(player, black_block_list, True)
    green_blocks_hit_list = pygame.sprite.spritecollide(player, green_block_list, True)

    # Move the blocks.
    black_block_list.update()
    green_block_list.update()

    # Check the list of collisions.
    for block in green_blocks_hit_list:
        score += 1

    for block in black_blocks_hit_list:
        lives -= 1

    #Creates the scrote variables using pretty font    
    score_text = font.render("Score: " +str(score), True, BLACK)
    lives_text = font.render("Lives: "+ str(lives), True, BLUE)

    #keeps the text on the page at these coordinates
    screen.blit(score_text, [500, 50])
    screen.blit(lives_text, [50, 50])

    
    # Draw the scrolling background
    #Add your scrolling background here
    #any_scroller.draw_buildings(screen)
    #any_scroller.move_buildings()

    # Draw all the sprites  
    all_sprites_list.draw(screen)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
exit()

