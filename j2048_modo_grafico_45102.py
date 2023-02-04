import pygame, sys
from j2048_gestor_45102 import inicializa_semente
from j2048_gestor_45102 import le_identificacao
from j2048_gestor_45102 import regista_grelha_inicial
from j2048_gestor_45102 import regista_jogada
from j2048_gestor_45102 import regista_pontos
from j2048_gestor_45102 import escreve_registo

from j2048_motor_45102 import novo_jogo
from j2048_motor_45102 import valor
from j2048_motor_45102 import terminou
from j2048_motor_45102 import pontuacao
from j2048_motor_45102 import actualizar_grelha
from j2048_motor_45102 import esquerda
from j2048_motor_45102 import direita
from j2048_motor_45102 import acima
from j2048_motor_45102 import abaixo
from j2048_motor_45102 import trocar_linhas_com_colunas
from j2048_motor_45102 import ganhou_ou_perdeu

# Main Controller #
def main():

    # Identificacao
    le_identificacao()
    inicializa_semente(None)
    jogo = novo_jogo()
    regista_grelha_inicial(valor(jogo,1,1),valor(jogo,1,2),valor(jogo,1,3),valor(jogo,1,4),
                       valor(jogo,2,1),valor(jogo,2,2),valor(jogo,2,3),valor(jogo,2,4),
                       valor(jogo,3,1),valor(jogo,3,2),valor(jogo,3,3),valor(jogo,3,4),
                       valor(jogo,4,1),valor(jogo,4,2),valor(jogo,4,3),valor(jogo,4,4))
    imprime_jogo(jogo)
    # Identificacao END

    global DISPLAY
    
    imprime_jogo(jogo)

    while True:
        if terminou(jogo) == True:
            perdeu = pygame.image.load('Perdeu.jpg')
            DISPLAY.blit(perdeu, (0,0))
            pygame.display.update()
            regista_pontos(pontuacao(jogo))
            mensagem_cloud = escreve_registo()
            print("Pontuação:", jogo[3])
            print("Terminou? ", jogo[2])             
            print(mensagem_cloud)
        if jogo[2] == True:
            ganhou = pygame.image.load('Ganhou.jpg')
            DISPLAY.blit(ganhou, (0,0))
            pygame.display.update()
            regista_pontos(pontuacao(jogo))
            mensagem_cloud = escreve_registo()             
            print("Pontuação", jogo[3])
            print("Terminou? ", jogo[2])             
            print(mensagem_cloud)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    jogo = esquerda(jogo)
                    imprime_jogo(jogo)
                    regista_jogada('a')
                elif event.key == pygame.K_s:
                    jogo = abaixo(jogo)                                     
                    imprime_jogo(jogo)
                    regista_jogada('s')
                elif event.key == pygame.K_d:
                    jogo = direita(jogo)
                    imprime_jogo(jogo)
                    regista_jogada('d')
                elif event.key == pygame.K_w:
                    jogo = acima(jogo)
                    imprime_jogo(jogo)
                    regista_jogada('w')
                elif event.key == pygame.K_n:
                    jogo = novo_jogo()
                    imprime_jogo(jogo)

                    regista_pontos(jogo[3])
                    mensagem = escreve_registo()
                    print(mensagem)
                    le_identificacao()
                    inicializa_semente(None)
                    g = jogo [0]
                    regista_grelha_inicial (g[0][0], g[0][1], g[0][2],g[0][3],
                                            g[1][0], g[1][1], g[1][2],g[1][3],
                                            g[2][0], g[2][1], g[2][2],g[2][3],
                                            g[3][0], g[3][1], g[3][2],g[3][3])
                elif event.key == pygame.K_LEFT:
                    jogo = esquerda(jogo)
                    imprime_jogo(jogo)
                    regista_jogada('a')
                
                elif event.key == pygame.K_RIGHT:
                    jogo = direita(jogo)
                    imprime_jogo(jogo)
                    regista_jogada('d')
                
                elif event.key == pygame.K_UP:
                    jogo = acima(jogo)
                    imprime_jogo(jogo)
                    regista_jogada('w')
                
                elif event.key == pygame.K_DOWN:
                    jogo = abaixo(jogo)
                    imprime_jogo(jogo)
                    regista_jogada('s')
                elif event.key == pygame.K_q:
                    regista_pontos(jogo[3])
                    mensagem = escreve_registo()
                    print("Pontuacao = " + str(pontuacao(jogo)))
                    print(mensagem)  
                    pygame.quit()
                    sys.exit()
                    
        pygame.display.update()
