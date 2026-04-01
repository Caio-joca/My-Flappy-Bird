#Biblioteca para jogos pygames
import pygame
#biblioteca de comandos específicos em python, como sys.exit() para fechar o jogo e o terminal
import sys

#tentativa de aleatoriedade de canos
import random
# Função para carregar módulos da biblioteca pygame, se não precisarioamos carregar várias funções individualmente
pygame.init()


#Função de pontuação

def addingpoints():
    #LÓGICA PARA OS PONTOS
    point=0
    if pipe_position<=90 and pipe_position>=89:
        point+=1
        point_sound()
    if pipe_position2<=90 and pipe_position2>=89:
        point+=1  
        point_sound()
    if pipe_position3<=90 and pipe_position3>=89:
        point+=1
        point_sound()
    return point
    
#Função de reset de canos
def pipereset(posicaodocano,poscanoanterior,altcanodecimafunc,ycanodebaixofunc):
    if posicaodocano<=-100:
            posicaodocano=poscanoanterior+300
            altcanodecimafunc = random.randint(100, 400)
            ycanodebaixofunc  = altcanodecimafunc+150 
    return (posicaodocano, altcanodecimafunc, ycanodebaixofunc)
#Função para se ter música dentro do jogo
'''
Usamos pygame.mixer.sound() para sons rápidos como açoes de pulos
Para ações como trilha sonoras usamos pygame.mixer.music
'''
pygame.mixer.init()
#carregando os sons da pasta
som_pulo = pygame.mixer.Sound("Áudios/Voicy_Jump-sound.wav")
death_sound= pygame.mixer.Sound("Áudios/DeathSound_cortado.WAV")
som_de_ponto= pygame.mixer.Sound("Áudios/Voicy_Coin.wav")
pygame.mixer.music.load("Áudios/TempleOS Hymn - Risen - ZAMORA (youtube).mp3")
pygame.mixer.music.set_volume(0.7)
def som_de_pulo():
    som_pulo.play()

def death_sound_func(): #dimiuir o delay do som
    death_sound.play()

def point_sound():
    som_de_ponto.play()
def trilha():
    pygame.mixer.music.play(-1)
# Configurações da janela
LARGURA = 500
ALTURA = 700

#flappy 
def desenhar_ovni(tela, x, y):
    metal_claro = (180, 190, 205)
    metal_medio = (120, 130, 150)
    metal_escuro = (70, 80, 95)
    vidro = (110, 220, 255)
    vidro_luz = (200, 245, 255)
    contorno = (20, 25, 35)
    luz_amarela = (255, 220, 90)
    luz_vermelha = (255, 90, 90)
    luz_azul = (100, 180, 255)

    pygame.draw.ellipse(tela, metal_escuro, (x + 6, y + 26, 64, 20))
    pygame.draw.ellipse(tela, metal_medio, (x, y + 18, 78, 24))
    pygame.draw.ellipse(tela, metal_claro, (x + 8, y + 20, 62, 14))
    pygame.draw.ellipse(tela, vidro, (x + 20, y + 2, 36, 26))
    pygame.draw.ellipse(tela, vidro_luz, (x + 28, y + 6, 14, 8))
    pygame.draw.ellipse(tela, metal_escuro, (x + 28, y + 34, 20, 8))

    pygame.draw.circle(tela, luz_vermelha, (x + 14, y + 30), 4)
    pygame.draw.circle(tela, luz_amarela, (x + 28, y + 34), 4)
    pygame.draw.circle(tela, luz_azul, (x + 42, y + 35), 4)
    pygame.draw.circle(tela, luz_amarela, (x + 56, y + 34), 4)
    pygame.draw.circle(tela, luz_vermelha, (x + 68, y + 30), 4)

    pygame.draw.line(tela, (220, 225, 235), (x + 12, y + 24), (x + 24, y + 23), 2)
    pygame.draw.line(tela, (220, 225, 235), (x + 54, y + 23), (x + 66, y + 24), 2)

    pygame.draw.ellipse(tela, contorno, (x, y + 18, 78, 24), 2)
    pygame.draw.ellipse(tela, contorno, (x + 8, y + 20, 62, 14), 2)
    pygame.draw.ellipse(tela, contorno, (x + 20, y + 2, 36, 26), 2)
    pygame.draw.ellipse(tela, contorno, (x + 28, y + 34, 20, 8), 2)

    pygame.draw.circle(tela, (255, 255, 255), (x + 34, y + 10), 3)

