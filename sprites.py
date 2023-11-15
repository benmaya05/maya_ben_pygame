# This file was created by: Ben Maya 10/24/2023
import pygame as pg
from pygame.sprite import Sprite

from pygame.math import Vector2 as vec
import os
from settings import *

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
'''important becuase I had to add a lot of custom made images... never got to adding sound'''
snd_folder = os.path.join(game_folder, 'sounds')

class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        self.game = game
        '''below I imported my custom made sprite for the player's character'''
        self.image = pg.image.load(os.path.join(img_folder, 'maya_ben_mainpy_drop.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.pos = vec(WIDTH/2, 320)
        '''changed "self.pos = vec(WIDTH/2, HEIGHT/2)" to "self.pos = vec(WIDTH/2, 320)" so that player would start near the ground...
        there was a problem where points were either getting subtracted/added because player spawned on them'''
        self.vel = vec(0,0)
        self.acc = vec(0,0) 
    def controls(self):
        '''controls for the key board
        a == left
        d == right
        space == jump'''
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5
        if keys[pg.K_d]:
            self.acc.x = 5
        if keys[pg.K_SPACE]:
            self.jump()
    def jump(self):
        hits = pg.sprite.spritecollide(self, self.game.all_platforms, False)
        if hits:
            print("i can jump")
            self.vel.y = -PLAYER_JUMP
    def update(self):
        self.acc = vec(0,PLAYER_GRAV)
        self.controls()
        # if friction - apply here
        self.acc.x += self.vel.x * -PLAYER_FRIC
        # self.acc.y += self.vel.y * -0.3
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
        ''' changed language for it to make more sense to me...
        "pluspoints" and "minuspoints"'''
        pluspoints = pg.sprite.spritecollide(self, self.game.all_points, True)
        if pluspoints:
            self.game.score += 1
        '''added in this code below to subtract points from score when player collides with a fireball'''
        minuspoints = pg.sprite.spritecollide(self, self.game.all_fires, True)
        if minuspoints:
            self.game.score -= 1
'''
class Ground(Sprite):
    def __init__(self, x, y, w, h, category):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y'''




# Platforms
class Platform(Sprite):
    def __init__(self, x, y, w, h, category):
        '''category can be either moving or normal'''
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        '''self.image = pg.image.load(os.path.join(img_folder, 'maya_ben_mainpy_lavaplat.png')).convert()
        originally where I tried to import my custom platform image... but this ruined the groun platform'''
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.category = category
        self.speed = 0
        if self.category == "moving":
            self.speed = 5
            '''added a custom image which I created for all the moving platforms to go with the fire vs. water theme
            only applied this custom image to moving plats because if I applied it to all plat it would ruin the "groun platfirm"'''
            self.image = pg.image.load(os.path.join(img_folder, 'maya_ben_mainpy_lavaplat.png')).convert()
        '''if self.category == "lava":
            self.image.fill(RED) 
        ATTEMPTED TO ADD LAVA PLATFORMS HERE'''
    def update(self):
        if self.category == "moving":
            self.rect.x += self.speed
            if self.rect.x + self.rect.w > WIDTH or self.rect.x < 0:
                self.speed = -self.speed
        '''if self.category == "lava":
            hits = pg.sprite.spritecollide(Player(self), self.all_platforms, False)
            if hits:
                self.score -= 1
                AGAIN ATTEMPTED TO ADD LAVA PLATFORMS HERE'''

# Points
class Point(Sprite):
    def __init__(self, x, y, w, h, kind):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        '''code below allowed me to import my own custum image for the player's sprite'''
        self.image = pg.image.load(os.path.join(img_folder, 'maya_ben_mainpy_h2o.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.kind = kind
        self.pos = vec(WIDTH/2, HEIGHT/2)

# Fires
'''used very similar code to what we had for the "Points" class... 
there was no "kind" value for this class, so I got rid of that'''
class Fire(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        "imported my custon made sprite for the Fire here below"
        self.image = pg.image.load(os.path.join(img_folder, 'maya_ben_mainpy_fire.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pos = vec(WIDTH/2, HEIGHT/2)
    
    def update(self):
        pass