# This file was created by: Ben Maya on 10/05/2023
# Content from Chris Bradfield; Kids Can Code
# KidsCanCode - Game Development with Pygame video series
# Video link: https://youtu.be/Omlq0XVvIn0

# important libraries and packages
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
import os
from settings import *
from sprites import *

vec = pg.math.Vector2

# setup asset folders here
game_folder = os.path.dirname(__file__)
# img_folder = os.path.join(myGame, 'theBell.png')

'''# game settings
WIDTH = 500
HEIGHT = 500 
FPS = 30'''

# player settings
PLAYER_JUMP = 100
PLAYER_GRAV = 1

# define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(GREEN)
        # self.image = pg.image.load(os.path.join(myGame, 'theBell.png')).convert()
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        print(self.rect.center)
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5
        if keys[pg.K_d]:
            self.acc.x = 5
        # if keys[pg.K_w]:
            self.acc.y = -5
        # if keys[pg.K_s]:
            self.acc.y = 5
        if keys[pg.K_SPACE]:
            self.jump()
    def jump(self):
        hits = pg.sprite.spritecollide(self, all_platforms, False)
        if hits:
            print("i can jump")
            self.vel.y = -PLAYER_JUMP
    def update(self):
        # self.rect.x += 5
        # self.rect.y += 5
        self.acc = vec(0, PLAYER_GRAV)
        self.controls()
        hits = pg.sprite.spritecollide(self, all_platforms, False)
        if hits:
            print("I've collided")
            if self.rect.bottom >= hits[0].rect.bottom-5:
                self.rect.bottom = hits[0].rect.top
                self.vel.y = 0
        # if fricction - apply here
        self.acc.x += self.vel.x * -0.2
        self.acc.y += self.vel.y * -0.2
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        '''
        if self.rect.x > WIDTH:
            self.rect.x = 0
        if self.rect.y > HEIGHT:
            self.rect.y = 0
        '''
        self.rect.midbottom = self.pos

# platforms

class Platform(Sprite):
    def __init__(self, x, y, w, h, k):
        Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(BLACK)
        # self.image = pg.image.load(os.path.join(img_folder, 'theBell.png')).convert()
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.kind = k
        # self.pos = vec(WIDTH/2, HEIGHT/2)
        # self.vel = vec(0,0)
        # self.acc = vec(0,0)
        print(self.rect.center)
    # def update(self):
        self.pos = self.rect.x
        self.rect.x = self.pos + 2

class Mob(Sprite):
    def __init__(self, x, y, w, h, k):
        Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.kind = k
    def seeking(self):
        if player.rect.x > self.rect.x:
            self.rect.x +=1
        if player.rect.x > self.rect.x:
            self.rect.x -=1
        if player.rect.y > self.rect.y:
            self.rect.y +=1
        if player.rect.y > self.rect.y:
            self.rect.y +=1
    def update(self):
        self.seeking()


class Ice_plat(Platform):
    def __init__(self, x, y, w, h, k):
        Platform.__init__(self)

# init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game...")
clock = pg.time.Clock()

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("My Game...")
        clock = pg.time.Clock()
    def new(self):
        # create a group for all sprites
        self.all_sprites = pg.sprite.Group()
        self.all_platforms = pg.sprite.Group()
        self.all_mobs = pg.sprite.Group()
        # instantiate  class
        player = Player()
        plat = Platform(50, 300, 75, 200, "normal")
        plat1 = Platform(250, 75, 75, 450, "moving")
        plat2 = Platform(400, 350, 75, 200, "moving")
        # instances to groups
        self.all_sprites.add(self.player)

for p in PLATFORM_LIST:
    # instantiation of the Platform class
    plat = Platform(*p)
    all_sprites.add(plat)
    all_platforms.add(plat)

for m in range(0, 25):
    m = Mob(randint(0, WIDTH), randint (0, HEIGHT/2))
    all_sprites.add(m)
'''all_sprites.add(plat)
all_sprites.add(plat1)
all_sprites.add(plat2)
all_platforms.add(plat)
all_platforms.add(plat1)
all_platforms.add(plat2)'''






# Game loop
running = True
while running:
    # keep the loop running using clock
    clock.tick(FPS)
        
    for event in pg.event.get():
        # check for closed window
        if event.type == pg.QUIT:
            running = False
    
    ############ Update ##############
    # update all sprites
    all_sprites.update()

    # this is what prevents the player from falling through the platform when falling down...
    if player.vel.y > 0:
            hits = pg.sprite.spritecollide(player, all_platforms, False)
            if hits:
                player.pos.y = hits[0].rect.top
                player.vel.y = 0
                
    # this prevents the player from jumping up through a platform
    '''if player.vel.y < 0:
        hits = pg.sprite.spritecollide(player, all_platforms, False)
        if hits:
            print("ouch")
            if player.rect.bottom >= hits[0].rect.top - 5:
                player.rect.top = hits[0].rect.bottom
                player.acc.y = 5
                player.vel.y = 0'''

    ############ Draw ################
    # draw the background screen
    screen.fill(RED)
    # draw all sprites
    all_sprites.draw(screen)
    
    # buffer - after drawing everything, flip display
    pg.display.flip()


pg.quit()