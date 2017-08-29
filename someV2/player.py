import pygame
import constants
import levels

from platforms import MovingPlatform
from spritesheet_functions import SpriteSheet
 
    # --- BATMAN Player Sprite
class Player(pygame.sprite.Sprite):
    # this class represents the bar at the bottom that the player controls

    # -- methods
    def __init__(self):
        #constructor function
        super(Player, self).__init__()

        # attributes
        # set vector speed
        self.change_x = 0
        self.change_y = 0

        # this holds all the animated images for walking left/right
        self.walking_frames_l = []
        self.walking_frames_r = []

        # What direction is the player facing?
        self.direction = "R"

        # list of sprites we can bump up against
        self.level = None

        sprite_sheet = SpriteSheet('batsprite.png')
        # Load all the right facing images into a list
        #image = sprite_sheet.get_image(18,750,104,148)
        #self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(421,269,39,66)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(464,272,36,64)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(502,271,38,64)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(542,273,42,63)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(2,202,36,60)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(43,205,51,60)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(97,206,67,57)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(167,208,60,58)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(231,209,60,59)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(296,207,68,59)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(367,210,69,49)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(436,204,63,57)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(501,200,63,63)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(567,204,65,55)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(2,277,67,58)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(69,274,64,63)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(137,278,63,60)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(202,281,67,56)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(277,277,68,52)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(352,281,62,56)
        self.walking_frames_r.append(image)




        # Load all the right facing images, then flip to face left

        #image = sprite_sheet.get_image(18,750,104,148)
        #image = pygame.transform.flip(image, True, False)
        #self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(421,269,39,66)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(464,272,36,64)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(502,271,38,64)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(542,273,42,63)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(2,202,36,60)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(43,205,51,60)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(97,206,67,57)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(167,208,60,58)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(231,209,60,59)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(296,207,68,59)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(367,210,69,49)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(436,204,63,57)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(501,200,63,63)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(567,204,65,55)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(2,277,67,58)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(69,274,64,63)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(137,278,63,60)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(202,281,67,56)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(277,277,68,52)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(352,281,62,56)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)


        # Set the image player starts with
        self.image = self.walking_frames_r[0]

        # set a reference to the image rect
        self.rect = self.image.get_rect()

        # -- Weapon & Shield init
        self.shield = 100
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()



    def update(self):
        # unhide if hidden
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.y = 340
            #self.rect.bottom = HEIGHT - 10
        # move the player
        # Gravity
        self.calc_grav()

        # move left/right
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        # see if hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right

        # move up/down
        self.rect.y += self.change_y

        # -- Shoot
        #keystate = pygame.key.get_pressed()
        #if keystate[pygame.K_SPACE]:
            #self.shoot()

        # check if hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # stop vertival movement
            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

    def calc_grav(self):
        # calc effects of gravity
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # see if we are on the ground
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def jump(self):

        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # if it's ok to jump, set speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -10

    # Player Controlled Movement
    def go_left(self):
        # called when user hits the Left Arrow
        self.change_x = -6
        self.direction = "L"

    def go_right(self):
        self.change_x =6
        self.direction = "R"

    def stop(self):
        # called when nothing is being pressed
        self.change_x = 0

    def shoot(self):

        bullet = Bullet()
        # -- autofire
        #now = pygame.time.get_ticks()
        #if now - self.last_shot > self.shoot_delay:
            #self.last_shot = now
            #bullet = Bullet()
            #active_sprite_list.add(bullet)
            #bullet.add(bullets)

    def hide(self):
        # hide player temporarily
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (constants.WIDTH / 2, constants.HEIGHT + 200)


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,5))
        self.image = pygame.image.load('batarang_img.png').convert()
        transColor = self.image.get_at((0,0))
        self.image.set_colorkey(transColor)
        self.rect = self.image.get_rect()

        self.speedx = 10


    def update(self):
        self.rect.x += self.speedx



        # kill if it moves off the top of the screen
        if self.rect.left < 0 or self.rect.right > 6000:
            self.kill()
