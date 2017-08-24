import pygame
import constants
import levels
import random
from spritesheet_functions import SpriteSheet
from os import path


pygame.init()
size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)

# -- establish image path
img_dir = path.join(path.dirname(__file__), 'img')

enemy_anim = {}
enemy_anim['fly'] = []
for i in range(6):
    filename = 'dragonFly0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    transColor = img.get_at((0,0))
    img.set_colorkey(transColor)
    enemy_anim['fly'].append(img)



class FlyEnemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.anim = enemy_anim['fly'][0]
        self.image = self.anim
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(1200, 4500)
        self.rect.y = random.randrange(5, 120)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-6,-3)



        self.boundary_left = 0
        self.boundary_right = 0

    def update(self):

        self.rect.x += self.speedx

        # Check the boundaries and see if we need to reverse
        #if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            #self.change_y *= -1


        #cur_pos = self.rect.x - self.level.world_shift
        #if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            #self.change_x *= -1
            #self.image = pygame.transform.flip(self.image, True, False)
