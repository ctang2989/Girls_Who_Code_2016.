import pygame
import random

pygame.init()

screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height]) #method to create block / square
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = screen_width
        
class otherBlock(Block):
    def update(self):
        super().__init__(color, width, height)
        self.rect.x -= 3
        if self.rect.x < 0:
            self.rect.y = random.randrange(0, screen_height)
            self.rect.x = screen_width + 10
            
            
class Player(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		super().__init__()
		
		self.image = pygame.Surface([width, height]) #method to create block / square
		self.image.fill(color)

		self.rect = self.image.get_rect()
		self.rect.x = 300
		self.rect.y = 200
	

black_block_list = pygame.sprite.Group()
green_block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
player = Player(RED, 20, 15)

def make_blocks():
    all_sprites_list.add(player)
    
    for i in range(50):   
        black_block = otherBlock(BLACK, 20, 15)
        green_block = otherBlock(GREEN, 20, 15)
        
        black_block.rect.x = random.randrange(screen_width, screen_width * 2)
        black_block.rect.y = random.randrange(screen_height)

        green_block.rect.x = random.randrange(screen_width, screen_width * 2)
        green_block.rect.y = random.randrange(screen_height)

        black_block_list.add(black_block)
        green_block_list.add(green_block)
        all_sprites_list.add(black_block)
        all_sprites_list.add(green_block)
