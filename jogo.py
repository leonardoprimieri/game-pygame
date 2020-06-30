import pygame
import time
import random
from functions.userFunctions import userInfos

userInfos()


pygame.init()

screen_width = 800
screen_height = 600
game_display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ship Man Marcão")
icon = pygame.image.load("assets/ironIcon.png")
pygame.display.set_icon(icon)
explosion_sound = pygame.mixer.Sound("assets/explosao.wav")

laser_sound = pygame.mixer.Sound("assets/laser.wav")


clock = pygame.time.Clock()
ship = pygame.image.load("assets/mandalorianShip.png")
ship_width = 120
ship_height = 100

laser = pygame.image.load("assets/laser.png")
laser_width = 50
laser_height = 250

background = pygame.image.load("assets/space.jpg")

white = (0, 0, 0)


def showShip(x, y):
    game_display.blit(ship, (x, y))


def showlaser(x, y):
    game_display.blit(laser, (x, y))


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


def showCount(count):
    font = pygame.font.SysFont(None, 45)
    text = font.render("Desvios: "+str(count), True, white)
    game_display.blit(text, (10, 30))


def game_loop():
    pygame.mixer.music.load("assets/ironsound.mp3")
    pygame.mixer.music.play(-1)

    ship_position_x = 600
    ship_position_y = 200
    move_y = 0
    laser_speed = 5
    laser_position_y = random.randrange(0, screen_height)
    laser_position_x = -250
    dodge = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move_y = -10
                elif event.key == pygame.K_DOWN:
                    move_y = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    move_y = 0
        ship_position_y = ship_position_y + move_y

        game_display.fill(white)
        game_display.blit(background, (0, 0))

        showShip(ship_position_x, ship_position_y)

        showlaser(laser_position_x, laser_position_y)
        laser_position_x = laser_position_x + laser_speed

        if laser_position_x > screen_width:
            pygame.mixer.Sound.play(laser_sound)
            laser_position_x = 0 - laser_width
            laser_speed += 1
            laser_position_y = random.randrange(0, screen_width)
            dodge = dodge + 1

        showCount(dodge)

        if ship_position_y > screen_height - ship_height:
            ship_position_y = 500
        elif ship_position_y < 0:
            ship_position_y = 0

        if ship_position_x + 130 < laser_position_x + laser_height:
            if ship_position_y < laser_position_y and ship_position_y + ship_width > laser_position_y or laser_position_y + laser_width > ship_position_y and laser_position_y + laser_width < ship_position_y + ship_width:
                dead()

        pygame.display.update()
        clock.tick(60)


game_loop()
