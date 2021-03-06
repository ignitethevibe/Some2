import pygame
import constants
import levels
from player import Player, Bullet
from fly_enemy import FlyEnemy






def main():
    global screen, font, clock
    # -- Main Program ----

    pygame.init()

    # Set the screen dimensions
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Some-2")

    clock = pygame.time.Clock()

    font = pygame.font.Font('freesansbold.ttf', 25)



    #while True:
        #StartScreen()
    runGame()


    # -- Main Program Loop ---
def runGame():
    # create player




    # init Player
    player = Player()
    bullet = Bullet()
    drag = FlyEnemy()


    level_list = []
    level_list.append(levels.Level_01(player, bullet, drag))
    level_list.append(levels.Level_02(player, bullet, drag))


    # set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
    player.level = current_level


    # Sprite Groups
    active_sprite_list = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    enemies = pygame.sprite.Group()



    player.rect.x = 340
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height + 100
    active_sprite_list.add(player)
    enemies.add(drag)
    active_sprite_list.add(drag)
    #active_sprite_list.add(bullet)
    #bullets.add(bullet)
    bullet_count = 0

     #-- Timer Display Setup
    frame_count = 0

    start_time = 45


    # loop until the user clicks the close button
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
                if event.key == pygame.K_SPACE:
                    player.shoot()
                    bullet.rect.x = player.rect.centerx
                    bullet.rect.y = player.rect.y
                    active_sprite_list.add(bullet)
                    bullets.add(bullet)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        bulletCounter = 0





            # update the player
        active_sprite_list.update()

            #update items in the level
        current_level.update()




            # If the player gets near the right side, shift world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)

            # if player gets near left side, shift world right (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)

            # If player gets to end of level, go to next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

        # player collide with FlyEnemy
        flyhit = pygame.sprite.spritecollide(player, enemies, True)
        for hit in flyhit:
            player.kill()
            done = True

        # - Batarang Kill Enemies 
        bathit = pygame.sprite.groupcollide(enemies, bullets, True, True)
        for hit in bathit:
            enemies.kill()

        # -- Win Screen once player reaches end
        #if current_level_no > len(level_list)-2:
            #done = True
            #winScreen()

            # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)



        # --- Timer going up ---
        # Calculate total seconds
        total_seconds = frame_count // constants.frame_rate

        #Calculate for Going Down ---
        #total_seconds = start_time - (frame_count // constants.frame_rate)
        #if total_seconds < 0:
            #total_seconds = 0

        # Divide by 60 to get total minutes
        minutes = total_seconds // 60

        # use remainder to get seconds
        seconds = total_seconds % 60

        # Python string formatting to format into leading zeros
        output_string = "Time Wasted: {0:02}:{1:02}".format(minutes, seconds)

        #blit to screen
        text_time = font.render(output_string, True, constants.red)
        screen.blit(text_time, [15, 5])
        # -------------------Timer-----------
            # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        frame_count += 1
            # limit to 60 frames per second
        clock.tick(constants.frame_rate)

            # update screen
        pygame.display.flip()


        # Add GamesOver Screen
        #if total_seconds == 0:
            #done = True
            #gameOver()


    # to avoid exit errors
    pygame.quit()

if __name__ == '__main__':
    main()
