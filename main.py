import pygame
import math
import time

pygame.mixer.init()
from pygame.locals import *
import random

"""Some variable declarations"""
pygame.init()  # initializing pygame
pygame.font.init()  # initializing font
pygame.mixer.init()  # initializing mixer

"""screen width and height"""
screen_width = 600  # screen width
screen_height = 500  # screen height
window = pygame.display.set_mode((screen_width, screen_height))  # getting window

"""initial state and position of bullet"""
bullet_state = "ready"
bulletx = 0  # initial x position of bullet
bullety_change = 500 - 64  # initial bullet y position

"""loading bullet.png or images of bullet """
bullet_img = pygame.image.load("bullet.png").convert_alpha()  # image of bullet

"""setting game icon and caption"""
pygame.display.set_icon(pygame.image.load("game logo.png"))  # setting logo of game
pygame.display.set_caption("Space invader")  # getting caption

"""  writing about options of main menu  """
text = pygame.font.Font("freesansbold.ttf", 40)  # creating a object of Font class with ttf file
start = text.render("Start game", True, (255, 255, 255))  # rendering  start text
text_about = pygame.font.Font("freesansbold.ttf", 40)
about = text_about.render("About", True, (255, 255, 255))  # rendering about text
rect_about = about.get_rect(topleft=(230, 200))
rect_start = start.get_rect(topleft=(230, 150))
help = text.render("Help", True, (255, 255, 255))
rect_help = help.get_rect(topleft=(230, 250))

