from j2048_motor_45102 import novo_jogo
from j2048_motor_45102 import valor
from j2048_motor_45102 import terminou
from j2048_motor_45102 import pontuacao
from j2048_motor_45102 import atualizar_grelha
from j2048_motor_45102 import esquerda
from j2048_motor_45102 import direita
from j2048_motor_45102 import acima
from j2048_motor_45102 import abaixo
from j2048_motor_45102 import trocar_linhas_com_colunas

def alinhar (uma_string):

    return uma_string

def print_2048(jogo):

    pontos = pontuacao(jogo)

    print("pontos =" + str(pontos))
    
    for l in range(4):
        linha_string = ""
        for c in range(4):
            linha_string = linha_string + alinhar(str(valor(jogo, l+1, c+1))) + " "
        print(linha_string)


# Cria um novo jogo
jogo = novo_jogo()
print_2048(jogo)

tecla = None

while tecla != 'q' and not(terminou(jogo)):

    tecla = input()

    if tecla == 'n':
        jogo = novo_jogo()

    elif tecla == 'a':
        jogo = esquerda(jogo)

    elif tecla == 'd':
        jogo = direita(jogo)

    elif tecla == 'w':
        jogo = acima(jogo)

    elif tecla == 's':
        jogo = abaixo(jogo)
    

    print_2048(jogo)
    
