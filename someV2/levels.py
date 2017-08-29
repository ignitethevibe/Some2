import pygame

import constants
import platforms
from fly_enemy import FlyEnemy
from player import Bullet


class Level():
    # generic super class used to define level

    def __init__(self, player, bullet, drag):
        # Constructor. Pass in a handle to player. needed for when collides

        # Lists of sprites used in all levels
        # Add or Remove Lists needed for game
        self.platform_list = None
        self.enemy_list = None

        self.char_list = None

        # Background Image
        self.background = None

        # How far this world has been scrolled to left/right
        self.world_shift = 0
        self.level_limit = -1000
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group()
        self.player = player
        self.bullet = bullet
        self.drag = drag


    # update everything on this level
    def update(self):
        self.platform_list.update()
        self.enemy_list.update()
        self.bullet_list.update()


    def draw(self, screen):
        # draw everything on this level
        # don't shift the background as much as the sprites are shifted
        # to give a feeling of depth
        screen.fill(constants.blue)
        screen.blit(self.background, (self.world_shift // 3,0))

        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.bullet_list.draw(screen)


    def shift_world(self, shift_x):
        # when the user moves left/right scroll everything

        # keep track of shift amount'
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

        for bullet in self.bullet_list:
            bullet.rect.x += shift_x


# Create platforms for the Level
class Level_01(Level):
    # Definiton for Level 1

    def __init__(self, player, bullet, drag):
        # create level 1

        # call the constructor
        Level.__init__(self, player, bullet, drag)

        self.background = pygame.image.load('cityscape.png').convert()
        self.background.set_colorkey(constants.white)
        self.level_limit = -4000
        #bullet = Bullet(player.rect.x, player.rect.y)
        self.bullet_list.add(bullet)
        for i in range(6):
            drag = FlyEnemy()
            self.enemy_list.add(drag)

        # Array with type of platform, and x, y location of the platform
        level = [[platforms.METAL_BLOCK1, 420, 565],
                [platforms.METAL_BLOCK3, 465, 565],
                [platforms.METAL_BLOCK2, 510, 565],
                [platforms.BIG_BLOCK_RIGHT, 555, 530],
                [platforms.BIG_BLOCK_LEFT, 626, 530],
                [platforms.GRINDO, 765, 395],
                [platforms.BLOCK_O_TOP, 905, 395],
                [platforms.BLOCK_O_TOP, 948, 395],
                [platforms.REC_O_TOP1, 1025, 370],
                [platforms.REC_O_TOP1, 1165, 315],
                # G-Blocks
                [platforms.BIG_BLOCK, 935, 509],
                [platforms.LIGHT_NEON_BLOCK, 1021, 509],
                [platforms.M_COLUMN, 1055, 572],
                [platforms.LARGE_COLUMN, 1295, 464],
                [platforms.SMILEY, 1294, 412],
                #
                [platforms.BIG_BLOCK_RIGHT2, 1705, 530],
                [platforms.BIG_BLOCK_RIGHT, 1705, 460],
                [platforms.BIG_BLOCK_LEFT2, 1776, 530],
                [platforms.BIG_BLOCK_LEFT, 1776, 460],
                [platforms.BIG_PIPE_BLOCK, 1730, 373],
                # - Continuous Path and add enemies
                [platforms.REC_O_TOP1, 1847, 555],
                [platforms.REC_O_TOP3, 1944, 555],
                [platforms.REC_O_TOP2, 2032, 555],
                [platforms.REC_O_TOP3, 2126, 555],
                [platforms.REC_O_TOP1, 2214, 555],
                [platforms.REC_O_TOP1, 2311, 555],
                [platforms.REC_O_TOP1, 2408, 555],
                [platforms.BLOCK_O_LEFT, 2501, 525],
                [platforms.REC_O_TOP2, 2548, 525],
                [platforms.REC_O_TOP1, 2642, 525],
                [platforms.REC_O_TOP1, 2739, 525],
                [platforms.REC_O_TOP1, 2832, 525],
                [platforms.REC_O_TOP1, 2925, 525],
                [platforms.REC_O_TOP1, 2918, 525],
                [platforms.REC_O_TOP1, 3011, 525],
                [platforms.REC_O_TOP1, 3106, 525],
                [platforms.BIG_BLOCK_RIGHT2, 3203, 530],
                [platforms.BIG_BLOCK_RIGHT, 3203, 460],
                [platforms.BIG_BLOCK_LEFT2, 3274, 530],
                [platforms.BIG_BLOCK_LEFT, 3274, 460],
                [platforms.BLOCK_O_TOP, 3345, 475],
                [platforms.BLOCK_O_TOP, 3388, 475],
                [platforms.BLOCK_O_TOP, 3421, 475],
                [platforms.BLOCK_O_TOP, 3464, 475],
                [platforms.BLOCK_O_TOP, 3507, 475],
                [platforms.GEAR_BLOCK1, 3345, 520],
                [platforms.GEAR_BLOCK1, 3345, 559],
                [platforms.GEAR_BLOCK1, 3345, 598],

                    ]

        # Go through array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.METAL_RECT1)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)





# add Level 2
class Level_02(Level):
    def __init__(self, player, bullet, drag):
        Level.__init__(self, player, bullet, drag)

        self.background = pygame.image.load('pokeclouds.png').convert()
        self.background.set_colorkey(constants.white)
        self.level_limit = -1000

        level = [[platforms.METAL_BLOCK3,0, 550 ],
                [platforms.METAL_BLOCK1, 132, 550],
                [platforms.METAL_BLOCK2, 264, 550],
                ]


        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # moving
        block = platforms.MovingPlatform(platforms.METAL_RECT_THIN1)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