# Main Controller end
#def perdeu():
#    print("Perdeu")

DISPLAY = pygame.display.set_mode((400, 400), 0, 32)
    
# void Update ()  
def mudaGrelha(grelha, pontos): 
    vetor = [grelha[0][0],grelha[0][1],grelha[0][2],grelha[0][3],
             grelha[1][0],grelha[1][1],grelha[1][2],grelha[1][3],
             grelha[2][0],grelha[2][1],grelha[2][2],grelha[2][3],
             grelha[3][0],grelha[3][1],grelha[3][2],grelha[3][3]]
    pygame.init()

    WHITE = (255, 255, 255)                                                 
    blue = (0, 0, 255)                                                      
                                                                            
    FONT = pygame.font.SysFont('Arial', 25)                                 
    pygame.display.set_caption('jogo2048_A45102')                           

    global DISPLAY
    
    #DISPLAY = pygame.display.set_mode((400, 400), 0, 32)                   
    DISPLAY.fill((WHITE))                                                   
    pygame.draw.rect(DISPLAY , (238,228,218), (15,15, 200,30))
    pontos1 = str(pontos)                                                   
    DISPLAY.blit(FONT.render("Pontos =", True, (119,110,101)), (15,15))     
    DISPLAY.blit(FONT.render(pontos1, True, (119,110,101)), (100,15))       
    
    k = 1                                                                   
    while k < 17:                                                           
        retangulo(FONT, DISPLAY, k, vetor[k-1])                             
        k += 1                                                              
                                                                            
    pygame.display.update()                                               
# Update END
# void Draw ()
def retangulo(FONT, DISPLAY, pos, valor):
    x = [20, 80, 140, 200,20, 80, 140, 200,20, 80, 140, 200,20, 80, 140, 200]               
    y = [100, 100, 100, 100, 160, 160, 160, 160, 220, 220, 220, 220, 280, 280, 280, 280]    

    num = str(valor)                                                                        
    blue = (0, 0, 255)                                                                      
    yvar = 7                                                                                
    if len(num) == 1:                                                                       
        yvar = 25                                                                           
    elif len(num) == 2:                                                                     
        yvar = 19                                                                           
    elif len(num) == 3:                                                                     
        yvar = 13                                                                           
    if valor == 2:                  #Color                #Pos      #Rectangle Size                                                      
        pygame.draw.rect(DISPLAY, (238,228,218), (x[pos-1], y[pos-1], 60, 60))
    if valor == 4:
        pygame.draw.rect(DISPLAY, (237,224,200), (x[pos-1], y[pos-1], 60, 60))
    if valor == 8:
        pygame.draw.rect(DISPLAY, (242,177,121), (x[pos-1], y[pos-1], 60, 60))
    if valor == 16:
        pygame.draw.rect(DISPLAY, (245,149,99), (x[pos-1], y[pos-1], 60, 60))
    if valor == 32:
        pygame.draw.rect(DISPLAY, (246,124,95), (x[pos-1], y[pos-1], 60, 60))
    if valor == 64:
        pygame.draw.rect(DISPLAY, (246,94,59), (x[pos-1], y[pos-1], 60, 60))                 
    if valor == 128:
        pygame.draw.rect(DISPLAY, (237,207,114), (x[pos-1], y[pos-1], 60, 60))
    if valor == 256:
        pygame.draw.rect(DISPLAY, (227,192,44), (x[pos-1], y[pos-1], 60, 60))
    if valor == 512:
        pygame.draw.rect(DISPLAY, (226,184,19), (x[pos-1], y[pos-1], 60, 60))
    if valor == 1024:
        pygame.draw.rect(DISPLAY, (255,215,0), (x[pos-1], y[pos-1], 60, 60))
    if valor == 2048:
        pygame.draw.rect(DISPLAY, (100, 100, 100), (x[pos-1], y[pos-1], 60, 60))

                                #Color       #Pos                   #Size #Width
    pygame.draw.rect(DISPLAY, (187,173,160), (x[pos-1], y[pos-1], 60, 60), 4) 
    if valor != 0:              #Put the number in
        DISPLAY.blit(FONT.render(num, True, (119,110,101)), (x[pos-1] + yvar, y[pos-1] + 15))
    pygame.display.update()
# Draw END
def imprime_jogo(jogo):
    grelha = jogo[0]
    mudaGrelha(grelha, jogo[3])

main()
################################################################################
        

