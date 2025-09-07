import math
import pygame
import random
SCREEN_WIDTH= 800
SCEEN_HEIGHT=500
PLAYER_START_X=370
PLAYER_START_Y= 380
ENEMY_START_Y_MIN=50
ENEMY_START_Y_MAX=150
ENEMY_SPEED_X=4
ENEMY_SPEED_Y=40
BULLET_SPEED_Y=10
BULLET_SPEED_X=27 
pygame.init()
screen=pygame.display.set_mode((
SCREEN_WIDTH,SCEEN_HEIGHT
))

background = pygame.image.load('c:/Users/ibrah/Downloads/spacerni.jpg')
pygame.display.set_caption('Space invader')
Playerimg=pygame.image.load('c:\Users/ibrah/Downloads/rocku.jpg')
playerX= PLAYER_START_X
playerY=PLAYER_START_Y
playerX_change = 0

enemy_Img=[]
enemyX_change=[]
enemyY_change = []
num_of_enemies=6