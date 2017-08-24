# -- Used to add graphics and images to levels that don't infere with character

import pygame
from spritesheet_functions import SpriteSheet

# These constants define our platform types:
# -- Name of file
# -- X Location of sprite
# -- Y location of sprite
# -- Width of sprite
# -- Height of Sprite




class Decal(pygame.sprite.Sprite):

    def __init__(self, sprite_sheet_data):
        super(Decal, self).__init__()

        sprite_sheet = SpriteSheet("some_sheet.png")
        # grab the image for this platform
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
        self.rect = self.image.get_rect()

class MovingDecal(Platform):
    # fancy decal that can move
    def __init__(self, sprite_sheet_data):
        super(MovingDecal, self).__init__(sprite_sheet_data)

        self.change_x = 0
        self.change_y = 0

        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0

        self.level = None
        self.player = None

    def update(self):


        # move left/right
        self.rect.x += self.change_x




        # move up/down
        self.rect.y += self.change_y
