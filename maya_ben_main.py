# This file was created by: Ben Maya on 10/24/2023
# code from Chris Bradfield's tutorials
# content from kids can code: http://kidscancode.org/blog/
# https://github.com/kidscancode/pygame_tutorials/tree/master/platform

'''
GameDesign:
Goals
Rules
Feedback
Freedom

Goals for code:
1. Immersive/Creative World (platforms and background)
2. Creative Sprites (for user and mobs/"coins")
3. Fire Subtract a Point Mob (new class)

ALL SPRITES WERE SELF-MADE USING A "PIXEL STUDIO APP"

'''


# import libraries and modules
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
import os
from settings import *
from sprites import *

vec = pg.math.Vector2

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
'''important becuase I had to add a lot of custom made images... never got to adding sound'''
snd_folder = os.path.join(game_folder, 'sounds')

class Game:
    def __init__(self):
        # init pygame and create a window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("My Game...")
        self.clock = pg.time.Clock()
        self.running = True
    
    def new(self):
        # create a group for all sprites
        self.bgimage = pg.image.load(os.path.join(img_folder, 'maya_ben_mainpy_bg.png')).convert()
        '''code above is part of what allowed me to get my custom made background into the game
        credit: https://www.askpython.com/python-modules/pygame-looping-background '''
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.all_platforms = pg.sprite.Group()
        self.all_points = pg.sprite.Group()
        self.all_fires = pg.sprite.Group()
        '''new "fire" class I made up... when player hits fire subtract a point'''
        # instantiate classes
        self.player = Player(self)
        # add instances to groups
        self.all_sprites.add(self.player)
        for p in PLATFORM_LIST:
            # instantiation of the Platform class
            plat = Platform(*p)
            self.all_sprites.add(plat)
            self.all_platforms.add(plat)

        for m in range(0,10):
            '''used variable "m" because this class was originally "mobs" although I changed it to Points... 
            variable "p" was alerady being used for "Platforms"
            '''
            m = Point(randint(0, WIDTH), randint(0, HEIGHT/2), 20, 20, "normal")
            self.all_sprites.add(m)
            self.all_points.add(m)
        
        '''more or less used same code for the fire balls as I did for the points
        only decided to have 7 fireballs instead of 10 because the game was too difficult.'''
        for f in range(0,7):
            f = Fire(randint(0, WIDTH), randint(0, HEIGHT/2), 20, 20)
            self.all_sprites.add(f)
            self.all_fires.add(f)

        self.run()
    '''this code below "runs" the game... all the updates, time, sprites, images''' 
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()

        # this is what prevents the player from falling through the platform when falling down...
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.all_platforms, False)
            '''when the player and the platform "collides"'''
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
                self.player.vel.x = hits[0].speed*1.5


    def events(self):
        for event in pg.event.get():
        # check for closed window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
    def draw_text(self, text, size, color, x, y):
            font_name = pg.font.match_font('arial')
            font = pg.font.Font(font_name, size)
            text_surface = font.render(text, True, color)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x,y)
            self.screen.blit(text_surface, text_rect)

    def show_start_screen(self):
            pass
    def show_go_screen(self):
            pass
    def draw(self):
        self.screen.blit(self.bgimage, (0,0))
        '''drawing the bacckground image I introduced earlier in this code
        credit: https://www.askpython.com/python-modules/pygame-looping-background'''
        # draw all sprites
        self.all_sprites.draw(self.screen)
        self.draw_text("Score: " + str(self.score), 22, WHITE, WIDTH/2, HEIGHT/10)
        '''these two lines above help display the score'''
        # buffer - after drawing everything, flip display
        pg.display.flip()    
    
g = Game()
while g.running:
    g.new()

pg.quit()