#CENÁRIO
def desenhar_ceu_apocaliptico(tela, largura, altura):
    cor_topo = (45, 18, 35)      # roxo escuro
    cor_meio = (130, 45, 35)     # vermelho queimado
    cor_base = (210, 110, 50)    # brilho sujo no horizonte

    for y in range(altura):
        proporcao = y / altura

        if proporcao < 0.6:
            p = proporcao / 0.6
            r = int(cor_topo[0] * (1 - p) + cor_meio[0] * p)
            g = int(cor_topo[1] * (1 - p) + cor_meio[1] * p)
            b = int(cor_topo[2] * (1 - p) + cor_meio[2] * p)
        else:
            p = (proporcao - 0.6) / 0.4
            r = int(cor_meio[0] * (1 - p) + cor_base[0] * p)
            g = int(cor_meio[1] * (1 - p) + cor_base[1] * p)
            b = int(cor_meio[2] * (1 - p) + cor_base[2] * p)

        pygame.draw.line(tela, (r, g, b), (0, y), (largura, y))


def desenhar_fumaca_apocaliptica(tela):
    fumaça1 = (90, 70, 75)
    fumaça2 = (120, 90, 90)
    fumaça3 = (70, 55, 60)

    # nuvens/fumaça distantes
    pygame.draw.circle(tela, fumaça1, (80, 130), 35)
    pygame.draw.circle(tela, fumaça2, (120, 120), 45)
    pygame.draw.circle(tela, fumaça3, (160, 135), 30)

    pygame.draw.circle(tela, fumaça1, (330, 110), 40)
    pygame.draw.circle(tela, fumaça2, (370, 95), 55)
    pygame.draw.circle(tela, fumaça3, (420, 120), 35)

    # camada de névoa baixa
    pygame.draw.ellipse(tela, (100, 70, 60), (0, 470, 500, 90))
    pygame.draw.ellipse(tela, (80, 60, 55), (0, 520, 500, 100))


def desenhar_horizonte_apocaliptico(tela, largura, altura):
    # chão escuro
    pygame.draw.rect(tela, (35, 28, 25), (0, altura - 70, largura, 70))

    # silhuetas de ruínas
    ruina = (25, 22, 24)
    pygame.draw.rect(tela, ruina, (20, altura - 150, 40, 80))
    pygame.draw.rect(tela, ruina, (70, altura - 180, 30, 110))
    pygame.draw.rect(tela, ruina, (120, altura - 140, 45, 70))
    pygame.draw.rect(tela, ruina, (210, altura - 200, 35, 130))
    pygame.draw.rect(tela, ruina, (260, altura - 160, 55, 90))
    pygame.draw.rect(tela, ruina, (350, altura - 190, 30, 120))
    pygame.draw.rect(tela, ruina, (400, altura - 145, 50, 75))

    # antenas / mastros destruídos
    pygame.draw.line(tela, (20, 20, 20), (85, altura - 180), (92, altura - 230), 3)
    pygame.draw.line(tela, (20, 20, 20), (225, altura - 200), (215, altura - 250), 3)
    pygame.draw.line(tela, (20, 20, 20), (365, altura - 190), (370, altura - 235), 3)

    # brilho alienígena no horizonte
    pygame.draw.circle(tela, (80, 255, 180), (430, altura - 78), 18)
    pygame.draw.circle(tela, (40, 160, 120), (430, altura - 78), 28, 2)

    pygame.draw.circle(tela, (120, 220, 255), (120, altura - 74), 10)
    pygame.draw.circle(tela, (60, 120, 150), (120, altura - 74), 20, 2)


def desenhar_luzes_ets(tela):
    # feixes discretos
    pygame.draw.polygon(
        tela,
        (70, 255, 200),
        [(110, 90), (135, 90), (170, 260), (80, 260)]
    )

    pygame.draw.polygon(
        tela,
        (90, 220, 255),
        [(360, 60), (385, 60), (430, 250), (330, 250)]
    )

    # discos/luzes no céu
    pygame.draw.ellipse(tela, (100, 255, 200), (90, 75, 60, 14))
    pygame.draw.ellipse(tela, (130, 240, 255), (340, 45, 70, 16))
    pygame.draw.ellipse(tela, (20, 50, 45), (90, 75, 60, 14), 2)
    pygame.draw.ellipse(tela, (20, 50, 45), (340, 45, 70, 16), 2)


