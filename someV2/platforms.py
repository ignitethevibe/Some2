# - module for managing platforms

import pygame
from spritesheet_functions import SpriteSheet

# These constants define our platform types:
# -- Name of file
# -- X Location of sprite
# -- Y location of sprite
# -- Width of sprite
# -- Height of Sprite

# ---- bottom right sprites ---
# -- Blocks and Rectangles
METAL_BLOCK1        = (1680, 1030, 45, 45)
METAL_BLOCK2        = (1727,1032,45,45)
METAL_BLOCK3        = (1725, 1077, 45, 45)
GEAR_BLOCK1         = (1613, 597,41,39) # orange patterned
GRINDO              = (1497, 887, 89, 48)
BIG_BLOCK           = (1591, 986, 86,91)
BIG_BLOCK_RIGHT     = (1864, 1033, 71, 70)
BIG_BLOCK_LEFT      = (1974, 1032, 71, 70)
BIG_BLOCK_RIGHT2    = (1864, 1139, 71, 70) # bottom
BIG_BLOCK_LEFT2     = (1976, 1142, 71, 70) # bottom 
BLOCK_O_TOP         = (1635, 1168, 43 ,48) # 0_TOP = Orange Top
REC_O_TOP1          = (1678, 964 ,97, 19)
REC_O_TOP2          = (1772, 962, 94, 24)
REC_O_TOP3          = (1953,1009,88,20)
BLOCK_O_LEFT        = (1704, 639, 47, 50)

SOLID_M_COLUMN      = (1637,893,38,92)

# -- Graphic Blocks
BRIGHT_NEON_BLOCK   = (1405, 1215, 88, 66)
LIGHT_NEON_BLOCK    = (1589, 1216, 88, 66)
M_COLUMN            = (1598,763,30,48)
LARGE_COLUMN        = (1843, 734, 41, 136)
SMILEY              = (1473, 592, 44, 52)
BIG_PIPE_BLOCK      = (1314, 940, 92, 87)

# -- For Moving

METAL_RECT1         = (1728, 760 ,89,39)
METAL_RECT_THIN1    = (1728, 802, 87, 18)
M_SHAPED            = (1406, 1017, 84, 59)

# ---             -----



class Platform(pygame.sprite.Sprite):

    def __init__(self, sprite_sheet_data):
        super(Platform, self).__init__()

        sprite_sheet = SpriteSheet("some_tiles.png")
        # grab the image for this platform
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
        self.rect = self.image.get_rect()

class MovingPlatform(Platform):
    # fancy platform that can move
    def __init__(self, sprite_sheet_data):
        super(MovingPlatform, self).__init__(sprite_sheet_data)

        self.change_x = 0
        self.change_y = 0

        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0

        self.level = None
        self.player = None

    def update(self):
        # if player is in the way it will shove player out of the way

        # move left/right
        self.rect.x += self.change_x

        # See if hit player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                self.player.rect.left = self.rect.right

        # move up/down
        self.rect.y += self.change_y

        # check for collision
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        # check boundaries if need to reverse movement
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
