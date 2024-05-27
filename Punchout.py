import pygame
from pygame.locals import *
import random

pygame.init()
screen_width = 833
screen_height = 581
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Boxing Game')
clock = pygame.time.Clock()


# Load images
background_IMG = pygame.image.load('background.jpg')
boxer_stand = pygame.transform.scale(pygame.image.load('boxer-stand.png'), (85, 200))
boxer_left_punch = pygame.transform.scale(pygame.image.load('boxer-left-punch.png'), (85, 200))
boxer_right_punch = pygame.transform.scale(pygame.image.load('boxer-right-punch.png'), (85, 200))
enemy_stand = pygame.transform.scale(pygame.image.load('enemy-stand.png'), (120, 240))
enemy_punch1 = pygame.transform.scale(pygame.image.load('enemy-punch1.png'), (120, 240))
enemy_punch2 = pygame.transform.scale(pygame.image.load('enemy-punch2.png'), (120, 240))
enemy_block = pygame.transform.scale(pygame.image.load('enemy-block.png'), (120, 240))

class Boxer:
    def __init__(self, x, y):
        self.image = boxer_stand
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 100

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def punch_left(self):
        self.image = boxer_left_punch

    def punch_right(self):
        self.image = boxer_right_punch

    def stand(self):
        self.image = boxer_stand

class Enemy:
    def __init__(self, x, y):
        self.image = enemy_stand
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 100
        

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    
enemy = Enemy(340, 150)
boxer = Boxer(350, 375)


run = True
while run:
    screen.blit(background_IMG, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
#----------------------------------- will be boxing gloves
        elif event.type == KEYDOWN:
            if event.key == K_l:
                boxer.punch_left()
            elif event.key == K_r:
                boxer.punch_right()
        elif event.type == KEYUP:
            if event.key in [K_l, K_r]:
                boxer.stand()
#------------------------------------ will be boxing gloves 


    boxer.draw(screen)
    enemy.draw(screen)
    pygame.display.update()
    clock.tick(60)  # Limit the frame rate to 60 frames per second

pygame.quit()