def desenhar_cano_cima_apocaliptico(tela, x, largura, altura):
    metal = (85, 88, 78)
    metal_escuro = (45, 48, 42)
    ferrugem = (130, 70, 35)
    ferrugem_escura = (90, 45, 20)
    brilho_et = (80, 255, 170)
    borda = (20, 20, 18)

    # corpo
    pygame.draw.rect(tela, metal, (x, 0, largura, altura))
    pygame.draw.rect(tela, metal_escuro, (x + largura - 12, 0, 12, altura))
    pygame.draw.rect(tela, borda, (x, 0, largura, altura), 3)

    # tampa industrial
    pygame.draw.rect(tela, metal_escuro, (x - 8, altura - 20, largura + 16, 20))
    pygame.draw.rect(tela, borda, (x - 8, altura - 20, largura + 16, 20), 3)

    # faixas horizontais
    for faixa_y in range(30, altura - 25, 55):
        pygame.draw.rect(tela, metal_escuro, (x + 4, faixa_y, largura - 8, 6))

    # ferrugem
    pygame.draw.circle(tela, ferrugem, (x + 22, max(15, altura // 3)), 10)
    pygame.draw.circle(tela, ferrugem_escura, (x + 60, max(30, altura // 2)), 8)
    pygame.draw.circle(tela, ferrugem, (x + 40, max(20, altura - 45)), 7)

    # rachaduras
    pygame.draw.line(tela, borda, (x + 18, 40), (x + 28, 65), 2)
    pygame.draw.line(tela, borda, (x + 28, 65), (x + 20, 82), 2)

    pygame.draw.line(tela, borda, (x + 55, 110), (x + 48, 130), 2)
    pygame.draw.line(tela, borda, (x + 48, 130), (x + 60, 148), 2)

    # brilho alienígena discreto
    pygame.draw.rect(tela, brilho_et, (x + 8, max(8, altura - 50), 8, 20))
    pygame.draw.rect(tela, (30, 80, 60), (x + 8, max(8, altura - 50), 8, 20), 2)


def desenhar_cano_baixo_apocaliptico(tela, x, y, largura, altura_tela):
    metal = (85, 88, 78)
    metal_escuro = (45, 48, 42)
    ferrugem = (130, 70, 35)
    ferrugem_escura = (90, 45, 20)
    brilho_et = (80, 255, 170)
    borda = (20, 20, 18)

    altura = altura_tela - y

    # corpo
    pygame.draw.rect(tela, metal, (x, y, largura, altura))
    pygame.draw.rect(tela, metal_escuro, (x + largura - 12, y, 12, altura))
    pygame.draw.rect(tela, borda, (x, y, largura, altura), 3)

    # tampa industrial
    pygame.draw.rect(tela, metal_escuro, (x - 8, y, largura + 16, 20))
    pygame.draw.rect(tela, borda, (x - 8, y, largura + 16, 20), 3)

    # faixas horizontais
    for faixa_y in range(y + 30, altura_tela - 25, 55):
        pygame.draw.rect(tela, metal_escuro, (x + 4, faixa_y, largura - 8, 6))

    # ferrugem
    pygame.draw.circle(tela, ferrugem, (x + 20, y + 40), 10)
    pygame.draw.circle(tela, ferrugem_escura, (x + 58, y + 80), 8)
    pygame.draw.circle(tela, ferrugem, (x + 35, y + 130), 9)

    # rachaduras
    pygame.draw.line(tela, borda, (x + 22, y + 35), (x + 30, y + 55), 2)
    pygame.draw.line(tela, borda, (x + 30, y + 55), (x + 18, y + 72), 2)

    pygame.draw.line(tela, borda, (x + 60, y + 95), (x + 48, y + 118), 2)
    pygame.draw.line(tela, borda, (x + 48, y + 118), (x + 57, y + 138), 2)

    # brilho alienígena discreto
    pygame.draw.rect(tela, brilho_et, (x + largura - 20, y + 28, 8, 20))
    pygame.draw.rect(tela, (30, 80, 60), (x + largura - 20, y + 28, 8, 20), 2)




#Configurações da gravidade
y=5
run = False
gravity = 5

#Movimento do cano
velocidade = 5
x=0
altcanodecima = 400
ycanodebaixo = 550
pipe_position = 400

#2° Cano
pipe_position2 = 700
alt2canodecima = 500
y2canodebaixo = 650

#3° Cano
pipe_position3 = 1100
alt3canodecima = 500
y3canodebaixo = 650


#Aleatoriedade do cano
pipetime= pygame.USEREVENT+1
'''pygame.time.set_timer(pipetime, 2000)'''
numeroycanodebaixo = 0

'''#pygame.display.set_mode é uma função de um módulo de um ubmódulo display que está dentro do módulo display,
A navegaão é feita a partir de ".", cada ponto repreenta a entrada em uma pasta de um módulo'''
#acessa algo dentro de algo com "."
'''Aqui estamos entrando nos módulos de display até chegarmos em setmode para a tela, esta função usa o parenteses
com separação de numeros por virgulas, ou seja, uma tupla. Pois os parametros de resolução não podem mudar'''
tela = pygame.display.set_mode((LARGURA, ALTURA))
"""Esta funçã esta declarando que na legenda da janela do jogo, ira aparecer o titulo dentro do print """
pygame.display.set_caption("Flappy Bird - Início")

#Variavel para o flappy bird
xflappy=100
yflappy=150

# Cores
AZUL = (135, 206, 235)
BRANCO = (255, 255, 255)
AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
VERDE = (0, 128,0)
# Aqui estamos configurando o clock do jogo, mais para baixo no código tem a declaração de que esse clock
#vai definir o fps do jogo, mas esse fps no caso é a taxa de atualização do JOGO, não somente da tela do usuário
clock = pygame.time.Clock() 
''' Este comando está criando o clock do programa, mais a frente temos que configurar
dentro do loop do jogo '''

# Variável para manter o jogo rodando
rodando = True
diferenca=0
#tentativa de botão de saída
notrunning= True
espaco=None
recorde=0
points=0
queda=1.03
pulo=False
# Toca música, fora do while pois se não fica resetando sempre
trilha()
while rodando:
    # Preenche o fundo
    desenhar_ceu_apocaliptico(tela, LARGURA, ALTURA)
    desenhar_fumaca_apocaliptica(tela)
    desenhar_luzes_ets(tela)
    desenhar_horizonte_apocaliptico(tela, LARGURA, ALTURA)
    '''essa função verifica se um botão foi pressionado, somente o toque, então o programa não vai saber 
     se ainda está pressionado ou não '''
    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN: #aqui estu fazendo com que o programa reconheça o apertar da tecla x para assim fechar a jannela
            if evento.key == pygame.K_SPACE :
                run=True
                pulo=True
                som_de_pulo()
                tempodeespaco = pygame.time.get_ticks()
                espaco = pygame.K_SPACE
            if evento.key == pygame.K_ESCAPE:
                rodando= False
        elif evento.type == pygame.QUIT:
            rodando = False
        '''if evento.type == pipetime:
            altcanodecima = random.randint(100, 400)
            ycanodebaixo  = altcanodecima+150 
            last_pipe_time = pygame.time.get_ticks()'''


    if notrunning== True and run== False:
        pygame.draw.rect(tela, VERDE, (150, 200, 200, 60))
        pygame.draw.rect(tela, VERDE, (150, 270, 200, 60))
        pygame.draw.rect(tela, VERDE, (150, 340, 200, 60))
        fonte = pygame.font.SysFont(None, 40)
        textoimagem = fonte.render("Start", False, BRANCO)
        imagemsaida = fonte.render("Esc", False, BRANCO)
        imagemrecorde = fonte.render(f"Recorde {recorde}", False, BRANCO)
        tela.blit(textoimagem, (220, 215))
        tela.blit(imagemsaida, (220, 355))
        tela.blit(imagemrecorde, (180, 285))# X e Y
        pipe_position = 400
        pipe_position2 = 700
        pipe_position3 = 1100
        pulo = False
        espaco = None
        gravity = 5
        y = 5
        tempodeespaco = 0

    
    yflappy=100-y
    desenhar_ovni(tela, xflappy, yflappy)
                                #  X         Y     LARGURA ALTURA
    '''pygame.draw.rect(tela,BRANCO,(xflappy,yflappy  ,50   ,50))
    #Boca do flappi bird em amarelo
    pygame.draw.rect(tela,AMARELO,(115,130-y,25,20))
    #Contorno em preto da boca do flappy Bird
    pygame.draw.rect(tela,PRETO,(115,130-y,25,1))
    pygame.draw.rect(tela,PRETO,(115,149-y,25,1))
    pygame.draw.rect(tela,PRETO,(115,130-y,1,20))
    pygame.draw.rect(tela,PRETO,(140,130-y,1,20))
    pygame.draw.rect(tela,PRETO,(115,139-y,25,1))'''

    '''randomheightA = random.randint(400, 800)
    randomheightB = random.randint(0,400)'''
    #Iniciando o design dos canos
    '''PRIMEIRO CANO'''
                  #        x     y         larg        altura
    '''pygame.draw.rect(tela, VERDE, (pipe_position, 0,        100, altcanodecima)) #cano de cima(a altura aleatória deve ser de 100 a 400)
    pygame.draw.rect(tela, VERDE, (pipe_position, ycanodebaixo, 100,     900)) #cano de baixo(a posição do y deve ser de 250 a 600 )
    '''
    '''SEGUNDO CANO'''
     
    '''pygame.draw.rect(tela, VERDE, (pipe_position2, 0,        100, alt2canodecima)) #cano de cima(a altura aleatória deve ser de 100 a 400)
    pygame.draw.rect(tela, VERDE, (pipe_position2, y2canodebaixo, 100,     900)) #cano de baixo(a posição do y deve ser de 250 a 600 )
    '''
    '''TERCEIRO CANO'''
    
    '''pygame.draw.rect(tela, VERDE, (pipe_position3, 0,        100, alt3canodecima)) #cano de cima(a altura aleatória deve ser de 100 a 400)
    pygame.draw.rect(tela, VERDE, (pipe_position3, y3canodebaixo, 100,     900)) #cano de baixo(a posição do y deve ser de 250 a 600 )
    '''
    #cano 
    desenhar_cano_cima_apocaliptico(tela, pipe_position, 100, altcanodecima)
    desenhar_cano_baixo_apocaliptico(tela, pipe_position, ycanodebaixo, 100, ALTURA)

    desenhar_cano_cima_apocaliptico(tela, pipe_position2, 100, alt2canodecima)
    desenhar_cano_baixo_apocaliptico(tela, pipe_position2, y2canodebaixo, 100, ALTURA)

    desenhar_cano_cima_apocaliptico(tela, pipe_position3, 100, alt3canodecima)
    desenhar_cano_baixo_apocaliptico(tela, pipe_position3, y3canodebaixo, 100, ALTURA)

    if run== True:
        if pulo ==True:
            if tempo-tempodeespaco < 175 :
                y+=15
            else:
                pulo=False
        imagemponto = fonte.render(f"{points}", False, BRANCO)
        tela.blit(imagemponto, (220, 105))
        gravity=gravity*queda #queda=1.05 gravity inicialmente= 5
        '''if gravity>=10:
            queda=1'''
        y-=(gravity) #Velocidade de queda
        x=(velocidade) #Velocidade com que o cano se movimenta
        if espaco == pygame.K_SPACE :
            gravity=5
            espaco= None
        pygame.time.set_timer(pipetime, 2000)
        pipe_position-=x
        pipe_position2-=x
        pipe_position3-=x
        points+=addingpoints() 
        #Reinício do cano
        pipe_position, altcanodecima, ycanodebaixo=pipereset(pipe_position,pipe_position3,altcanodecima,ycanodebaixo)
        pipe_position2, alt2canodecima, y2canodebaixo=pipereset(pipe_position2,pipe_position,alt2canodecima,y2canodebaixo)
        pipe_position3, alt3canodecima, y3canodebaixo=pipereset(pipe_position3,pipe_position2,alt3canodecima,y3canodebaixo)

        #LÓGICA PARA COLISÃO  
        #if (pipe_position <= xflappy <= pipe_position + 100 or pipe_position2 <= xflappy <= pipe_position2 + 100 or pipe_position3 <= xflappy <= pipe_position3 + 100) and (yflappy <= altcanodecima or yflappy >= ycanodebaixo):
        if ((pipe_position <= xflappy <= pipe_position + 100 and (yflappy <= altcanodecima or yflappy+40 >= ycanodebaixo)) or (pipe_position2 <= xflappy <= pipe_position2 + 100 and (yflappy <= alt2canodecima or yflappy+40 >= y2canodebaixo)) or (pipe_position3 <= xflappy <= pipe_position3 + 100 and (yflappy <= alt3canodecima or yflappy+40 >= y3canodebaixo)) or (-100 >= yflappy) or yflappy>= 700) :
            death_sound_func()
            notrunning = True
            run = False
            y = 5  # Resetando a posição do Flappy Bird
            recorde = max(recorde, points)  # Atualizando o recorde se a pontuação atual for maior
            points = 0  # Resetando a pontuação

    tempo = pygame.time.get_ticks()
    print(f'Tempo: {tempo} ms')
    print(yflappy)
    # Atualiza a tela
    pygame.display.update()

    # Define FPS a 60
    clock.tick(60)
    '''Está função faz com que o ´python calcule o tempo passado do loop anteiror até o atual
     e calcula para permitir o loop acontecer somente quando passar por esse tempo, é como se fosse um delay
      ou um sleep porém o clock tick permite que o loop chegue até o final do loop '''
    
    '''A diferença de cloc.tick() para o delay ou time.sleep() é que o delay vai parar totalmente o código
    ou seja, nem inputs vai receber mais, porém com o clock,tick() ele ainda vai receber inputs, como os de teclado
    mas a resposta do rpograma só vaiv ir depois do tempo declarado de FPS'''

pygame.quit()
sys.exit()