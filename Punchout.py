#resources used:
# chatgpt was used in the areas that contain ramdonising 
# Writting designed on https://cooltext.com 
# how to make screens and how to add the text to the end screen 
import pygame
from pygame.locals import *
import random

pygame.init()
screen_width = 833
screen_height = 581
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('PUNCHOUT! 1987')
clock = pygame.time.Clock()
#ticks = pygame.time.get_ticks(60)
collision_tolerance = 10
platform_velocity= 3 
#round_finish = False  
#ready_img = pygame.image.load('cooltext459272792198354.gif')
##screen.blit(ready_img, (300,300))
#pygame.wait(500)
#remove.ready_img

# Load images
background_IMG = pygame.image.load('background.jpg')
punchout_img = pygame.image.load('cooltext459279938783312.gif')
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
                enemy.health = enemy.health - 1
                boxer.punches = boxer.punches + 1
   if enemy.rect.colliderect(boxer):
        if abs(boxer.rect.x - enemy.rect.x) < collision_tolerance: #if they collide
                boxer.health = boxer.health - 1
                enemy.punches = enemy.punches + 1                                          
#collison when boxer hits enemy 
    #health is deceased 
    #punch number increases 
    #when the boxer punches and is in the same area as the enemy AND the enemy does not have the box image 
    #then health is decrease from the enemy, same with the boxer.
       # ready go images that disapear when the game starts 

def endscreen(surface,boxer,enemy):
   toughRob = pygame.transform.scale(pygame.image.load('cooltext459331236944502.png'), (200, 100))
   you = pygame.transform.scale(pygame.image.load('cooltext459331271650950.png'), (100, 100))
   pygame.draw.rect(surface,(0,0,0), pygame.Rect(150, 10, 500, screen_height - 20)) #x,y,wight,hieght 
   font = pygame.font.Font(None, 30)
   boxerpunch_text = font.render("Number of punches " + str(boxer.punches),True, (255, 255, 255))
   boxerhealth_text = font.render("Health score " + str(boxer.health),True, (255, 255, 255))
   boxerblocks_text = font.render("Number of blocks " + str(boxer.blocks), True, (255, 255, 255))
   enemypunch_text = font.render("Number of punches " + str(enemy.punches),True, (255, 255, 255))
   enemyblocks_text = font.render("Number of blocks " + str(enemy.blocks),True, (255, 255, 255))
   enemyhealth_text = font.render("Health score " + str(enemy.health),True, (255, 255, 255))
   
   surface.blit(toughRob, (153, 10))
   surface.blit(you,(400, 10))
   surface.blit(enemypunch_text, (153, 300))
   surface.blit(enemyhealth_text, (153, 200))
   surface.blit(enemyblocks_text, (153, 100))
   surface.blit(boxerpunch_text, (400, 300))
   surface.blit(boxerblocks_text, (400, 200))
   surface.blit(boxerhealth_text, (400, 100))
   
  

   pygame.display.flip()
   pygame.time.delay(10000)

   

class Boxer:
    def __init__(self, x, y): #function names and setup taken from last project (not the code inside)
        self.image = boxer_stand
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 100
        self.punches = 0 
        self.blocks = 0

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
        self.velocity = platform_velocity #last project 
        self.action_time = 0  # Initialize action_time
        self.action = 'stand' #chatgpt
        self.health = 100
        self.punches = 0 
        self.blocks = 0
        self.move_timer = 0 #chatgpt
        self.move_duration = random.randint(30, 120) #chatgpt

    def draw(self, surface):
        surface.blit(self.image, self.rect)
   
    def update(self):
        if self.action_time == 0: #chatgpt 
            self.action = random.choice(['punch_left', 'punch_right', 'block', 'stand'])#chatgpt 
            if self.action in ['punch_left', 'punch_right']: #chatgpt 
                self.action_time = 30 #punches are faster (more realistic) #chatgpt 
            else:
                self.action_time = 60 #chatgpt 

            if self.action == 'punch_left':
                self.image = enemy_punch1
            elif self.action == 'punch_right':
                self.image = enemy_punch2
            elif self.action == 'block':
                self.image = enemy_block
            elif self.action == 'stand':
                self.image = enemy_stand
        else:
            self.action_time -= 1 #chatgpt
            #if the enemy is not punching or blocking then it must go into the stand position 
            if self.action_time == 0 and self.action != 'stand':#chatgpt
                self.action = 'stand' #chatgpt
                self.action_time = 60 #chatgpt
                self.image = enemy_stand #chatgpt

        if self.move_timer <= 0: #chatgpt
            self.move_timer = self.move_duration  # Reset move timer #chatgpt
            self.move_duration = random.randint(30, 120)  # Set new random duration #chatgpt
            self.velocity = random.choice([-platform_velocity, platform_velocity])  # Randomly choose new velocity direction #chatgpt
        else: 
            self.move_timer -= 1 #chatgpt
            self.rect.x += self.velocity  # Move the enemy #chatgpt

        # only allowed to move in a certain area, and enemy turns around when its reached the end of the area
        if self.rect.left <= 150 or self.rect.right >= screen_width - 250:
            self.velocity *= -1

#class Rounds():
   # def __init__(timer_ticking,round):
      #  if timer_ticking1 = False:
            #round = round + 1

        #if round > 3:

enemy = Enemy(340, 150) #last project 
boxer = Boxer(350, 250) #last project 
starttime = pygame.time.get_ticks()

# GAME LOOP
run = True
while run :
    screen.blit(background_IMG, (0, 0))
    screen.blit(punchout_img, (80, 25))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
#----------------------------------- will be boxing gloves
        elif event.type == KEYDOWN:
            if event.key == K_l:
                boxer.punch_left()
                if enemy.image != enemy_block:
                    collision_check(collision_tolerance, enemy, boxer)
                else:
                    enemy.blocks = enemy.blocks + 1

            elif event.key == K_r:
                boxer.punch_right()
                if enemy.image != enemy_block:
                    collision_check(collision_tolerance, enemy, boxer)
                else: 
                    enemy.blocks = enemy.blocks + 1

        elif event.type == KEYUP:
            if event.key in [K_l, K_r]:
                boxer.stand()
        
#------------------------------------ will be boxing gloves 
        if enemy.rect.colliderect(boxer):
            if boxer.image != boxer.blocks:
                collision_check(collision_tolerance, enemy, boxer)
            else:
                boxer.blocks = boxer.blocks + 1
    duration_of_game =(pygame.time.get_ticks()-starttime) /1000 #chatgpt
    print(duration_of_game)
    if duration_of_game > 30:
        endscreen(screen, boxer, enemy)
        run = False

    enemy.draw(screen)
    enemy.update()
    boxer.draw(screen)
    
    pygame.display.update()
    clock.tick(60)  # Limit the frame rate to 60 frames per second

pygame.quit()
# next steps 
# varables that store (done with collision )
    #how many punches 
    #how many blocks 
    #health score 

# round only lasts 2mins, when timer is up round 2 then round 3 
    #after that a text box outputting
        # who won 
        # health of both 
        # number of punches 
        # how many blocks 


#whats in the code:
#ready go images that disapear when the game starts 
#timers which runs for 1min saying what round the game is on 
# boxing match happens DONE 
# after round 3 there is a screen saying who won. 