"""loading and playing background music"""
pygame.mixer.music.load("game background sound.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)


""" declaring some empty list for enemy images and their coordinates"""
temp = "enemy"
list_all_enemy_img = [pygame.image.load(temp + str(i) + ".png") for i in range(1, 8)]
enemies_img = []
x_enemies = []
y_enemies = []
no_enemies = random.randint(1, 3)
def enemy_enemy():


    """generates the random images of enemies"""
    for no in range(0, no_enemies):
        enemy = random.choice(list_all_enemy_img)
        enemies_img.append(enemy)

    """generate the random coordinates for enemy image """
    for coordinates in range(0, no_enemies):
        x_enemy = random.randint(0, 600 - 65)
        x_enemies.append(x_enemy)
        y_enemies.append(0)
enemy_enemy()

"""declaring some empty lists"""
no_bullet =7
bullet_enemyx = []
bullet_enemyy = []
def bullet_enemy():
    """generating random coordinates of bullet"""
    for index in range(0, no_bullet):
        bullet_enemyx.append(random.randint(0, 600 - 64))
        random_bullety = random.randint(500, 700)
        bullet_enemyy.append(-random_bullety)

bullet_enemy()


def help_text():
    while True:
        """blitting and updating for background"""
        window.blit(pygame.image.load("background.png"), (0, 0))  # blitting background image

        """looking for events"""
        for event_about in pygame.event.get():
            """Closing the game """
            if event_about.type == pygame.QUIT or (event_about.type == KEYDOWN and event_about.key == K_ESCAPE):
                pygame.quit()
                break
            if event_about.type == KEYDOWN and event_about.key == K_BACKSPACE:
                return
        text_headinghelp = pygame.font.Font("freesansbold.ttf", 55)  # creating new objects
        help_heading = text_headinghelp.render("Help", True, (0, 0, 0))  # render the font
        height_help = help_heading.get_height()  # storing the size of variable on height_help text
        window.blit(help_heading, (200, 30))

        text_description_aboutgame = pygame.font.Font("freesansbold.ttf", 23)  # creating new objects
        description_help = text_description_aboutgame.render("If  you  find any  bugs or want  to make  any ", True,
                                                             (255, 255, 255))
        description_help1 = text_description_aboutgame.render(" suggestion for enhancement of game you can ", True,
                                                              (255, 255, 255))
        description_help2 = text_description_aboutgame.render("simply mail on  \"vishwaofficial791@gmail.com\". ", True,
                                                              (255, 255, 255))
        window.blit(description_help, (20, height_help + 30 + 20))

        window.blit(description_help1, (20, height_help + 30 + 20 + description_help.get_height() + 10))

        window.blit(description_help2, (
            20, height_help + 30 + 20 + description_help.get_height() + 10 + description_help.get_height() + 10))

        text_description_aboutgame = pygame.font.Font("freesansbold.ttf", 23)  # creating new objects
        go_back = text_description_aboutgame.render("<BACK", True, (255, 255, 255))
        rect_goback = go_back.get_rect(topleft=(2, 2))
        window.blit(go_back, (2, 2))
        pygame.display.update()
        event_mouse_help = pygame.mouse.get_pressed()
        pos_mouse_help = pygame.mouse.get_pos()
        """checking cursor for going back"""
        if rect_goback.collidepoint(pos_mouse_help):
            set_underlineback()
            if event_mouse_help[0]:
                return


def about_text():
    """Under About option"""
    while True:

        """blitting and updating for background"""
        window.blit(pygame.image.load("background.png"), (0, 0))  # blitting background image

        """looking for events"""
        for event_about in pygame.event.get():
            """Closing the game """
            if event_about.type == pygame.QUIT or (event_about.type == KEYDOWN and event_about.key == K_ESCAPE):
                pygame.quit()
                break
            if event_about.type == KEYDOWN and event_about.key == K_BACKSPACE:
                return
        """blitting and updating for \'about the game\'"""
        text_aboutthegame = pygame.font.Font("freesansbold.ttf", 55)  # creating new objects
        about_the_game = text_aboutthegame.render("About The Game-", True, (0, 0, 0))  # render the font
        height_aboutthegame = text_aboutthegame.get_height()  # storing the size of variable on height_aboutthegame
        window.blit(about_the_game, (80, 20))

        """blitting and updating for \'description for the game\'"""
        text_description_aboutgame = pygame.font.Font("freesansbold.ttf", 23)  # creating new objects
        go_back = text_description_aboutgame.render("<BACK", True, (255, 255, 255))
        rect_goback = go_back.get_rect(topleft=(2, 2))
        window.blit(go_back, (2, 2))

        description_game1 = text_description_aboutgame.render("This game is written in Python 3.7.1 ",
                                                              True, (255, 255, 255))
        description_game2 = text_description_aboutgame.render("Being a 2d game,it is user friendly and interactive ",
                                                              True, (255, 255, 255))
        description_game3 = text_description_aboutgame.render("This game contain many  options. The help option is ",
                                                              True, (255, 255, 255))
        description_game4 = text_description_aboutgame.render("provided if you stuck somewhere.", True, (255, 255, 255))
        height_description1 = description_game1.get_height()  # assigning the value of height to variable
        window.blit(description_game1, (10, height_aboutthegame + 30))

        window.blit(description_game2, (10, height_aboutthegame + 30 + height_description1 + 10))

        window.blit(description_game3,
                    (10, height_aboutthegame + 30 + height_description1 + 10 + height_description1 + 10))

        window.blit(description_game4, (
            10,
            height_aboutthegame + 30 + height_description1 + 10 + height_description1 + 10 + height_description1 + 10))

        """blitting and updating for \"description of about the developer\""""
        heading_developer = text_aboutthegame.render("About The Developer", True,
                                                     (0, 0, 0))  # rendering for heading of about the game
        window.blit(heading_developer, (20, 250))

        description_developer = text_description_aboutgame.render("This game is designed and written by", True,
                                                                  (255, 255, 255))
        description_developer1 = text_description_aboutgame.render("Vishwa", True, (255, 255, 255))
        window.blit(description_developer, (10, 250 + heading_developer.get_height() + 10))

        window.blit(description_developer1,
                    (10, 250 + heading_developer.get_height() + 10 + description_developer.get_height() + 10))
        pygame.display.update()  # updating display
        event_mouse_about = pygame.mouse.get_pressed()
        pos_mouse_about = pygame.mouse.get_pos()
        """checking cursor for going back"""
        if rect_goback.collidepoint(pos_mouse_about):
            set_underlineback()
            if event_mouse_about[0]:
                return


def set_underlinehelp():
    """This function set underline on help text and set itallic"""
    text_start = pygame.font.Font("freesansbold.ttf", 40)  # creating a object of Font class with ttf file
    text_start.set_underline(True)  # setting underline
    text_start.set_italic(True)  # setting italic
    help = text_start.render("Help", True, (255, 255, 255))  # start text with underline and italic
    window.blit(help, (230, 250))  # bliiting the start text with underline and italic
    pygame.display.update()  # updating  the start text with underline and italic


def set_underlineback():
    """This function underline the back and set italic"""
    text_description_aboutgame = pygame.font.Font("freesansbold.ttf", 23)
    text_description_aboutgame.set_underline(True)
    text_description_aboutgame.set_italic(True)
    go_back1 = text_description_aboutgame.render("<BACK", True, (255, 255, 255))
    window.blit(go_back1, (2, 2))
    pygame.display.update()


def set_underlinetostart():
    """This function set underline on start text and set itallic"""
    text_start = pygame.font.Font("freesansbold.ttf", 40)  # creating a object of Font class with ttf file
    text_start.set_underline(True)  # setting underline
    text_start.set_italic(True)  # setting italic
    start = text_start.render("Start game", True, (255, 255, 255))  # start text with underline and italic
    window.blit(start, (230, 150))  # bliiting the start text with underline and italic
    pygame.display.update()  # updating  the start text with underline and italic


def set_underlinetoabout():
    """This function set underline to about text and italic it"""
    text_about = pygame.font.Font("freesansbold.ttf", 40)  # creating a object of Font class with ttf file
    text_about.set_underline(True)  # setting underline
    text_about.set_italic(True)  # setting italic
    about = text_about.render("About", True, (255, 255, 255))  # start text with underline and italic
    window.blit(about, (230, 200))  # bliiting the start text with underline and italic
    pygame.display.update()  # updating  the start text with underline and italic


def start_text():
    """This function contain the real game"""
    # infinite loop for game

    playerx = 290  # initial x position of player
    playery = 500 - 64 - 5  # initial y position of player
    bkg = pygame.image.load("background.png").convert()  # background image 1
    bkg2 = pygame.image.load("background.png").convert()  # background image 2
    bkgy = 0  # initial y position for background image 1
    bkgy2 = -925  # initial y position for background image 2
    enemy_img1 = pygame.image.load("enemy1.png").convert_alpha()
    bullet = pygame.image.load("bullet.png").convert_alpha()
    bullet_img_enemy = pygame.image.load("bullet enemy.png").convert_alpha()
    score_user = 0
    text = pygame.font.Font("freesansbold.ttf", 38)
    score = text.render("Score:" + str(score_user), True, (255, 255, 255))
    blast = pygame.image.load("blast.png").convert_alpha()

    while True:

        """scrolling background image"""
        window.blit(bkg, (0, bkgy))
        bkgy = bkgy + 1
        window.blit(bkg2, (0, bkgy2))
        bkgy2 += 1
        if bkgy2 == 0:
            bkgy = -925
        if bkgy == 0:
            bkgy2 = -925
        """blitting for enemy images"""
        global bullety_change
        global bulletx

        for events in pygame.event.get():
            if events.type == pygame.QUIT or (
                    events.type == KEYDOWN and events.key == K_ESCAPE):  # closing the game with cross mark  and escape key

                pygame.quit()

        player_img = pygame.image.load("player.png")
        window.blit(pygame.image.load("player.png").convert_alpha(), (playerx, playery))  # blitting for player image

        input_key = pygame.key.get_pressed()
        """moving right"""
        if input_key[K_RIGHT]:
            playerx += 7
            if playerx > 600 - player_img.get_width():
                playerx = 600 - player_img.get_width()
            else:
                pass

            window.blit(pygame.image.load("player.png").convert_alpha(),
                        (playerx, playery))  # blitting for player image
        """moving left """
        if input_key[K_LEFT]:
            playerx -= 7
            if playerx < 0:
                playerx = 0
            else:
                pass
            window.blit(pygame.image.load("player.png").convert_alpha(),
                        (playerx, playery))  # blitting for player image
        """ moving down"""
        if input_key[K_DOWN]:
            playery += 7
            if playery > 500 - player_img.get_height():
                playery = 500 - player_img.get_height()

            window.blit(pygame.image.load("player.png").convert_alpha(),
                        (playerx, playery))  # blitting for player image
        """ moving up """
        if input_key[K_UP]:
            playery -= 7
            if playery < 0:
                playery = 0
            else:
                pass

            window.blit(pygame.image.load("player.png").convert_alpha(),
                        (playerx, playery))  # blitting for player image
        """bullet shoot only if it is out of screen"""

        if input_key[K_SPACE]:
            global bullet_state
            if bullet_state is "ready":
                """playingt bullet sound"""
                bullet_sound = pygame.mixer.Sound("player shot.wav")
                pygame.mixer.music.set_volume(0.2)
                bullet_sound.play()
                bulletx = playerx + 20
                fire_bullet(bulletx, playery)
                bullety_change = playery

        """reseting bullet position"""
        if bullety_change <= 0:
            bullet_state = "ready"
            bullety_change = 480
        """finally firing bullet"""
        if bullet_state == "fire":
            if bullety_change > 0:
                bullety_change -=13
                rect_bullet = bullet_img.get_rect(topleft=(bulletx, bullety_change))
                fire_bullet(bulletx, bullety_change)
        # global x_enemies
        global bullet_enemyy
        global no_enemies
        """ blitting and generating enemies """
        for index in range(0, no_enemies):

            window.blit(enemies_img[index], (x_enemies[index], y_enemies[index]))
            enemy_rect = enemies_img[index].get_rect(topleft=(x_enemies[index], y_enemies[index]))
            """ cheking for enemy killing """
            iscollide = collide_bullet(x_enemies[index], y_enemies[index], bullety_change, bulletx, enemy_rect)

            if iscollide:
                score_user = score_user + 1
                score = text.render("Score:" + str(score_user), True, (255, 255, 255))
                enemy_killed_sound = pygame.mixer.Sound("enemy killed.wav")
                pygame.mixer.music.set_volume(0.1)
                enemy_killed_sound.play()
                enemies_img[index] = random.choice(list_all_enemy_img)
                x_enemies[index] = random.randint(0, 600 - 65)
                changed_y_enemy = random.randint(70, 100)
                y_enemies[index] = -changed_y_enemy

                inc_img_enemy = random.randint(0, 1)
                if no_enemies != 3:
                    for i in range(0, inc_img_enemy):
                        enemies_img.append(random.choice(list_all_enemy_img))
                        x_enemies.append(random.randint(0, 600 - 65))
                        y_enemy = random.randint(70, 200)
                        y_enemies.append(-y_enemy)
                        bullet_enemyy.append(0)
                    no_enemies = no_enemies + inc_img_enemy
        """ incrimenting the y cordinates of enemies """
        for index in range(0, no_enemies):
            if y_enemies[index] > 550:
                y_enemies[index] = -70
            else:
                y_enemies[index] += 2

                """checking if player died or not with enemy's spaceship"""
                x_enemy_present = x_enemies[index]
                temp_enemy_rect = enemies_img[index].get_rect(topleft=(x_enemies[index], y_enemies[index]))

                isplayer_died = player_died(y_enemies[index], x_enemy_present, playery, playerx, temp_enemy_rect)
                if isplayer_died:
                    window.blit(blast, (playerx, playery))
                    player_lose_sound = pygame.mixer.Sound("player lose.wav")
                    pygame.mixer.music.set_volume(0.1)
                    player_lose_sound.play()
                    game_over()
                    window.blit(score,(150,100))
                    pygame.display.update()
                    """reseting"""
                    enemies_img.clear()
                    x_enemies.clear()
                    y_enemies.clear()
                    bullet_enemyx.clear()
                    bullet_enemyy.clear()
                    bullet_enemy()
                    enemy_enemy()

                    time.sleep(3)
                    return

        for index in range(no_bullet):
            window.blit(bullet_img_enemy, (bullet_enemyx[index], bullet_enemyy[index]))
            rect_bullet_enemy = pygame.image.load("player.png").get_rect(topleft=(playerx, playery))
            isplayerdied_bullet = player_died_bullet(bullet_enemyx[index], bullet_enemyy[index], rect_bullet_enemy)
            """"checking if player died by enemies'bullet"""
            if isplayerdied_bullet:
                window.blit(blast, (playerx, playery))
                enemy_killed_sound = pygame.mixer.Sound("player lose.wav")
                pygame.mixer.music.set_volume(0.1)
                enemy_killed_sound.play()
                game_over()
                window.blit(score,(150,100))
                pygame.display.update()
                """reseting everything in game"""
                enemies_img.clear()
                x_enemies.clear()
                y_enemies.clear()
                bullet_enemyx.clear()
                bullet_enemyy.clear()
                bullet_enemy()
                enemy_enemy()

                time.sleep(3)
                return
        """ moving random bullet """
        for index in range(no_bullet):
            random_endpoint = random.randint(700, 1000)
            if bullet_enemyy[index] > random_endpoint:
                random_startpoint = random.randint(100, 200)
                bullet_enemyy[index] = -random_startpoint
            else:
                bullet_enemyy[index] += 2
        window.blit(score, (0, 0))
        pygame.display.update()


def player_died_bullet(playerx, playery, rect_enemy):
    """this function cheks if player died by enemies bullet"""
    pos_player = playerx, playery
    if rect_enemy.collidepoint(pos_player):
        return True
    else:
        return False


def game_over():
    """blitting game over text"""
    text = pygame.font.Font("freesansbold.ttf", 70)
    game_over = text.render("Game Over", True, (255, 255, 255))
    window.blit(game_over, (150, 250))


def player_died(enemyy, enemyx, playery, playerx, enemy_rect):
    """This function checks if player died or not"""
    pos_player = playerx, playery
    if enemy_rect.collidepoint(pos_player):
        return True
    else:
        return False


def collide_bullet(enemyx, enemyy, bullety, bulletx, rect_enemy):
    """This functions checks if bullet collide with enemies or not"""
    # distance=math.sqrt(math.pow(enemyx-bulletx,2)+math.pow(enemyy-bullety,2))
    pos = bulletx, bullety_change
    if rect_enemy.collidepoint(pos):
        return True
    else:
        return False


def fire_bullet(bulletx, bullety):
    """this function blit the image of bullet"""

    global bullet_state
    bullet_state = "fire"
    window.blit(bullet_img, (bulletx, bullety))


clock = pygame.time.Clock()
# main game  loop
while True:
    """Blitting and updating"""

    """background image"""

    window.blit(pygame.image.load("background.png"), (0, 0))  # blitting background image

    """start text
    """
    window.blit(start, (230, 150))  # blitting start text

    """about text"""
    window.blit(about, (230, 200))

    pos_mouse = pygame.mouse.get_pos()
    """help text"""
    window.blit(help, (230, 250))  # blitting start text

    """events """
    for events in pygame.event.get():
        if events.type == pygame.QUIT or (
                events.type == KEYDOWN and events.key == K_ESCAPE):  # closing the game with cross mark  and escape key
            pygame.quit()
    event_mouse = pygame.mouse.get_pressed()
    """checking for pointer on start text"""
    if rect_start.collidepoint(pos_mouse):
        set_underlinetostart()
        """game start"""
        if event_mouse[0]:
            start_text()
    # """checking for cursor on about text"""
    if rect_about.collidepoint(pos_mouse):
        set_underlinetoabout()
        if event_mouse[0]:
            """All information about the game and developer"""
            about_text()
    """checking for cursor on help text"""
    if rect_help.collidepoint(pos_mouse):
        set_underlinehelp()
        """Going inside help option"""
        if event_mouse[0]:
            help_text()
    textt=pygame.font.Font("freesansbold.ttf",15)
    developer=textt.render("Vishwa -Make It Easy!",True,(255,255,255))
    window.blit(developer,(445,480))
    pygame.display.update()  # updatingfor player image
