# This file was created by: Ben Maya on 10/24/2023

# Content from Chris Bradfield; Kids Can Code
# KidsCanCode - Game Development with Pygame video series
# Video link: https://youtu.be/OmlQ0XCvIn0 

# game settings 
WIDTH = 800
HEIGHT = 400
FPS = 30
'''window which the game will played in'''

# player settings
PLAYER_JUMP = 25
PLAYER_GRAV = 1.5
global PLAYER_FRIC
PLAYER_FRIC = 0.2


# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


PLATFORM_LIST = [(0, HEIGHT - 10, WIDTH, 10, "normal"),
                 (699, HEIGHT - 100, 100, 20, "moving"),
                 (0, HEIGHT - 200, 100, 20, "moving"),
                 (400, HEIGHT - 300, 100, 20, "moving"),
                 ]
'''added 1 "moving" platform... originally had five but there was not enough space to move around
had to mess around the with x and y values for the moving platforms to place them at different parts of the map
the one "normal" platform is just the ground'''