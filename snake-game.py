import pygame
import time
import random

# Inicializar o pygame
pygame.init()

# Definir cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Definir tamanho da tela
largura = 600
altura = 400

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

# Configurações da cobra
tamanho_cobra = 10
velocidade_cobra = 15

clock = pygame.time.Clock()

# Fonte para exibir a pontuação
fonte = pygame.font.SysFont("bahnschrift", 25)

def mostrar_pontuacao(pontos):
    valor = fonte.render(f"Pontuação: {pontos}", True, branco)
    tela.blit(valor, [10, 10])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, verde, [pixel[0], pixel[1], tamanho, tamanho])

def jogo():
    game_over = False
    game_close = False

    x = largura / 2
    y = altura / 2

    delta_x = 0
    delta_y = 0

    corpo_cobra = []
    comprimento_cobra = 1

    comida_x = round(random.randrange(0, largura - tamanho_cobra) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura - tamanho_cobra) / 10.0) * 10.0

    while not game_over:
        while game_close:
            tela.fill(preto)
            mensagem = fonte.render("Game Over! Pressione C para jogar de novo ou Q para sair", True, vermelho)
            tela.blit(mensagem, [largura / 6, altura / 3])
            mostrar_pontuacao(comprimento_cobra - 1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        jogo()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    delta_x = -tamanho_cobra
                    delta_y = 0
                elif event.key == pygame.K_RIGHT:
                    delta_x = tamanho_cobra
                    delta_y = 0
                elif event.key == pygame.K_UP:
                    delta_x = 0
                    delta_y = -tamanho_cobra
                elif event.key == pygame.K_DOWN:
                    delta_x = 0
                    delta_y = tamanho_cobra
        
        if x >= largura or x < 0 or y >= altura or y < 0:
            game_close = True
        
        x += delta_x
        y += delta_y
        tela.fill(preto)
        pygame.draw.rect(tela, azul, [comida_x, comida_y, tamanho_cobra, tamanho_cobra])
        
        corpo_cobra.append([x, y])
        if len(corpo_cobra) > comprimento_cobra:
            del corpo_cobra[0]
        
        for segmento in corpo_cobra[:-1]:
            if segmento == [x, y]:
                game_close = True
        
        desenhar_cobra(tamanho_cobra, corpo_cobra)
        mostrar_pontuacao(comprimento_cobra - 1)
        
        pygame.display.update()
        
        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_cobra) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura - tamanho_cobra) / 10.0) * 10.0
            comprimento_cobra += 1
        
        clock.tick(velocidade_cobra)
    
    pygame.quit()
    quit()

jogo()
