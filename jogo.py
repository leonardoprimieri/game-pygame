import pygame
import time
import random

pygame.init()

######## Variáveis Globais ########
tela_largura = 800
tela_altura = 600
gameDisplay = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption("Iron Man Marcão")
icone = pygame.image.load("assets/ironIcon.png")
pygame.display.set_icon(icone)
explosao_sound = pygame.mixer.Sound("assets/explosao.wav")
missile_sound = pygame.mixer.Sound("assets/missile.wav")



clock = pygame.time.Clock()
# RGB
black = (0, 0, 0)
white = (255, 255, 255)
ironMan = pygame.image.load("assets/ironLarge.png")
iron_largura = 120
iron_altura = 100

missile = pygame.image.load("assets/missile.png")
missile_largura = 50
missile_altura = 250

fundo = pygame.image.load("assets/sky.png")

######## Funções Globais ########


def mostrarIron(x, y):
    gameDisplay.blit(ironMan, (x, y))


def mostraMissile(x, y):
    gameDisplay.blit(missile, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (tela_largura/2, tela_altura/2)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)
    game_loop()


def dead():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(explosao_sound)
    message_display("Você Morreu")


def escrePlacar(contador):
    font = pygame.font.SysFont(None, 45)
    text = font.render("Desvios: "+str(contador), True, white)
    gameDisplay.blit(text, (10, 30))

# Looping do Jogo


def game_loop():
    pygame.mixer.music.load("assets/ironsound.mp3")
    pygame.mixer.music.play(-1)

    iron_posicaoX = 350
    iron_posicaoY = 450
    movimentoX = 0
    missile_spped = 7
    missile_posicaoX = random.randrange(0, tela_largura)
    missile_posicaoY = -250
    desvios = 0

    while True:
        # inicio - Interação do usuário
        # event.get do pygame, devolve uma lista de eventos da janela
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                # fecha tudo!
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    movimentoX = -10
                elif evento.key == pygame.K_RIGHT:
                    movimentoX = 10
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    movimentoX = 0
        iron_posicaoX = iron_posicaoX + movimentoX
        # fim - Interação do usuário

        # Alterando a cor de fundo da tela
        gameDisplay.fill(white)
        gameDisplay.blit(fundo, (0, 0))

        mostrarIron(iron_posicaoX, iron_posicaoY)

        mostraMissile(missile_posicaoX, missile_posicaoY)
        missile_posicaoY = missile_posicaoY + missile_spped

        if missile_posicaoY > tela_altura:
            pygame.mixer.Sound.play(missile_sound)
            missile_posicaoY = 0 - missile_altura
            missile_spped += 1
            missile_posicaoX = random.randrange(0, tela_largura)
            desvios = desvios + 1

        escrePlacar(desvios)

        if iron_posicaoX > tela_largura - iron_largura:
            iron_posicaoX = tela_largura - iron_largura
        elif iron_posicaoX < 0:
            iron_posicaoX = 0

        if iron_posicaoY+50 < missile_posicaoY + missile_altura:
            if iron_posicaoX < missile_posicaoX and iron_posicaoX + iron_largura > missile_posicaoX or missile_posicaoX+missile_largura > iron_posicaoX and missile_posicaoX + missile_largura < iron_posicaoX + iron_largura:
                dead()

        pygame.display.update()
        clock.tick(60)


game_loop()
