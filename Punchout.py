import pygame
from pygame.locals import *
import random

pygame.init()
screen_width = 833
screen_height = 581
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Boxing Game')
clock = pygame.time.Clock()
collision_tolerance = 10
platform_velocity= 3 




# Load images
background_IMG = pygame.image.load('background.jpg')
boxer_stand = pygame.transform.scale(pygame.image.load('boxer-stand.png'), (85, 200))
boxer_left_punch = pygame.transform.scale(pygame.image.load('boxer-left-punch.png'), (85, 200))
boxer_right_punch = pygame.transform.scale(pygame.image.load('boxer-right-punch.png'), (85, 200))
enemy_stand = pygame.transform.scale(pygame.image.load('enemy-stand.png'), (150, 260))
enemy_punch1 = pygame.transform.scale(pygame.image.load('enemy-punch1.png'), (150, 260))
enemy_punch2 = pygame.transform.scale(pygame.image.load('enemy-punch2.png'), (170, 275))
enemy_block = pygame.transform.scale(pygame.image.load('enemy-block.png'), (150, 260))

def collision_check(collision_tolerance,enemy,boxer,):
   if boxer.rect.colliderect(enemy):
        if abs(enemy.rect.x - boxer.rect.x) < collision_tolerance: #if they collide
                boxer.score = boxer.score + 5

                                           
#collison when boxer hits enemy = health is deceased 
    #when the boxer punches and is in the same area as the enemy AND the enemy does not have the box image 
    #then health is decrease from the enemy, same with the boxer.
        
    

class Boxer:
    def __init__(self, x, y):
        self.image = boxer_stand
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.score = 0 

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
        self.velocity = platform_velocity
        self.action_time = 0  # Initialize action_time
        self.action = 'stand' 
        self.score = 0 
        self.move_timer = 0
        self.move_duration = random.randint(30, 120)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
   
    def update(self):
        if self.action_time == 0:
            self.action = random.choice(['punch_left', 'punch_right', 'block', 'stand'])
            if self.action in ['punch_left', 'punch_right']:
                self.action_time = 30 #punches are faster (more realistic)
            else:
                self.action_time = 60 

            if self.action == 'punch_left':
                self.image = enemy_punch1
            elif self.action == 'punch_right':
                self.image = enemy_punch2
            elif self.action == 'block':
                self.image = enemy_block
            elif self.action == 'stand':
                self.image = enemy_stand
        else:
            self.action_time -= 1
            #if the enemy is not punching or blocking then it must go into the stand position 
            if self.action_time == 0 and self.action != 'stand':
                self.action = 'stand'
                self.action_time = 60
                self.image = enemy_stand

        if self.move_timer <= 0:
            self.move_timer = self.move_duration  # Reset move timer
            self.move_duration = random.randint(30, 120)  # Set new random duration
            self.velocity = random.choice([-platform_velocity, platform_velocity])  # Randomly choose new velocity direction
        else:
            self.move_timer -= 1
            self.rect.x += self.velocity  # Move the enemy

        # only allowed to move in a certain area, and enemy turns around when its reached the end of the area
        if self.rect.left <= 150 or self.rect.right >= screen_width - 250:
            self.velocity *= -1
#lines 67 to 105 are from chatgpt 
enemy = Enemy(340, 150)
boxer = Boxer(350, 250)

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
                if enemy.image != enemy_block:
                    collision_check(collision_tolerance, enemy, boxer)
            elif event.key == K_r:
                boxer.punch_right()
                if enemy.image != enemy_block:
                    collision_check(collision_tolerance, enemy, boxer)
        elif event.type == KEYUP:
            if event.key in [K_l, K_r]:
                boxer.stand()
#------------------------------------ will be boxing gloves 

    enemy.draw(screen)
    enemy.update()
    boxer.draw(screen)
    pygame.display.update()
    clock.tick(60)  # Limit the frame rate to 60 frames per second

pygame.quit()
# next steps 
# collison when boxer hits enemy = health is deceased 
    #when the boxer punches and is in the same area as the enemy AND the enemy does not have the box image DONE 
    #score is added DONE 
# make the enemy move side to side - moving rocks in other game 
# make boxer hit randomly  DONE 
# round1 screen 
# options to play again 