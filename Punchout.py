import pygame
from pygame.locals import *

pygame.init()
screen_width = 833
screen_height = 581
screen = pygame.display.set_mode ((screen_width, screen_height))
pygame.display.set_caption('Platformer')
#load image 
background_IMG = pygame.image.load('background.jpg')

class Player:
    def __init__(self, x, y):
        # Load and resize and posistioning the icecube
        self.image = pygame.transform.scale(pygame.image.load('boxer-stand.png'),(100,150))
        self.rect = self.image.get_rect()
        self.rect.x =- 0 #left 
        self.rect.x = 350 #  right  of the screen
        self.rect.y = 400   #  bottom of the screen
    def draw(self, surface):
        surface.blit(self.image, self.rect) #show on screen(surface)


class Enemy:
    def __init__(self, x, y):
        # Load and resize and posistioning the icecube
        self.image = pygame.transform.scale(pygame.image.load('enemy-stand.png'),(150,200))
        self.rect = self.image.get_rect()  
        self.rect.x =- 0 #left 
        self.rect.x = 330 #  right  of the screen
        self.rect.y = 200 #  bottom of the screen
    def draw(self, surface):
        surface.blit(self.image, self.rect)      
        
        
        
       
        
    
run = True
while run:

    screen.blit(background_IMG,(0, 0))
    boxer = Player(10,10)
    enemy = Enemy(10,10)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            run = False
        
    boxer.draw(screen) #have to make an update and draw 
    enemy.draw(screen)
    pygame.display.update()
pygame.quit ()
