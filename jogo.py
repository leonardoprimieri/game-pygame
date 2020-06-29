import pygame
import time
import random
from functions.userFunctions import userInfos

userInfos()


pygame.init()

screen_width = 800
screen_height = 600
game_display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Iron Man Marcão")
icon = pygame.image.load("assets/ironIcon.png")
pygame.display.set_icon(icon)
explosion_sound = pygame.mixer.Sound("assets/explosao.wav")
missile_sound = pygame.mixer.Sound("assets/missile.wav")


clock = pygame.time.Clock()
iron_man = pygame.image.load("assets/ironLarge.png")
iron_width = 120
iron_height = 100

missile = pygame.image.load("assets/missile.png")
missile_width = 50
missile_height = 250

background = pygame.image.load("assets/sky.png")

white = (0, 0, 0)


def showIron(x, y):
    game_display.blit(iron_man, (x, y))


def showMissile(x, y):
    game_display.blit(missile, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def messageDisplay(text):
    large_text = pygame.font.Font("freesansbold.ttf", 115)
    TextSurf, TextRect = text_objects(text, large_text)
    TextRect.center = (screen_width/2, screen_height/2)
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)
    game_loop()


def dead():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(explosion_sound)
    messageDisplay("Você Morreu")


def showCount(contador):
    font = pygame.font.SysFont(None, 45)
    text = font.render("dodge: "+str(contador), True, white)
    game_display.blit(text, (10, 30))


def game_loop():
    pygame.mixer.music.load("assets/ironsound.mp3")
    pygame.mixer.music.play(-1)

    iron_position_x = 350
    iron_position_y = 450
    move_x = 0
    missile_speed = 7
    missile_position_x = random.randrange(0, screen_width)
    missile_position_y = -250
    dodge = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_x = -10
                elif event.key == pygame.K_RIGHT:
                    move_x = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    move_x = 0
        iron_position_x = iron_position_x + move_x

        game_display.fill(white)
        game_display.blit(background, (0, 0))

        showIron(iron_position_x, iron_position_y)

        showMissile(missile_position_x, missile_position_y)
        missile_position_y = missile_position_y + missile_speed

        if missile_position_y > screen_height:
            pygame.mixer.Sound.play(missile_sound)
            missile_position_y = 0 - missile_height
            missile_speed += 1
            missile_position_x = random.randrange(0, screen_width)
            dodge = dodge + 1

        showCount(dodge)

        if iron_position_x > screen_width - iron_width:
            iron_position_x = screen_width - iron_width
        elif iron_position_x < 0:
            iron_position_x = 0

        if iron_position_y+50 < missile_position_y + missile_height:
            if iron_position_x < missile_position_x and iron_position_x + iron_width > missile_position_x or missile_position_x+missile_width > iron_position_x and missile_position_x + missile_width < iron_position_x + iron_width:
                dead()

        pygame.display.update()
        clock.tick(60)


game_loop()
